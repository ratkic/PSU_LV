import urllib.request
import pandas as pd
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

# url koji sadrzi xml datoteku s mjerenjima:
url = 'http://iszz.azo.hr/iskzl/rs/podatak/export/xml?postaja=160&polutant=5&tipPodatka=0&vrijemeOd=01.01.2017&vrijemeDo=31.12.2017'

airQualityHR = urllib.request.urlopen(url).read()
root = ET.fromstring(airQualityHR)

df = pd.DataFrame(columns=('mjerenje', 'vrijeme'))

# Iteriranje kroz mjerenja dnevne koncentracije lebdećih čestica PM10 za 2017. godinu za grad Osijek
for child in root.iter('podatak'):
    time = pd.to_datetime(child.find('vrijeme').text, utc=True)
    if time.year == 2017 and child.find('postaja').text == 'Osijek':
        measurement = float(child.find('vrijednost').text)
        df = df.append({'mjerenje': measurement, 'vrijeme': time}, ignore_index=True)

# Plot mjerenja
df.plot(y='mjerenje', x='vrijeme')
plt.title('Mjerenja PM10 u 2017. za Osijek')
plt.show()

# Ispis tri datuma u godini kada je koncentracija PM10 bila najveća
top_dates = df.nlargest(3, 'mjerenje')['vrijeme'].dt.date
print("Tri datuma u 2017. godini kada je koncentracija PM10 bila najveća:")
for date in top_dates:
    print(date)
