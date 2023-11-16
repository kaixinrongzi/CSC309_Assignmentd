from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.db import IntegrityError
import traceback, json

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method != "POST":
        return JsonResponse({'message' : "Method not allowed."}, status=405)
    try:
        form = RegisterForm(json.loads(request.body))
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data.get('email'),
                first_name=form.cleaned_data.get('phone'),  # doesn't matter
                password=form.cleaned_data['password1'],
            )
            return JsonResponse({'message' : "User added."})
    except IntegrityError:
        return JsonResponse({'message' : "Username already exists."}, status=409)
    except:
        traceback.print_exc()
    # handles any error or invalid form
    return JsonResponse({'message' : "Unknown error."}, status=400)
