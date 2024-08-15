from django.shortcuts import render
import datetime
# Create your views here.

def filters(request):
    da=datetime.datetime.now()
    d={'data':'ThIs aRe bUiLt iN fIlTerS','da':da,'c':11}
    return render(request,'filters.html',d)

def userfilters(request):
    d={'data':'ToDaY wE ArE dEaLinG wItH UsErDeFinEd FilTeRs'}
    return render(request,'userfilters.html',d)