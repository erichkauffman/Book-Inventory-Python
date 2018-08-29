CREATE TABLE IF NOT EXISTS item (
itemId INT PRIMARY KEY,
title TEXT NOT NULL,
upc TEXT NOT NULL,
yearPrinted INT,
description TEXT NOT NULL,
condition INT NOT NULL,
datePurchased DATE NOT NULL,
locationPurchased TEXT NOT NULL,
amountPaid INT,
sellPrice INT,
siteListed INT,
removalAction BOOLEAN,
dateRemoved DATE);