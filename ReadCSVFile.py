import csv
import numpy
from geopy.distance import geodesic
import seaborn

def calculatedistance(lat,long):
    citycenter = (41.881832, -87.623177)
    return (geodesic(citycenter, (lat,long)).miles)

with open('Chicago_Public_Schools_-_School_Progress_Reports_SY2122.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    schoollist = []
    x = []
    y = []
    for row in csv_reader:
        if line_count == 0:
            columnliststring = str(", ".join(row))
            columnlist = list(columnliststring.split(', '))
            line_count += 1
        else:
            if (row[columnlist.index('SAT_Grade_11_Score_School_Avg')]) != '':
                if int(row[columnlist.index('SAT_Grade_11_Score_School_Avg')]) > 0:
                    if int(row[columnlist.index('SAT_Grade_11_Score_School_Avg')]) <= 1600:
                        schoollist.append([row[columnlist.index('Long_Name')],(calculatedistance((float(row[columnlist.index('School_Latitude')])),(float(row[columnlist.index('School_Longitude')])))),int(row[columnlist.index('SAT_Grade_11_Score_School_Avg')])])
                        y.append(int(row[columnlist.index('SAT_Grade_11_Score_School_Avg')]))
                        x.append((calculatedistance((float(row[columnlist.index('School_Latitude')])),(float(row[columnlist.index('School_Longitude')])))))
            line_count += 1
    x = numpy.array(x).reshape((-1,1))
    y = numpy.array(y)
    seaborn.regplot(x=x,y=y)


