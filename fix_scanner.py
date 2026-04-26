import re

# 讀取檔案
with open(r'e:\anti-gravity\stock\stock_analysis\ui\app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 替換掃描按鈕
old_btn = '    scan_btn = st.sidebar.button("開始掃描 (Start Scan)")'
new_btn = '    scan_btn = st.button("🚀 開始掃描", type="primary", use_container_width=True)'

if old_btn in content:
    content = content.replace(old_btn, new_btn)
    print("✅ 成功替換掃描按鈕")
else:
    print("❌ 找不到要替換的按鈕")
    # 搜尋相關內容
    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        if 'scan_btn' in line and 'sidebar' in line:
            print(f"Line {i}: {line}")

# 寫回檔案
with open(r'e:\anti-gravity\stock\stock_analysis\ui\app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("完成！")
