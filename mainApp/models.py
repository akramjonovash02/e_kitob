from django.db import models

class Bolim(models.Model):
    nom = models.CharField(max_length=255)
    haqida = models.TextField()

    def __str__(self):
        return self.nom

class Muallif(models.Model):
    ism= models.CharField(max_length=255)
    tirik=models.BooleanField(default=False)
    mamlakat=models.CharField(max_length=50)

    def __str__(self):
        return self.ism

class Kitob(models.Model):
    nom=models.CharField(max_length=255)
    muallif=models.ForeignKey(Muallif, on_delete=models.CASCADE)
    yil=models.PositiveIntegerField()
    bolim=models.ForeignKey(Bolim, on_delete=models.CASCADE)
    file=models.FileField(null=True, blank=True)

    def __str__(self):
        return self.nom
