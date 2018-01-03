from django.shortcuts import render
from django.views.generic.base import View
from django import forms
from .form import articaleForm

# Create your views here.
class articaleView(View):
    def post(self,request):
        upform = articaleForm(request.POST)
        if upform.is_valid():
            aa = upform.save(commit=False)
            aa.save()
            upform.save_m2m()
            return render(request, 'upform.html', {'selfforms': upform})