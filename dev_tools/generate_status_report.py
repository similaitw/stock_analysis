
import os
import ast
from pathlib import Path

class StatusGenerator:
    def __init__(self, src_dir, report_file):
        self.src_dir = Path(src_dir)
        self.report_file = Path(report_file)

    def generate(self):
        print(f"Generating status report for {self.src_dir}...")
        
        cats = {} # cat_name -> list of {name, docstring, has_todo}
        
        files = sorted(list(self.src_dir.glob("*.py")))
        for fPath in files:
            if fPath.name == "__init__.py": continue
            
            cat_name = fPath.stem
            cats[cat_name] = []
            
            with open(fPath, 'r', encoding='utf-8') as f:
                try:
                    tree = ast.parse(f.read(), filename=str(fPath))
                except SyntaxError:
                    print(f"Skipping {fPath}: Syntax Error")
                    continue
            
            # Find class (Usually "CategoryNameStrategies")
            for node in tree.body:
                if isinstance(node, ast.ClassDef):
                    # Iterate methods
                    for item in node.body:
                        if isinstance(item, ast.FunctionDef):
                            # extract docstring
                            doc = ast.get_docstring(item)
                            orig_name = item.name
                            if doc:
                                for line in doc.split('\n'):
                                    if "Strategy:" in line:
                                        orig_name = line.split("Strategy:")[1].strip()
                                        break
                            
                            # Check body for "TODO" or "pass"
                            # We can check source lines if we had them, simpler to check if node contains Expr(Str("TODO")) or just check raw source text of body
                            
                            # Simple heuristic: AST doesn't easily tell us "TODO" in comments.
                            # So I will re-read the function body from file content by line number
                            
                            has_todo = False
                            # Read file lines for this function
                            with open(fPath, 'r', encoding='utf-8') as f:
                                file_lines = f.readlines()
                                # func body lines: item.lineno to end (or next func)
                                # simpler: just grep the file for "TODO" inside this function block? No hard to determine scope.
                                
                                # Better: just check if the function body contains a "TODO" comment or string literal "TODO"
                                # AST way:
                                for child in ast.walk(item):
                                    # Check for TODO string literals (docstrings or TODO strings)
                                    if isinstance(child, ast.Constant) and isinstance(child.value, str) and "TODO" in child.value:
                                        has_todo = True
                                        break
                                    # Comments are NOT in AST. But we put logic in strings/logic blocks.
                                
                                # Our generated code has "# TODO: Implement..." so it's a comment.
                                # Let's read the source segment.
                                start = item.lineno - 1
                                end = item.end_lineno
                                func_source = "".join(file_lines[start:end])
                                if "TODO:" in func_source:
                                    has_todo = True
                                
                            cats[cat_name].append({
                                "name": item.name,
                                "orig_name": orig_name,
                                "status": "🔴" if has_todo else "🟢"
                            })

        # Write Report
        with open(self.report_file, 'w', encoding='utf-8') as f:
            f.write("# 📊 XScript 策略轉換狀態表\n\n")
            f.write("> 此表由 `dev_tools/generate_status_report.py` 自動分析程式碼生成。\n\n")
            
            total = sum(len(x) for x in cats.values())
            done = sum(1 for lx in cats.values() for x in lx if x['status'] == "🟢")
            f.write(f"**總進度**: {done} / {total} ({(done/total*100):.1f}%)\n\n")
            
            for cat, strategies in cats.items():
                if not strategies: continue
                f.write(f"## 📂 {cat} ({len(strategies)})\n\n")
                f.write("| 狀態 | Python 函式 | 原始策略 (XScript) |\n")
                f.write("|---|---|---|\n")
                for s in strategies:
                    f.write(f"| {s['status']} | `{s['name']}` | {s['orig_name']} |\n")
                f.write("\n")

        print(f"Report generated: {self.report_file}")

if __name__ == "__main__":
    report_path = Path(r"e:\anti-gravity\stock\stock_analysis\strategies\MakeList.md")
    src_path = Path(r"e:\anti-gravity\stock\stock_analysis\strategies\auto_generated")
    
    gen = StatusGenerator(src_path, report_path)
    gen.generate()
