from datetime import datetime

for i in range(0,24,2):
    date = datetime(2025, 12, 16, 1+i)
    print(date.hour)