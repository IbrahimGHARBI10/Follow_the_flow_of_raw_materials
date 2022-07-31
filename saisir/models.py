# Create your models here.

from django.db import models
import datetime as dt
from datetime import date, datetime


# Create your models here.

type={
    ('Sensible','Sensible'),
        ('Non Sensible','Non Sensible'),
}

etape={
    ('Comprimés nus','Comprimés nus'),
    ('Comprimés Peliculés','Comprimés Peliculés'),
    ('Gellules','Gellules'),
}

class Lot(models.Model):
    N_lot=models.CharField(primary_key=True,max_length=1000)

    def __str__(self):
        return f'{self.N_lot}'

class Produit(models.Model):
    code_Produit=models.CharField(max_length=1000)
    Produit=models.CharField(max_length=1000)
    N_Lot=models.OneToOneField(Lot,on_delete=models.CASCADE)    
    date_created=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=('-date_created',)
    @property
    def entre(self):
        entre=self.date_created.strftime("%d/%m/%y %H:%M")
        return entre
    def __str__(self):
        return f'{self.code_Produit}--{self.N_Lot}'

class ReconciliatModel(models.Model):
    N_Lot=models.OneToOneField(Lot,on_delete=models.CASCADE)
    Type=models.CharField(choices=type,max_length=200,null=False)
    forme=models.CharField(max_length=2000,null=True, blank=True)
    quantité=models.FloatField(null=True, blank=True)
    n_sac=models.IntegerField(null=True, blank=True)
    emplacement=models.CharField(max_length=200,null=True, blank=True)
    agent=models.CharField(max_length=200,null=True, blank=True)
    d_sortie=models.DateTimeField(null=True,blank=True)
    d_entre=models.DateTimeField(null=True,blank=True)
    qu=models.FloatField(null=True, blank=True)

    @property
    def hh(self):
        try:
            dispo=((self.quantité-self.qu)/self.quantité)*100
        except:
            dispo=100
        if dispo >0 :
            dispo=round(dispo,2)
        else:
            dispo=0

        return dispo  
    @property
    def duree(self):
        try:
            duree=self.d_sortie-self.d_entre
        except:
            duree=0
        return duree
    @property
    def j_stock(self):
        today=date.today()
        try:
            j_stock= today - self.d_entre.date()  
        except:
            j_stock= today   

        j_stock=(str(j_stock).split(",",7)[0]).split(" ",4)[0]
        return j_stock    
    @property
    def dat_e(self):
        if self.Type =='Sensible':
            self.Date_Expiration=self.d_entre + dt.timedelta(days = 3)
            exp=self.Date_Expiration.strftime("%d/%m/%y")
        else:
            self.Date_Expiration=self.d_entre + dt.timedelta(days = 15)
            exp=self.Date_Expiration.strftime("%d/%m/%y")

        return exp
    @property
    def entre(self):
        entre=self.d_entre.strftime("%d/%m/%y %H:%M")
        return entre
    @property
    def sortie(self):
        try:
            sortie=self.d_sortie.strftime("%d/%m/%y %H:%M")
        except:
            sortie=''
        return sortie

    @property
    def contr(self):
        today=dt.datetime.today()
        if self.Type =='Sensible':
            Date_Expiration=self.d_entre + dt.timedelta(days = 3)
            c_c=2
        else:
            Date_Expiration=self.d_entre + dt.timedelta(days = 15)
            c_c=5
        d1 = datetime.strftime(Date_Expiration, '%d-%m-%Y')
        d2 = datetime.strftime(today, '%d-%m-%Y')
        d1 = datetime.strptime(d1,'%d-%m-%Y')
        d2 = datetime.strptime(d2, '%d-%m-%Y')
        try:
            j_stock= d1-d2   
            j_stock=(str(j_stock).split("-",1)[0]).split(" ",1)[0]
            j_j=int(j_stock)
        except:
            j_j=0
            
        if j_j > c_c :
            j_j=1
        else:
            j_j=0
        return j_j        
    def __str__(self):
        return f'{self.forme}-{self.N_Lot}' 
     
