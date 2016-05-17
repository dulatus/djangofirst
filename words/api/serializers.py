from rest_framework.serializers import  ModelSerializer,StringRelatedField 

from  ..models import Word

class ShortSerializer(ModelSerializer):
	class Meta:
		model = Word
		fields = ("id","title","language")


class DetailSerializer(ModelSerializer):
	translations = ShortSerializer(many = True)
	synonyms = ShortSerializer(many = True)
	antonyms = ShortSerializer(many = True)
	class  Meta:
			model = Word
			fields = ("id","title","language","description","translations","synonyms","antonyms")
