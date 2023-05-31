from django import forms
from django.forms import ModelForm
from .models import *

class Feedback_Form(ModelForm):
    feedback_name = models.CharField('Имя', max_length=50, default='')
    feedback_phone = models.CharField('Телефонный номер', max_length=20, null=False)

    class Meta:
        model = Feedback
        fields = ['feedback_name', 'feedback_phone']
        labels = {'feedback_name': 'Ваше имя', 'feedback_phone': 'Ваш телефон'}


class Rewiew_Form(ModelForm):
    review_name = forms.CharField(label='Ваше имя', max_length=200, initial='Гость', help_text='Введите ваше имя')
    reviwe_rate = forms.IntegerField(label='Ваша оценка', validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ], help_text='Введите оценку от 1 до 5')
    reviwe_text = forms.CharField(label='Ваш отзыв', widget=forms.Textarea, help_text='Введите ваш отзыв')
    class Meta:
        model = Review
        fields = ['review_name', 'reviwe_rate', 'reviwe_text']
        labels = {'review_name': 'Ваше имя', 'reviwe_rate': 'Ваша оценка', 'reviwe_text': 'Ваш отзыв'}

class Client_Form(ModelForm):
    class Meta:
        model = Client
        fields = ['client_name', 'client_surname', 'client_notes', 'client_phone', 'client_date', 'client_service']
        widgets = {
            'client_notes': forms.Textarea(attrs={'rows': 3}),
            'client_date': forms.DateInput(attrs={'type': 'date'}),
        }
