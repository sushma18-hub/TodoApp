# import shutil
# shutil is limited wont allow to slect folder so using zipfile directory
import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    # pathlib used to concatinate the path
    dest_path = pathlib.Path(dest_dir,"comprsed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:

        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            # arcname is used to extract only the finalpath name i.e 1.txt, if it is not used
            # all the complete path it will consider and create the zip folder
            archive.write(filepath, arcname=filepath.name)


if __name__ =="__main__":
    make_archive(filepaths=["1.txt","2.txt"],dest_dir="dest")