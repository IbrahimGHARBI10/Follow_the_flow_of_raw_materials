from django.shortcuts import render,redirect
from . forms import *
from . filter import *
from . models import *
# Create your views here.
def register_information_lot(request):
    
        if request.method == 'POST':
            u_form = SaisirLotForm(request.POST)
            p_form = SaisirForm(request.POST)
            
            if u_form.is_valid() and p_form.is_valid():
                user = u_form.save()
                p_form.instance.N_Lot = user  
                p_form.save()
                return redirect('users-register-etape')    
        else:
            u_form = SaisirLotForm()
            p_form = SaisirForm()
        context={
            'u_form':u_form,
                    'p_form':p_form,
                }        
        return render(request,'saisir_produit.html',context)

def register_etape(request):

    return render(request,'etapes.html')

def register_etape_compression(request):
        if request.method == 'POST':
                form = CompressionForm(request.POST)
                if  form.is_valid() :
                    form.save()
                    return redirect('users-register-etape')            
        else:
                    form = CompressionForm()
        context={
                                'form':form,
                                }        
        return render(request,'compression.html',context)

def register_etape_mouillage(request):
        if request.method == 'POST':
                form = MouillageForm(request.POST)
                if  form.is_valid():
                    form.save()
                    return redirect('users-register-etape')            
        else:
                    form = MouillageForm()
        context={
                                'form':form,
                                }        
        return render(request,'mouillage.html',context)


def register_etape_calibrage(request):
        if request.method == 'POST':
                form = CalibrageForm(request.POST)
                if  form.is_valid() :
                    form.save()
                    return redirect('users-register-etape')            
        else:
                    form = CalibrageForm()
        context={
                                'form':form,
                                }        
        return render(request,'calibrage.html',context)


def register_etape_granulat(request):
        if request.method == 'POST':
                form = GranulatForm(request.POST)
                if  form.is_valid() :
                    form.save()
                    return redirect('users-register-etape')    
        else:
                    form = CompressionForm()
        context={
                                'form':form,
                                }        
        return render(request,'granulat.html',context)
def register_etape_ms(request):
        if request.method == 'POST':
                form = MiseEnBlisterForm(request.POST)
                if  form.is_valid() :
                    form.save()
                    return redirect('users-register-etape')    
        else:
                    form = MiseEnBlisterForm()
        context={
                                'form':form,
                                }        
        return render(request,'ms.html',context)
def register_etape_mf(request):
        if request.method == 'POST':
                form = MiseEnFlaconForm(request.POST)
                if  form.is_valid() :
                    form.save()
                    return redirect('users-register-etape')    
        else:
                    form = MiseEnFlaconForm()
        context={
                                'form':form,
                                }        
        return render(request,'mf.html',context)
def register_etape_vrac(request):
        if request.method == 'POST':
                form = VracForm(request.POST)
                if  form.is_valid() :
                    form.save()
                    return redirect('users-register-etape')    
        else:
                    form = VracForm()
        context={
                                'form':form,
                                }        
        return render(request,'vrac.html',context)
def register_etape_melange(request):
        if request.method == 'POST':
                form = MelangeForm(request.POST)
                if  form.is_valid() :
                    form.save()
                    return redirect('users-register-etape')        
        else:
                    form = MelangeForm()
        context={
                                'form':form,
                                }        
        return render(request,'melange.html',context)

def register_etape_sechage(request):
        if request.method == 'POST':
                form = SechageForm(request.POST)
                if  form.is_valid() :
                    form.save()
                    return redirect('users-register-etape')        
        else:
                    form = SechageForm()
        context={
                                'form':form,
                                }        
        return render(request,'sechage.html',context)



def register_etape_psf(request):
        if request.method == 'POST':
                form =  PsfForm(request.POST)
                if  form.is_valid() :
                    form.save()
                    return redirect('users-register-etape')    
        else:
                    form =  PsfForm()
        context={
                                'form':form,
                                }        
        return render(request,'psf.html',context)

