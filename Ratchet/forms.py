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
