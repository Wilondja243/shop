from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response

from .models import Category, Product, Article
from .serializers import CategorySerializer, ProductSerializer, ArticleSerializer

class CategoryViewSet(ReadOnlyModelViewSet):

    serializer_class = CategorySerializer
    
    def get_queryset(self):
        queryset = Category.objects.filter(active=True)

        category_id = self.request.GET.get('category_id')
        
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        return queryset
        
    
class ProductViewSet(ReadOnlyModelViewSet):

    serializer_class = ProductSerializer

    def get_queryset(self, *args):
        queryset = Product.objects.filter(active=True)
         
        product_id = self.request.GET.get('product_id')
        if product_id is not None:
            queryset = queryset.filter(id=product_id)
        return queryset
    
class ArticleViewSet(ReadOnlyModelViewSet):

    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.filter(active=True)

        product_id = self.request.GET.get('product_id')

        if product_id is not None:
            queryset = queryset.filter(product_id = product_id)
        return queryset