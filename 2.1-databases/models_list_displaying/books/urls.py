from django.urls import path, register_converter

from . import views, converters

register_converter(converters.PubDateConverter, 'date')

urlpatterns = [
    path('', views.index_view, name = 'index'),
    path('books/', views.books_view, name='books'),
    path('books/<date:dt>/', views.books_pagination_view, name='book')
]
