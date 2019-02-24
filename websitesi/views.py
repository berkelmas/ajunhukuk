from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Makaleler, MakaleTags, isilanlari, Contact

# Create your views here.

def anasayfa(request):

    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

    return render(request, 'websitesi/index.html', { 'nbar' : 'anasayfa', 'ucmakale' : ucmakale})

def hakkimizda(request):

    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

    return render(request, 'websitesi/about.html', { 'nbar' : 'hakkimizda', 'ucmakale' : ucmakale})

def uzmanliklar(request):

    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

    return render(request, 'websitesi/uzmanliklar.html', { 'nbar' : 'uzmanliklar', 'ucmakale' : ucmakale})

def kariyer(request):

    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

    kariyer = isilanlari.objects.all()


    return render(request, 'websitesi/kariyerolanaklari.html', { 'nbar' : 'kariyer', 'ucmakale' : ucmakale, 'kariyer' : kariyer})

def makaleler(request):

    if request.GET.get('hukuki-alan'):

        alan = request.GET.get('hukuki-alan')

        makale_list = Makaleler.objects.filter(makale_kategori=alan)

        print(request.GET.get('hukuki-alan'))

        paginator = Paginator(makale_list, 4)

        page = request.GET.get('page')
        articles = paginator.get_page(page)
        ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

        return render(request, 'websitesi/makaleler.html', {'nbar' : 'makaleler', 'articles' : articles, 'ucmakale' : ucmakale})

    else:
        makale_list = Makaleler.objects.all()
        paginator = Paginator(makale_list, 4)

        page = request.GET.get('page')
        articles = paginator.get_page(page)

        ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

        return render(request, 'websitesi/makaleler.html', {'nbar': 'makaleler', 'articles': articles, 'ucmakale' : ucmakale})

def iletisim(request):

    if request.method == 'POST':

        adsoyad = request.POST.get('isim')
        email = request.POST.get('email')
        konu = request.POST.get('konu')
        telefon = request.POST.get('telefon')
        mesaj = request.POST.get('mesaj')

        iletisim = Contact(iletisim_adsoyad=adsoyad, iletisim_telefon=telefon, iletisim_mail=email,
                               iletisim_konu=konu, iletisim_mesaj=mesaj)
        iletisim.save()
        return redirect('anasayfa')

    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

    return render(request, 'websitesi/iletisim.html', { 'nbar' : 'iletisim', 'ucmakale' : ucmakale})


def makaledetay(request, makaleslug):

    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

    oncekimakale = Makaleler.objects.all().order_by('?').first()
    sonrakimakale = Makaleler.objects.all().order_by('?').first()

    makale = Makaleler.objects.get(makale_slug=makaleslug)


    return render(request, 'websitesi/tekmakale.html', {'nbar' : 'makaledetay', 'makale' : makale,'ucmakale' : ucmakale, 'oncekimakale' : oncekimakale, 'sonrakimakale' : sonrakimakale})






def ailehukuku(request):

    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

    return render(request, 'websitesi/ailehukuku.html', {'nbar' : 'altuzmanliklar', 'nalt' : 'ailehukuku', 'ucmakale' : ucmakale})

def ishukuku(request):

    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

    return render(request, 'websitesi/ishukuku.html', {'nbar' : 'altuzmanliklar', 'nalt' : 'ishukuku', 'ucmakale' : ucmakale})

def saglikhukuku(request):

    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

    return render(request, 'websitesi/saglikhukuku.html', {'nbar' : 'altuzmanliklar', 'nalt' : 'saglikhukuku', 'ucmakale' : ucmakale})

def ticarethukuku(request):

    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

    return render(request, 'websitesi/ticarethukuku.html', {'nbar' : 'altuzmanliklar', 'nalt' : 'ticarethukuku', 'ucmakale' : ucmakale})


def cezahukuku(request):

    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

    return render(request, 'websitesi/cezahukuku.html', {'nbar' : 'altuzmanliklar', 'nalt' : 'cezahukuku', 'ucmakale' : ucmakale})

def gayrimenkulhukuku(request):

    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

    return render(request, 'websitesi/gayrimenkulhukuku.html', {'nbar' : 'altuzmanliklar', 'nalt' : 'gayrimenkulhukuku', 'ucmakale' : ucmakale})

def sozlesmelerhukuku(request):

    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

    return render(request, 'websitesi/sozlesmelerhukuku.html', {'nbar' : 'altuzmanliklar', 'nalt' : 'sozlesmelerhukuku', 'ucmakale' : ucmakale})

def icrahukuku(request):

    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

    return render(request, 'websitesi/icrahukuku.html', {'nbar' : 'altuzmanliklar', 'nalt' : 'icrahukuku', 'ucmakale' : ucmakale})

def trafikhukuku(request):

    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

    return render(request, 'websitesi/trafikhukuku.html', {'nbar' : 'altuzmanliklar', 'nalt' : 'trafikhukuku', 'ucmakale' : ucmakale})