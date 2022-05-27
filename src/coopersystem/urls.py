from django.urls import path
from django.conf.urls import url
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from produtos.views import (ProdutoViewSet, PedidoViewSet, schema_view)


router = routers.DefaultRouter()

router.register(r'produtos', ProdutoViewSet)
router.register(r'pedidos', PedidoViewSet)

urlpatterns = [
    url(r'^$', schema_view, name='docs'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
