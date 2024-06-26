import pandas as pd

mtcars = pd.read_csv('mtcars.csv')

#1. Kojih 5 automobila ima najvecu potrosnju?
print("\nPet automobila s najvecom potrosnjom: \n", mtcars.sort_values(by=['mpg']).tail(5))

#2. Koja tri automobila s 8 cilindara imaju najmanju potrosnju?
osam_cil = mtcars[mtcars.cyl == 8]
print("\nTri automobila s 8 cilindara i najmanjom potrosnjom: \n", osam_cil.sort_values(by=['mpg']).head(3))

#3. Kolika je srednja potrosnja automobila sa 6 cilindara?
sest_cil = mtcars[mtcars.cyl == 6]
print("\nSrednja potrosnja automobila sa 6 cilindara: \n", sest_cil['mpg'].mean())

#4. Kolika je srednja potrosnja automobila s 4 cilindra mase izmedu 2000 i 2200 lbs?
cetiri_cil = mtcars[(mtcars.cyl == 4) & (mtcars.wt >= 2) & (mtcars.wt <= 2.2)]
print("\nSrednja potrosnja automobila s 4 cilindra mase izmedu 2000 i 2200 lbs: \n", cetiri_cil['mpg'].mean())

#5. Koliko je automobila s rucnim, a koliko s automatskim mjenjacem u ovom skupu podataka?
rucni = mtcars[mtcars['am'] == 0].am.count()
print("\nAutomobili s rucnim mjenjacem: \n", rucni)
automatski = mtcars[mtcars['am'] == 1].am.count()
print("\nAutomobili s automatskim mjenjacem: \n", automatski)

#6. Koliko je automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga?
automatskiHP = mtcars.query('am == 1 and hp > 100').am.count()
print("\nAutomobili s automatskim mjenjacem i snagom vecom od 100: \n", automatskiHP)

#7. Kolika je masa svakog automobila u kilogramima?
mtcars['kg'] = mtcars.wt*1000*0.45359237
print("\nMasa svakog automobila u kg: \n", mtcars[['car','kg']])