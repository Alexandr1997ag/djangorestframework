from rest_framework.response import Response
from django.shortcuts import render
from django.forms import model_to_dict
from .models import Women
from .serializers import WomenSerializer
from rest_framework.views import APIView


class WomenAPIView(APIView):
    def get(self, request):
        lst = Women.objects.all().values()
        return Response({'posts':list(lst)})

    def post(self, request):
        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': model_to_dict(post_new)})

# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
