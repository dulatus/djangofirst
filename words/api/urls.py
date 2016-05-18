from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^words/$', views.WordList.as_view(), name='WordList'),
    url(r'^words/pk=(?P<pk>\w+)/$', views.IdWord.as_view(), name='word_id'),
    url(r'^words/(?P<language>\w+)/$', views.LangWord.as_view(), name="word_language"),
    url(r'^words/(?P<language>\w+)/(?P<pk>\w+)/$', views.IdLangWord.as_view(), name='word_id_lang'),
    url(r'^words/(?P<language>\w+)/title=(?P<title>\w+)/$', views.TitleWord.as_view(), name='word_tile')
]
