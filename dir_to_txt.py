from os import listdir
from os.path import isfile, join

PLAYLIST_PATH = ''
all_files = [f for f in listdir(PLAYLIST_PATH) if isfile(join(PLAYLIST_PATH, f))]

with open('playlist.txt', 'w') as f:
    for item in all_files:
        f.write("%s\n" % item)
