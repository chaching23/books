from django.conf.urls import url
from . import views

urlpatterns = [ 
    url(r'^$', views.book),
    url(r'^add$', views.add_books),
    url(r'^books/(?P<book_id>\d+)$', views.view_books),
    url(r'^insert$', views.insert_author),


      # url(r'^authors$', views.author),
    # url(r'^authors/(?P<book_id>\d+)$', views.up),

]