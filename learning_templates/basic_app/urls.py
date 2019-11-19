from django.urls import path
from basic_app import views

# SET THE NAMESPACE!
app_name = 'basic_app'

urlpatterns=[
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]
# docs.djangoproject.com/en/1.10/topics/templates
# or google -->Django+Templates
