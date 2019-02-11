import csv
import os

def write_csv(row,path):
    if(os.path.exists(path)):
        with open(path, 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
    else:
        with open(path, 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(["Start Time","End Time","Latitude","Longitude"])
            writer.writerow(row)
        csvFile.close()

def srt_to_csv(file='./videos/DJI_0301.SRT'):
    if(os.path.exists(file) == False):
        print("File not found!")

    else:
        path = './files/'+((file.split('/')[-1]).split('.')[0])+'.csv'
        if(os.path.exists(path)):
            os.remove(path)

        f = open(file,'r')
        l = f.read().split('\n\n')
        l.pop(len(l)-1)
        dic = {}

        for i in l:
            subl = i.split('\n')
            time = subl[1]
            coord = subl[2]
            start,end = time.split('-->')
            lon,lat,_ = coord.rstrip().split(',')
            write_csv([start.strip(' '),end.strip(' '),lat,lon],path)

if __name__ == '__main__':
    srt_to_csv()
