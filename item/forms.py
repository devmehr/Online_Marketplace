from django import forms

from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('catagory', 'name', 'description', 'price', 'image',)

        widgets = {
            'catagory': forms.Select(attrs={
                'class': 'cus-classs',
            }),
            'name': forms.TextInput(attrs={

                'class': 'cus-classs'
            }),
            'description': forms.Textarea(attrs={

                'class': 'cus-classs'
            }),
            'price': forms.TextInput(attrs={

                'class': 'cus-classs'
            }),
            'image': forms.FileInput(attrs={

                'class': 'cus-classss'
            })
            
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold',)

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'cus-classs'
            }),
            'description': forms.Textarea(attrs={
                'class': 'cus-classs'
            }),
            'price': forms.TextInput(attrs={
                'class': 'cus-classs'
            }),
            'image': forms.FileInput(attrs={
                'class': 'cus-classss'
            })
        }