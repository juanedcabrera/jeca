from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home_view(request):
    return JsonResponse({"message": "Welcome to the home page!"})

def jobs_view(request):
    return JsonResponse({"mesage": "This is the jobs page!"})

def docs_view(request):
    return JsonResponse({'message': 'This is the page for all documents'})

def company_view(request):
    return JsonResponse({'message': 'This is the page with all the companies'})

def docs_view(request):
    return JsonResponse({'message': 'This is the page for all documents'})
