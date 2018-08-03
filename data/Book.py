class Book:
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
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.edition = edition
        self.printing = printing
        self.cover = cover
        self.yearPrinted = yearPrinted
        self.description = description
        self.condition = condition
        self.datePurchased = datePurchased
        self.locationPurchased = locationPurchased
        self.amountPaid = amountPaid
        self.sellPrice = sellPrice
        self.siteListed = siteListed
        self.removalAction = removalAction
        self.dateRemoved = dateRemoved
