import random
loh=[
    'First layer: Limbo',
    'Second layer:Lust',
    'Third layer:Gluttony',
    'Fourth layer:Greed',
    'Fifth layer:Anger',
    'Sixth layer:Heresy',
    'Seventh layer:Violence',
    'Eighth layer:Fraud',
    'Ninth layer:Treachery',
    'Tenth layer:Heaven'#Heaven is a part of hell cause we can't have nice things.
]

#loha=random.randint(0,len(loh)-1)
dag= 0 
dagar = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"]
for i in range(0,7):
    loha=random.randint(0,len(loh)-1)
    print(f"{dagar[dag].capitalize()} ")
    print(f"{loh[loha]}\n")
    dag+= 1