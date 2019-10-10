import csv
from collections import Counter, defaultdict, namedtuple
from pprint import pprint as pp


class Lp3DataAnalyser():
    """
    Class to store data of the lp3 charts exported from the CSV file.
    Data will be used to perform various analysis like most common 
    TOP 1 artist, song etc. 
    """
    def __init__(self, data):
        self.data = data

    def get_top_1(self):
        """
        Extracts all songs raned as TOP 1 from csv and stores them in a
        dictionary where artist is a key and song is a value (named tuple
        with position included). 
        """
        artists = defaultdict(list)
        Song = namedtuple("Song", "song position")
        with open(self.data, encoding='utf-8') as f:
            for line in csv.DictReader(f):
                position = int(line['Pozycja'])
                if position == 1:
                    artist = line['Wykonawca']
                    song = line['Piosenka']
                    s = Song(song=song, position=position)
                    artists[artist].append(s)
        return artists

    def most_common_top_1_song(self, data):
        """
        Counts how often songs apeared on the 1st place.
        Returns songs ranked from most common. 
        """
        top_songs = []
        for artist, songs in data.items():
            count_of_songs = Counter(songs)
            for song, number in count_of_songs.items():
                top_songs.append(f"{number:02d} times: {song.song} by {artist}")
        return sorted(top_songs, reverse=True)

if __name__ == "__main__":
    SONGS_DATA = 'lp3_2018.csv'
    test = Lp3DataAnalyser(SONGS_DATA)
    data = test.get_top_1()
    pp(test.most_common_top_1_song(data))
