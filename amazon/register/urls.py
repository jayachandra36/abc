from django.urls import path
from .views import create_account,getUsers, updatebyId, deletebyId, login, create_product, getProduct, updateProduct
from django.conf.urls import url
urlpatterns = [path('createAccount', create_account),
               path('getAll', getUsers),
               url(r'^updatebyId/(?P<pk>[0-9]+)$', updatebyId),
               url(r'^deletebyId/(?P<pk>[0-9]+)$', deletebyId),
               path('login', login),
               path('createProduct', create_product),
               path('getProduct', getProduct),
               url(r'^updateProduct/(?P<pk>[0-9]+)$', updateProduct)]