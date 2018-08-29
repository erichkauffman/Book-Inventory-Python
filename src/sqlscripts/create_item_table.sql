CREATE TABLE IF NOT EXISTS item (
itemId INTEGER NOT NULL PRIMARY KEY,
title TEXT NOT NULL,
upc TEXT NOT NULL,
year INT,
description TEXT NOT NULL,
condition INT NOT NULL,
datePurchased DATE NOT NULL,
locationPurchased TEXT NOT NULL,
amountPaid INT,
sellPrice INT,
siteListed INT,
removalAction BOOLEAN,
dateRemoved DATE);