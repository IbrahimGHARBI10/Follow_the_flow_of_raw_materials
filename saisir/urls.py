from django.urls import path
from . import views 
from django.contrib.auth import views as auth_view

urlpatterns=[
    
    path('',views.register_information_lot,name='users-register-lot'),
    path('etapes/',views.register_etape,name='users-register-etape'),
    
    path('Reconciliation/',views.register_etape_Reconciliat,name='etape-reconciliat'),
    path('Pesage/',views.register_etape_pesage,name='etape-pesage'),
    path('DoublePesage/',views.register_etape_doublepesage,name='etape-doublepesage'),
    path('Vrac/',views.register_etape_vrac,name='etape-vrac'),
    path('Psf/',views.register_etape_psf,name='etape-psf'),
    path('Melange/',views.register_etape_melange,name='etape-melange'),
    path('Granulation/',views.register_etape_granulat,name='etape-granulat'),
    path('MiseEnBlister/',views.register_etape_ms,name='etape-ms'),
    path('MiseEnFlacon/',views.register_etape_mf,name='etape-mf'),
    path('Compression/',views.register_etape_compression,name='etape-compression'),
    path('MisEenGellule/',views.register_etape_gelule,name='etape-gelule'),
    path('Pelliculage/',views.register_etape_peliculage,name='etape-peliculage'),
    path('MiseEnSachet/',views.register_etape_sachet,name='etape-sachet'),
    path('Sechage/',views.register_etape_sechage,name='etape-sechage'),
    path('Mouillage/',views.register_etape_mouillage,name='etape-mouillage'),
    path('Calibrage/',views.register_etape_calibrage,name='etape-calibrage'),
    

    path('show/',views.show_lot,name='show-lot'),
    path('reporting/',views.show_reporting,name='show-reporting'),
    path('showReconciliation/',views.reconiciliation_show,name='show-reconciliat'),
    path('showVrac/',views.vrac_show,name='show-vrac'),
    path('showPsf/',views.psf_show,name='show-psf'),



    path('detail/<int:pk>/',views.lot_detail,name='lot-detail'),
    
    path('doublepesage_edit/<int:pk>/',views.doublepesage_edit,name='douplepesage_edit'),
    path('gellule_edit/<int:pk>/',views.gelule_edit,name='gellule_edit'),
    path('granulat_edit/<int:pk>/',views.granulat_edit,name='granulat_edit'),
    path('doublepesage_edit/<int:pk>/',views.doublepesage_edit,name='doublepesage_edit'),
    path('melange_edit/<int:pk>/',views.melange_edit,name='melange_edit'),
    path('misenblister_edit/<int:pk>/',views.ms_edit,name='ms_edit'),
    path('misenflacon_edit/<int:pk>/',views.mf_edit,name='mf_edit'),
    path('peliculage_edit/<int:pk>/',views.peliculage_edit,name='peliculage_edit'),
    path('pesage_edit/<int:pk>/',views.pesage_edit,name='pesage_edit'),
    path('psf_edit/<int:pk>/',views.psf_edit,name='psf_edit'),
    path('reconciliat_edit/<int:pk>/',views.reconciliat_edit,name='reconciliat_edit'),
    path('vrac_edit/<int:pk>/',views.vrac_edit,name='vrac_edit'),
    path('compression_edit/<int:pk>/',views.compression_edit,name='compression_edit'),
    path('miseensachet_edit/<int:pk>/',views.sachet_edit,name='sachet_edit'),
    path('sechage_edit/<int:pk>/',views.sechage_edit,name='sechage_edit'),
    path('mouillage_edit/<int:pk>/',views.mouillage_edit,name='mouillage_edit'),
    path('calibrage_edit/<int:pk>/',views.calibrage_edit,name='calibrage_edit'),

    
    path('Done/',auth_view.LogoutView.as_view(template_name='saisir_done.html'),name='saisir_done'),
    
]