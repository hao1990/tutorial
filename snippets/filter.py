from django_filters import rest_framework as r_filters
from rest_framework import fields
from django.db.models import Q


class SnippetFilter(r_filters.filterset):
    """
    过滤器
    """
