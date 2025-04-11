from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('create/',create,name='create'),
    path('retrieve/',retrieve,name='retrieve'),
    path('search/',search,name='search'),
    path('delete/',delete,name='delete'),
    path('update/<int:book_no>',update,name='update'),
    path('updateb/',updateb,name='updateb'),
    path('view/<int:book_no>',viewbook,name='view'),
    path('deleteb/<int:book_no>',deleteb,name='deleteb')
]