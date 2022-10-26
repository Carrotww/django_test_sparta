from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.models import Article
from articles.serializers import ArticleSerializer
from rest_framework import status
from rest_framework.generics import get_object_or_404

# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        temp = Article.objects.all()
        article = temp[0]
        serializer = ArticleSerializer(article)
        serializer_all = ArticleSerializer(temp, many=True)

        """
        article_data = {
            "title":article.title,
            "content":article.content,
            "created_now": article.created_now,
            "updated_now": article.updated_now
        }
        """
        return Response(serializer_all.data)
    elif request.method == 'POST':
        print(request.data)
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid(): # 검증이 없으면 에러가 뜸
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)