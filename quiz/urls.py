from django.urls import path, include
from .views import helloAPI, getJobs

urlpatterns = [
    path("hello/", helloAPI),
    path(
        'search2/<str:keyword>/<int:Page_No>/<str:careerType>/<str:careerMin>/<str:careerMax>/<str:edu>/<str:cotype>/<str:jobtype>/<str:payMin>/<str:payMax>',
        getJobs),
]
