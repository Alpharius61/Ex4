from django.shortcuts import render, redirect
from bands.models import Band
from bands.models import BandsAdd
from bands.form import bandForm
# Create your views here.


def bands(request):
    # Récupérer toutes les groupes
    bands = BandsAdd.objects.all()

    context = {
        'bands': bands
    }
    return render(request, 'bands/bands.html', context)


def band_detail(request, band_id):
    # Récupérer un groupe en particulier grâce à son id (clé primaire)
    band = BandsAdd.objects.get(id=band_id)
    context = {'band': band}

    if request.method == 'POST':
        band.delete()
        return redirect('bands:index')

    

    return render(request, 'bands/band_detail.html', context)


def bandAdd(request):
    form = bandForm()
    if request.method == 'POST':
        form = bandForm(request.POST)
        if form.is_valid():
            form.save()
            print('save')
            return redirect('bands:index')

    context = {
        'form': form
    }
    return render(request, 'bands/band_add.html', context)

def bandUp(request):
    form = bandForm()
    if request.method == 'POST':
        form = bandForm(request.POST)
        if form.is_valid():
            form.save()
            print('save')
            return redirect('bands:index')

    context = {
        'form': form
    }
    return render(request, 'bands/bandUp.html', context)
