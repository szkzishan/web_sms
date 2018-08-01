# -*- coding: utf-8 -*-
from rest_framework import viewsets
from serializers import *
from models import *
from rest_framework import routers
from filters import *
from rest_framework import permissions
from rest_framework.filters import SearchFilter
from rest_framework_filters.backends import DjangoFilterBackend
from rest_framework import parsers,renderers
from django.contrib.auth.models import Permission
from rest_framework.decorators import api_view,permission_classes
router = routers.SimpleRouter()

# View %(table_name)s

class by_2mF4HV9zViewSet(viewsets.ModelViewSet):
    queryset = by_2mF4HV9zModel.objects.all()
    serializer_class = by_2mF4HV9zSerializer
    filter_backends = (SearchFilter,DjangoFilterBackend)
    search_fields = []
    filter_class = by_2mF4HV9zFilter
router.register(r'by_2mF4HV9z', by_2mF4HV9zViewSet,base_name='by_2mF4HV9z')

class userViewSet(viewsets.ModelViewSet):
    queryset = userModel.objects.all()
    serializer_class = userSerializer
    filter_backends = (SearchFilter,DjangoFilterBackend)
    search_fields = []
    filter_class = userFilter
router.register(r'user', userViewSet,base_name='user')

class be_hbigt2yMViewSet(viewsets.ModelViewSet):
    queryset = be_hbigt2yMModel.objects.all()
    serializer_class = be_hbigt2yMSerializer
    filter_backends = (SearchFilter,DjangoFilterBackend)
    search_fields = []
    filter_class = be_hbigt2yMFilter
router.register(r'be_hbigt2yM', be_hbigt2yMViewSet,base_name='be_hbigt2yM')



class FileViewSet(viewsets.ModelViewSet):
    parser_classes = (parsers.FormParser, parsers.MultiPartParser,)

    queryset = FileModel.objects.all()
    serializer_class = FileSerializer


router.register(r'file', FileViewSet, base_name="file")

class PermissionViewSet(viewsets.ModelViewSet):
    # permission_classes
    http_method_names = ['get', ]
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


router.register(r'permission', PermissionViewSet, base_name="permission")

# add permission to user
class PermissionUserViewSet(viewsets.GenericViewSet):
    serializer_class = PermissionUserSerializer
    http_method_names = ("post","delete")
    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return serializer.save()
router.register(r'permissionuser', PermissionUserViewSet, base_name="permissionuser")

@api_view(["GET", ])
@permission_classes([permissions.IsAuthenticated,])
def get_user_id(request):
    user_id = request.user.id
    return Response({"user_id": user_id})
