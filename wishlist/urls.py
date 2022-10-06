from django.urls import path
from wishlist.views import register, login_user, logout_user, show_ajax, show_ajax_afterSubmit, show_wishlist, show_XML, show_JSON, show_JSON_by_id, show_XML_by_id

app_name = 'wishlist'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_XML, name='show_XML'),
    path('json/', show_JSON, name='show_JSON'),
    path('json/<int:id>', show_JSON_by_id, name='show_JSON_by_id'),
    path('xml/<int:id>', show_XML_by_id, name='show_XML_by_id'),
    path('ajax/', show_ajax, name='show_ajax'),
    path('ajax/submit/', show_ajax_afterSubmit, name='after_submit')
]
