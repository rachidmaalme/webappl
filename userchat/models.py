from django.db import models

# Create your models here.


class Countries(models.Model):
     matricule = models.CharField(max_length=10)
     img = models.ImageField(upload_to ='post_img/')
     def __str__(self):
        return self.matricule


class Gendar(models.Model):
     sex = models.CharField(max_length=6)
     def __str__(self):
        return self.sex

class NativeSpeeker(models.Model):
        matNSpeakN = models.CharField(max_length=10)
        def __str__(self):
            return self.matNSpeakN



class PracticalSpeeker(models.Model):
        matpSpeak = models.CharField(max_length=2)
        def __str__(self):
            return self.matpSpeak

class Fonction(models.Model):
    intitule = models.CharField(max_length=30)
    def __str__(self):
        return self.intitule


class Personne(models.Model):
    courriel = models.EmailField()
    nom= models.CharField(max_length=10)
    Prenom = models.CharField(max_length=10)
    date_de_naissance = models.DateField()
    mot_de_passe = models.CharField(max_length=32)
    country = models.ForeignKey(Countries, on_delete = models.CASCADE)
    NativeSpeeker = models.ForeignKey(NativeSpeeker, on_delete = models.CASCADE)
    PracticeSpeeker = models.ForeignKey(PracticalSpeeker, on_delete = models.CASCADE)
    gendar=models.ForeignKey(Gendar,on_delete = models.CASCADE)
    amis = models.ManyToManyField("self",null=True, blank=True)
    def __str__ (self):
        return self.nom + self.Prenom


class Message(models.Model):
    auteur = models.ForeignKey(Personne, on_delete = models.CASCADE)
    contenu = models.TextField()
    date_de_publication = models.DateField(auto_now=True)
    def __str__(self) :
        if len(self.contenu) > 20:
              return self.contenu[:19] + "..."
        else:
              return self.contenu
