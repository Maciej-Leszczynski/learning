import csv
from collections import defaultdict, namedtuple, Counter

MOVIE_DATA = 'movies.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')

def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    directors = defaultdict(list)
    with open(MOVIE_DATA, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                if int(line['title_year']) >= MIN_YEAR:
                    director = line['director_name']
                    title = line['movie_title'].rstrip('\xa0')
                    year = int(line['title_year'])
                    score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=title, year=year, score=score)
            directors[director].append(m)
    return directors

def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    aver_directors = defaultdict(list)
    for director in directors:
        movies = directors[director]
        if len(movies) >= MIN_MOVIES:
            mean = _calc_mean(movies)
            aver_directors[director].append(mean)
    return aver_directors

def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    score = 0
    count = 0
    for movie in movies:
        score += movie.score
        count += 1
    score /= count
    return score


if __name__ == '__main__':
    directors = get_movies_by_director()
    director = directors['Wes Anderson'] 
    print(len(director))
    print(get_average_scores(directors))