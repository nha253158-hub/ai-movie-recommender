from pathlib import Path
DATASET_PATH = Path("TMDB_movie_dataset_v11.csv")
USE_COLUMNS = [
    "title",
    "runtime",
    "release_date",
    "genres",
    "production_countries",
    "popularity",
    "vote_count",
    "vote_average",
]
MIN_VOTE_COUNT = 500
MIN_VOTE_AVERAGE = 0.0
TOP_N_GENRES = 10
TOP_N_COUNTRIES = 10
NUMERIC_FEATURES = ["runtime","release_year","popularity","vote_count"]
CATEGORICAL_FEATURES = ["genres","production_countries"]
TEST_SIZE =0.2
RANDOM_STATE = 42
N_RECOMMENDATIONS = 5
SHORTLIST_MULTIPLIER =4
MIN_RATING =1.0
MAX_RATING = 10.0
