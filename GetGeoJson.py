import os
import argparse

parser = argparse.ArgumentParser(description="File-path")
parser.add_argument("path")
args = parser.parse_args()

os.system("ls "+args.path+"/*/*.shp > shp_list.txt")
f = open("shp_list.txt", "r")
line2 = f.readlines()
f.close()


for line in line2:
    filename = line
    jsonname = line.replace(".shp",".json")
    filename = filename.replace("\n","")
    jsonname = jsonname.replace("\n","")
    command = 'ogr2ogr -lco "ENCODING=UTF-8" -f GeoJSON '+jsonname+" "+filename
    print(command)
    os.system(command)