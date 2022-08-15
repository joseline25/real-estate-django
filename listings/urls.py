from django.urls import path
from . import views

urlpatterns = [
    path('list', views.listing_list, name='list'),
    path('<int:id>', views.listing_retrieve, name='list_details'),
    path('create_listing', views.listing_create, name='create_listing'),
    path('<int:id>/edit', views.listing_update, name='update_listing'),
    path('<int:id>/delete', views.listing_delete, name='delete_listing'),
    
    
    path('<int:id>/create_booking', views.booking_create, name='create_booking'),
     
    # login et enregistrement utilisateur 
    
    path("enregistrement/", views.registerPage, name="enregistrement"),
    path("", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("user/", views.userPage, name="user-page"),
    
    # search
    
    path("search_listing/", views.search_listing, name="search_listing"),
]



