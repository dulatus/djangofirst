
from serializers import ShortSerializer, DetailSerializer
from  ..models import Word
from rest_framework import generics

class WordList(generics.ListAPIView):
	serializer_class = DetailSerializer
	def get_queryset(self):
		if self.request.method == 'GET':
			return Word.objects.all()

class LanguageWord(generics.ListAPIView):
	
    serializer_class = DetailSerializer
    def get_queryset(self):
        """
        This viewset is for the word/en routes
        Will return the custom filtered queryset
        """

        if self.request.method == 'GET':
        	language = self.kwargs.get('language')
        	queryset = Word.objects.filter(language=language)
        	return queryset

class TitleWord(generics.ListAPIView):
	serializer_class = DetailSerializer
	def get_queryset(self):
		if self.request.method == 'GET':
			words = Word.objects.all()
			language = self.kwargs.get('language')
			title = self.kwargs.get('title')
			queryset = Word.objects.filter(language = language).filter(title = title)
			return queryset

class IdWord(generics.ListAPIView):
	serializer_class = DetailSerializer
	def get_queryset(self):
		if self.request.method == 'GET':
			language = self.kwargs.get('language')
			pk = self.kwargs.get('pk')
			queryset = words.filter(language=language).filter(pk = pk)
			return queryset
class IdWord(generics.ListAPIView):
	serializer_class = DetailSerializer
	def get_queryset(self):
		if self.request.method == 'GET':
			pk = self.kwargs.get('pk')
			queryset = Word.objects.filter(pk = pk)
			return queryset



