from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

# https://stackoverflow.com/questions/72105628/get-next-page-number-instead-of-next-page-link-django-rest-framework


class PageNumberPagination(PageNumberPagination):
    # Replace `next` and `previous` pagination URLs with actual page numbers
    # page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        next_page_number = None
        if self.page.has_next():
            next_page_number = self.page.next_page_number()

        previous_page_number = None
        if self.page.has_previous():
            previous_page_number = self.page.previous_page_number()

        return Response(
            {
                "next": next_page_number,
                "previous": previous_page_number,
                "count": self.page.paginator.count,
                "results": data,
            }
        )
