DROP TABLE registeredCards;
CREATE TABLE registeredCards (
    name VARCHAR(100) UNIQUE,
    serial VARCHAR(8) UNIQUE
    );
