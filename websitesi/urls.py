from django.urls import path

from .views import anasayfa, hakkimizda, uzmanliklar, kariyer, iletisim, ailehukuku, ishukuku, \
    saglikhukuku, cezahukuku, gayrimenkulhukuku, sozlesmelerhukuku, icrahukuku, trafikhukuku, ticarethukuku, \
    makaleler, makaledetay

urlpatterns = [
    path('', anasayfa, name="anasayfa"),
    path('hakkimizda/', hakkimizda, name="hakkimizda"),
    path('uzmanlik-alanlarimiz/', uzmanliklar, name="uzmanliklar"),
    path('kariyer-olanaklari/', kariyer, name="kariyer"),
    path('iletisim/', iletisim, name="iletisim"),
    path('aile-hukuku/', ailehukuku, name="ailehukuku"),
    path('is-hukuku/', ishukuku, name="ishukuku"),
    path('saglik-hukuku/', saglikhukuku, name="saglikhukuku"),
    path('ceza-hukuku/', cezahukuku, name="cezahukuku"),
    path('gayrimenkul-hukuku/', gayrimenkulhukuku, name="gayrimenkulhukuku"),
    path('sozlesmeler-hukuku/', sozlesmelerhukuku, name="sozlesmelerhukuku"),
    path('icra-iflas-hukuku/', icrahukuku, name="icrahukuku"),
    path('trafik-hukuku/', trafikhukuku, name="trafikhukuku"),
    path('ticaret-hukuku/', ticarethukuku, name="ticarethukuku"),
    path('hukuki-yayinlar/', makaleler, name="makaleler"),
    path('<slug:makaleslug>/', makaledetay, name="makaledetay")
]