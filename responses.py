import csv

with open('resp2.csv') as f:
	mread=csv.DictReader(f)
	overall=[]
	for row in mread:
		# each team is a row
		
		if row['Team or Individual?']=='Team':
			#process Team
			l=[]
			d_cap={}
			d_cap['Cup Type']=row["Northwestern World Cup (32 team) or Women's World Cup?"]
			d_cap['Team Affiliation?']=row['Team Affiliation? ']
			d_cap['Team Level']=row['Team Level ']
			d_cap["Captain's Name"]=row["Captain's Name "]
			d_cap["Captain's Email"]=row["Captain's Email"]
			d_cap["Ex-Club"]=row['Has the Captain ever been on the Northwestern Club Soccer roster?']
			d_cap['Player Name']=row["Captain's Name "]
			d_cap['Player Email']=row["Captain's Email"]
			

			l.append(d_cap)
			for i in xrange(2,17):
				if not(row["Player "+str(i)+" Name"]=="" and row["Player "+str(i)+" Email"]==""):

					d={}
					d['Cup Type']=row["Northwestern World Cup (32 team) or Women's World Cup?"]
					d['Team Affiliation?']=row['Team Affiliation? ']
					d['Team Level']=row['Team Level ']
					d["Captain's Name"]=row["Captain's Name "]
					d["Captain's Email"]=row["Captain's Email"]
					club_str="Has Player "+str(i)+" ever been on the Northwestern Club Soccer roster?"
					d["Ex-Club"]=row[club_str]
					d['Player Name']=row["Player "+str(i)+" Name"]

					d['Player Email']=row["Player "+str(i)+" Email"]
					
					l.append(d)

			overall.append(l)

		elif row['Team or Individual?']=='Individual':
			#process Individual
			pass

with open('players.csv', 'w') as writef:
    fieldnames = ['Cup Type','Team Affiliation?','Team Level',"Captain's Name","Captain's Email","Ex-Club","Player Name", "Player Email"]
    writer = csv.DictWriter(writef, fieldnames=fieldnames)
    writer.writeheader()
    
    for teamList in overall:
    	#teamList is a list of dicts
    	for playerDict in teamList:
    		#playerDict is a dict of player info
    		writer.writerow(playerDict)







