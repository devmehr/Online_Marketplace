from django import forms

from conversation.models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.TextInput(attrs={
                'class': 'cus-con-send',
                'type': 'text',
                'placeholder': 'Message'
            })
        }