from django.shortcuts import render

def drinks(request):
    return render(request, 'drinks/drinks.html')
