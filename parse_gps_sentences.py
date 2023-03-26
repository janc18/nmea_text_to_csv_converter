import pandas as pd
import sys
import os
GPGLL={
    "Latitude":[],
    "N_S Indicator":[],
    "Longitude":[],
    "E_W Indicator":[],
    "UTC time":[],
    "Status":[],
    "Mode":[],
    "Checksum":[]
    }
GPRMC={
    "UTC time":[],
    "Status":[],
    "Latitude":[],
    "N_S Indicator":[],
    "Longitude":[],
    "E/W Indicator":[],
    "Speed over ground":[],
    "Course over ground":[],
    "Date":[],
    "Magnetic variation,degrees":[],
    "Magnetic variation,direction":[],
    "Mode":[],
    "Checksum":[]
}
GPVTG={
    "Course":[],
    "Reference":[],
    "Course2":[],
    "Reference2":[],
    "Speed(knots)":[],
    "Unit(knots)":[],
    "Speed(kilometers)":[],
    "Unit(kilometers)":[],
    "Mode":[],
    "Checksum":[]
}
GPGGA={
    "UTC time":[],
    "Latitude":[],
    "N_S Indicator":[],
    "Longitude":[],
    "E_W Indicator":[],
    "Position Fix Indicator":[],
    "Satellites used":[],
    "HDOP":[],
    "MSL Altitude":[],
    "Units(MSL)":[],
    "Geoid separation":[],
    "Units(Geoid)":[],
    "Age of diff. corr":[],
    "Diff.ref.station ID":[],
    "Checksum":[]
}
    
def fill_x_list(gps_sentence,listf):

    data=open(sys.argv[1],'r')
    count=0
    while True:

        line=data.readline()
        line=line.strip()

        if (line[:6]==gps_sentence):
            count+=1

            line=line.split(',',-1)
            checksum= line[-1].split("*")[1]
            line[-1] =line[-1].split("*")[0]
            line.append(checksum)

            for i in range(1,len(line)):
                namekey=tuple(listf.items())[i-1][0]
                listf[namekey].append(line[i])

        if not line:
            break
    
    print("Quantity of:",gps_sentence,'sentences',str(count),sep=None)
    data.close()
    return listf

GPVTG=fill_x_list("$GPVTG",GPVTG)
GPGGA=fill_x_list("$GPGGA",GPGGA)
GPMRC=fill_x_list("$GPRMC",GPRMC)
GPGLL=fill_x_list("$GPGLL",GPGLL)

save_path=sys.argv[2]+'/output/'

if not os.path.exists(save_path):
    os.makedirs(save_path)

data_csv=pd.DataFrame.from_dict(data=GPGLL,orient='index')
o=data_csv.T
o.to_csv(save_path+'GPGLL.csv')
data_csv=pd.DataFrame.from_dict(data=GPVTG,orient='index')
o=data_csv.T
o.to_csv(save_path+'GPVTG.csv')
data_csv=pd.DataFrame.from_dict(data=GPMRC,orient='index')
o=data_csv.T
o.to_csv(save_path+'GPMRC.csv')
data_csv=pd.DataFrame.from_dict(data=GPGGA,orient='index')
o=data_csv.T
o.to_csv(save_path+'GPGGA.csv')
