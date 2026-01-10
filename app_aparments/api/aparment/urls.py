from app_aparments.api.aparment.views import ApartmentViewsetFilter,ApartmentPagination,ApartmentGeneralMethods,ApartmentMethodsById,CreateImage
from django.urls import path

urlpatterns = [
    path("apartment/", ApartmentGeneralMethods.as_view(),name = 'apartment'),
    path("apartment/<id>/", ApartmentMethodsById.as_view()),
    path("apartment-filtering/", ApartmentViewsetFilter.as_view({'get':'list'})), 
    path("apartment-pagination/", ApartmentPagination.as_view()),
    path("apartment-image/",CreateImage.as_view()),

]