class VracModel(models.Model):
    N_Lot=models.OneToOneField(Lot,on_delete=models.CASCADE)
    Type=models.CharField(choices=type,max_length=200,null=False)
    forme=models.CharField(max_length=2000,null=True, blank=True)
    quantité=models.FloatField(null=True, blank=True)
    n_sac=models.IntegerField(null=True, blank=True)
    emplacement=models.CharField(max_length=200,null=True, blank=True)
    agent=models.CharField(max_length=200,null=True, blank=True)
    d_sortie=models.DateTimeField(null=True, blank=True)
    d_entre=models.DateTimeField(null=True, blank=True)
    qu=models.FloatField(null=True, blank=True)

    @property
    def entre(self):
        entre=self.d_entre.strftime("%d/%m/%y %H:%M")
        return entre
    @property
    def sortie(self):
        try:
            sortie=self.d_sortie.strftime("%d/%m/%y %H:%M")
        except:
            sortie=''
        return sortie

    @property
    def hh(self):
        try:
            dispo=((self.quantité-self.qu)/self.quantité)*100
        except:
            dispo=100
        if dispo >0 :
            dispo=round(dispo,2)

        else:
            dispo=0

        return dispo    

    @property
    def duree(self):
        try:
            duree=self.d_sortie-self.d_entre
        except:
            duree=0
        return duree
    @property
    def j_stock(self):
        today=date.today()
        try:
            j_stock= today - self.d_entre.date()  
        except:
            j_stock= today   

        j_stock=(str(j_stock).split(",",7)[0]).split(" ",4)[0]
        return j_stock    
    @property
    def dat_e(self):
        if self.Type =='Sensible':
            Date_Expiration=self.d_entre + dt.timedelta(days = 7)
        else:
            Date_Expiration=self.d_entre + dt.timedelta(days = 45)
            
        return Date_Expiration.strftime("%d/%m/%y %H:%M")

    @property
    def contr(self):
        today=dt.datetime.today()
        if self.Type =='Sensible':
            Date_Expiration=self.d_entre + dt.timedelta(days = 7)
            c_c=4
        else:
            Date_Expiration=self.d_entre + dt.timedelta(days = 45)
            c_c=5
        d1 = datetime.strftime(Date_Expiration, '%d-%m-%Y')
        d2 = datetime.strftime(today, '%d-%m-%Y')
        d1 = datetime.strptime(d1,'%d-%m-%Y')
        d2 = datetime.strptime(d2, '%d-%m-%Y')
        try:
            j_stock= d1-d2   
            j_stock=(str(j_stock).split("-",1)[0]).split(" ",1)[0]
            j_j=int(j_stock)
        except:
            j_j=0
            
        if j_j > c_c :
            j_j=1
        else:
            j_j=0
        return j_j        
    def __str__(self):
        return f'-{self.N_Lot}' 
     
        
