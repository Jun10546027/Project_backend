from .models import Item
from .serializers import UserSerializer
from .models import search_id


#rest_framework
from rest_framework import  viewsets , status
from rest_framework.decorators import permission_classes,action
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.pagination import PageNumberPagination


class DataViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = UserSerializer
    #設定解析類型
    parser_classes = (JSONParser,)

    @action(methods=['get'],detail=True)
    def raw_sql_search_id(self, request,pk=None):
        try:
            id = self.get_object().id
        except:
            id = request.data
        #我們可以經由print發現request都是空的
        # print(request.data)
        items= search_id(id=id)
        serializer = UserSerializer(items,context = {'request':request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def get_permissions(self):
        if self.action in ('create',):
            self.permission_classes = [IsAuthenticated,]
        return [permission() for permission in self.permission_classes]

    #Get 方法
    def list(self, request, **kwargs):
        users = Item.objects.all()
        print(self.pagination_class.page_size)
        serializer = UserSerializer(users,context = {'request':request},many=True)

        return Response(serializer.data,status = status.HTTP_200_OK)

    #繼承permission，讓他只在有登入下作業
    @permission_classes((IsAuthenticated,))
    def create(self, request, **kwargs):
        id = request.data.get('id')
        title = request.data.get('title')
        MyClass = request.data.get('MyClass')
        content = request.data.get('content')
        users = Item.objects.create(id = id,title= title,MyClass=MyClass,content=content)
        serializer = UserSerializer(users,context = {'request':request})
        print(serializer.data)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    @permission_classes((IsAuthenticated,))
    def delete(self,request,**kwargs):
        id = request.data.get('id')
        user = Item.objects.delete(id = id)
        return Response(status=status.HTTP_204_NO_CONTENT)
