DROP TABLE IF EXISTS registeredCards;
CREATE TABLE registeredCards (
    name VARCHAR(100) UNIQUE,
    serial VARCHAR(8) UNIQUE,
	timestamp DATE DEFAULT (datetime('now','localtime'))
    );
