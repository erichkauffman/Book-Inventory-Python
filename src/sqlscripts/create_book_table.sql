CREATE TABLE IF NOT EXISTS book (
author TEXT NOT NULL,
edition INT NOT NULL,
printing INT,
cover INT NOT NULL,
FOREIGN KEY (item) REFERENCES item(itemId));




