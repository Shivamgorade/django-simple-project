from django.shortcuts import render, redirect
from .forms import FormDataForm
from .models import FormData

def form_view(request):
    if request.method == 'POST':
        form = FormDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to dashboard after submit
    else:
        form = FormDataForm()
    return render(request, 'form.html', {'form': form})

def dashboard_view(request):
    data = FormData.objects.all().order_by('-timestamp')
    return render(request, 'dashboard.html', {'data': data})
