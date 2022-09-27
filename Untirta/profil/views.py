from django.shortcuts import render

# Create your views here.
def indexprofil(request):
    judul = "PROFIL"
    

    konteks={
        'title': judul,
    }
    return render(request,'profil.html',konteks)