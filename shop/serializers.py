from rest_framework import serializers


from .models import Article, Category, Product

class ProductSerializer(serializers.ModelSerializer):

    articles = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id','date_created','date_updated','name','category','articles']

    def get_articles(self, instance):
        queryset = instance.articles.filter(active=True)
        serializer = ArticleSerializer(queryset, many=True)
        return serializer.data

class CategorySerializer(serializers.ModelSerializer):

    products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id','date_created','name','description','products']

    def get_products(self, instance):
        queryset = instance.products.filter(active=True)
        serializer = ProductSerializer(queryset, many=True)
        return serializer.data

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ['id','date_created','date_updated','name','price','product']
