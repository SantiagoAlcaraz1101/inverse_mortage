SELECT
    propiedades.estrato,
    propiedades.valor_comercial,
    propiedades.antiguedad,
    propiedades.legalidad,
    personas.posee_titulo_propiedad,
    propiedades.id_propiedad
FROM propiedades
JOIN personas ON propiedades.id_propiedad = personas.id_propiedad
WHERE nombre_apellido_persona ILIKE %s;