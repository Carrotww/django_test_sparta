from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from article.models import Article
from article.serializers import ArticleSerializer, ArticleCreateSerializer

# Create your views here.

class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        slz = ArticleSerializer(articles, many=True)
        if not slz.data:
            return Response("no data in article")
        return Response(slz.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        slz = ArticleCreateSerializer(data=request.data)
        if slz.is_valid():
            slz.save(user=request.user)
            return Response(slz.data, status.HTTP_200_OK)
        else:
            return Response(slz.errors, status=status.HTTP_400_BAD_REQUEST)