class PsfModel(models.Model):
    N_Lot=models.OneToOneField(Lot,on_delete=models.CASCADE)
    Type=models.CharField(choices=type,max_length=200,null=False)
    Forme=models.CharField(choices=etape,max_length=200,null=False)
    Quantité=models.FloatField(null=True, blank=True)
    N_sac=models.IntegerField(null=True, blank=True)
    Emplacement=models.CharField(max_length=200,null=True, blank=True)
    Agent=models.CharField(max_length=200,null=True, blank=True)
    D_sortie=models.DateTimeField(null=True, blank=True)
    D_entre=models.DateTimeField(null=True, blank=True)
    qu=models.FloatField(null=True, blank=True)

    @property
    def entre(self):
        entre=self.D_entre.strftime("%d/%m/%y %H:%M")
        return entre
    @property
    def sortie(self):
        try:
            sortie=self.D_sortie.strftime("%d/%m/%y %H:%M")
        except:
            sortie=''
        return sortie

    @property
    def hh(self):
        try:
            dispo=((self.Quantité-self.qu)/self.Quantité)*100
        except:
            dispo=100
        if dispo >0 :
            dispo=round(dispo,2)
        else:
            dispo=0

        return dispo    

    @property
    def duree(self):
        try:
            duree=self.D_sortie-self.D_entre
        except:
            duree=0
        return duree
    @property
    def j_stock(self):
        today=date.today()
        try:
            j_stock= today - self.D_entre.date()  
        except:
            j_stock= today   

        j_stock=(str(j_stock).split(",",7)[0]).split(" ",4)[0]
        return j_stock    
    @property
    def dat_e(self):
        if self.Forme=='Comprimés nus':
            if self.Type =='Sensible':
                Date_Expiration=self.D_entre + dt.timedelta(days = 7)
            else:
                Date_Expiration=self.D_entre + dt.timedelta(days = 90)
        elif self.Forme=='Comprimés Peliculés':
            if self.Type =='Sensible':
                Date_Expiration=self.D_entre + dt.timedelta(days = 3)
            else:
                Date_Expiration=self.D_entre + dt.timedelta(days = 60)
        else:
            if self.Type =='Sensible':
                Date_Expiration=self.D_entre + dt.timedelta(days = 3)
            else:
                Date_Expiration=self.D_entre + dt.timedelta(days = 60)
        return Date_Expiration.strftime("%d/%m/%y %H:%M")   
    def __str__(self):
        return f'-{self.N_Lot}'     
    @property
    def contr(self):
        today=dt.datetime.today()
        if self.Forme=='Comprimé nus':
            if self.Type =='Sensible':
                Date_Expiration=self.D_entre + dt.timedelta(days = 7)
                c_c=4
            else:
                Date_Expiration=self.D_entre + dt.timedelta(days = 90)
                c_c=10
        elif self.Forme=='Comprimé Peliculé':
            if self.Type =='Sensible':
                Date_Expiration=self.D_entre + dt.timedelta(days = 3)
                c_c=2           
            else:
                Date_Expiration=self.D_entre + dt.timedelta(days = 60)
                c_c=10
        else:
            if self.Type =='Sensible':
                Date_Expiration=self.D_entre + dt.timedelta(days = 3)
                c_c=2
            else:
                Date_Expiration=self.D_entre + dt.timedelta(days = 60)
                c_c=10
        d1 = datetime.strftime(Date_Expiration, '%d-%m-%Y')
        d2 = datetime.strftime(today, '%d-%m-%Y')
        d1 = datetime.strptime(d1,'%d-%m-%Y')
        d2 = datetime.strptime(d2, '%d-%m-%Y')
        try:
            j_stock= d1-d2   
            j_stock=(str(j_stock).split("-",1)[0]).split(" ",1)[0]
            j_j=int(j_stock)
        except:
            j_j=0
            
        if j_j > c_c :
            j_j=1
        else:
            j_j=0
        return j_j
         

class SechageModel(models.Model):
    N_Lot=models.OneToOneField(Lot,on_delete=models.CASCADE)
    Operateur=models.CharField(max_length=200,null=True, blank=True)
    Humidité=models.CharField(max_length=2000,null=True, blank=True)
    Température=models.CharField(max_length=2000,null=True, blank=True)
    Temps_de_Séchage=models.CharField(max_length=2000,null=True, blank=True)
    Date_Debut =models.DateTimeField(null=True, blank=True)
    Date_Fin =models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.Operateur}--{self.N_Lot}'
    @property
    def entre(self):    
        entre=self.Date_Debut.strftime("%d/%m/%y %H:%M")
        return entre
    @property
    def sortie(self):
        try:
            sortie=self.Date_Fin.strftime("%d/%m/%y %H:%M")
        except:
            sortie=''
        return sortie   
    @property
    def duree(self):
        try:
            duree=self.Date_Fin-self.Date_Debut
        except:
            duree=0
        return duree



