from rest_framework import serializers 

from . import models

class WordSerializer(serializers.HyperlinkedModelSerializer):
				
		class  Meta:
			model = models.Word
			fields = ("id","title","language","description","translations")