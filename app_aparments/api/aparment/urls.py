from app_aparments.api.aparment.views import AparmentFiltering,AparmentPagination,AparmentGeneralMethods,AparmentMethodsById,CreateImage
from django.urls import path

urlpatterns = [
    path("aparment/", AparmentGeneralMethods.as_view()),
    path("aparment/<id>/", AparmentMethodsById.as_view()),
    path("aparment-filtering/", AparmentFiltering.as_view()), 
    path("aparment-pagination/", AparmentPagination.as_view()),
    path("apartment-image/",CreateImage.as_view()),

]
