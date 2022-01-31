from .forms import WordListForm
from django.views.generic.edit import FormView

class ImportWordsFormView(FormView):
	template_name ='form.html'
	form_class = WordListForm
	success_url = '/thanks/'
	
	
