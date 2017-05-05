from django.conf.urls import patterns, include, url
from Events import views


# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'add$',views.add_html,name='add'),
    url(r'search$',views.Search_html,name='search'),
    url(r'filters$',views.filters_html,name='filters'),
    url(r'^list_date$',views.filter_by_date,name='list_date'),
    url(r'^list_place$',views.filters_by_place,name='filtersplace'),
    url(r'^list_date_place$',views.filter_by_dateplace,name='filtersdateplace'),
    url(r'^range_date$',views.filters_range_by_date,name='filterrangebydate'),
    url(r'^upcoming_past_today$',views.list_by_todaydate,name='filterbytodaysdate'),
    url(r'^add_event$', views.add_event123,name='add_event123'),
    url(r'^del_event$', views.delete_event, name='del_event'),
    url(r'^search_event$', views.search_event, name='search_event'),
    url(r'^update_event$', views.update_event, name='update_event123'),
    url(r'^list_by_date$', views.list_by_date, name='list_by_date'),
    url(r'^list_by_date_place$', views.list_by_date_place, name='list_by_date_place'),
    url(r'^list_by_place$', views.list_by_place, name='list_by_place'),
    url(r'^range_by_date$', views.range_by_date, name='range_by_date')
    ]

