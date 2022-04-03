import csv
rows=[]
with open('dwarf_stars.csv',"r") as f:
  csv_reader=csv.reader(f)
  for row in csv_reader:
    rows.append(row)
headers=rows[0]   
planet_data_rows=rows[1:]
print(headers)
print(planet_data_rows[1]) 


temp_list=list(planet_data_rows)
for planet_data in temp_list:
  star_mass=planet_data[3]
  if star_mass.lower()=='unknown':
     planet_data_rows.remove(planet_data)
  
with open('final.csv',"a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerow(planet_data_rows)   