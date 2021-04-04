from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/register')
def index(request):
    return render(request,'frontend/build/index.html')