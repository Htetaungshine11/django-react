from django.shortcuts import render,redirect,reverse
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.forms.models import model_to_dict
# Create your views here.
def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        form.save()
        return redirect('/home')
        
    return render(request,'templates/register/register.html',{'form':form})