def register_etape_pesage(request):
        if request.method == 'POST':
                form = PesageForm(request.POST)
                if  form.is_valid() :
                    form.save()
                    return redirect('users-register-etape')    
        else:
                    form = PesageForm()
        context={
                                'form':form,
                                }        
        return render(request,'pesage.html',context)
def register_etape_doublepesage(request):
        if request.method == 'POST':
                form = DoublePesageForm(request.POST)
                if  form.is_valid() :
                    form.save()
                    return redirect('users-register-etape')    
                
        else:
                    form = DoublePesageForm()
        context={
                                'form':form,
                                }        
        return render(request,'doublepesage.html',context)
def register_etape_Reconciliat(request):
        if request.method == 'POST':
                form = ReconciliatForm(request.POST)
                if  form.is_valid() :
                    form.save()
                    return redirect('users-register-etape')    
        else:
                    form = ReconciliatForm()
        context={
                                'form':form,
                                }        
        return render(request,'reconciliat.html',context)

def register_etape_gelule(request):
        if request.method == 'POST':
                form = GeluleForm(request.POST)
                if  form.is_valid() :
                    form.save()
                    return redirect('users-register-etape')    
        else:
                    form = GeluleForm()
        context={
                                'form':form,
                                }        
        return render(request,'gellule.html',context)

def register_etape_sachet(request):
        if request.method == 'POST':
                form = SachetForm(request.POST)
                if  form.is_valid() :
                    form.save()
                    return redirect('users-register-etape')    
        else:
                    form = SachetForm()
        context={
                                'form':form,
                                }        
        return render(request,'sachet.html',context)



def register_etape_peliculage(request):
        if request.method == 'POST':
                form = PeliculageForm(request.POST)
                if  form.is_valid() :
                    form.save()
                    return redirect('users-register-etape')    
        else:
                    form = PeliculageForm()
        context={
                                'form':form,
                                }        
        return render(request,'peliculage.html',context)
def lot_detail(request, pk):
    lotde=Produit.objects.get(id=pk)
    try:
        comp=CompressionModel.objects.get(N_Lot=lotde.N_Lot)    
    except:
        comp=None 
    try:
        rec=ReconciliatModel.objects.get(N_Lot=lotde.N_Lot)    
    except:
        rec=None    
    try:
        vrac=VracModel.objects.get(N_Lot=lotde.N_Lot)    
    except:
        vrac=None    
    try:
        pl=PeliculageModel.objects.get(N_Lot=lotde.N_Lot)    
    except:
        pl=None    
    try:
        mg=GeluleModel.objects.get(N_Lot=lotde.N_Lot)    
    except:
        mg=None    

    try:
        psf=PsfModel.objects.get(N_Lot=lotde.N_Lot)    
    except:
        psf=None    
    try:
        dpesage=DoublePesageModel.objects.get(N_Lot=lotde.N_Lot)    
    except:
        dpesage=None    
    try:
        pesage=PesageModel.objects.get(N_Lot=lotde.N_Lot)    
    except:
        pesage=None    
    try:
        gran=GranulatModel.objects.get(N_Lot=lotde.N_Lot)    
    except:
        gran=None    
    try:
        melange=MelangeModel.objects.get(N_Lot=lotde.N_Lot)    
    except:
        melange=None    

    try:
        ms=MiseEnBlisterModel.objects.get(N_Lot=lotde.N_Lot)    
    except:
        ms=None    
    try:
        mf=MiseEnFlaconModel.objects.get(N_Lot=lotde.N_Lot)    
    except:
        mf=None    
  
    try:
        sachet=SachetModel.objects.get(N_Lot=lotde.N_Lot)    
    except:
        sachet=None 
    try:
        sechage=SechageModel.objects.get(N_Lot=lotde.N_Lot)    
    except:
        sechage=None   
    try:
        mouillage=MouillageModel.objects.get(N_Lot=lotde.N_Lot)    
    except:
        mouillage=None    
    try:
        calibrage=CalibrageModel.objects.get(N_Lot=lotde.N_Lot)    
    except:
        calibrage=None   
    context={
        
        'lotde':lotde,
        'sachet':sachet,
        'sechage':sechage,
        'comp':comp,
        'melange':melange,
        'gran':gran,
        'pesage':pesage,
        'dpesage':dpesage,
        'ms':ms,
        'mf':mf,
        'comp':comp,
        'psf':psf,
        'mouillage':mouillage,
        'calibrage':calibrage,
        'vrac':vrac,
        'rec':rec,
        'pl':pl,
        'mg':mg,

        }    
    

    return render(request,'lot_detail.html', context)

