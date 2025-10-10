import fnmatch
import os


def music_finder(root, extension):
    for path, directories, files in os.walk(root):
        for emp3 in fnmatch.filter(files, '*.{}'.format(extension)):
            new_path = os.path.abspath(path)
            yield os.path.join(os.path.normpath(new_path), emp3)


my_music = music_finder('C:/Users/mateu/IdeaProjects/genexample/musicFiles/music', 'emp3')

for s in my_music:
    print(s)
