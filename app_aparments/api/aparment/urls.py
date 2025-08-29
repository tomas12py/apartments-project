from app_aparments.api.aparment.views import ApartmentFiltering,ApartmentPagination,ApartmentGeneralMethods,ApartmentMethodsById,CreateImage
from django.urls import path

urlpatterns = [
    path("apartment/", ApartmentGeneralMethods.as_view(),name = 'apartment'),
    path("apartment/<id>/", ApartmentMethodsById.as_view()),
    path("apartment-filtering/", ApartmentFiltering.as_view()), 
    path("apartment-pagination/", ApartmentPagination.as_view()),
    path("apartment-image/",CreateImage.as_view()),

]
