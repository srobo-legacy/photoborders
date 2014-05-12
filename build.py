

teams=[
["BRK","Brockenhurst College","Team Brocket",""],
["BWS","Bishop Wordsworth School","Someone Else's Swag Lab",""],
["CLF","Clifton High School","Team Ninja Bot","Joint 3rd Place"],
["CLY","Collyers Sixth Form College","Team Collyer's",""],
["GRD","Gordano School","Team GRD","2nd Place"],
["GRS","Greshams School","Gresham's Robotics",""],
["GYG","Guernsey Grammar School","",""],
["HRS","Hills Road Sixth Form College","Systemetric",""],#"Robot and Team Image Award"],
["HSO","Headington School","HSO","1st Place"],
["ICE","Iceni Academy","Team ICE",""],
["KES","King Edward VI School","Team KES",""],
["KHS","Kingsbury High School","Team KHS",""],
["MAI2","Gymnasium Markt Indersdorf","No English Available",""],
["MFG","Mirfield Free Grammar","MFG Robotics",""],
["PAG","Pate's Grammar School","WAYNE Robotics",""],
["PSC","Peter Symonds College","The Astromechs",""],#"Online Presence Award"],
["QMC","Queen Mary's College","Team QMC",""],
["RED","Redland Green School","RED",""],
["RGS","Royal Grammar School, Guildford","",""],
["RUN","Runshaw College","Colossal Denominators","Joint 3rd Place"],
["SWI","South Wilts Grammar School for Girls","Team GB (Geoffry Bourne)",""],
["TBG","Torquay Boys Grammar School","Team TBG",""],#"Rookie Award and First Robot Movement Award"],
["TWG","Tunbridge Wells Grammar School for Boys","Team TWG",""]
]

from PIL import Image
from lxml import etree
import os

for team in teams:
	#alter svg names
	pipe = ""
	if not team[3]=="":
		pipe +="| sed \"s/School Name/"+team[1]+" ("+team[3]+")/\" "
	else:
		pipe +="| sed \"s/School Name/"+team[1]+"/\" "
	pipe +="| sed \"s/Team Name/"+team[2]+"/\" "

	#calculate photo dimensions
	image_file = "photos/"+team[0]+".jpg"
	img = Image.open(image_file)
	width, height = img.size

	ratio=450.00/height
	newwidth=width*ratio
	newheight=height*ratio
	print "Img Height:",newheight
	print "Img Width:",newwidth

	#image loaction
	bgwidth=1052.3622
	bgheight=744.09448
	imglocx=(bgwidth-newwidth)/2
	print "Img Location:",imglocx

	#change image size and location and set to team photo
	pipe +="| sed 's/width=\"679.41174\"/width=\""+str(newwidth)+"\"/' "
	pipe +="| sed 's/x=\"189.68349\"/x=\""+str(imglocx)+"\"/' "
	pipe +="| sed 's/HSO.JPG/"+team[0]+".jpg/'"

	# perform replacements
	print pipe
	os.system("cat background.svg "+pipe+" > build/"+team[0]+".svg")

	#convert to noce format
	os.system("inkscape -d 600 -f build/"+team[0]+".svg -e out/"+team[0]+".jpg" )
