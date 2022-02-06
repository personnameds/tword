from .forms import WordListForm, ImportFileForm
from django.views.generic.edit import FormView
from .models import Word

#From a copy and paste into the box with comma seperated words
class ImportWordsFormView(FormView):
	template_name ='form.html'
	form_class = WordListForm
	success_url = '/thanks/'
	
	def form_valid(self, form):
		word_list = form.cleaned_data['word_list']
		word_list = word_list.split(',')
		for word in word_list:
			if Word.objects.filter(word = word).exists():
				pass
			else:
				w = Word(
					word = word,
					word_level = form.cleaned_data['word_level'],
					word_length = len(word),
					)
				w.save()
		return super().form_valid(form)

##From a text file with /r/n

#Import Function, enter file name
#Make this a selection window in future
#Only works in home directory
class ImportFileFormView(FormView):
	template_name = 'form.html'
	form_class = ImportFileForm
	success_url = '/thanks/'

	def form_valid(self, form):
		filename=form.cleaned_data['filename']
		
		with open(filename) as file:
			for line in file:
				word = line.rstrip()
				
				if Word.objects.filter(word = word).exists():
					pass
				else:
					w = Word(
						word = word,
						word_level = '',
						word_length = len(word),
						)
					w.save()
					
		return super().form_valid(form)
