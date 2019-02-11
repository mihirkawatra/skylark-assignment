from utils.haversine import haversine
from utils.img_to_csv import img_to_csv
from utils.srt_to_csv import srt_to_csv
import csv
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Path to the .csv file containing the assets and their coordinates.", default='./files/assets.csv')
parser.add_argument("-v", "--vicinity", help="Vicinity of points. Default value set to 50 metres.", default=50)

output_path = './output/task2.csv'
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
            writer.writerow(["Asset Name","List of points in vicinity of " + str(vicinity) + " metres"])
            writer.writerow(row)
        csvFile.close()

def task2(asset_path='./files/assets.csv',vicinity=50):

    if(os.path.exists(output_path)):
        os.remove(output_path)

    if(os.path.exists(img_path) == False):
        img_to_csv()

    with open(asset_path, 'r') as assetfile:
        asset_reader = csv.DictReader(assetfile)
        for point in asset_reader:
            l = ""
            with open(img_path, 'r') as imgfile:
                img_reader = csv.DictReader(imgfile)
                for img in img_reader:
                    if((haversine([float(point["latitude"]),float(point["longitude"])],[float(img["Latitude"]),float(img["Longitude"])])*1000)<=int(vicinity)):
                            l = l + str(img["Image Name"]) + ", "
                write_csv([point["asset_name"],l[:-2]],vicinity)

if __name__ == '__main__':
    args = parser.parse_args()
    task1(srt=args.file,vicinity=float(args.vicinity))
