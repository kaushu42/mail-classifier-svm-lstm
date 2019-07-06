from django.urls import path

import UI.frontend.views as views

urlpatterns = [
    path('', views.index),
    path('predict', views.predict),
]
