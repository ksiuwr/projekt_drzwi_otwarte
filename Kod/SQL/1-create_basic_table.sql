DROP TABLE IF EXISTS registeredCards;
CREATE TABLE registeredCards (
    name VARCHAR(100) UNIQUE,
    serial VARCHAR(8) UNIQUE,
    last_used DATE NOT NULL (datetime('now','localtime')),
    timestamp DATE NOT NULL DEFAULT (datetime('now','localtime'))
    );
