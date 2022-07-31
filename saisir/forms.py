from random import choices
from django import forms
from .models import *
from CycleDeProduit import settings

class SaisirLotForm(forms.ModelForm):

    class Meta:
        model=Lot
        fields = ['N_lot']

class SaisirForm(forms.ModelForm):

    class Meta: 
        model=Produit
        fields = ['Produit','code_Produit']

class SaisirForm3(forms.ModelForm):
    class Meta: 
        model=Lot
        fields = ['N_lot']

class SaisirFormC(forms.ModelForm):
    Date_Debut=forms.DateTimeField(required=False)
    Date_Fin=forms.DateTimeField(required=False)
    class Meta: 
        model=CompressionModel
        fields = ['Date_Debut','Date_Fin']
        


class CompressionForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)

    class Meta:
        model=CompressionModel
        fields = '__all__'
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),                   
                }

class CompressionUpdateForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=CompressionModel
        fields = ['Date_Debut','Date_Fin']
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),                   
                }

class MouillageForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)

    class Meta:
        model=MouillageModel
        fields = '__all__'
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),                   
                }
                
class MouillageUpdateForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=MouillageModel
        fields = ['Date_Debut','Date_Fin']
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),                   
                }


class CalibrageForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)

    class Meta:
        model=CalibrageModel
        fields = '__all__'
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),                   
                }
                
class CalibrageUpdateForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=CalibrageModel
        fields = ['Date_Debut','Date_Fin']
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),                   
                }


class MelangeForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=MelangeModel
        fields = '__all__'
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),

        }
class MelangeUpdateForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=MelangeModel
        fields = ['Date_Debut','Date_Fin']
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),

        }

class GeluleForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=GeluleModel
        fields = '__all__'
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),

        }
class GeluleUpdateForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=GeluleModel
        fields = ['Date_Debut','Date_Fin']
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),

        }

class PeliculageForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=PeliculageModel
        fields = '__all__'
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),

        }
class PeliculageUpdateForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=PeliculageModel
        fields = ['Date_Debut','Date_Fin']
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),

        }

class PesageForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=PesageModel
        fields = '__all__'
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),

        }
class PesageUpdateForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=PesageModel
        fields = ['Date_Debut','Date_Fin']
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),

        }

class DoublePesageForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=DoublePesageModel
        fields = '__all__'
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),
        }
class DoublePesageUpdateForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=DoublePesageModel
        fields = ['Date_Debut','Date_Fin']
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ReconciliatForm(forms.ModelForm):
    d_entre=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    d_sortie=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    
    class Meta:
        model=ReconciliatModel
        fields = ['N_Lot','Type','forme','quantité','n_sac','emplacement','agent','d_entre','d_sortie']
        widgets={ 
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),
        }

class VracForm(forms.ModelForm):
    d_entre=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    d_sortie=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=VracModel
        fields = ['N_Lot','Type','forme','quantité','n_sac','emplacement','agent','d_entre','d_sortie']
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),
        }
class GranulatForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=GranulatModel
        fields = '__all__'
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),
        }
class GranulatUpdateForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=GranulatModel
        fields = ['Date_Debut','Date_Fin']
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SachetForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=SachetModel
        fields = '__all__'
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),
        }
class SachetUpdateForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=SachetModel
        fields = ['Date_Debut','Date_Fin']
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),
        }


class MelangeForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=MelangeModel
        fields ='__all__'
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),
        }
class MelangeUpdateForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=MelangeModel
        fields = ['Date_Debut','Date_Fin']
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),
        }

class MiseEnBlisterForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=MiseEnBlisterModel
        fields = '__all__'
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),
        }
class MiseEnBlisterUpdateForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=MiseEnBlisterModel
        fields = ['Date_Debut','Date_Fin']
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),
        }


class MiseEnFlaconForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=MiseEnFlaconModel
        fields = '__all__'
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),
        }
class MiseEnFlaconUpdateForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=MiseEnFlaconModel
        fields = ['Date_Debut','Date_Fin']
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),
        }




class SechageForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=SechageModel
        fields = '__all__'
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),
        }
class SechageUpdateForm(forms.ModelForm):
    Date_Debut=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Date_Fin=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=SechageModel
        fields = ['Date_Debut','Date_Fin']
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),
        }



class PsfForm(forms.ModelForm):
    D_entre=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    D_sortie=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=PsfModel
        fields = ['N_Lot','Type','Forme','Quantité','N_sac','Emplacement','Agent','D_entre','D_sortie']
        
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PsfUpdateForm(forms.ModelForm):

    D_entre=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    D_sortie=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=PsfModel
        fields = ['D_sortie','D_entre','qu']
        
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),
        }
class VracUpdateForm(forms.ModelForm):
    d_entre=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    d_sortie=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=VracModel
        fields = ['d_sortie','d_entre','qu']
        
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),
        }
class ReconciliatUpdateForm(forms.ModelForm):
    d_entre=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    d_sortie=forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    class Meta:
        model=ReconciliatModel
        fields = ['d_sortie','d_entre','qu']
        
        widgets={
                        'N_Lot': forms.TextInput(attrs={'class': 'form-control'}),
        }