def show_lot(request):
    posts=Produit.objects.all()
    myFilter=PostFilter(request.GET,queryset=posts)
    posts=myFilter.qs
 
    if request.method=='POST':
        form=SaisirForm3(request.POST)

        if form.is_valid():
            instance=form.save(commit=False)
            instance.N_Lot=request.N_Lot
            instance.save()
            return redirect('show-lot')
    else:
        form=SaisirForm3()
    context={
            'form':form,
            'posts':posts,
            'myFilter':myFilter,
        }
    return render(request,'affichage.html', context)



def show_reporting(request):

    posts=CompressionModel.objects.all()
    myFilter=PostFilter1(request.GET,queryset=posts)
    posts=myFilter.qs


    posts1=GranulatModel.objects.all()
    myFilter=PostFilter2(request.GET,queryset=posts1)
    posts1=myFilter.qs
    
    posts2=PesageModel.objects.all()
    myFilter=PostFilter3(request.GET,queryset=posts2)
    posts2=myFilter.qs
    
    posts3=DoublePesageModel.objects.all()
    myFilter=PostFilter4(request.GET,queryset=posts3)
    posts3=myFilter.qs
    
    posts4=MiseEnBlisterModel.objects.all()
    myFilter=PostFilter5(request.GET,queryset=posts4)
    posts4=myFilter.qs
    
    posts5=SachetModel.objects.all()
    myFilter=PostFilter6(request.GET,queryset=posts5)
    posts5=myFilter.qs
    
    posts6=GeluleModel.objects.all()
    myFilter=PostFilter7(request.GET,queryset=posts6)
    posts6=myFilter.qs
    
    posts7=MelangeModel.objects.all()
    myFilter=PostFilter8(request.GET,queryset=posts7)
    posts7=myFilter.qs
    
    posts8=SechageModel.objects.all()
    myFilter=PostFilter9(request.GET,queryset=posts8)
    posts8=myFilter.qs
    
    posts9=PeliculageModel.objects.all()
    myFilter=PostFilter10(request.GET,queryset=posts9)
    posts9=myFilter.qs
    
    if request.method=='POST':
        results=request.GET['ope']
        form=SaisirForm3(request.GET)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.N_lot=request.N_lot
            instance.save()
            results.save()
            return redirect('show-reporting')
    else:
            form=SaisirForm3()
            try:
                results=request.GET['ope']
            except:
                results=request.POST.get('ope','')
    context={
            'form':form,
            'posts':posts,
            'posts1':posts1,
            'posts2':posts2,
            'posts3':posts3,
            'posts4':posts4,
            'posts5':posts5,
            'posts6':posts6,
            'posts7':posts7,
            'posts8':posts8,
            'posts9':posts9,
            'results':results,
            'myFilter':myFilter,
            }
    return render(request,'reporting.html', context)




def reconiciliation_show(request):
    recs=ReconciliatModel.objects.all()
    myFilter=PostFilterR(request.GET,queryset=recs)
    recs=myFilter.qs
    if request.method=='POST':
        form=ReconciliatForm(request.POST)
       
        if form.is_valid():
            instance=form.save(commit=False)
            instance.N_Lot=request.N_Lot
            instance.save()
            return redirect('show-reconciliat')
    else:
        form=ReconciliatForm()
        context={
            'form':form,
            'recs':recs,
            'myFilter':myFilter,
        }
    return render(request,'reconciliation.html', context)