class CompressionModel(models.Model):
    N_Lot=models.OneToOneField(Lot,on_delete=models.CASCADE)
    Operateur=models.CharField(max_length=200,null=True, blank=True)
    Quantité=models.FloatField(null=True, blank=True)
    Cadence=models.FloatField(null=True, blank=True)

    Date_Debut =models.DateTimeField(null=True, blank=True)
    Date_Fin =models.DateTimeField(null=True, blank=True)
    Rendement=models.CharField(max_length=200,null=True, blank=True)
    @property
    def entre(self):
        entre=self.Date_Debut.strftime("%d/%m/%y %H:%M")
        return entre
    @property
    def sortie(self):
        try:
            sortie=self.Date_Fin.strftime("%d/%m/%y %H:%M")
        except:
            sortie=''
        return sortie
    def __str__(self):
        return f'{self.Operateur}--{self.N_Lot}'
    @property
    def duree(self):
        try:
            duree=self.Date_Fin-self.Date_Debut
        except:
            duree=0
        return duree
    @property
    def duree_th(self):
        try:
            d_th=self.Quantité/self.Cadence  
        except:
            d_th=0
        return round(d_th,2)        

class SachetModel(models.Model):
    N_Lot=models.OneToOneField(Lot,on_delete=models.CASCADE)
    Operateur=models.CharField(max_length=200,null=True, blank=True)
    Quantité=models.FloatField(null=True, blank=True)
    Cadence=models.FloatField(null=True, blank=True)
    Date_Debut =models.DateTimeField(null=True, blank=True)
    Date_Fin =models.DateTimeField(null=True, blank=True)
    Rendement=models.CharField(max_length=200,null=True, blank=True)
    
    @property
    def entre(self):
        entre=self.Date_Debut.strftime("%d/%m/%y %H:%M")
        return entre
    @property
    def sortie(self):
        try:
            sortie=self.Date_Fin.strftime("%d/%m/%y %H:%M")
        except:
            sortie=''
        return sortie
    def __str__(self):
        return f'{self.Operateur}--{self.N_Lot}'
    @property
    def duree(self):
        try:
            duree=self.Date_Fin-self.Date_Debut
        except:
            duree=0
        return duree
    @property
    def duree_th(self):
        try:
            d_th=self.Quantité/self.Cadence  
        except:
            d_th=0
        return round(d_th,2)        
class PesageModel(models.Model):
    N_Lot=models.OneToOneField(Lot,on_delete=models.CASCADE)
    operateur=models.CharField(max_length=200,null=True, blank=True)
    Matiere_Non_Pesée=models.TextField(max_length=2000,null=True, blank=True)
    Quantité=models.FloatField(null=True, blank=True)
    Date_Debut =models.DateTimeField(null=True, blank=True)
    Date_Fin =models.DateTimeField(null=True, blank=True)
    @property
    def entre(self):
        entre=self.Date_Debut.strftime("%d/%m/%y %H:%M")
        return entre
    @property
    def sortie(self):
        try:
            sortie=self.Date_Fin.strftime("%d/%m/%y %H:%M")
        except:
            sortie=''
        return sortie
    def __str__(self):
        return f'{self.operateur}--{self.N_Lot}'
    @property
    def duree(self):
        try:
            duree=self.Date_Fin-self.Date_Debut
        except:
            duree=0
        return duree
class MouillageModel(models.Model):
    N_Lot=models.OneToOneField(Lot,on_delete=models.CASCADE)
    operateur=models.CharField(max_length=200,null=True, blank=True)
    Quantité=models.CharField(max_length=2000,null=True, blank=True)
    Date_Debut =models.DateTimeField(null=True, blank=True)
    Date_Fin =models.DateTimeField(null=True, blank=True)
    @property
    def entre(self):
        entre=self.Date_Debut.strftime("%d/%m/%y %H:%M")
        return entre
    @property
    def sortie(self):
        try:
            sortie=self.Date_Fin.strftime("%d/%m/%y %H:%M")
        except:
            sortie=''
        return sortie
    def __str__(self):
        return f'{self.operateur}--{self.N_Lot}'
    @property
    def duree(self):
        try:
            duree=self.Date_Fin-self.Date_Debut
        except:
            duree=0
        return duree
class CalibrageModel(models.Model):
    N_Lot=models.OneToOneField(Lot,on_delete=models.CASCADE)
    Operateur=models.CharField(max_length=2000,blank=True,null=True)
    Tamis=models.CharField(max_length=2000,blank=True,null=True)
    Date_Debut =models.DateTimeField(null=True, blank=True)
    Date_Fin =models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return f'{self.Operateur}--{self.N_Lot}'
    def duree(self):
        try:
            duree=self.Date_Fin-self.Date_Debut
        except:
            duree=0
        return duree
    @property
    def entre(self):
        entre=self.Date_Debut.strftime("%d/%m/%y %H:%M")
        return entre
    @property
    def sortie(self):
        try:
            sortie=self.Date_Fin.strftime("%d/%m/%y %H:%M")
        except:
            sortie=''
        return sortie
