from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('formInput',views.formInput,name='formInput'),
    path('formInput',views.formInput,name='formInput'),
    path('addData', views.addData, name='addData'),
    path('showData', views.showData, name='showData'),
    path('displayData', views.displayData, name='displayData'),
    path('displayDatat', views.displayDatat, name='displayDatat'),
    path('studentsView', views.studentsView, name='studentsView'),
    path('pdf_view/<name>', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf', views.pdf, name="pdf"),
    path('pdf_download/<name>', views.DownloadPDF.as_view(), name="pdf_download"),
    path('pdf_download/<name>', views.DownloadPDF.as_view(), name="pdf_download"),
     path('students', views.students, name="students"),
     path('map', views.map, name="map"),
    path('addmapData', views.addmapData, name='addmapData'),
    path('map_location/', views.map_location, name='map_location'),
    path('mapData/', views.mapData, name='mapData'),
    path('fees/', views.fees, name='fees'),
    path('success/', views.success, name='success'),


    # path('pay/', views.start_payment, name="payment"),
    # path('payment/success/', views.handle_payment_success, name="payment_success")



  
]

