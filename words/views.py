from rest_framework import viewsets

# Create your views here.
from forms import WordSerializer
from . import models
from rest_framework import generics

class  WordViewSet(viewsets.ModelViewSet):
		queryset = models.Word.objects.all()
		serializer_class = WordSerializer
		filter_fields = ['id','language','translations',]


class WordList(generics.ListAPIView):
	
    serializer_class = WordSerializer

    def get_queryset(self):
        """
        This viewset is for the word/en routes
        Will return the custom filtered queryset
        """
        language = self.kwargs['language']
        return models.Word.objects.filter(language=language)