class DoublePesageModel(models.Model):
    N_Lot=models.OneToOneField(Lot,on_delete=models.CASCADE)
    operateur=models.CharField(max_length=200,null=True, blank=True)
    Quantité=models.FloatField(null=True, blank=True)

    Date_Debut =models.DateTimeField(null=True, blank=True)
    Date_Fin =models.DateTimeField(null=True, blank=True)
    @property
    def entre(self):
        entre=self.Date_Debut.strftime("%d/%m/%y %H:%M")
        return entre
    @property
    def sortie(self):
        try:
            sortie=self.Date_Fin.strftime("%d/%m/%y %H:%M")
        except:
            sortie=''
        return sortie
    def duree(self):
        try:
            duree=self.Date_Fin-self.Date_Debut
        except:
            duree=0
        return duree
    def __str__(self):
        return f'{self.operateur}-{self.N_Lot}'
class GranulatModel(models.Model):
    N_Lot=models.OneToOneField(Lot,on_delete=models.CASCADE)
    Operateur=models.CharField(max_length=200,null=True, blank=True)
    Poids_des_granulés_calibrés=models.FloatField(null=True, blank=True)
    Poids_théorique=models.FloatField(max_length=200,null=True, blank=True)
    Date_Debut =models.DateTimeField(max_length=200,null=True, blank=True)
    Date_Fin =models.DateTimeField(max_length=200,null=True, blank=True)
    Rendement=models.CharField(max_length=200,null=True, blank=True)
    
    def __str__(self):
        return f'{self.Operateur}--{self.N_Lot}'
    @property
    def entre(self):
        entre=self.Date_Debut.strftime("%d/%m/%y %H:%M")
        return entre
    @property
    def sortie(self):
        try:
            sortie=self.Date_Fin.strftime("%d/%m/%y %H:%M")
        except:
            sortie=''
        return sortie
    def duree(self):
        try:
            duree=self.Date_Fin-self.Date_Debut
        except:
            duree=0
        return duree
    @property
    def duree_th(self):
        try:
            d_th=self.Quantité/self.Cadence  
        except:
            d_th=0
        return round(d_th,2) 

class GeluleModel(models.Model):
    N_Lot=models.OneToOneField(Lot,on_delete=models.CASCADE)
    Operateur=models.CharField(max_length=200,null=True, blank=True)
    Quantité=models.FloatField(null=True, blank=True)
    Cadence=models.FloatField(null=True, blank=True)
    Date_Debut =models.DateTimeField(null=True, blank=True)
    Date_Fin =models.DateTimeField(null=True, blank=True)
    Rendement=models.CharField(max_length=200,null=True, blank=True)
    
    def __str__(self):
        return f'{self.Operateur}--{self.N_Lot}'
    @property
    def entre(self):
        entre=self.Date_Debut.strftime("%d/%m/%y %H:%M")
        return entre
    @property
    def sortie(self):
        try:
            sortie=self.Date_Fin.strftime("%d/%m/%y %H:%M")
        except:
            sortie=''
        return sortie
    def duree(self):
        try:
            duree=self.Date_Fin-self.Date_Debut
        except:
            duree=0
        return duree    
    @property
    def duree_th(self):
        try:
            d_th=self.Quantité/self.Cadence  
        except:
            d_th=0
        return round(d_th,2)  


