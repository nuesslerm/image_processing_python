from sys import argv, exit
from os.path import join, isdir, isfile, splitext
from os import getcwd, makedirs, walk, listdir
import re
from PIL import Image

# grab the first and second argument using sys
# check if new folder exists
# loop through folder and convert images to png
# save to new folder


def assess_input_errors(args):
    if len(args[1:]) != 2:
        print("please provide folderpath to convert + new folderpath")
        return True
    return False


def get_input_args(args):
    folder_to_convert = args[1]
    new_folder_name = args[2]

    # return value is going to be a tuple (folder_to_convert, new_folder_name),
    # which can be unpacked later
    return folder_to_convert, new_folder_name


def get_verified_path(folder_to_convert):
    abs_path_pattern = re.compile(r"^/Users")

    # untested change
    path_to_check = (
        folder_to_convert
        if abs_path_pattern.search(folder_to_convert)
        # else join(getcwd(), folder_to_convert.replace("./", ""))
        else folder_to_convert
    )

    if not isdir(path_to_check):
        print(
            "First arg needs to be folder that contains jpg files.\n"
            + "Please provide absolute folder path or a relative path from current directory"
        )
        return None
    return path_to_check


def get_list_of_jpg(dir):
    # https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
    # os.listdir() will get you everything that's in a directory - files and directories.
    # onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    list_of_jpg = [join(dir, f) for f in listdir(dir) if isfile(join(dir, f))]

    # list_of_jpg = []
    # for (_, _, filenames) in walk(folder_to_convert):
    #     for filename in filenames:
    #         list_of_jpg.append(join(folder_to_convert, filename))
    #     break

    return list_of_jpg


def create_new_folder(new_folder_name):
    # untested change
    # new_folder = join(getcwd(), new_folder_name)
    new_folder = new_folder_name

    if isdir(new_folder):
        return new_folder

    try:
        makedirs(new_folder)
        return new_folder
    except OSError:
        return None


def convert_files_to_png(list_of_jpg, new_folder_name):
    filename_pattern = re.compile(r"[^\/]+(?=\.)")

    try:
        counter = 0
        for jpg_path in list_of_jpg:
            jpg = Image.open(jpg_path)
            clean_name = filename_pattern.findall(jpg_path)[0]
            # splitext returns a tuple where index 0 is the filepath up to the filename .
            # second index is going to be the file extension, .e.g. ".jpg"
            # clean_name = splitext(jpg_path)[0]
            jpg.save(f"{new_folder_name}/converted_{clean_name}.png")
            print(f"{clean_name} file was converted")
            counter += 1
        return counter
    except:
        return None


def main():
    if assess_input_errors(argv):
        exit()

    folder_to_convert, new_folder_name = get_input_args(argv)

    folder_to_convert = get_verified_path(folder_to_convert)
    new_folder = create_new_folder(new_folder_name)

    if not (folder_to_convert or new_folder):
        exit()

    list_of_jpg = get_list_of_jpg(folder_to_convert)

    num_converted_images = convert_files_to_png(list_of_jpg, new_folder)

    if type(num_converted_images) == int and num_converted_images != 0:
        print(f"{num_converted_images} have been converted successfully")
    elif type(num_converted_images) == int and num_converted_images == 0:
        print("There were no images to convert. The new folder is empty.")
    else:
        print("There has been an error converting your images")


if __name__ == "__main__":
    main()