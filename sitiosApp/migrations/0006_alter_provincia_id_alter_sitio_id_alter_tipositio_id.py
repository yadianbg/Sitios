# Generated by Django 4.2 on 2023-04-10 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitiosApp', '0005_alter_provincia_id_alter_sitio_id_alter_tipositio_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provincia',
            name='id',
            field=models.UUIDField(default='26cd81aa91ff4c1c957f121d031ce763', editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='sitio',
            name='id',
            field=models.UUIDField(default='26cd81aa91ff4c1c957f121d031ce763', editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='tipositio',
            name='id',
            field=models.UUIDField(default='26cd81aa91ff4c1c957f121d031ce763', editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Id'),
        ),
    ]