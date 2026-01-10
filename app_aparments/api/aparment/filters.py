from  app_aparments.models import Apartment
import django_filters 


class ApartmentFiltering(django_filters.FilterSet):

    location = django_filters.CharFilter(field_name = 'location', lookup_expr='icontains')
    rooms = django_filters.NumberFilter(field_name = 'rooms')
    min_price = django_filters.NumberFilter(field_name = 'price',lookup_expr = "gte")
    max_price = django_filters.NumberFilter(field_name = 'price',lookup_expr = 'lte')
    bathrooms = django_filters.CharFilter(field_name = 'bathrooms')
    min_square_meters = django_filters.NumberFilter(field_name = 'square_meters',lookup_expr='gte')
    max_square_meters = django_filters.NumberFilter(field_name='square_meters',lookup_expr='lte')

    class Meta():

        model = Apartment
        fields = ['location','rooms','min_price','max_price','bathrooms','min_square_meters','max_square_meters']