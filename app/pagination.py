from rest_framework.pagination import PageNumberPagination ,LimitOffsetPagination , CursorPagination

class MyPagination(PageNumberPagination):
    page_size = 5
    page_query_param  = 'p'
    
class MyLimitPagination(LimitOffsetPagination):
    default_limit = 3
    limit_query_param = 'lim'
    offset_query_param = 'off'
    max_limit = 4

class MyCursorPagination(CursorPagination):
    page_size = 5
    ordering = 'name'