from rest_framework.pagination import PageNumberPagination
from django.conf import settings
from rest_framework.response import Response


class StandardResultPagination(PageNumberPagination):
    page_size = getattr(settings , 'PAGINATION_PAGE_SIZE' , 1)
    page_size_query_param = 'page_size'
    max_page_size = 2
    page_query_param = 'page'

    def get_paginated_response(self, data):
        return Response({
            'metadata': {
                'Count': self.page.paginator.count,
                'Next': self.get_next_link(),
                'Previous': self.get_previous_link(),
                'Current_Page': self.page.number,
                'Number_pages': self.page.paginator.num_pages,
                'Number_object': len(data),
            },
            'result': data
        })
