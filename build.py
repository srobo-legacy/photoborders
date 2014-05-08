

teams=[
#["TLA","school name","given name"]
["HSO","Headdington School","HSO","1st"]
]


import os

for team in teams:
	#alter svg names
	os.system("cat background.svg | sed 's/School Name/"+team[1]+"/' | sed 's/Team Name/"+team[2]+"/' > build/"+team[0]+".svg")
	#add SR logo
	#add Photo
	#convert to noce format

