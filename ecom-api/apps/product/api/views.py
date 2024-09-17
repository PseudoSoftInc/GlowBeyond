from django.http import Http404
from django.db.models import Q
from rest_framework.mixins import ListModelMixin
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import ProductSerializer, CategorySerializer
from ..models import Product, Category


class FetchCategories(viewsets.GenericViewSet, ListModelMixin):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()

    def get_category(self, slug):
        try:
            return Category.objects.get(slug=slug)
        except Category.DoesNotExist:
            raise Http404

    @action(detail=False, methods=["get"])
    def category_details(self, request):
        query_params = request.query_params
        category_slug = query_params["category_slug"]
        queryset = self.get_category(category_slug)
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)


class FetchLatestProducts(viewsets.GenericViewSet, ListModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

    @action(detail=False, methods=["get"])
    def product_details(self, request):
        query_params = request.query_params
        try:
            category_slug = query_params["category_slug"]
            product_slug = query_params["product_slug"]
            queryset = Product.objects.filter(category__slug=category_slug).get(
                slug=product_slug
            )
            serializer = ProductSerializer(queryset)
            return Response(serializer.data)
        except Product.DoesNotExist:
            raise Http404


class Search(viewsets.ViewSet):
    def getProduct(self, query):
        try:
            return Product.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
        except Product.DoesNotExist:
            raise Http404
        ...

    @action(detail=False, methods=["post"])
    def search(self, request):
        query = request.data.get("query")
        products = self.getProduct(query)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
