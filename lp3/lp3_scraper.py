import csv
import requests
from bs4 import BeautifulSoup


class lp3:
    """Klasa pobiera top 10 piosenek z notowania listy przebojów na podstawie podanego numeru notowania"""

    def __init__(self, lp3_no):
        self.lp3_no = lp3_no
        self.songs = []

    def get_songs(self):
        source  = requests.get(f'http://lp3.polskieradio.pl/notowania/?numer={self.lp3_no}').text
        soup = BeautifulSoup(source, 'lxml')
        lp3_html = soup.find('div', class_='boxNotowanie')
        positions = lp3_html.find_all('div', class_='BoxTrack')
        for position in positions:
            place = positions.index(position) + 1
            artist = position.find('span', class_='bArtist').a.text
            song = position.find('span', class_='bTitle').a.text
            self.songs.append((place, artist, song, self.lp3_no))
            if place >= 10:
                break
        return self.songs




if __name__ == '__main__':
    # Zapisanie wyników notowań w 2018 roku (numery 1875-1926) za pomocą klasy lp3
    with open("lp3_2018.csv", "w", newline="", encoding="utf-8") as csv_file:
        fieldnames = ["Pozycja", "Wykonawca", "Piosenka", "Nr_notowania"]
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for number in range(1875, 1927):
            notowanie = lp3(number)
            for song_lp in notowanie.get_songs():
                position, artist, song, lp3_no = song_lp
                csv_writer.writerow(
                    {
                        "Pozycja": position,
                        "Wykonawca": artist,
                        "Piosenka": song,
                        "Nr_notowania": lp3_no,
                    }
                )
