from django.urls import path
from .views import AvisosVigentesListView

app_name = "avisos"

urlpatterns = [
    path("avisos/", AvisosVigentesListView.as_view(), name="vigentes"),
]
