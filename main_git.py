import matplotlib.pyplot as plt
import pandas as pd


dom = pd.read_csv('zillow.csv')

dom = dom.sort_values(by='Year').reset_index(drop = True) #rest(drop)удаление стрых индексов
print(dom)

before_2000 = 0
after_2015 = 0

for i in range(len(dom)):
    if dom['Year'][i] < 2000:
        before_2000 += 1
    if dom['Year'][i] > 2015:
        after_2015 += 1

between = len(dom) - before_2000 - after_2015

labels = 'before_2000','after_2015','2000 - 2015'
sizes = [before_2000, after_2015, between]

fig, ax = plt.subplots()
explode = (0.1, 0.07, 0.07)

ax.pie(sizes, explode=explode, labels=labels, autopct='%1.0f%%', shadow=True, startangle=90)

plt.show()


