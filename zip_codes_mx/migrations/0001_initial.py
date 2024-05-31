# Generated by Django 5.0.6 on 2024-05-31 23:45

import django.contrib.postgres.indexes
import django.contrib.postgres.search
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('search_vector', django.contrib.postgres.search.SearchVectorField()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('search_vector', django.contrib.postgres.search.SearchVectorField()),
                ('municipality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zip_codes_mx.municipality')),
            ],
        ),
        migrations.CreateModel(
            name='PostalCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zip_codes_mx.city')),
            ],
        ),
        migrations.CreateModel(
            name='Settlement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('search_vector', django.contrib.postgres.search.SearchVectorField()),
                ('settlement_type', models.CharField(max_length=255)),
                ('postal_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zip_codes_mx.postalcode')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('entity_number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('search_vector', django.contrib.postgres.search.SearchVectorField()),
            ],
            options={
                'indexes': [django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='zip_codes_m_search__00087c_gin')],
            },
        ),
        migrations.AddField(
            model_name='municipality',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zip_codes_mx.state'),
        ),
        migrations.AddIndex(
            model_name='city',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='zip_codes_m_search__8c8068_gin'),
        ),
        migrations.AddIndex(
            model_name='postalcode',
            index=django.contrib.postgres.indexes.GinIndex(fields=['code'], name='zip_codes_m_code_2a15ef_gin'),
        ),
        migrations.AddIndex(
            model_name='settlement',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='zip_codes_m_search__aa6c2e_gin'),
        ),
        migrations.AddIndex(
            model_name='municipality',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='zip_codes_m_search__40780a_gin'),
        ),
    ]
