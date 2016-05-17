from __future__ import unicode_literals

from django.db import models

# Create your models here.
class  Word(models.Model):
	languages = (('en', 'english'),('kz', 'kazakh'),('ru', 'russian'))
	title = models.CharField(max_length=25)
	language = models.CharField(max_length=2,choices = languages)
	description = models.CharField(max_length=200)
	translations = models.ManyToManyField("self",blank=True)
	synonyms = models.ManyToManyField("self",blank=True)
	antonyms = models.ManyToManyField("self",blank=True)
	def __unicode__(self):
		return self.title

