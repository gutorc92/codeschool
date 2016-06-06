from django.conf.urls import url
from cs_friendhelp import views

urlpatterns = [
    url(r'^help/ask-frind/$',views.friendhelper.as_view()),
]