def vrac_show(request):
    vracs=VracModel.objects.all()
    myFilter=PostFilterR(request.GET,queryset=vracs)
    vracs=myFilter.qs
    if request.method=='POST':
        form=VracForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.N_Lot=request.N_Lot
            instance.save()
            return redirect('show-vrac')
    else:
        form=VracForm()
        context={
            'form':form,
            'vracs':vracs,
            'myFilter':myFilter,
        }
    return render(request,'vracs.html', context)

def psf_show(request):
    psfs=PsfModel.objects.all()
    myFilter=PostFilterP(request.GET,queryset=psfs)
    psfs=myFilter.qs
    if request.method=='POST':
        form=PsfForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.N_Lot=request.N_Lot
            instance.save()
            return redirect('show-psf')
    else:
        form=PsfForm()
        context={
            'form':form,
            'psfs':psfs,
            'myFilter':myFilter,
        }
    return render(request,'psfs.html', context)


def reconciliat_edit(request,pk):
    
    rec=ReconciliatModel.objects.get(id=pk)
    if request.method=='POST':
        form=ReconciliatUpdateForm(request.POST, instance=rec)
        if form.is_valid():
            form.save()
            return redirect('users-register-etape')
    else:
                form=ReconciliatUpdateForm( instance=rec)

    context={
        'rec':rec,
        'form':form,
    }
    
    return render(request,'reconciliat_edit.html',context)
def doublepesage_edit(request,pk):
    
    rec=DoublePesageModel.objects.get(id=pk)
    if request.method=='POST':
        form=DoublePesageUpdateForm(request.POST, instance=rec)
        if form.is_valid():
            form.save()
            return redirect('users-register-etape')
    else:
                form=DoublePesageUpdateForm( instance=rec)

    context={
        'rec':rec,
        'form':form,
    }
    
    return render(request,'doublepesage_edit.html',context)
def pesage_edit(request,pk):
    
    rec=PesageModel.objects.get(id=pk)
    if request.method=='POST':
        form=PesageUpdateForm(request.POST, instance=rec)
        if form.is_valid():
            form.save()
            return redirect('users-register-etape')
    else:
                form=PesageUpdateForm( instance=rec)

    context={
        'rec':rec,
        'form':form,
    }
    
    return render(request,'pesage_edit.html',context)

def calibrage_edit(request,pk):
    
    rec=CalibrageModel.objects.get(id=pk)
    if request.method=='POST':
        form=CalibrageUpdateForm(request.POST, instance=rec)
        if form.is_valid():
            form.save()
            return redirect('users-register-etape')
    else:
                form=CalibrageUpdateForm( instance=rec)

    context={
        'rec':rec,
        'form':form,
    }
    
    return render(request,'calibrage_edit.html',context)

def mouillage_edit(request,pk):
    
    rec=MouillageModel.objects.get(id=pk)
    if request.method=='POST':
        form=MouillageUpdateForm(request.POST, instance=rec)
        if form.is_valid():
            form.save()
            return redirect('users-register-etape')
    else:
                form=MouillageUpdateForm( instance=rec)

    context={
        'rec':rec,
        'form':form,
    }
    
    return render(request,'mouillage_edit.html',context)


def gelule_edit(request,pk):
    
    rec=GeluleModel.objects.get(id=pk)
    if request.method=='POST':
        form=GeluleUpdateForm(request.POST, instance=rec)
        if form.is_valid():
            form.save()
            return redirect('users-register-etape')
    else:
                form=GeluleUpdateForm( instance=rec)

    context={
        'rec':rec,
        'form':form,
    }
    
    return render(request,'gelule_edit.html',context)
def granulat_edit(request,pk):
    
    rec=GranulatModel.objects.get(id=pk)
    if request.method=='POST':
        form=GranulatUpdateForm(request.POST, instance=rec)
        if form.is_valid():
            form.save()
            return redirect('users-register-etape')
    else:
                form=GranulatUpdateForm( instance=rec)

    context={
        'rec':rec,
        'form':form,
    }
    
    return render(request,'granulat_edit.html',context)
