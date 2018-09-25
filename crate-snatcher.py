import sys
import shutil
from taglib import tagopen, InvalidMedia, ValidationError
import os
from librosa import beat

from os import path

def main():

    # DEBUGGING CODE

    print("\nDEBUG:\n\n")

    for index, args in enumerate(sys.argv):
        print(str(index) + ": " + args)
    print("number of args: " + str(len(sys.argv)))

    print("\n\n----END DEBUG----\n\n")

    # END DEBUGGING CODE

    # parse command line args

    if len(sys.argv) == 2:
        if sys.argv[1] == "-h":
            print("usage: [library_directory] [current_directory] [backup_directory][OPTIONS]")
            print("options: \n -b : copy to backup directory\n -h : show help")
            return

    if len(sys.argv) < 4:
        print("not enough args. use -h for usage help")
        return

    for index, arg in enumerate(sys.argv, 1):
        if index == 1:
            continue
        if path.exists(arg) == 0 or path.isdir(arg) == 0:
            print("error: argument " + str(index) + " \"" + arg + "\" is not a valid directory")
            exit(1)

    if len(sys.argv) == 5:
        option = sys.argv[4]

    library_dir = sys.argv[1]
    current_dir = sys.argv[2]
    backup_dir = sys.argv[3]

    print("library_dir: " + library_dir)
    print("current_dir: " + current_dir)
    print("backup_dir: " + backup_dir)

    # begin directory analysis

    for dirName, subdirList, fileList in os.walk(current_dir):
        print("Found directory: %s" % dirName)
        for fname in fileList:
            ext = path.splitext(fname)[1].lower()
            if ext == (".mp3" or ".wav" or ".flac"):
                print(path.join(dirName, fname))
                Track(path.join(dirName, fname))
            else:
                continue
    return


class Track:

    """Track class represents a specific audio file"""

    def __init__(self, fpath):

        self.path = fpath;
        self.fext = path.splitext(fpath)[1].lower()[1:]
        self.fname = path.splitext(path.split(fpath)[1])[0]

        self.tag = tagopen(fpath, readonly=False)

        for k, info in self.tag.items():
            print(k + ": ",  info)






def track_comp(fsrc_dir, fcomp_dir, comp_fname):
    pass

def get_mp3info(fpath):
    """Retrieves basic track information for the mp3 from ID3 tag
    returns a dictionary
    Parameters: fpath [FILEPATH]"""

    eyed3.log.setLevel("ERROR")
    try:
        f = eyed3.load(fpath)
        info = {
            "Artist": f.tag.artist,
            "Title": f.tag.title,
            "Album": f.tag.album,
            "Album Artist": f.tag.album_artist,
            "Track No.": f.tag.track_num
        }
    except ValueError as error:
        print(str(error) + " with track: %s" % path.split(fpath)[1])
        return 0

    return info

if __name__ == "__main__":
    main()
