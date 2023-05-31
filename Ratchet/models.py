from django.db import models
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
        ('Терапевт', 'Терапевт'),
        ('Хирург', 'Хирург'),
        ('Педиатр', 'Педиатр'),
        ('Невролог', 'Невролог'),
        ('Реабилитолог', 'Реабилитолог'),
        ('Стоматолог', 'Стоматолог'),
        ('Лор', 'Лор'),
        ('Травмотолог', 'Травмотолог')
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
