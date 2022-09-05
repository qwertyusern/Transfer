from django.shortcuts import render
from django.views import View
from .models import  *


class ClubsView(View):
    def get(self, request,d_nom):
        c = Club.objects.all()
        d=Club.objects.filter(davlat=d_nom)
        return render(request,"clubs.html", {"clubs":c,"davlats":d})

class AsosiyView(View):
    def get(self, request,d_nom):
        d = Club.objects.filter(davlat=d_nom)
        return render(request,"index.html", {"davlats":d})

class PlayersView(View):
    def get(self, request,d_nom):
        o = Oyinchi.objects.all()
        d = Club.objects.filter(davlat=d_nom)
        return render(request,"players.html",{"players":o,"davlats":d})

class U20PlayerView(View):
    def get(self, request,d_nom):
        d = Club.objects.filter(davlat=d_nom)
        p = Oyinchi.objects.filter(yosh__lte=20).order_by("-narx")
        return render(request,"U20-players.html", {"davlats":d,"players":p})

class TransferView(View):
    def get(self, request,d_nom,m_yil):
        t = Transfer.objects.filter(mavsum=m_yil)
        d = Club.objects.filter(davlat=d_nom)
        return render(request,"transfer-archive.html", {"davlats":d,"transfers":t})

class LastView(View):
    def get(self, request,d_nom):
        d = Club.objects.filter(davlat=d_nom)
        t = Transfer.objects.filter(mavsum="2022-2023")
        return render(request,"latest-transfers.html", {"davlats":d,"transfers":t})

class StatsView(View):
    def get(self, request,d_nom):
        d = Club.objects.filter(davlat=d_nom)
        t = Transfer.objects.filter(narx__gte=50)
        return render(request,"stats.html",{"davlats":d,"tansfers":t})

class UrinishView(View):
    def get(self, request,d_nom):
        d = Club.objects.filter(davlat=d_nom)
        return render(request,"tryouts.html", {"davlats":d})


class AboutView(View):
    def get(self, request,d_nom):
        d = Club.objects.filter(davlat=d_nom)
        return render(request,"about.html",{"davlats": d})




