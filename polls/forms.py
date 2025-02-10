from django import forms
from django.template.defaultfilters import title

from polls.models import ToDoItem

class ToDoItemCreateForm(forms.ModelForm):

    class Meta:
        model = ToDoItem
        fields = ('title', 'description', 'done')

        widgets = {
            'description': forms.Textarea(
                attrs={'cols': 30, 'rows': 5,}
            )
        }
        help_texts={
            'description': 'Some useful text',
        }
    # title = forms.CharField(
    #     max_length=256,
    #     # widget=forms.TextInput()
    #     # widget=forms.Textarea()
    # )

class ToDoItemUpdateForm(forms.ModelForm):
    model = ToDoItem

    class Meta(ToDoItemCreateForm.Meta):
        fields = (
            'title',
            'description',
            'done'
        )