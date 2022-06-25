# Generated by Django 4.0.5 on 2022-06-22 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('decriptor', models.TextField(verbose_name='Дескриптор')),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marker_name', models.CharField(max_length=255, verbose_name='Название магазина')),
                ('contacts', models.CharField(blank=True, max_length=255, null=True, verbose_name='контактная информация')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование обуви')),
                ('price', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Цена')),
                ('size35', models.PositiveIntegerField(default=0, verbose_name='количество размер 35')),
                ('size36', models.PositiveIntegerField(default=0, verbose_name='количество размер 36')),
                ('size37', models.PositiveIntegerField(default=0, verbose_name='количество размер 37')),
                ('size38', models.PositiveIntegerField(default=0, verbose_name='количество размер 38')),
                ('size39', models.PositiveIntegerField(default=0, verbose_name='количество размер 39')),
                ('size40', models.PositiveIntegerField(default=0, verbose_name='количество размер 40')),
                ('size41', models.PositiveIntegerField(default=0, verbose_name='количество размер 41')),
                ('size42', models.PositiveIntegerField(default=0, verbose_name='количество размер 42')),
                ('size43', models.PositiveIntegerField(default=0, verbose_name='количество размер 43')),
                ('size44', models.PositiveIntegerField(default=0, verbose_name='количество размер 44')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.market', verbose_name='Магазин')),
            ],
        ),
        migrations.DeleteModel(
            name='Image11',
        ),
        migrations.AddField(
            model_name='image',
            name='shoe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.shoe', verbose_name='Указывает от какой обуви фото'),
        ),
    ]