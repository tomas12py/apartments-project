from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status


class CustomPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = "page_size"
    max_page_size = 10
    page_query_param = "page"

    def get_page_size(self, request):
        page_size = request.query_params.get(self.page_size_query_param)

        if page_size and ("'" in page_size or '"' in page_size):
            raise ValidationError("The value can't contain quotes")

        return super().get_page_size(request)
