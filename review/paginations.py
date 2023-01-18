from rest_framework.pagination import PageNumberPagination

class HotelCommentPagination(PageNumberPagination):
    page_size = 5

class FunCommentPagination(PageNumberPagination):
    page_size = 5

class PlaceCommentPagination(PageNumberPagination):
    page_size = 5