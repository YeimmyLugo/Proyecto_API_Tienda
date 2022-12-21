from django.urls import path
from .views import CafeteriaApiView, CafeteriaDetailApiView, CafeteriaReferenciaApiView
urlpatterns = [
    path('', CafeteriaApiView.as_view(), name="Cafeteria_List"),
    path('<int:cafeteria_id>/', CafeteriaDetailApiView.as_view(), name="Cafeteria_detail"),
    path('<str:cafeteria_clasificacion>/', CafeteriaReferenciaApiView.as_view()),
]
