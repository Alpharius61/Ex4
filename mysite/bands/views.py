from django.shortcuts import render, redirect
from bands.models import Band
from bands.models import BandsManage
# Create your views here.


def bands(request):
    # Récupérer toutes les groupes
    bands = Band.objects.all()

    context = {
        'bands': bands
    }
    return render(request, 'bands/bands.html', context)


def band_detail(request, band_id):
    # Récupérer un groupe en particulier grâce à son id (clé primaire)
    band = Band.objects.get(id=band_id)
    context = {'band': band}
    return render(request, 'bands/band_detail.html', context)


def bandAdd(request):
    form = BandsManage
    if request.method == 'POST':
        form = BandsManage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bands:bands')

    context = {
        'form': form
    }
    return render(request, 'bands/band_add.html', context)
