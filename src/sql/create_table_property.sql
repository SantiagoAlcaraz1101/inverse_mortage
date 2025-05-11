CREATE TABLE propiedades (
    id_propiedad SERIAL PRIMARY KEY,
    estrato SMALLINT NOT NULL,
    valor_comercial REAL NOT NULL,
    antiguedad SMALLINT NOT NULL,
    legalidad BOOLEAN NOT NULL,
    impuestos BOOLEAN NOT NULL
);