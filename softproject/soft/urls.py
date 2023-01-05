from django.urls import path
from . import views

# app_name = 'soft'


urlpatterns = [
    path('', views.index_view, name='index'),
    path('book/', views.ListBookView.as_view(), name='list-book'),
    path('book/<int:pk>/detail/', views.DetailBookView.as_view(), name='detail-book'),
    path('book/create/', views.CreateBookView.as_view(), name='create-book'),
    path('book/<int:pk>/delete/', views.DeleteBookView.as_view(), name='delete-book'),
    path('book/<int:pk>/update/', views.UpdateBookView.as_view(), name='update-book'),
    path('book/<int:book_id>/review/', views.CreateReviewView.as_view(), name='review'),
    path('soft/menu/',views.MenuView.as_view(),name='menu-list'),
    path('soft/<int:pk>/map/', views.MapView.as_view(), name='map-detail'),
    
]
