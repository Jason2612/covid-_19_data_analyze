import pandas as pd

data = pd.read_csv('data\subset-covid-data.csv', encoding= 'UTF-8')
# data.head()
# data.info()
# data.date.value_counts()

cleaned_data = data[data.date == '2020-04-12']

# print("Trung binh so ca mac moi: " + str(cleaned_data.cases.mean()))
# print("Trung vi cua so ca mac moi: " + str(cleaned_data.cases.median()))

import matplotlib.pyplot as plt
plt.hist(cleaned_data.cases, bins = 200)
plt.title("Phan bo so ca mac moi")
plt.xlabel("So ca mac moi")
plt.ylabel("So luong quoc gia")

# print("Tong so ca nhiem va so ca cua cac chau luc")
# cleaned_data.groupby('continent')['cases','deaths'].sum()

print ("5 quốc gia có số ca nhiễm mới cao nhất")
data = data.sort_values('cases',ascending = False)
data.head(5)



