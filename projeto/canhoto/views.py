from django.shortcuts import render
from .models import Canhoto

def canhoto_list(request):
    template_name = 'canhoto_list.html'
    objects = Canhoto.objects.all()
    context = {'object_list': objects}
    return render(request, template_name, context)