# Generated by Django 5.1 on 2024-08-24 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('PrimeiroNome', models.CharField(max_length=255)),
                ('Ultimo_nome', models.CharField(max_length=255)),
                ('Cidade', models.CharField(max_length=255)),
                ('Estado', models.CharField(max_length=255)),
                ('Idade', models.IntegerField()),
            ],
            options={
                'db_table': 'People',
            },
        ),
    ]
