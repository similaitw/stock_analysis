
import os
import re
import codecs
from pathlib import Path

class XSConverter:
    def __init__(self, src_dir, dest_dir):
        self.src_dir = Path(src_dir)
        self.dest_dir = Path(dest_dir)
        self.dest_dir.mkdir(parents=True, exist_ok=True)
        self.strategies_map = {}  # Category -> List of Strategy Info

    def convert_all(self):
        """遞迴轉換所有 .xs 檔案，並依目錄分類生成 Python 模組"""
        print(f"Starting conversion from {self.src_dir} to {self.dest_dir}")
        self.strategies_map = {}
        
        # 清除舊的自動生成檔案 (保持乾淨)
        if self.dest_dir.exists():
            import shutil
            # shutil.rmtree(self.dest_dir) # 謹慎使用，或者只刪除特定檔案
            print(f"Notice: Destination {self.dest_dir} already exists.")
        
        self.dest_dir.mkdir(parents=True, exist_ok=True)
        
        for root, dirs, files in os.walk(self.src_dir):
            for file in files:
                if file.endswith(".xs"):
                    src_path = Path(root) / file
                    try:
                        self.process_file(src_path)
                    except Exception as e:
                        print(f"Error processing {src_path}: {e}")
        
        self.generate_python_files()

    def process_file(self, file_path):
        """解析單一 .xs 檔案，並儲存至 strategies_map"""
        try:
            # 嘗試不同編碼讀取
            content = ""
            for encoding in ['utf-8', 'cp950', 'bg18030', 'utf-16']:
                try:
                    with codecs.open(file_path, 'r', encoding=encoding) as f:
                        content = f.read()
                    break
                except UnicodeDecodeError:
                    continue
            
            if not content:
                print(f"Skipping {file_path}: Cannot decode")
                return

            # 解析 XS 結構
            file_stem = file_path.stem
            # Sanitize function name: remove spaces, dots, handle chinese
            func_name = re.sub(r'[^\w]', '_', file_stem)
            
            # If it starts with digit, prepend suffix
            if re.match(r'^\d', func_name): 
                func_name = f"strategy_{func_name}"
            
            # 解析分類 (使用完整相對路徑)
            rel_dir = file_path.parent.relative_to(self.src_dir)
            cat_key = str(rel_dir).replace('\\', '/')
            if cat_key == '.': cat_key = "common"
            
            # Sanitize category name for class name
            sanitized_cat = re.sub(r'[^\w/]', '_', cat_key)
            
            # Extract Inputs: input: Period(10, "Description"); -> gets Period, 10
            inputs = re.findall(r'input:\s*([a-zA-Z0-9_]+)\(([^),]+)', content, re.IGNORECASE)
            
            # Extract Logic Body
            body_lines = []
            for line in content.splitlines():
                if not re.match(r'^\s*(input:|variable:|setinputname|var:)', line, re.IGNORECASE):
                    body_lines.append(line)
            
            strategy_info = {
                "name": func_name,
                "original_name": file_stem,
                "inputs": inputs,
                "body": "\n".join(body_lines),
                "path": str(file_path)
            }
            
            if cat_key not in self.strategies_map:
                self.strategies_map[cat_key] = []
            self.strategies_map[cat_key].append(strategy_info)
            
            print(f"Analyzed: [{cat_key}] {file_stem} -> {func_name}")

        except Exception as e:
            print(f"Failed to process {file_path}: {e}")

    def generate_python_files(self):
        """根據 strategies_map 生成分層的 Python 模組"""
        for cat_key, strategies in self.strategies_map.items():
            # 建立子目錄
            parts = Path(cat_key).parts
            current_target = self.dest_dir
            for part in parts:
                safe_part = re.sub(r'[^\w]', '_', part)
                if safe_part and safe_part[0].isdigit(): safe_part = f"p_{safe_part}"
                current_target = current_target / safe_part
                current_target.mkdir(exist_ok=True)
                # 建立 __init__.py 讓其成為 package
                init_file = current_target / "__init__.py"
                if not init_file.exists():
                    with open(init_file, 'w', encoding='utf-8') as f:
                        f.write(f"# Category: {part}\n")

            # 在該目錄下生成策略檔案
            # 如果目錄本身就有名字，我們用 strategies.py
            py_path = current_target / "strategies.py"
            
            print(f"Generating {py_path} with {len(strategies)} strategies...")
            
            with open(py_path, 'w', encoding='utf-8') as f:
                f.write(f"# Auto-generated strategies for: {cat_key}\n")
                f.write("import pandas as pd\n")
                f.write("import numpy as np\n\n")
                
                # Class name from cat_key
                leaf_name = parts[-1] if parts else "Common"
                class_name = "".join(word.title() for word in re.sub(r'[^\w]', '_', leaf_name).split('_')) + "Strategies"
                if class_name and class_name[0].isdigit(): class_name = "Cat" + class_name
                
                f.write(f"class {class_name}:\n")
                
                for strat in strategies:
                    # Function Signature (保持原有邏輯)
                    args_str = "df: pd.DataFrame"
                    for inp_name, inp_val in strat['inputs']:
                        inp_val = inp_val.strip()
                        # ... (原有型別判斷邏輯) ...
                        if inp_val.isdigit(): py_type = 'int'
                        elif re.match(r'^-?\d+\.\d+$', inp_val): py_type = 'float'
                        else:
                            py_type = 'str'
                            if not (inp_val.startswith('"') or inp_val.startswith("'")):
                                inp_val = f'"{inp_val}"'
                        args_str += f", {inp_name}: {py_type} = {inp_val}"
                    
                    f.write(f"\n    @staticmethod\n")
                    f.write(f"    def {strat['name']}({args_str}) -> tuple[bool, str]:\n")
                    f.write(f'        """\n')
                    f.write(f"        Original Strategy: {strat['original_name']}\n")
                    f.write(f"        Source: {strat['path']}\n")
                    f.write(f"        XS Logic Reference:\n")
                    
                    # Indent and escape original logic
                    for line in strat['body'].splitlines():
                        if line.strip():
                            safe_line = line.replace('"""', "'''")
                            f.write(f"        {safe_line}\n")
                    f.write(f'        """\n')
                    
                    f.write("        if df.empty: return False, \"\"\n")
                    f.write("        # TODO: Implement indicators\n")
                    f.write("        return False, \"\"\n")

    def print_ascii_tree(self):
        """生成並顯示結果的 ASCII 目錄結構"""
        print("\nGenerated ASCII Structure:")
        print("="*40)
        self._tree_recursive(self.dest_dir, "")
        print("="*40)

    def _tree_recursive(self, path, prefix):
        contents = sorted(list(path.iterdir()))
        pointers = [True] * (len(contents) - 1) + [False]
        for pointer, path in zip(pointers, contents):
            if path.name.startswith("__"): continue
            marker = "├── " if pointer else "└── "
            print(f"{prefix}{marker}{path.name}")
            if path.is_dir():
                new_prefix = prefix + ("│   " if pointer else "    ")
                self._tree_recursive(path, new_prefix)

if __name__ == "__main__":
    SRC = r"e:\anti-gravity\stock\stock_analysis\temp_xscript_preset"
    # 使用正式目錄
    DEST = r"e:\anti-gravity\stock\stock_analysis\strategies\auto_generated"
    
    converter = XSConverter(SRC, DEST)
    converter.convert_all()
    converter.print_ascii_tree()
