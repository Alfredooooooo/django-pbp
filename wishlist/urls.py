from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_XML
from wishlist.views import show_JSON
from wishlist.views import show_JSON_by_id
from wishlist.views import show_XML_by_id

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_XML, name='show_XML'),
    path('json/', show_JSON, name='show_JSON'),
    path('json/<int:id>', show_JSON_by_id, name='show_JSON_by_id'),
    path('xml/<int:id>', show_XML_by_id, name='show_XML_by_id'),
]
