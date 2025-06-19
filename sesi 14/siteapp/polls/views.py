from django.http import HttpResponse

def alamat_view(request):
    return HttpResponse("Alamat: JL.Kp.Cibeber Sukamanah Cimanggu")

def telepon_view(request):
    return HttpResponse("Telepon: +62 858-6075-1896")