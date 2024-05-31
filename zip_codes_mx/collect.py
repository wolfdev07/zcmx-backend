import os
import pandas
import time
from django.conf import settings
from pathlib import Path
from zip_codes_mx.models import State, City, PostalCode, Settlement


url_xlx = os.path.join(settings.MEDIA_ROOT, 'collection.xls')

def create_zip_code_records(file_url, sheet_name):

    data = pandas.read_excel(file_url, sheet_name)
    
    # DEFINIR DATOS DE LOS ESTADOS
    state_name = data['d_estado'].unique()
    cities = data['D_mnpio'].unique()
    postal_codes = data['d_codigo'].unique()

    # CREAR LA ENTIDAD FEDERATIVA EN LA DB
    state, created =  State.objects.get_or_create(entity_number=sheet_name, name=state_name[0])

    if created:
        state.save()
        print(f'State {sheet_name} created')
    else:
        print(f'State {sheet_name} already exists')
    
    # CREAR CIUDADES, ITERAR LOS MUNICIPIOS UNICOS Y AGREGARLOS A LA DB

    counter = 0
    for city_name in cities:

        city, created = City.objects.get_or_create(state=state, name=city_name)
        if created:
            city.save()
            print(f'City {city_name} created')
            counter += 1
        else:
            print(f'City {city_name} already exists')
    
    # FINALIZAR ESTADO
    print(f'Se han creado {counter} municipios para {state_name}')

    # CREAR LOS CODIGOS POSTALES

    for code in postal_codes:
        code_to_search = data.loc[data['d_codigo'] == code]

        for indexer, row in code_to_search .iterrows():
            code_city = row['D_mnpio']
            settlement_name = row['d_asenta']
            settlement_type = row['d_tipo_asenta']

            assign_city = City.objects.get(state=state, name=code_city)
            try:
                postal_code = PostalCode.objects.get(city=assign_city, code=code)
                created_postal_code = False
            except:
                postal_code = PostalCode(city=assign_city, code=code)
                created_postal_code = True
            
            if created_postal_code:
                postal_code.save()
            
            settlement, created = Settlement.objects.get_or_create(postal_code=postal_code, name=settlement_name, settlement_type=settlement_type)
            if created:
                settlement.save()
            else:
                print(f'{settlement.postal_code.city.state.name}, {settlement.postal_code.city.name}, {settlement.settlement_type} {settlement.name} CP{settlement.postal_code} , ya registrado previamente...')



def collect_data(url):
    init_time = time.time()
    
    try:
        State.objects.get(number=32)
        objects_in_state = True
    except:
        objects_in_state =False

    if objects_in_state:

        print("Ya existen datos dentro de la Tabla Estados")

    else:

        for index in range(32,33):
            create_zip_code_records(url, index)
            
        
        # Registra el tiempo de finalización
        end_time = time.time()

        # Calcula el tiempo transcurrido
        time_elapsed = (end_time - init_time)
        if time_elapsed >= 60:
            print(f"Tiempo transcurrido: {time_elapsed/60} minutos")
        else:
            print(f"Tiempo transcurrido: {time_elapsed} segundos")

collect_data(url_xlx)