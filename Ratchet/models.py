from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg
from django.utils import timezone
from django.core.exceptions import ValidationError

class Feedback(models.Model):
    feedback_name = models.CharField('Имя', max_length=50, default='')
    feedback_phone = models.CharField('Телефонный номер', max_length=20, null=False)

    def __str__(self):
        return self.feedback_name

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратные связи'

class Employees(models.Model):
    DEPATRAMENTS = [
        ('Терапевт', 'Терапевт'), #
        ('Хирург', 'Хирург'), #
        ('Педиатр', 'Педиатр'), #
        ('Невролог', 'Невролог'), #
        ('Реабилитолог', 'Реабилитолог'), #
        ('Стоматолог', 'Стоматолог'), #
        ('Лор', 'Лор'), #
        ('Травмотолог', 'Травмотолог'), #
        ('Психиатр', 'Психиатр'), #
        ('Нарколог', 'Нарколог') #
    ]
    employee_full_name = models.CharField('Полное имя', max_length=200, default='Пример Пример Примеров')
    employee_age = models.IntegerField()
    employee_specialization = models.CharField('Специализация', max_length=50, choices=DEPATRAMENTS)
    employee_experience = models.IntegerField()
    employee_photo = models.ImageField(upload_to='media/', blank=True, null=True)
    employee_discription = models.TextField('Описание/достижения', blank=True, null=True)

    def __str__(self):
        return self.employee_full_name + " " + self.employee_specialization

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'


def calculate_average_rate():
    average_rating = Review.objects.aggregate(Avg('reviwe_rate'))['reviwe_rate__avg']
    return average_rating
class Review(models.Model):
    review_name = models.CharField('Ваше имя', max_length=200, default='Гость')
    reviwe_rate = models.IntegerField('Ваша оценка', validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ])
    reviwe_text = models.TextField('Ваш отзыв')
    def __str__(self):
        return self.review_name + " оставил отзыв на оценку " + str(self.reviwe_rate) + " баллов"
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class Service(models.Model):
    service_name = models.CharField('Название услуги', max_length=100, default='Консультация по телефону')
    service_description = models.TextField()
    service_image = models.ImageField(upload_to='media/', blank=True, null=True)
    service_price = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return self.service_name
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'



class Client(models.Model):
    client_name = models.CharField('Имя', max_length=100)
    client_surname = models.CharField('Фамилия', max_length=100)
    client_notes = models.TextField('Примечания', blank=True, null=True)
    client_phone = models.CharField('Номер телефона', max_length=20)
    client_date = models.DateField('Дата записи')
    client_service = models.ForeignKey(Service, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.client_name} {self.client_surname} записался на {self.client_service}'

    def clean(self):
        if self.client_date < timezone.now().date():
            raise ValidationError("Нельзя записаться на прошедшую дату")

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'