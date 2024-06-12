from django.db import models

from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField
# Models Postal Code APi

# MODELO ESTADOS DE MÉXICO
class State(models.Model):
    entity_number = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    search_vector = SearchVectorField()

    class Meta:
        indexes = [
            GinIndex(fields=['search_vector'], name='state_search_vector_gin'),
        ]

    def __str__(self):
        return self.name


# MODELO MUNICIPIOS DE MÉXICO
class Municipality(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    search_vector = SearchVectorField()

    class Meta:
        indexes = [
            GinIndex(fields=['search_vector'], name='municipality_search_vector_gin'),
        ]

    def __str__(self):
        return self.name


# MODELO CIUDADES DE MÉXICO
class City(models.Model):
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    search_vector = SearchVectorField()

    class Meta:
        indexes = [
            GinIndex(fields=['search_vector'], name='city_search_vector_gin'),
        ]

    def __str__(self):
        return self.name


# MODELO CÓDIGOS POSTALES DE MÉXICO
class PostalCode(models.Model):
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    code = models.CharField(max_length=50)

    class Meta:
        indexes = [
            GinIndex(fields=['code'], name='postal_code_code_gin', opclasses=['gin_trgm_ops']),
        ]

    def __str__(self):
        return self.code


# MODELO PARROQUIAS DE MÉXICO
class Settlement(models.Model):
    postal_code = models.ForeignKey(PostalCode, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    settlement_type = models.CharField(max_length=255)
    search_vector = SearchVectorField()
    city = models.ManyToManyField(City, null=True, blank=True)

    class Meta:
        indexes = [
            GinIndex(fields=['search_vector'], name='settlement_search_vector_gin'),
        ]

    def __str__(self):
        return self.name