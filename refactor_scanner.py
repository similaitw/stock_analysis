import re

# 讀取檔案
with open(r'e:\anti-gravity\stock\stock_analysis\ui\app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到策略選股區塊的開始和結束
start_marker = 'elif app_mode == "策略選股 (Strategy Scanner)":'
end_marker = 'elif app_mode == "即時監控 (Real-time Monitor)"'

# 找到開始位置
start_pos = content.find(start_marker)
if start_pos == -1:
    print("❌ 找不到策略選股區塊開始")
    exit(1)

# 找到結束位置
end_pos = content.find(end_marker, start_pos)
if end_pos == -1:
    print("❌ 找不到策略選股區塊結束")
    exit(1)

# 替換的新程式碼
new_code = '''elif app_mode == "策略選股 (Strategy Scanner)":
    from ui.scanner_page import render_scanner_page
    render_scanner_page()

'''

# 執行替換
new_content = content[:start_pos] + new_code + content[end_pos:]

# 寫回檔案
with open(r'e:\anti-gravity\stock\stock_analysis\ui\app.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"✅ 成功重構策略選股頁面")
print(f"   移除了 {end_pos - start_pos} 個字元的程式碼")
print(f"   替換為 {len(new_code)} 個字元的呼叫程式碼")
print(f"   程式碼減少了 {((end_pos - start_pos - len(new_code)) / (end_pos - start_pos) * 100):.1f}%")
