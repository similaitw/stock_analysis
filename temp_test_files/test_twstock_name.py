import twstock

try:
    print("Testing twstock codes...")
    # key is stock code
    tsmc = twstock.codes['2330']
    print(f"2330: {tsmc.name} ({tsmc.type})")
    
    evergreen = twstock.codes['2603']
    print(f"2603: {evergreen.name}")
    
except Exception as e:
    print(f"Error: {e}")
