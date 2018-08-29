from data.Item import Item

class Book:
    def __init__(self,
                 item: Item,
                 author: str,
                 edition: int,
                 printing: int,
                 cover: int,
                 dateRemoved: str):
        self.item = item
        self.author = author
        self.edition = edition
        self.printing = printing
        self.cover = cover
