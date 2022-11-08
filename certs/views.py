from django.shortcuts import render, HttpResponse
from .models import Certificate

# Create your views here.
def home(request, slug=""):
    std = {
        "student_name" : "No certificate found",
        "student_id" : "None",
        "cert_number" : None,
        "cert_created" : "Certificate ID is invalid",
        "course" : "-",
        "slug" : "nocertificate",
        "gdrive_id" : "1O0EVKgJOKO_Y4MYlz_eKuufdbcSKFsO7",
    }
    return render(request, 'nocert.html', {'std':std})


def cert_check(request, slug):
    try:
        std = Certificate.objects.filter(slug = slug)[0]
        return render(request, 'cert.html', {'std':std})
    except:
        std = {
            "student_name" : "No certificate found",
            "student_id" : "None",
            "cert_number" : None,
            "cert_created" : "Certificate ID is invalid",
            "course" : "-",
            "slug" : "nocertificate",
            "gdrive_id" : "1O0EVKgJOKO_Y4MYlz_eKuufdbcSKFsO7",
        }
        return render(request, 'nocert.html', {'std':std})

