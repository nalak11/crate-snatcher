import chunk
import sys
import shutil
import eyed3
import os
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
            print("usage: [source_directory] [comparison_directory] [backup_directory][OPTIONS]")
            print("options: \n -b : copy to backup directory\n -h : show help")
            return

    if len(sys.argv) < 4:
        print("not enough args. use -h for usage help")
        return

    for index, arg in enumerate(sys.argv, 1):
        if index == 1:
            continue
        if path.exists(arg) == 0 or path.isdir(arg) == 0:
            print("error: argument " + str(index) + " " + arg + " is not a valid directory")

    if len(sys.argv) == 5:
        option = sys.argv[4]

    src_dir = sys.argv[1]
    comp_dir = sys.argv[2]
    bak_dir = sys.argv[3]

    print("src_dir: " + src_dir)
    print("comp_dir: " + comp_dir)
    print("bak_dir: " + bak_dir)

    # begin directory analysis

    for dirName, subdirList, fileList in os.walk(comp_dir):
        print("Found directory: %s" % dirName)
        tracklist = [Track(path.join(dirName, fname)) for fname in fileList]

    return


class Track:

    """Track class represents a specific audio file, with easily accessible data"""

    def __init__(self, fpath):

        self.path = fpath;
        self.fext = path.splitext(fpath)[1].lower()[1:]
        self.fname = path.splitext(path.split(fpath)[1])[0]

        if self.fext == "mp3":
            self.info = get_mp3info(fpath)
            if self.info:
                print(self.info)

        elif self.fext == "wav":
            self.tags = parse_wavtags(fpath)

        elif self.fext == "flac":
            self.tags = parse_flactags(fpath)






def track_comp(fsrc_dir, fcomp_dir, comp_fname):
    dup_path = "NOT FOUND"
    print("finding mp3 %s" % comp_fname)

    for dirName, subdirList, fileList in os.walk(fsrc_dir):
            for src_fname in fileList:
                comp_f = eyed3.load(path.join(fcomp_dir, comp_fname))
                src_f = eyed3.load(path.join(dirName, src_fname))
                # if comp_f.tag.artist == src_fname:


    return dup_path

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

def parse_flactags(fpath):
    pass

def parse_wavtags(fpath):
    pass

if __name__ == "__main__":
    main()
