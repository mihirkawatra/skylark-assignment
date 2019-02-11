import simplekml
import csv
import os
from utils.srt_to_csv import srt_to_csv
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Path to the .srt file containing drone flight path.", default='./videos/DJI_0301.srt')

output_path = "./output/points.kml"

def kmlFunction(srt='./videos/DJI_0301.srt'):
    srt_path = './files/'+((srt.split('/')[-1]).split('.')[0])+'.csv'

    if(os.path.exists(srt_path) == False):
        srt_to_csv(srt)

    if(os.path.exists(output_path)):
        os.remove(output_path)

    kml = simplekml.Kml(name="DronePathKML")

    with open(srt_path, 'r') as srtfile:
        srt_reader = csv.DictReader(srtfile)
        for point in srt_reader:
            kml.newpoint(coords= [(float(point["Latitude"]),float(point["Longitude"]))])

    kml.save(output_path)

if __name__ == '__main__':
    args = parser.parse_args()
    kmlFunction(srt=args.file)
