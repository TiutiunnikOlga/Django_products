from django.forms import ModelForm
from django.core.exceptions import ValidationError
from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    FORBIDDEN_WORDS = {
        'казино', 'криптовалюта', 'крипта',
        'биржа', 'дешево', 'бесплатно',
        'обман', 'полиция', 'радар'
    }

    def check_forbidden_words(self, text):
        words = set(text.lower().split())
        forbidden_in_text = words.intersection(self.FORBIDDEN_WORDS)

        if forbidden_in_text:
            raise ValidationError(
                f'Текст не может содержать следующие слова: {", ".join(forbidden_in_text)}'
            )

    def clean_name(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')

        self.check_forbidden_words(name)
        return name

    def clean_description(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description')

        self.check_forbidden_words(description)
        return description

    def clean_price(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')

        if price < 0:
                raise ValidationError(f'Цена не может быть отрицательной')
        return price


    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class':'form-control',
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['photo'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Выберите фото'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Выберите категорию'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите стоимость'
        })
