from Model import *
from View import *


class Controller:
    def __init__(self):
        self.library = Library()
        self.service_history = []
        self.audio_output = Speakers()
        self.ui = Touchscreen()
        self.bank = CoinSlot()

    def play_next_song(self):
        songs_to_suggest = []
        for song in self.library:
            # filter logic
            songs_to_suggest.append(song)
        chosen_song = self.ui.prompt_for_next_song(songs_to_suggest)
        request_money(PRICE_PER_SONG)
        self.audio_output.play_song(chosen_song)
