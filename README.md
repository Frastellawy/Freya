# Freya
Freya is an app for downloading, unzipping and converting multiple files at once.
Initially designed to download and work with satellite images from the Creodias Finder website.

## Installing
Download the Python 3 installer package from the official website and install it, if not installed previously.

Run the following commands in the terminal to install required libraries
```
pip install requests
pip install requests
pip install Pillow
```
## Running the application
Download GUI.py, main.py, paths.txt and urls.txt files from repository. Run the **main.py** file just as any other Python script (.py).

## First run
When you run the app for the first time you must specify the paths to the appropriate folders.
Select "Paths" from the menu bar and specify paths as following:
* **Download** - path to folder, where downloaded .zip files will be stored.
* **Unpack** - path to folder, where .zip files from **Download Path** will be unpacked.
* **Convert** - path to folder with files you want to convert to different type.

## Downloading files
Open the **urls.txt** file and paste into it the paths to download data obtained from the https://finder.creodias.eu (also works with other download paths not obtained from that website).

Click on the **Downloading Files** button and wait until it's all done.

## Unpacking Files
Click on the **Unpacking Files** button. All .zip files contained in the Download folder will be unpacked and stored in Unpack directory.
After it's done you can choose whether you want to remove all .zip files or keep them.

## Converting Files
Make sure your Converting folder contain all files you want to convert (e.g. .tif files).
Click on the **Converting Files** button.
Enter the file types you want to convert and the file types you want to covert to (e.g .tif to .jpg). Click **OK** button to accept and wait until all files will be converted.


## Author
* **Frastellawy**
