from django.urls import path
from . import views

app_name='homepage'

urlpatterns = [
    path('',views.index,name='index'),
    path('seperate/<str:subject>/',views.seperate,name='seperate'),
    path('search/',views.search,name='search'),
    path('year/<str:year>/',views.more,name='more'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.log_in,name='log_in'),
    path('logout/',views.log_out,name='log_out'),
    path('year/',views.year,name='year'),
    path('FirstYear/',views.fy,name='fy'),
    path('ITbranch/',views.it,name='it'),
    path('Mechbranch/',views.mech,name='mech'),
    path('Compbranch/',views.comp,name='comp'),
    path('Extcbranch/',views.extc,name='extc'),
    path('Instrubranch/',views.instru,name='instru'),
    path('Civilbranch/',views.civil,name='civil'),
    path('<str:title>/',views.detail,name='bk_detail'),
]
