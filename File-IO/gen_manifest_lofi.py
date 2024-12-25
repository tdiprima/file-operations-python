# A tool for processing two CSV files based on given arguments: it validates if both files exist, reads through the lists line by line, and prints specific formatted output corresponding to 'map' or 'segmentation' type, also, it offers an optional function to replace a substring in the lines of the first file.
import os
import sys


def lo_fi(myargs):
    arrlen = len(myargs)
    my_list = myargs[0]
    image_list = myargs[1]
    manifest_type = myargs[2]
    replace_str = ''
    if arrlen == 4:
        replace_str = myargs[3]

    if not os.path.isfile(my_list):
        print("File path {} does not exist. Exiting...".format(my_list))
        sys.exit()

    if not os.path.isfile(image_list):
        print("File path {} does not exist. Exiting...".format(my_list))
        sys.exit()

    try:
        if manifest_type == 'segmentation':
            print('segmentdir,studyid,clinicaltrialsubjectid,imageid')

        if manifest_type == 'map':
            print('studyid,clinicaltrialsubjectid,imageid,filename')

        # if manifest_type == 'image':
        #     print('path,studyid,clinicaltrialsubjectid,imageid')

        with open(my_list) as fa:
            for line_a in fa:
                # Ignore blank lines
                if len(line_a.strip()) > 0:
                    if replace_str:
                        line_a = line_a.replace(replace_str, "")
                    with open(image_list) as fb:
                        next(fb)  # Skip header row
                        for line_b in fb:
                            key = line_a[:line_a.find(".")].strip()
                            val = line_b[:line_b.find(".")].strip()
                            row = line_b.strip().split(',')
                            # if key in val:
                            if key == val:
                                # print(line_b)
                                if manifest_type == 'map':
                                    print(row[1] + "," + row[2] + "," + row[3] + "," + line_a.strip())
                                if manifest_type == 'segmentation':
                                    print(line_a.strip() + "," + row[1] + "," + row[2] + "," + row[3])
                                # if manifest_type == 'image':
                                #     print(row[1] + "," + row[2] + "," + row[3] + "," + line_a.strip())
                                continue
    except Exception as ex:
        print(ex)
        sys.exit(1)


if __name__ == '__main__':
    # 1) Download httplinks.csv from PathDB
    # 2) ls -l | awk '{print $9}' > ~/myList.list
    if len(sys.argv) < 4:
        print('\nUSAGE:\n    python ' + os.path.basename(
            __file__) + ' /path/to/yourImageList.list /path/to/httplinks.csv manifest_type [map | segmentation] <optional: substring_to_replace>')
    else:
        lo_fi(sys.argv[1:])
