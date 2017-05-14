from django.shortcuts import render
from .forms import SignupForm


# Create your views here.

def signupform(request):
    # if form is submitted
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            return render(request, 'result.html', {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
            })
    else:
        form = SignupForm()
        return render(request, 'signupform.html', {'form': form});
