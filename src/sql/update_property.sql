UPDATE propiedades
SET 
estrato = %s,
valor_comercial = %s,
antiguedad = %s,
legalidad = %s,
impuestos = %s
WHERE id_propiedad = %s;