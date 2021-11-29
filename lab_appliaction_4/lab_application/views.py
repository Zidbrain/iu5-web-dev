from django.shortcuts import render
import lab_application.models as models

# Create your views here.


def master(request):
    return render(request, 'master.html', {'icecreams': models.IcecreamTypes.objects.all(),
                                           'companies': models.Company.objects.all()})


def icecreamview(request, id):
    links = models.IcecreamToCompany.objects.all()
    companies = []
    for item in links:
        if item.icecream_id==id:
            companies.append(models.Company.objects.filter(idcompany=item.company_id)[0])

    return render(request, 'details.html', {'item': models.IcecreamTypes.objects.filter(id=id)[0],
                                            'companies': companies})


def companyview(request):
    idcompany = int(request.GET.get('idcompany'))
    links = models.IcecreamToCompany.objects.all()
    icecreams = []
    for item in links:
        if item.company_id == idcompany:
            icecreams.append(models.IcecreamTypes.objects.filter(id=item.icecream_id)[0])

    return render(request, 'company.html', {'company': models.Company.objects.filter(idcompany=idcompany)[0],
                                            'icecreams': icecreams})