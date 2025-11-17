from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
import re
# Create your views here.
def Index(request):
    return render(request, "suggest/main.html")