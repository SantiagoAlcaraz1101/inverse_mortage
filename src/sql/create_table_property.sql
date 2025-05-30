CREATE TABLE if not exists propiedades (
    id_propiedad VARCHAR(256) PRIMARY KEY,
    estrato SMALLINT NOT NULL,
    valor_comercial REAL NOT NULL,
    antiguedad SMALLINT NOT NULL,
    legalidad BOOLEAN NOT NULL,
    impuestos BOOLEAN NOT NULL
);