# skylark-assignment

Technical Assignment for the role of Software Developer @ **Skylark Drones**

## Setting Up

 - `virtualenv -p python3 ./env`
 - `source env/bin/activate` 
 -  `pip install -r requirements.txt`

## Task 1

For every second in the video, a list of all the images that lie within "v" metres of the drone position in ".csv" format.
Drone positions at every second of time given in a ".srt" file.

### How to run

    python task1.py --file <PATH_TO_SRT_FILE> --vicinity <VALUE_OF_V_IN_METRES>

## Task 2

From an "assets.csv" file of some points of interest for the client, a list of all images within "v" meters of these POIs in ".csv" format.

### How to run

    python task2.py --file <PATH_TO_ASSET_FILE> --vicinity <VALUE_OF_V_IN_METRES>

## Task 3

Given a ".srt" file containing the drone positions at every point of time, return a KML of the drone path.

### How to run

    python task3.py --file <PATH_TO_SRT_FILE>

## Outputs

All output files can be found in the "output" directory.

## Notes

 - This project uses two third party libraries:
	 - piexif: To read encoded EXIF data from images.
	 - simplekml: To create KML mapping of the drone path.<br> <br>
	Future prospects include eliminating these external dependencies.
 - To find help on the command line arguments for any of the files, run:
	 
	 `python <FILENAME>.py -h`
