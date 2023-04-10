# Generated by Django 4.2 on 2023-04-10 04:35

from django.db import migrations, models
import sitiosApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('sitiosApp', '0006_alter_provincia_id_alter_sitio_id_alter_tipositio_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provincia',
            name='id',
            field=models.CharField(default=sitiosApp.models.generate_primary_key, editable=False, max_length=32, primary_key=True, serialize=False, unique=True, verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='sitio',
            name='id',
            field=models.CharField(default=sitiosApp.models.generate_primary_key, editable=False, max_length=32, primary_key=True, serialize=False, unique=True, verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='tipositio',
            name='id',
            field=models.CharField(default=sitiosApp.models.generate_primary_key, editable=False, max_length=32, primary_key=True, serialize=False, unique=True, verbose_name='Id'),
        ),
    ]