class PeliculageModel(models.Model):
    N_Lot=models.OneToOneField(Lot,on_delete=models.CASCADE)
    Operateur=models.CharField(max_length=200,null=True, blank=True)
    Quantité=models.CharField(max_length=2000,null=True, blank=True)
    Date_Debut =models.DateTimeField(null=True, blank=True)
    Date_Fin =models.DateTimeField(null=True, blank=True)
    Rendement=models.CharField(max_length=200,null=True, blank=True)
    
    def __str__(self):
        return f'{self.Operateur}--{self.N_Lot}'
    @property
    def entre(self):
        entre=self.Date_Debut.strftime("%d/%m/%y %H:%M")
        return entre
    @property
    def sortie(self):
        try:
            sortie=self.Date_Fin.strftime("%d/%m/%y %H:%M")
        except:
            sortie=''
        return sortie
    def duree(self):
        try:
            duree=self.Date_Fin-self.Date_Debut
        except:
            duree=0
        return duree
    @property
    def duree_th(self):
        try:
            d_th=self.Quantité/self.Cadence  
        except:
            d_th=0
        return round(d_th,2) 


class MelangeModel(models.Model):
    N_Lot=models.OneToOneField(Lot,on_delete=models.CASCADE)
    Operateur=models.CharField(max_length=200,null=True, blank=True)
    Quantité=models.FloatField(null=True, blank=True)
    Date_Debut =models.DateTimeField(null=True, blank=True)
    Date_Fin =models.DateTimeField(null=True, blank=True)
    Rendement=models.CharField(max_length=200,null=True, blank=True)
    
    def __str__(self):
        return f'{self.Operateur}--{self.N_Lot}'
    @property
    def entre(self):
        entre=self.Date_Debut.strftime("%d/%m/%y %H:%M")
        return entre
    @property
    def sortie(self):
        try:
            sortie=self.Date_Fin.strftime("%d/%m/%y %H:%M")
        except:
            sortie=''
        return sortie
    def duree(self):
        try:
            duree=self.Date_Fin-self.Date_Debut
        except:
            duree=0
        return duree
    @property
    def duree_th(self):
        try:
            d_th=self.Quantité/self.Cadence  
        except:
            d_th=0
        return round(d_th,2)
class MiseEnBlisterModel(models.Model):
    N_Lot=models.OneToOneField(Lot,on_delete=models.CASCADE)
    Operateur=models.CharField(max_length=200,null=True, blank=True)
    Quantité=models.FloatField(null=True, blank=True)
    Cadence=models.FloatField(null=True, blank=True)

    Date_Debut =models.DateTimeField(null=True, blank=True)
    Date_Fin =models.DateTimeField(null=True, blank=True)
    Rendement=models.CharField(max_length=200,null=True, blank=True)
    
    def __str__(self):
        return f'{self.Operateur}--{self.N_Lot}'
    @property
    def entre(self):
        entre=self.Date_Debut.strftime("%d/%m/%y %H:%M")
        return entre
    @property
    def sortie(self):
        try:
            sortie=self.Date_Fin.strftime("%d/%m/%y %H:%M")
        except:
            sortie=''
        return sortie
    @property
    def duree(self):
        try:
            duree=self.Date_Fin-self.Date_Debut
        except:
            duree=0
        return duree
    @property
    def duree_th(self):
        try:
            d_th=self.Quantité/self.Cadence  
        except:
            d_th=0
        return round(d_th,2)        

class MiseEnFlaconModel(models.Model):
    N_Lot=models.OneToOneField(Lot,on_delete=models.CASCADE)
    Operateur=models.CharField(max_length=200,null=True, blank=True)
    Quantité=models.FloatField(null=True, blank=True)
    Cadence=models.FloatField(null=True, blank=True)

    Date_Debut =models.DateTimeField(null=True, blank=True)
    Date_Fin =models.DateTimeField(null=True, blank=True)
    Rendement=models.CharField(max_length=200,null=True, blank=True)
    
    def __str__(self):
        return f'{self.Operateur}--{self.N_Lot}'
    @property
    def entre(self):
        entre=self.Date_Debut.strftime("%d/%m/%y %H:%M")
        return entre
    @property
    def sortie(self):
        try:
            sortie=self.Date_Fin.strftime("%d/%m/%y %H:%M")
        except:
            sortie=''
        return sortie
    def duree(self):
        try:
            duree=self.Date_Fin-self.Date_Debut
        except:
            duree=0
        return duree
    @property
    def duree_th(self):
        try:
            d_th=self.Quantité/self.Cadence  
        except:
            d_th=0
        return round(d_th,2)        