def melange_edit(request,pk):
    
    rec=MelangeModel.objects.get(id=pk)
    if request.method=='POST':
        form=MelangeUpdateForm(request.POST, instance=rec)
        if form.is_valid():
            form.save()
            return redirect('users-register-etape')
    else:
                form=MelangeUpdateForm( instance=rec)

    context={
        'rec':rec,
        'form':form,
    }
    
    return render(request,'melange_edit.html',context)

def sechage_edit(request,pk):
    
    rec=SechageModel.objects.get(id=pk)
    if request.method=='POST':
        form=SechageUpdateForm(request.POST, instance=rec)
        if form.is_valid():
            form.save()
            return redirect('users-register-etape')
    else:
                form=SechageUpdateForm( instance=rec)

    context={
        'rec':rec,
        'form':form,
    }
    
    return render(request,'sechage_edit.html',context)


def ms_edit(request,pk):
    
    rec=MiseEnBlisterModel.objects.get(id=pk)
    if request.method=='POST':
        form=MiseEnBlisterUpdateForm(request.POST, instance=rec)
        if form.is_valid():
            form.save()
            return redirect('users-register-etape')
    else:
                form=MiseEnBlisterUpdateForm( instance=rec)

    context={
        'rec':rec,
        'form':form,
    }
    
    return render(request,'ms_edit.html',context)

def mf_edit(request,pk):
    
    rec=MiseEnFlaconModel.objects.get(id=pk)
    if request.method=='POST':
        form=MiseEnFlaconUpdateForm(request.POST, instance=rec)
        if form.is_valid():
            form.save()
            return redirect('users-register-etape')
    else:
                form=MiseEnFlaconUpdateForm( instance=rec)

    context={
        'rec':rec,
        'form':form,
    }
    
    return render(request,'mf_edit.html',context)

def peliculage_edit(request,pk):
    
    rec=PeliculageModel.objects.get(id=pk)
    if request.method=='POST':
        form=PeliculageUpdateForm(request.POST, instance=rec)
        if form.is_valid():
            form.save()
            return redirect('users-register-etape')
    else:
                form=PeliculageUpdateForm( instance=rec)

    context={
        'rec':rec,
        'form':form,
    }
    
    return render(request,'peliculage_edit.html',context)
def psf_edit(request,pk):
    
    rec=PsfModel.objects.get(id=pk)
    if request.method=='POST':
        form=PsfUpdateForm(request.POST, instance=rec)
        if form.is_valid():
            form.save()
            return redirect('users-register-etape')
    else:
                form=PsfUpdateForm( instance=rec)

    context={
        'rec':rec,
        'form':form,
    }
    
    return render(request,'psf_edit.html',context)
def vrac_edit(request,pk):
    
    rec=VracModel.objects.get(id=pk)
    if request.method=='POST':
        form=VracUpdateForm(request.POST, instance=rec)
        if form.is_valid():
            form.save()
            return redirect('users-register-etape')
    else:
                form=VracUpdateForm( instance=rec)

    context={
        'rec':rec,
        'form':form,
    }
    
    return render(request,'vrac_edit.html',context)
def compression_edit(request,pk):
    
    rec=CompressionModel.objects.get(id=pk)
    if request.method=='POST':
        form=CompressionUpdateForm(request.POST, instance=rec)
        if form.is_valid():
            form.save()
            return redirect('users-register-etape')
    else:
                form=CompressionUpdateForm( instance=rec)

    context={
        'rec':rec,
        'form':form,
    }
    
    return render(request,'compression_edit.html',context)

def sachet_edit(request,pk):
    
    sachet=SachetModel.objects.get(id=pk)
    if request.method=='POST':
        form=SachetUpdateForm(request.POST, instance=sachet)
        if form.is_valid():
            form.save()
            return redirect('users-register-etape')
    else:
                form=CompressionUpdateForm( instance=sachet)

    context={
        'sachet':sachet,
        'form':form,
    }
    
    return render(request,'sachet_edit.html',context)
