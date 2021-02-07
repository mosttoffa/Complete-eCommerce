from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView





class HomeView(TemplateView):  # Home View 
    template_name = "home.html"


