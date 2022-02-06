from django import forms
from .models import Word

class WordListForm(forms.Form):
	word_level = forms.ChoiceField(choices=Word.WORD_LEVEL,required=False)
	#source
	word_list = forms.CharField(widget=forms.Textarea)

class ImportFileForm(forms.Form):
	filename=forms.CharField(max_length=50)