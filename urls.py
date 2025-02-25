from django.urls import include, path


app_name = 'tgames'

urlpatterns = [
    path('calculator/',include('tgames.calculator.urls')),
    path('guess/',include('tgames.guess.urls')),
    
]
