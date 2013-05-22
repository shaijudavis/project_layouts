from django.forms import ModelForm

from flatpages_plus.models import FlatPage

class FlatpageForm(ModelForm):
    class Meta:
        model = FlatPage
        fields = ['url', 'name', 'title', 'content']
