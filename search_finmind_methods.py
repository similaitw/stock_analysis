from FinMind.data import DataLoader
dl = DataLoader()
print("Methods matching 'fin' or 'div' or 'stat':")
for m in dir(dl):
    if 'fin' in m or 'div' in m or 'stat' in m:
       print(m)
