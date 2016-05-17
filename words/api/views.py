from rest_framework import generics

from serializers import DetailSerializer


from ..models import Word


class WordList(generics.ListAPIView):
    serializer_class = DetailSerializer

    def get_queryset(self):
            if self.request.method == 'GET':
                return Word.objects.all()


class LangWord(generics.ListAPIView):
    serializer_class = DetailSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            language = self.kwargs.get('language')
            queryset = Word.objects.filter(language=language)
            return queryset


class TitleWord(generics.ListAPIView):
    serializer_class = DetailSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            language = self.kwargs.get('language')
            title = self.kwargs.get('title')
            words = Word.objects.all()
            queryset = words.filter(language=language).filter(title=title)
            return queryset


class IdLangWord(generics.ListAPIView):
    serializer_class = DetailSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            language = self.kwargs.get('language')
            pk = self.kwargs.get('pk')
            queryset = Word.objects.filter(language=language).filter(pk=pk)
            return queryset


class IdWord(generics.ListAPIView):
    serializer_class = DetailSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            pk = self.kwargs.get('pk')
            queryset = Word.objects.filter(pk=pk)
            return queryset
