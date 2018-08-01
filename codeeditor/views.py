# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, status, views, generics
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView

from models import *
from rest_framework import permissions
from serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import routers
from filters import *
from rest_framework_filters.backends import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import parsers, renderers
import uitls
from django.contrib.auth.models import Permission

router = routers.SimpleRouter()

# Create your view here.
# 配置系统参数  install_env
# 服务器环境监测 check_env
# 程序源码创建   create_code
# 数据库构建     create_database
# 程序远程启动   runserver
# 自动联调测试   auto_debug
# 系统档案准备   create_docs
OPERATE_FUN = {
    "install_env": "install",
    "env_check_install": "check_env",
    "create_code": "push_project",
    "create_database": "project_migrate",
    "runserver": "project_runserver",
    "auto_debug": "",
    "create_docs": "",
}


@api_view(["POST", ])
@permission_classes([permissions.IsAuthenticated, ])
def deploy_app(request, operation):
    serializer = GetAppSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    app = serializer.get_app(serializer.data)
    deploy = uitls.DeployProject(app)
    exec_fun = getattr(deploy, OPERATE_FUN.get(operation))
    data = exec_fun()
    deploy.clsoe()
    return Response(data)


@api_view(["POST", ])
def app_config(request):
    '''
    post:
        创建创建数据库表

    :param request:
    :return:
    '''
    serializer = GetAppSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print serializer.data
        config = uitls.get_app_config(serializer.data.get("app_id"))
        return Response(config)


class ServerViewSet(viewsets.ModelViewSet):
    queryset = SereverModel.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (IsOwnerFilterBackend, DjangoFilterBackend)
    serializer_class = SveverSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        data["user"] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


router.register(r'server', ServerViewSet, base_name="server")


class AppViewSet(viewsets.ModelViewSet):
    queryset = AppModel.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (IsOwnerFilterBackend, DjangoFilterBackend)
    serializer_class = AppSerializer
    filter_class = AppFilter

    def create(self, request, *args, **kwargs):
        data = request.data
        data["user"] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


router.register(r'app', AppViewSet, base_name="app")


class TableViewSet(viewsets.ModelViewSet):
    queryset = TableModel.objects.all()
    serializer_class = TableSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_class = TableFilter


router.register(r'table', TableViewSet, base_name="table")


class FieldViewSet(viewsets.ModelViewSet):
    queryset = FieldModel.objects.all()
    serializer_class = FieldSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_class = FieldFilter


router.register(r'field', FieldViewSet, base_name="field")


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
    http_method_names = ("post", "delete")

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return serializer.save()


router.register(r'permissionuser', PermissionUserViewSet, base_name="permissionuser")


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser, parsers.FileUploadParser)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, "user_id": user.id})


obtain_auth_token = ObtainAuthToken.as_view()


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', ]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


router.register(r'users', UserViewSet, base_name="users")
