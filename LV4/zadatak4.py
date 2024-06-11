import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ucitavanje ociscenih podataka
df = pd.read_csv('cars_processed.csv')
print(df.info())

# razliciti prikazi
sns.pairplot(df, hue='fuel')

sns.relplot(data=df, x='km_driven', y='selling_price', hue='fuel')
df = df.drop(['name','mileage'], axis=1)

obj_cols = df.select_dtypes(object).columns.values.tolist()
num_cols = df.select_dtypes(np.number).columns.values.tolist()

fig = plt.figure(figsize=[15,8])
for col in range(len(obj_cols)):
    plt.subplot(2,2,col+1)
    sns.countplot(x=obj_cols[col], data=df)

df.boxplot(by ='fuel', column =['selling_price'], grid = False)

df.hist(['selling_price'], grid = False)

tabcorr = df.corr()
sns.heatmap(df.corr(), annot=True, linewidths=2, cmap= 'coolwarm') 

plt.show()

print("Zadatak1:")
print("Broj mjerenja (automobila) u datasetu:", df.shape[0])

print("Zadatak2:")
print(df.info())

print("Zadatak3:")
najskuplji_automobil = df.loc[df['selling_price'].idxmax()]
najjeftiniji_automobil = df.loc[df['selling_price'].idxmin()]
print("Najskuplji automobil:\n", najskuplji_automobil)
print("\nNajjeftiniji automobil:\n", najjeftiniji_automobil)

print("Zadatak4:")
broj_automobila_2012 = df['year'].value_counts()[2012]
print("Broj automobila proizvedenih 2012. godine:", broj_automobila_2012)

print("Zadatak5:")
najvise_km_automobil = df.loc[df['km_driven'].idxmax()]
najmanje_km_automobil = df.loc[df['km_driven'].idxmin()]
print("Automobil s najviše kilometara:\n", najvise_km_automobil)
print("\nAutomobil s najmanje kilometara:\n", najmanje_km_automobil)

print("Zadatak6:")
najcesce_sjedala = df['seats'].mode()[0]
print("Najčešći broj sjedala:", najcesce_sjedala)

print("Zadatak7:")
prosjek_km_dizel = df[df['fuel'] == 'Diesel']['km_driven'].mean()
prosjek_km_benzin = df[df['fuel'] == 'Petrol']['km_driven'].mean()

print("Prosječna kilometraža za automobile s dizel motorom:", prosjek_km_dizel)
print("Prosječna kilometraža za automobile s benzinskim motorom:", prosjek_km_benzin)

