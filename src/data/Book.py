from Item import Item

class Book(Item):
    def __init__(self,
                 id: int,
                 title: str,
                 author: str,
                 isbn: str,
                 edition: int,
                 printing: int,
                 cover: int,
                 yearPrinted: int,
                 description: str,
                 condition: int,
                 datePurchased: str,
                 locationPurchased: str,
                 amountPaid: int,
                 sellPrice: int,
                 siteListed: int,
                 removalAction: bool,
                 dateRemoved: str):
        super().__init__(id,
                         title, 
                         isbn,
                         yearPrinted,
                         description,
                         condition,
                         datePurchased,
                         locationPurchased,
                         amountPaid,
                         sellPrice,
                         siteListed,
                         removalAction,
                         dateRemoved)
        self.author = author
        self.edition = edition
        self.printing = printing
        self.cover = cover
