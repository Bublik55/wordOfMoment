from django.urls import path
from words.views import word_stubs
from words.views import word_list

urlpatterns = [
    path('words/',word_list),
    path('words/<int:pk>',word_stubs)
]