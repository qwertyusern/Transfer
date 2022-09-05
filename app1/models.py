from django.db import models



class Club(models.Model):
    nom = models.CharField(max_length=80)
    rasm = models.FileField()
    president = models.CharField(max_length=50)
    rec_tr = models.PositiveSmallIntegerField()
    rec_ar = models.PositiveSmallIntegerField()
    murabbiy = models.CharField(max_length=50, null=True)
    yil = models.DateField(null=True)
    davlat = models.CharField(max_length=80)


class Oyinchi(models.Model):
    ism = models.CharField(max_length=50)
    yosh = models.PositiveSmallIntegerField()
    davlat = models.CharField(max_length=80)
    pozitsiya = models.CharField(max_length=20)
    narx = models.PositiveSmallIntegerField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)



class Transfer(models.Model):
    oyinchi = models.ForeignKey(Oyinchi, on_delete=models.CASCADE)
    narx = models.PositiveSmallIntegerField()
    mavsum = models.CharField(max_length=50)
    tr_narx = models.PositiveSmallIntegerField()
    club_dan = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="cl_from")
    club_ga = models.ForeignKey(Club, on_delete=models.CASCADE)



