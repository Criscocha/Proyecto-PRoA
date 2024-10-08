# Generated by Django 5.1.1 on 2024-10-08 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proa', '0002_evento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='eventos_imagenes/')),
            ],
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='titulo',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='imagen',
        ),
    ]
