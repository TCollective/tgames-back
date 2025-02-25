from django.urls import include, path


app_name = 'tgames'

urlpatterns = [
    path('',include('tgames.calculator.urls')),
]
