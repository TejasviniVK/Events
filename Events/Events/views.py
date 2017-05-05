from django.shortcuts import render

__author__ = 'cfit001'

from django.http import HttpResponse
import datetime
from Events.models import Details, Cities


def index(request):
    return render(request, 'Main1.html', {})


def add_html(request):
    Place = Cities.objects.all()
    return render(request, 'Add.html', {'Place': Place})


def Search_html(request):
    event_name = Details.objects.all()
    return render(request, 'Search.html', {'event_name': event_name})


def filters_html(request):
    return render(request, 'filters.html', {})


def filter_by_date(request):
    return render(request, 'filter_by_date.html', {})


def filters_by_place(request):
    Place = Cities.objects.all()
    return render(request, 'filter_by_place.html', {'Place': Place})


def filter_by_dateplace(request):
    Place = Cities.objects.all()
    return render(request, 'filter_by_date&place.html', {'Place': Place})


def filters_range_by_date(request):
    return render(request, 'filter_range_by_date.html', {})


def add_event123(request):
    if request.method == 'POST':
        user_name = request.POST.get("Event_Name")
        user_date = request.POST.get("Event_Date")
        user_info = request.POST.get("Event_Info")
        user_place = request.POST.get("Event_Place").capitalize()

        if user_place == 'Other':
            user_place = request.POST.get('new_place').capitalize()

        Details(name=user_name, date=user_date, place=user_place, info=user_info).save()

        cities = [i.city for i in Cities.objects.all()]
        if user_place not in cities:
            Cities(city=user_place).save()

        return HttpResponse("Event Added Successfully!!!Congratulations")

    else:
        return HttpResponse("Something went wrong")


def delete_event(request):
    if request.method == 'POST':
        user_del_ID = request.POST.get("search_ID")
        Details.objects.get(id=user_del_ID).delete()
        return HttpResponse("Deletion Successfull")
    else:
        return HttpResponse("Something went wrong!")


def update_event(request):
    if request.method == 'POST':
        search_ID = request.POST.get("search_ID")
        name_update = request.POST.get("Event_Name")
        date_update = request.POST.get("Event_Date")
        info_update = request.POST.get("Event_Info")
        place_update = request.POST.get("Event_Place")
        Details.objects.filter(id=search_ID).update(name=name_update, date=date_update, place=place_update, info=info_update)
        return HttpResponse("Event Updated Successfully")
    else:
        return HttpResponse("Something went wrong!!!")


def search_event(request):
    if request.method == 'POST':
        search_ID = request.POST.get("search_ID")
        data = Details.objects.get(id=search_ID)
        return render(request, 'search_event.html',
                      {'cities': Cities.objects.all(), 'data': data})
    else:
        return HttpResponse("Something went wrong")


def list_by_date_place(request):
    if request.method == "POST":
        date_ss = request.POST.get("Date_Place")
        place_ss = request.POST.get("Place_Date")
        dateandplace = Details.objects.filter(date=date_ss, place=place_ss)
        if not dateandplace:
            return HttpResponse("No events available")
        else:
            return render(request, 'list_by_date.html', {'data': dateandplace})


def list_by_place(request):
    if request.method == 'POST':
        place_s = request.POST.get("Place_Search")
        place_find = Details.objects.filter(place=place_s).order_by('date')
        if not place_find:
            return HttpResponse("No events available")
        else:
            return render(request, 'list_by_date.html', {'data': place_find})
    else:
        return HttpResponse("Something went wrong!")


def list_by_date(request):
    if request.method == 'POST':
        date_s = request.POST.get("Date_Search")
        date_find = Details.objects.filter(date=date_s).order_by('date')
        if not date_find:
            return HttpResponse("No events available")
        else:
            return render(request, 'list_by_date.html', {'data': date_find})
    else:
        return HttpResponse("Something went wrong!")


def range_by_date(request):
    if request.method == 'POST':
        date1 = request.POST.get("Date1")
        date2 = request.POST.get("Date2")
        if date1<date2:
            rangedate = Details.objects.filter(date__range=(date1, date2)).order_by('date')
        else:
             rangedate = Details.objects.filter(date__range=(date2, date1)).order_by('date')
        if not rangedate:
            return HttpResponse("No events available")
        else:
            return render(request, 'list_by_date.html', {'data': rangedate})
    else:
        return HttpResponse("Something went wrong!")


def list_by_todaydate(request):
    today = datetime.date.today()
    todayu = unicode(today)
    todayfinal = Details.objects.filter(date=todayu)
    upcoming = Details.objects.filter(date__gt=todayu).order_by('date')
    past = Details.objects.filter(date__lt=todayu).order_by('date')
    return render(request, 'filter_by_todaydate.html',{'todaylist': todayfinal, 'upcominglist': upcoming, 'pastlist': past})
