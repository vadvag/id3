import os


class MP3Format:
    def __init__(self, name, path):
        self.name = name + '.mp3'
        self.path = path

    version = ['ID3v1', 'ID3v2']

    def get_current_folder(self):
        return os.getcwd()

    def read_tags(self):
        with open(self.show_full_file_path(), 'rb') as this_track:
            this_track.read()

    def show_full_file_path(self):
        return '{}/{}'.format(os.getcwd(), self.name)


mp3_track = MP3Format('Китай', 'Romantic collection')

# Путь к текеущему каталогу
# https://docs.python.org/3/library/os.html#module-os
print(mp3_track.get_current_folder())
print(mp3_track.show_full_file_path())
print(mp3_track.read_tags())

