import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel(r"C:\Users\Eigenaar\OneDrive - Montessori Scholengemeenschap Amsterdam\act\Leerjaar 1\Bits Of You\BitsOfYou.github.io\data.xlsx")

keerGecheckt = data["Hoeveel keer"]
keerCijferGekregen = data["Nieuw cijfer(s)?"]
keerIngeschreven = data["Ingeschreven?"]
keerWijziging = data["Wijziging?"]
dagen = ["Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag"]
gechecktDict = {"Dag": dagen, "Hoeveel keer gecheckt": [keerGecheckt[0], keerGecheckt[1], keerGecheckt[2], keerGecheckt[3], keerGecheckt[4]]}
cijferDict = {"Dag": dagen, "Hoeveel cijfers gekregen": [keerCijferGekregen[0], keerCijferGekregen[1], keerCijferGekregen[2], keerCijferGekregen[3], keerCijferGekregen[4]]}
wijzigingDict = {"Dag": dagen, "Hoevaak een wijziging": [keerWijziging[0], keerWijziging[1], keerWijziging[2], keerWijziging[3], keerWijziging[4]]}
ingeschrevenDict = {"Dag": dagen, "Hoevaak ingeschreven": [keerIngeschreven[0], keerIngeschreven[1], keerIngeschreven[2], keerIngeschreven[3], keerIngeschreven[4]]}

dfCheck = pd.DataFrame(gechecktDict)
dfCijfer = pd.DataFrame(cijferDict)
dfWijziging = pd.DataFrame(wijzigingDict)
dfIngeschreven = pd.DataFrame(ingeschrevenDict)

checkPNG = dfCheck.plot(kind="line", x="Dag", y="Hoeveel keer gecheckt").get_figure()
cijferPNG = dfCijfer.plot(kind="line", x="Dag", y="Hoeveel cijfers gekregen").get_figure()
wijzigingPNG = dfWijziging.plot(kind="line", x="Dag", y="Hoevaak een wijziging").get_figure()
ingeschrevenPNG = dfIngeschreven.plot(kind="line", x="Dag", y="Hoevaak ingeschreven").get_figure()

checkPNG.savefig("grafiekCheck.png")
cijferPNG.savefig("grafiekCijfer.png")
wijzigingPNG.savefig("grafiekWijziging.png")
ingeschrevenPNG.savefig("grafiekIngeschreven.png")