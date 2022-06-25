from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image as Im
import numpy

from .algorithm import descriptor_generate, hist_generate


User = get_user_model()

class Market(models.Model):
	user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
	marker_name = models.CharField(max_length=255, verbose_name='Название магазина')
	contacts = models.CharField(max_length=255, verbose_name='контактная информация', null=True, blank=True)

	def __str__(self):
		return '{}: {}'.format(self.user.first_name, self.marker_name)

class Shoe(models.Model):
	user = models.ForeignKey(Market, verbose_name='Магазин', on_delete=models.CASCADE)

	title = models.CharField(max_length=255, verbose_name='Наименование обуви')
	price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Цена')

	size35 = models.PositiveIntegerField(default=0, verbose_name='количество размер 35')
	size36 = models.PositiveIntegerField(default=0, verbose_name='количество размер 36')
	size37 = models.PositiveIntegerField(default=0, verbose_name='количество размер 37')
	size38 = models.PositiveIntegerField(default=0, verbose_name='количество размер 38')
	size39 = models.PositiveIntegerField(default=0, verbose_name='количество размер 39')
	size40 = models.PositiveIntegerField(default=0, verbose_name='количество размер 40')
	size41 = models.PositiveIntegerField(default=0, verbose_name='количество размер 41')
	size42 = models.PositiveIntegerField(default=0, verbose_name='количество размер 42')
	size43 = models.PositiveIntegerField(default=0, verbose_name='количество размер 43')
	size44 = models.PositiveIntegerField(default=0, verbose_name='количество размер 44')

	def __str__(self):
		return '{}: {}'.format(self.user, self.title)

class ImageShoe(models.Model):
	image = models.ImageField(upload_to='images/')
	shoe = models.ForeignKey(Shoe, verbose_name='Указывает от какой обуви фото', on_delete=models.CASCADE)
	descriptor = models.BinaryField(verbose_name='Дескриптор')
	histogram = models.BinaryField(verbose_name='Гистограмма')

	def __str__(self):
		return '{} : {}'.format(self.id, self.shoe.title)

	def save(self, *args, **kwargs):
		img = Im.open(self.image)
		open_cv_image = numpy.array(img)
		open_cv_image = open_cv_image[:, :, ::-1].copy()
		self.histogram = hist_generate(open_cv_image).tostring()
		self.histogram = descriptor_generate(open_cv_image).tostring()
		super(ImageShoe, self).save(*args, **kwargs)