from django import forms
from .models import Recipe, Category


class RecipeChoiceForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'origin_country', 'cooking_time', 'description', 'history', 'cooking_descr', 'image']

    def __init__(self, **kwargs):
        super(RecipeChoiceForm, self).__init__(**kwargs)
        self.fields['name'].widget.attrs.update({'class': 'content-form-input', 'style': 'height: 47px; width: 300px'})
        self.fields['name'].label = 'Название'
        self.fields['origin_country'].widget.attrs.update({'class': 'content-form-input', 'style': 'height: 47px; width: 300px'})
        self.fields['origin_country'].label = 'Страна происхождения'
        self.fields['cooking_time'].widget.attrs.update({'class': 'content-form-input', 'style': 'height: 47px; width: 100px'})
        self.fields['cooking_time'].label = 'Время приготовления (мин.)'
        self.fields['description'].widget.attrs.update({'class': 'content-form-input', 'style': 'height: 198px; resize:none'})
        self.fields['description'].label = 'Описание'
        self.fields['history'].widget.attrs.update({'class': 'content-form-input', 'style': 'height: 198px; resize:none'})
        self.fields['history'].label = 'История рецепта'
        self.fields['cooking_descr'].widget.attrs.update({'class': 'content-form-input', 'style': 'height: 198px; resize:none'})
        self.fields['cooking_descr'].label = 'Приготовление'
        self.fields['image'].widget.attrs.update({"name": "image", "id": "upload-photo", "accept": "image/*", "onchange": "previewImage()"})
        self.fields['image'].label_suffix = '*'

    image = forms.ImageField(widget=forms.FileInput, required=False)
