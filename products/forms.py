from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating']

    rating = forms.ChoiceField(choices=[(i, str(i)) for i in range(1, 6)], widget=forms.Select())

    def clean_rating(self):
        rating = int(self.cleaned_data.get('rating'))
        if rating not in range(1, 6):
            raise forms.ValidationError("Invalid rating. Choose a number between 1 and 5.")
        return rating