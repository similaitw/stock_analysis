from FinMind.data import DataLoader
import inspect

api = DataLoader()
methods = [m for m in dir(api) if callable(getattr(api, m)) and not m.startswith('_')]

print("Searching for 'lending', 'borrow', 'balance', 'margin':")
for m in methods:
    if any(k in m.lower() for k in ['lending', 'borrow', 'balance', 'margin']):
        print(m)
