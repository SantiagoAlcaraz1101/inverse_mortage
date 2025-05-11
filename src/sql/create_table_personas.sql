CREATE TABLE personas(
    id_persona SERIAL PRIMARY KEY,
    nombre_apellido_persona VARCHAR(50) NOT NULL,
    edad SMALLINT NOT NULL,
    es_mujer BOOLEAN NOT NULL,
    condicion_discapacidad BOOLEAN NOT NULL,
    posee_titulo_propiedad BOOLEAN NOT NULL,
    id_propiedad INT NOT NULL,
    CONSTRAINT fk_propiedad FOREIGN KEY (id_propiedad) REFERENCES propiedades(id_propiedad)
)