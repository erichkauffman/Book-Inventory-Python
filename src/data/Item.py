class Item:
    def __init__(self,
                 itemId: int,
                 title: str,
                 upc: str,
                 year: int,
                 description: str,
                 condition: int,
                 datePurchased: str,
                 locationPurchased: str,
                 amountPaid: int,
                 sellPrice: int,
                 siteListed: int,
                 removalAction: bool,
                 dateRemoved: str):
        self.itemId = itemId
        self.title = title
        self.upc = upc
        self.year = year
        self.description = description
        self.condition = condition
        self.datePurchased = datePurchased
        self.locationPurchased = locationPurchased
        self.amountPaid = amountPaid
        self.sellPrice = sellPrice
        self.siteListed = siteListed
        self.removalAction = removalAction
        self.dateRemoved = dateRemoved
