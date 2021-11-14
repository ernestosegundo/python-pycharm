from datetime import datetime

PRICE_PER_SONG = 1.20


class Song:
    def __init__(self, name, artist, genre, artwork):
        self.artist = artist
        self.name = name
        self.genre = genre
        self.artwork = artwork


class Library:
    def __init__(self):
        self.songs = []


class ServiceInfo:
    def __init__(self, status, engineer_name):
        self.service_date = datetime.now()
        self.status = status
        self.engineer = engineer_name
