# Generated by Django 4.0.3 on 2022-03-28 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clase', '0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='datos',
        ),
        migrations.DeleteModel(
            name='empresa',
        ),
        migrations.DeleteModel(
            name='salario',
        ),
    ]