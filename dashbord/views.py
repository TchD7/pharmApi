from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import PharmForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required



# Create your views here.
#conexion au dashbord
@login_required
def  create(request):
    form = PharmForm()
    de_garde = Pharms_de_garde.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        pharm_list = Pharms.objects.filter(name__icontains=q)
    else:
        pharm_list = Pharms.objects.all()
    if request.method == 'POST':
        form = PharmForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Pharmacie enrégistré")
            return redirect('create')
        else:
            messages.error(request, "Il y'a erreur")
            return redirect('create')
    context = {
            'de_garde':de_garde,
            'form': form,
            'pharm_list': pharm_list,
            
        }
    return render(request, 'create.html',context)


def update(request,pharm_id):
    pharm_id = int(pharm_id)
    pharm = Pharms.objects.get(id = pharm_id)
    pharm_form = PharmForm(request.POST, instance = pharm)
    if pharm_form.is_valid():
        pharm_form.save()
        return redirect('create')
    context = {
        'form': pharm_form
    }
    return render(request,'create.html',context)
def delete(request,pharm_id):
    pharm_id = int(pharm_id)
    try:
        pharmS = Pharms.objects.get(id = pharm_id)
    except Pharms.DoesNotExist:
        return redirect('create')
    pharmS.delete()
    messages.error(request, "Pharmacie suprimer")
    return redirect('create')

#de garde
def garde(request, **kwargs):
    pharm_list = Pharms.objects.filter(id = kwargs.get('pharm_id',"")).first()
    de_garde, status = Pharms_de_garde(pharm_list = pharm_list)
    garde.is_garde()
    return redirect('create')


def delete_on_garde(request,pharm_id):
    pharm_id = int(pharm_id)
    try:
        eject = Pharms_de_garde.objects.filter(id=pharm_id)
    except eject.DoesNotExist:
        return redirect('create')
    eject.delete()
    return redirect('create')
    