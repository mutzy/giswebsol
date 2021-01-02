from django.shortcuts import render
from django.http import HttpResponse
from .resources import dataimportResource
from .models import dataimport
from tablib import Dataset
from django.contrib import messages
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.utils.html import escapejs
import json
from django.core import serializers
from django.contrib.auth.decorators import login_required



@login_required
def index(request):

    if request.method == 'POST':
        dataimport_resource = dataimportResource()
        dataset = Dataset()
        new_import = request.FILES['file']

        if not new_import.name.endswith('.xlsx'):
            messages.info(request, "wrong format")
            return render(request, 'home.html')
            print("Wrong Format")
        imported_data = dataset.load(new_import.read())
        for data in imported_data:
            value = dataimport(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8]
            )
            value.save()
    return render(request,'home.html')

@login_required
def index_alt(request):

    if request.method == 'POST':
        dataimport_resource = dataimportResource()
        dataset = Dataset()
        new_import = request.FILES['file_alt']

        if not new_import.name.endswith('.xlsx'):
            messages.info(request, "wrong format")
            return render(request, 'home.html')
            print("Wrong Format")
        imported_data = dataset.load(new_import.read())
        for data in imported_data:
            value = dataimport(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8]
            )
            value.save()
            return render(request,'home.html')
    return render(request,'home.html')

@login_required
def my_form(request):
    if request.method == 'POST':  
        if request.POST.get('hour') and request.POST.get('minutes') and request.POST.get('period') and request.POST.get('country') and request.POST.get('province') and request.POST.get('latitude') and request.POST.get('longtitude') and request.POST.get('narrative'):
            hour = request.POST.get('hour') 
            minutes = request.POST.get('minutes')
            period = request.POST.get('period')
            country = request.POST.get('country')
            province = request.POST.get('province')
            latitude = request.POST.get('latitude')
            longtitude = request.POST.get('longtitude') 
            narrative = request.POST.get('narrative')

            import_data = dataimport(country=country,province=province,latitude=latitude,longtitude=longtitude,narrative=narrative,hour=hour,minutes=minutes,period=period)
            import_data.save()
            return render(request, 'home.html')
    else:
        return render(request, 'home.html')
@login_required
def search(request):
    ctx = {}
    url_parameter = request.GET.get('q')
   
    if url_parameter:
        information = dataimport.objects.filter(country__icontains=url_parameter)
    else:
        #information = dataimport.objects.all() #get all from database
        information = None
    ctx["information"] = information
    
    # This takes the first book query an reformats the data so it can be read
    # by the map script on the frontend.
    #map_info = [{"loc":[float(info.longtitude), float(info.latitude)]} for info in information]

    if request.is_ajax():
        html = render_to_string(
            template_name="snippets/display.html", 
            context={"information": information}
        )

        data_dict = {"html_from_view": html}


        return JsonResponse(data=data_dict, safe=False)
    #return JsonResponse({"map_info": map_info})
    return render(request, "home.html", context)
@login_required
def detailview(request, d_id):
    ctx = {}
   
    if url_parameter:
        information = dataimport.objects.filter(id__icontains=d_id)
    else:
        #information = dataimport.objects.all() #get all from database
        information = None
    ctx["information"] = information
    
    # This takes the first book query an reformats the data so it can be read
    # by the map script on the frontend.
    #map_info = [{"loc":[float(info.longtitude), float(info.latitude)]} for info in information]

    if request.is_ajax():
        html = render_to_string(
            template_name="snippets/map.html", 
            context={"information": information}
        )

        data_dict = {"html_from_view": html}


        return JsonResponse(data=data_dict, safe=False)
    #return JsonResponse({"map_info": map_info})
    return render(request, "home.html", context)

