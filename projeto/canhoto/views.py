import csv
import io
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView
from .models import Canhoto
from .forms import CanhotoForm

def canhoto_list(request):
    template_name = 'canhoto_list.html'
    objects = Canhoto.objects.all()
    search = request.GET.get('search')
    if search:
        objects = objects.filter(codigo__icontains=search) #icontains pesquisa por tudo aquilo que contenha o que é pesquisado.
    context = {'object_list': objects}
    return render(request, template_name, context)

'''
class CanhotoList(ListView):
    model = Canhoto
    template_name = 'canhoto_list.html'
    paginate_by = 6
'''


def canhoto_detail(request, pk):
    template_name = 'canhoto_detail.html'
    obj = Canhoto.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)

def canhoto_add(request):
    template_name = 'canhoto_form.html'
    return render(request, template_name)

class CanhotoCreate(CreateView):
    model = Canhoto
    template_name = 'canhoto_form.html'
    form_class = CanhotoForm

class CanhotoUpdate(UpdateView):
    model = Canhoto
    template_name = 'canhoto_form.html'
    form_class = CanhotoForm

def save_data(data):
    '''
    Salva os dados no bd
    '''
    aux = []
    for item in data:
        codigo = item.get('codigo')
        data = item.get('data')
        valor = item.get('valor')
        tipo = item.get('tipo')
        obj = Canhoto(
            codigo=codigo,
            data=data,
            valor=valor,
            tipo=tipo,
        )
        aux.append(obj)
    Canhoto.objects.bulk_create(aux)

def import_csv(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        # Lendo arquivo InMemoryUploadedFile
        file = myfile.read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(file))
        # Gerando uma list comprehension
        data = [line for line in reader]
        save_data(data)
        return HttpResponseRedirect(reverse('canhoto:canhoto_list'))

    template_name = 'canhoto_import.html'
    return render(request, template_name)
