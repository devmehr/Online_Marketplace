from django import forms

from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('catagory', 'name', 'description', 'price', 'image',)

        widgets = {
            'catagory': forms.Select(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'price': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
        }