from django import forms
from django.apps import apps  

from .models import ConversationMessage

Item = apps.get_model('item', 'Item')  

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
        }
