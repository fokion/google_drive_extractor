# Google drive extractor

Extract and migrate photos and videos when you takeout your data from Google.

---

![Python application](https://github.com/fokion/google_drive_extractor/workflows/Python%20application/badge.svg)

---
This is a personal project that I did in order to extract my 60GB of Google Drive data to OneDrive and to my NAS.

By default, it should treat most of the video and image extensions that I had ok but feel free to make a PR to add more.



## Known Limitations

If you have done an edit in Google Photos the photo that is edited has the same name but with a suffix that is incremented by the amount of times that you have edited it. This is not taken into account by this script and copies everything

## Usage 
You give the input directory which contains all the `takeout-*.zip` files and an output directory where it will export all the files from those zips
```bash
python extractor.py  -i <input directory> -o <output directory> -e <extensions file>
```

- `e` Extensions file a line separated list of extensions that we want to take into consideration ( see in tests an example of it)
