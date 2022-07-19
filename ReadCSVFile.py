import csv
from geopy.distance import geodesic


def calculatedistance(lat,long):
    citycenter = (41.881832, -87.623177)
    return (geodesic(citycenter, (lat,long)).miles)

with open(r'C:\Users\roarl\Downloads\Chicago_Public_Schools_-_School_Progress_Reports_SY2122.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    schoolrowlist = []
    schoollist = []
    coordlist = []
    for row in csv_reader:
        if line_count == 0:
            columnliststring = str(", ".join(row))
            columnlist = list(columnliststring.split(', '))
            line_count += 1
        else:
            if (row[columnlist.index('SAT_Grade_11_Score_School_Avg')]) != '':
                if int(row[columnlist.index('SAT_Grade_11_Score_School_Avg')]) > 0:
                    if int(row[columnlist.index('SAT_Grade_11_Score_School_Avg')]) <= 1600:
                        schoollist.append(row[columnlist.index('Long_Name')])
                        schoolrowlist.append(line_count)
            line_count += 1
    for school in schoollist:
        schoolrow = schoolrowlist[schoollist.index(school)]
        templist = [school]
        templist.append(schoolrowlist[columnlist.index('School_Latitude')])
        templist.append(schoolrowlist[columnlist.index('School_Longitude')])
##        templist.append(calculatedistance(schoolrowlist[columnlist.index('School_Latitude')], schoolrowlist[columnlist.index('School_Longitude')]))
        schoollist[schoolrow-1] = templist
print(schoollist)