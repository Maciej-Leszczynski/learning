import csv
from collections import Counter, defaultdict, namedtuple

class Lp3DataAnalyser():
    """
    Class to store data of the lp3 charts exported from the CSV file.
    Data will be used to perform various analysis like most common 
    TOP 1 artist, song etc. 
    """
    def __init__(self, data):
        self.data = data

    def get_artists_songs_top(self, X):
        """
        Extracts all songs from csv and stores them in a dictionary
        where artist is a key and song is a value (named tuple with 
        position included). 
        X is a number of TOP songs user wants to analyse in each chart.
        """
        artists = defaultdict(list)
        Song = namedtuple("Song", "song position")
        with open(self.data, encoding='utf-8') as f:
            for line in csv.DictReader(f):
                artist = line['Wykonawca']
                song = line['Piosenka']
                position = int(line['Pozycja'])

                if position <= X:
                    s = Song(song=song, position=position)
                    artists[artist].append(s)
        return artists

    def count_how_often_song_apear(self, data):
        """
        Counts and prints how often song apeared on the list baseing
        on the data from get_artists_songs_top method.
        """
        for artist, songs in data.items():
            count_of_songs = Counter(songs)
            for song, number in count_of_songs.items():
                print(f"{artist}:")
                print(f"\t{song.song}: {number}")
                print("*" * 50)

if __name__ == "__main__":
    SONGS_DATA = 'lp3_2018.csv'
    test = Lp3DataAnalyser(SONGS_DATA)
    data = test.get_artists_songs_top(1)
    # print(data)
    test.count_how_often_song_apear(data)