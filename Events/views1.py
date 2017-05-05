__author__ = 'cfit001'

from django.shortcuts import render
import uuid
from django.http import HttpResponse
from Events.JsonHandler1 import *
import datetime

def index(request):
    storage = JsonHandler().read_json()
    data = storage['cities']
    data5 = {}
    for key in storage:
        if key != 'cities':
            data5.update({key: storage[key]["Event_Name"]})
    return render(request, 'Main1.html', {'data': data, 'dataname': data5})


def add_html(request):
    storage = JsonHandler().read_json()
    Place = storage['cities']
    return render(request, 'Add.html', {'Place': Place})


def Search_html(request):
    storage = JsonHandler().read_json()
    event_name = {}
    for key in storage:
        if key != 'cities':
            event_name.update({key: storage[key]['Event_Name']})
    return render(request, 'Search.html', {'event_name': event_name})


def filters_html(request):
    return render(request, 'filters.html', {})


def filter_by_date(request):
    return render(request, 'filter_by_date.html', {})


def filters_by_place(request):
    storage = JsonHandler().read_json()
    Place = storage['cities']
    return render(request, 'filter_by_place.html', {'Place': Place})


def filter_by_dateplace(request):
    storage = JsonHandler().read_json()
    Place = storage['cities']
    return render(request, 'filter_by_date&place.html', {'Place': Place})


def filters_range_by_date(request):
    return render(request, 'filter_range_by_date.html', {})


def add_event123(request):
    storage = JsonHandler().read_json()
    if request.method == 'POST':
        ID = uuid.uuid4()
        name = request.POST.get("Event_Name")
        date = request.POST.get("Event_Date")
        info = request.POST.get("Event_Info")
        place = request.POST.get("Event_Place")
        if place == 'other':
            place = request.POST.get('new_place')
        for key in storage:
            if key != 'cities' and storage[key]["Event_Name"]==name:
                return HttpResponse("Please enter another event name!This name already exists")
        data = {'Event_Name': name,
                'Event_Date': date,
                'Event_Info': info,
                'Event_Place':place
                }
        JsonHandler().write_json(str(ID), data)
        return HttpResponse("Event Added Successfully!!!Congratulations.")
    else:
        return HttpResponse("Something went wrong")


def delete_event(request):
    if request.method == 'POST':
        del_ID = request.POST.get("search_ID")
        mes = JsonHandler().delete_eventJH(del_ID)
        return HttpResponse(mes)
    else:
        return HttpResponse("Something went wrong")


def update_event(request):
    if request.method == 'POST':
        storage = JsonHandler().read_json()
        search_ID = request.POST.get("search_ID")
        if search_ID in storage:
            name = request.POST.get("Event_Name")
            date = request.POST.get("Event_Date")
            info = request.POST.get("Event_Info")
            place = request.POST.get("Event_Place")
            data = {'Event_Name': name,
                    'Event_Date': date,
                    'Event_Info': info,
                    'Event_Place': place
                    }

            JsonHandler().write_json(search_ID, data)
            return HttpResponse("Event Updated Successfully!!!")
        else:
            return HttpResponse("Event not found!!!")
    else:
        return HttpResponse("Something went wrong!!!")


def search_event(request):
    if request.method == 'POST':
        search_ID = request.POST.get("search_ID")
        storage = JsonHandler().read_json()
        if search_ID in storage:
            return render(request, 'search_event.html',
                          {'data': storage[search_ID], 'search_ID': search_ID, 'cities': storage['cities']})
        else:
            return HttpResponse("ID not found!!!SORRY")

    else:
        return HttpResponse("Something went wrong")


def list_by_date_place(request):
    if request.method == "POST":
        storage = JsonHandler().read_json()
        date_ss = request.POST.get("Date_Place")
        place_ss = request.POST.get("Place_Date")
        dict2 = {}
        data = storage['cities']
        for key in storage:
            if key != 'cities' and storage[key]["Event_Date"] == date_ss and storage[key]["Event_Place"] == place_ss:
                dict2.update({key: storage[key]})
        if len(dict2):
            return render(request, 'list_by_date_place.html', {'data': dict2})
        else:
            return HttpResponse("Sorry!No events on the same date and place!:(")
    else:
        return HttpResponse("Something went wrong")


def list_by_place(request):
    if request.method == "POST":
        storage = JsonHandler().read_json()
        place_s = request.POST.get("Place_Search")
        dict2 = {}

        for key in storage:
            if key != 'cities' and storage[key]["Event_Place"] == place_s:
                dict2.update({key: storage[key]})
        if len(dict2):
            return render(request, 'list_by_place.html', {'data1': dict2})
        else:
            return HttpResponse("Sorry!!No Events in that place")
    else:
        return HttpResponse("Something went wrong!!")


def list_by_date(request):
    if request.method == 'POST':
        storage = JsonHandler().read_json()
        date_s = request.POST.get("Date_Search")
        dict2 = {}
        for key in storage:
            if key != 'cities' and storage[key]["Event_Date"] == date_s:
                dict2.update({key: storage[key]})
        if len(dict2):
            return render(request, 'list_by_date.html', {'data': dict2})
        else:
            return HttpResponse("Sorry!No events on that day!:(")
    else:
        return HttpResponse("Something went wrong!!!")


def range_by_date(request):
    if request.method == "POST":
        storage = JsonHandler().read_json()
        date1 = request.POST.get("Date1")
        date2 = request.POST.get("Date2")
        dict2 = {}
        if (date1 == date2):
            for key in storage:
                if key != 'cities' and storage[key]["Event_Date"] == date1:
                    dict2.update({key: storage[key]})
        elif (date1 > date2):
            date3 = ()
            date3 = date1
            date1 = date2
            date2 = date3
        for key in storage:
            if key != 'cities' and date1 <= storage[key]["Event_Date"] <= date2:
                dict2.update({key: storage[key]})
        else:
            for key in storage:
                if key != 'cities' and date1 <= storage[key]["Event_Date"] <= date2:
                    dict2.update({key: storage[key]})
        if len(dict2):
            return render(request, 'range_by_date.html', {'data': dict2})
        else:
            return HttpResponse("Sorry no events during that time")
    else:
        return HttpResponse("Something went wrong")


def list_by_todaydate(request):
    storage = JsonHandler().read_json()
    today = datetime.date.today()
    today1 = unicode(today)
    dict_up = {}
    dict_today = {}
    dict_past = {}
    for key in storage:
        if key != 'cities' and today1 == storage[key]["Event_Date"]:
            dict_today.update({key: storage[key]})
        if key != 'cities' and today1 > storage[key]["Event_Date"]:
            dict_past.update({key: storage[key]})
        if key != 'cities' and today1 < storage[key]["Event_Date"]:
            dict_up.update({key: storage[key]})

    return render(request, 'filter_by_todaydate.html',
                  {'data_today': dict_today, 'data_upcoming': dict_up, 'data_past': dict_past})

