from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import contacts, pageNotFound, home, product_card

app_name = CatalogConfig.name

urlpatterns = [

    path('', home, name='products'),
    path("contacts/", views.contacts, name="contacts/"),
    path("<int:pk>/product_card/", views.product_card, name="product_card/")

]

handler404 = pageNotFound
