from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg

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
    employee_discription = models.TextField('Описание/достижения' ,blank=True, null=True)

    def __str__(self):
        return self.employee_full_name + " " + self.employee_specialization

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'

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

def calculate_average_rate():
    average_rating = Review.objects.aggregate(Avg('reviwe_rate'))['reviwe_rate__avg']
    return average_rating
