import os
files = os.listdir('./images')

from PIL import Image,ExifTags
count=0
fail=[]
for path in files:
    try:
        image = Image.open('./images/'+path)
        exif = { ExifTags.TAGS[k]: v for k, v in image._getexif().items() if k in ExifTags.TAGS }
        print(exif)
        print("-----------------------------------------------------------")
        count+=1
    except:
        fail.append(path)
        continue
print(count)
print(len(files))
print(fail)
# import exiftool
# print(files)
# with exiftool.ExifTool() as et:
#    for f in files:
#        metadata = et.get_tags(f)
#        print(metadata)
#        print("-----------------------------------------------------------")
# for d in metadata:
#     print("{:20.20} {:20.20}".format(d["SourceFile"],d["EXIF:DateTimeOriginal"]))

# import pyexiv2
# #for f in files:
# f = files[0]
# metadata = pyexiv2.ImageMetadata(f)
# print(metadata.read())
# print(metadata.exif_keys)
