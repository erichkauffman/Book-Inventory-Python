CREATE TABLE IF NOT EXISTS "book"(
title TEXT NOT NULL,
author TEXT NOT NULL,
isbn TEXT NOT NULL,
edition INT NOT NULL,
printing INT,
cover INT NOT NULL,
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



