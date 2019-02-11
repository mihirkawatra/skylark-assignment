from utils.haversine import haversine
from utils.img_to_csv import img_to_csv
from utils.srt_to_csv import srt_to_csv
import csv
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Path to the .srt file containing drone flight path.", default='./videos/DJI_0301.srt')
parser.add_argument("-v", "--vicinity", help="Vicinity of points. Default value set to 35 metres.", default=35)

output_path = './output/task1.csv'
img_path = './files/img_data.csv'

def write_csv(row, vicinity):
    if(os.path.exists(output_path)):
        with open(output_path, 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
    else:
        with open(output_path, 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(["Start Time","End Time","List of points in vicinity of " + str(vicinity) + " metres"])
            writer.writerow(row)
        csvFile.close()

def task1(srt='./videos/DJI_0301.srt',vicinity=35):
    srt_path = './files/'+((srt.split('/')[-1]).split('.')[0])+'.csv'

    if(os.path.exists(output_path)):
        os.remove(output_path)

    if(os.path.exists(srt_path) == False):
        srt_to_csv(srt)

    if(os.path.exists(img_path) == False):
        img_to_csv()

    with open(srt_path, 'r') as srtfile:
        srt_reader = csv.DictReader(srtfile)
        for point in srt_reader:
            l = ""
            with open(img_path, 'r') as imgfile:
                img_reader = csv.DictReader(imgfile)
                for img in img_reader:
                    if((haversine([float(point["Latitude"]),float(point["Longitude"])],[float(img["Latitude"]),float(img["Longitude"])])*1000)<=int(vicinity)):
                            l = l+str(img["Image Name"])+", "
                write_csv([point["Start Time"],point["End Time"], l[:-2]],vicinity)

if __name__ == '__main__':
    args = parser.parse_args()
    task1(srt=args.file,vicinity=float(args.vicinity))
