from django.shortcuts import render

# Create your views here.
def yubisayu(request):
    return render(request, 'index.html')