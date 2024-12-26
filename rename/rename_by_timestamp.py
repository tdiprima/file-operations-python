"""
Read the metadata of all files in my directory, such as the date and time,
and then rename the files according to their creation date and time.
The resulting file name will be in the format: YYYY-MM-DD_HH:MM:SS_file_name
"""
import datetime
import os

for file in os.listdir("."):
    if os.path.isfile(file):
        # Get creation time
        seconds_since_epoch = os.path.getctime(file)

        # Format it
        timestamp = datetime.datetime.fromtimestamp(seconds_since_epoch)
        short = timestamp.strftime("%Y-%m-%d_%H:%M:%S")

        # KNOW BEFORE YOU GO!
        print(file, f"{short}_{file}")

        # Rename file
        # os.rename(file, f"{created}_{file}")
