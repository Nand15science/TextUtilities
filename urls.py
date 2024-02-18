
from django.contrib import admin
import django.urls
from django.urls import path
from .import view

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',view.index,name='index'),
#     path('hello/',view.hello),
#     path('jojo/',view.jo),
#     path('lnks/',view.linksV)
# ]


urlpatterns=[
    path('admin/',admin.site.urls),
    path('',view.index,name="Home"),
    # path('removepunc/',view.removepunc,name="punc"),
    path('analyze/',view.analyze,name='analyze'),
    path('Aboutus.html/', view.Aboutus, name='Aboutus'),
    path('Contact.html/',view.Contactus),


]