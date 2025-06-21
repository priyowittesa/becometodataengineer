import sys

import pandas as pd

# print(sys.argv)

# day = sys.argv[1]

# print(f'job finished successfully = {day}')

names = ['Ani', 'Budi', 'Cici']
ages = []
for name in names:
    age_input = input(f"masukkan umur untuk {name}: ")
    ages.append(int(age_input))
data = {'Name': names, 'Age': ages}
df = pd.DataFrame(data)
print(df)