from django.shortcuts import render
from .forms import SimpleForm

def form_view(request):
    if request.method == 'POST':
        form = SimpleForm(request.POST)
        if form.is_valid():
            return render(request, 'success.html')  # optional success template
    else:
        form = SimpleForm()
    return render(request, 'form.html', {'form': form})
