from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Employees, Review, calculate_average_rate, Service
from .forms import Feedback_Form, Rewiew_Form, Client_Form

def index(request):
    model = Employees
    employees = Employees.objects.all()[:3]
    context = {'employees': employees}
    template_name = 'index.html'
    return render(request, template_name, context)

def feedback(request):
    if request.method == "POST":
        form = Feedback_Form(request.POST)
        if form.is_valid():
            messages.success(request, 'Заявка успешно оставлена!')
            form.save()
        else:
            messages.error(request, 'Ошибка заполнения формы!')
    else:
        form = Feedback_Form()  # Создайте пустой экземпляр формы для передачи в контекст
    return render(request, 'feedback.html', {'form': form})



def review(request):
    review_model = Review.objects.all().reverse()
    average_rating = round(calculate_average_rate(), 1)
    if request.method == "POST":
        form = Rewiew_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Новый отзыв')
            return redirect('index')  # Перенаправление на страницу обратной связи после успешного сохранения формы
        else:
            messages.error(request, 'Ошибка оставления')
    else:
        form = Rewiew_Form()
    return render(request, 'review.html', {'form': form, 'review_model': review_model, 'average_rating': average_rating})

def doctors(request):
    model = Employees
    employees = Employees.objects.all()
    context = {'employees': employees}
    template_name = 'doctors.html'
    return render(request, template_name, context)


def services(request):
    if request.method == 'POST':
        form = Client_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services')  # Перенаправление после успешного сохранения формы
    else:
        form = Client_Form()

    services = Service.objects.all()
    context = {'form': form, 'services': services}
    template_name = 'services.html'
    return render(request, template_name, context)
