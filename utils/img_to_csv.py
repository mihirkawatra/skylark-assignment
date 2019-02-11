import piexif
import os
import csv

def decimal_degrees(d):
    lat = d[2]
    lon = d[4]
    lat = float(lat[0][0]/lat[0][1]) + float(lat[1][0]/lat[1][1]/60.0) + float(lat[2][0]/lat[2][1]/3600.0)
    lon = float(lon[0][0]/lon[0][1]) + float(lon[1][0]/lon[1][1]/60.0) + float(lon[2][0]/lon[2][1]/3600.0)
    lat = -1*lat if d[1].decode() == 'S' else lat
    lon = -1*lon if d[3].decode() == 'W' else lon
    return lat,lon

def write_csv(row, filepath):
    if(os.path.exists(filepath)):
        with open(filepath, 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
    else:
        with open(filepath, 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(["Image Name","Latitude","Longitude"])
            writer.writerow(row)
        csvFile.close()

def img_to_csv():
    fail=[]
    filepath = './files/img_data.csv'
    files = os.listdir('./images')
    for i in files:
        if(i.split('.')[-1] not in ['jpg','JPG','jpeg','JPEG','png','PNG']):
            files.remove(i)

    if(os.path.exists(file_path)):
        os.remove(file_path)

    for path in files:
        try:
            print(path)
            exif_dict = piexif.load('./images/'+path)
            lat,lon = decimal_degrees(exif_dict["GPS"])
            # print(lat,lon)
            write_csv([path,lat,lon],filepath)
            print("-------------------------------------------")
        except:
            fail.append(path)
            continue

    if(len(fail)!=0):
        print("Following files have failed: ")
        print(fail)

    return(len(fail))

if __name__ == '__main__':
    img_to_csv()
