import matplotlib.pyplot as plt
import pandas as pd

mtcars = pd.read_csv('mtcars.csv')

# Postavljanje podgrafova (2 reda, 2 stupca) s određenom veličinom slike
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# 1. Barplot potrošnje automobila s 4, 6 i 8 cilindara
axs[0, 0].bar(['4 cyl', '6 cyl', '8 cyl'], mtcars.groupby('cyl')['mpg'].mean(), color=['blue', 'orange', 'green'])
axs[0, 0].set_title('Prosječna potrošnja automobila po broju cilindara')  # Postavljanje naslova podgrafovima
axs[0, 0].set_xlabel('Broj cilindara')  # Postavljanje oznake x osi
axs[0, 0].set_ylabel('Prosječna potrošnja (mpg)')  # Postavljanje oznake y osi

# 2. Boxplot distribucije težine automobila s 4, 6 i 8 cilindara
mtcars.boxplot(column='wt', by='cyl', ax=axs[0, 1])  # Boxplot distribucije težine prema broju cilindara
axs[0, 1].set_title('Distribucija težine automobila po broju cilindara')  # Postavljanje naslova podgrafovima
axs[0, 1].set_xlabel('Broj cilindara')  # Postavljanje oznake x osi
axs[0, 1].set_ylabel('Težina (lbs)')  # Postavljanje oznake y osi
axs[0, 1].set_xticklabels(['4 cyl', '6 cyl', '8 cyl'])  # Postavljanje oznaka x osi

# 3. Grafički odgovor na pitanje imaju li automobili s ručnim mjenjačem veću potrošnju od automobila s automatskim mjenjačem
mtcars.groupby('am')['mpg'].mean().plot(kind='bar', ax=axs[1, 0], color=['blue', 'orange'])  # Barplot potrošnje s grupiranjem prema mjenjaču
axs[1, 0].set_title('Prosječna potrošnja automobila s ručnim i automatskim mjenjačem')  # Postavljanje naslova podgrafovima
axs[1, 0].set_xlabel('Mjenjač')  # Postavljanje oznake x osi
axs[1, 0].set_ylabel('Prosječna potrošnja (mpg)')  # Postavljanje oznake y osi
axs[1, 0].set_xticklabels(['Ručni', 'Automatski'], rotation=0)  # Postavljanje oznaka x osi i rotiranje za 0 stupnjeva

# 4. Scatter plot odnosa ubrzanja i snage automobila za automobile s ručnim odnosno automatskim mjenjačem
axs[1, 1].scatter(mtcars[mtcars['am'] == 0]['hp'], mtcars[mtcars['am'] == 0]['qsec'], label='Ručni', color='blue')  # Scatter plot za automobile s ručnim mjenjačem
axs[1, 1].scatter(mtcars[mtcars['am'] == 1]['hp'], mtcars[mtcars['am'] == 1]['qsec'], label='Automatski', color='orange')  # Scatter plot za automobile s automatskim mjenjačem
axs[1, 1].set_title('Odnos ubrzanja i snage automobila')  # Postavljanje naslova podgrafovima
axs[1, 1].set_xlabel('Snaga (hp)')  # Postavljanje oznake x osi
axs[1, 1].set_ylabel('Ubrzanje (qsec)')  # Postavljanje oznake y osi
axs[1, 1].legend()  # Prikazivanje legende

# Postavljanje razmaka između podgrafova radi bolje čitljivosti
plt.tight_layout()

# Prikazivanje grafova
plt.show()
