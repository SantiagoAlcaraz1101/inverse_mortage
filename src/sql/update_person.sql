UPDATE personas
SET 
    nombre_apellido_persona = %s,
    edad = %s,
    es_mujer = %s,
    condicion_discapacidad = %s,
    posee_titulo_propiedad = %s,
    id_propiedad = %s
WHERE 
    id_persona = %s;