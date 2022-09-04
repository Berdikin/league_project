from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', InsuranceHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('addclient/', addclient, name='add_client'),
    path('allclients/', allclients, name='all_clients'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('client/<int:client_id>/', show_client, name='client'),
    path('post/<int:insurance_id>/', post, name='insurance'),
    path('type/<int:type_id>/', show_type, name='type')
]

