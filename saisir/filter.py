import django_filters
from .models import *

class PostFilter (django_filters.FilterSet):
    N_Lot=django_filters.CharFilter()
    class Meta:
        model= Produit
        fields = ['Produit','code_Produit','N_Lot']

class PostFilter33 (django_filters.FilterSet):
    class Meta:
        model= Produit
        fields = ['Produit','code_Produit']

class PostFilter1 (django_filters.FilterSet):
    Date_Debut=django_filters.DateRangeFilter()
    Date_Fin=django_filters.DateRangeFilter()
    class Meta:
        model= CompressionModel
        fields = ['Date_Debut','Date_Fin']
        
class PostFilter2 (django_filters.FilterSet):
    Date_Debut=django_filters.DateRangeFilter()
    Date_Fin=django_filters.DateRangeFilter()
    class Meta:
        model= GranulatModel
        fields = ['Date_Debut','Date_Fin']


class PostFilter3 (django_filters.FilterSet):
    Date_Debut=django_filters.DateRangeFilter()
    Date_Fin=django_filters.DateRangeFilter()
    class Meta:
        model= PesageModel
        fields = ['Date_Debut','Date_Fin']

class PostFilter4 (django_filters.FilterSet):
    Date_Debut=django_filters.DateRangeFilter()
    Date_Fin=django_filters.DateRangeFilter()
    class Meta:
        model= DoublePesageModel
        fields = ['Date_Debut','Date_Fin']

class PostFilter5 (django_filters.FilterSet):
    Date_Debut=django_filters.DateRangeFilter()
    Date_Fin=django_filters.DateRangeFilter()
    class Meta:
        model= MiseEnBlisterModel
        fields = ['Date_Debut','Date_Fin']

class PostFilter6 (django_filters.FilterSet):
    Date_Debut=django_filters.DateRangeFilter()
    Date_Fin=django_filters.DateRangeFilter()
    class Meta:
        model= SachetModel
        fields = ['Date_Debut','Date_Fin']

class PostFilter7 (django_filters.FilterSet):
    Date_Debut=django_filters.DateRangeFilter()
    Date_Fin=django_filters.DateRangeFilter()
    class Meta:
        model= GeluleModel
        fields = ['Date_Debut','Date_Fin']

class PostFilter8 (django_filters.FilterSet):
    Date_Debut=django_filters.DateRangeFilter()
    Date_Fin=django_filters.DateRangeFilter()
    class Meta:
        model= MelangeModel
        fields = ['Date_Debut','Date_Fin']

class PostFilter9 (django_filters.FilterSet):
    Date_Debut=django_filters.DateRangeFilter()
    Date_Fin=django_filters.DateRangeFilter()
    class Meta:
        model= SechageModel
        fields = ['Date_Debut','Date_Fin']

class PostFilter10 (django_filters.FilterSet):
    Date_Debut=django_filters.DateRangeFilter()
    Date_Fin=django_filters.DateRangeFilter()
    class Meta:
        model= PeliculageModel
        fields = ['Date_Debut','Date_Fin']
class PostFilterR (django_filters.FilterSet):
    d_entre=django_filters.DateRangeFilter()
    class Meta:
        model= ReconciliatModel
        fields = ['d_entre']
class PostFilterV (django_filters.FilterSet):
    d_entre=django_filters.DateRangeFilter()
    class Meta:
        model= VracModel
        fields = ['d_entre']
class PostFilterP (django_filters.FilterSet):
    D_entre=django_filters.DateRangeFilter()
    class Meta:
        model= PsfModel
        fields = ['D_entre']

      

        