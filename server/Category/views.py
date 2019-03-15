from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.


@csrf_exempt
def getCategories(request):
	data = Category.objects.all().values()
	return JsonResponse(list(data),safe=False)