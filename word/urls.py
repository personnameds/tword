from django.urls import path
from . import views

urlpatterns = [
    path('importwords', views.ImportWordsFormView.as_view(), name='importwords-formview'),
	path('importfile', views.ImportFileFormView.as_view(), name='importfile-formview'),
]
