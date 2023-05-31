from django.shortcuts import render
from django.contrib import messages
from .models import Employees
from .forms import Feedback_Form

def index(request):
    model = Employees
    employees = Employees.objects.all()#[:3]
    context = {'employees': employees}
    template_name = 'index.html'
    return render(request, template_name, context)


from django.shortcuts import render
from django.contrib import messages
from .forms import Feedback_Form

def feedback(request):
    if request.method == "POST":
        form = Feedback_Form(request.POST)
        if form.is_valid():
            messages.success(request, 'Заявка успешно оставлена!')
            form.save()
        else:
            messages.error(request, 'Ошибка заполнения формы!')
    return render(request, 'feedback.html', {'form': Feedback_Form})


