import glob


class Model:
    def __init__(self):
        # English car model hangman_words_en.db
        self.database_name = 'databases/hangman_words_ee.db'
        self.image_files = glob.glob('images/*.png')  # All hangman images
        # New game
        self.new_word = None  # see mida tuleb arvata
        self.user_word = []  # tühi list
        self.all_user_chars = []  # tähed mis kasutaja on leidnud
        self.counter = 0  # valesti arvatud tähed kokku lugeda
        # Leaderboard
        self.player_name = 'UNKOWN'
        self.leaderboard_file = 'leaderboard.txt'
        self.score_data = []  # eelneva faili sisu