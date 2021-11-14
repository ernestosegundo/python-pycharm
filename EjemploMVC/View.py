class Touchscreen:
    def select_song(self):
        pass

    @staticmethod
    def prompt_for_next_song(songs):
        for song in songs:
            # display the songs
            pass
        return "Dark Chest of Wonders"


class Speakers:
    def __init__(self):
        self.volume = 5

    def get_louder(self):
        self.volume += 1

    def get_quieter(self):
        self.volume -= 1

    def play_song(self, song):
        pass


class CoinSlot:
    def __init__(self, float_):
        self.amount = float_

    def request_money(self, amount):
        # wait for money
        # give change
        self.amount += amount
        return True
