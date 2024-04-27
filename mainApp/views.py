from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import *

class BolimlarView(View):
    def get(self, request):
        bolimlar = Bolim.objects.all()
        return render(request, "bolim.html", {'bolimlar':bolimlar})

class KitoblarView(View):
    def get(self, request):
        kitoblar = Kitob.objects.all().order_by('nom')
        return render(request, "kitob.html", {'kitoblar':kitoblar})

class TirikKitobView(View):
    def  get(self,request):
        tirik_mualliflar = Muallif.objects.filter(tirik=True)
        kitoblar = Kitob.objects.filter(muallif__in=tirik_mualliflar)
        return render(request, 'tirik_kitob.html', {'kitoblar': kitoblar})

def KitobView(request, pk):
    kitob = get_object_or_404(Kitob, pk=pk)
    return render(request, 'kitob2.html', {'kitob': kitob})


def kitob_ochirish(request, pk):
    kitob = get_object_or_404(Kitob, pk=pk)
    if request.method == 'POST':
        kitob.delete()
        return redirect('kitoblar')
    return render(request, 'kitob2.html', {'kitob':kitob})
