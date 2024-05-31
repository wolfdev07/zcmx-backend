from django.db import connection

# MOTOR DE BUSQUEDA DE NOMBRES DE CIUDADES
def city_name_search_engine(name):
    
    query = """SELECT * FROM zip_codes_mx_city
        WHERE unaccent(lower(name)) = unaccent(lower(%s))"""
    
    with connection.cursor() as cursor:
        cursor.execute(query, [name])
        return cursor.fetchall()