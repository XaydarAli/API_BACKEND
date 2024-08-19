from django.urls import include
from rest_framework import routers
from .views import AdvisorViewSetWeb,AuthorViewSetWeb,BlogViewSetWeb,ServiceViewSetWeb,ReviewViewSetWeb
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, re_path

schema_view = get_schema_view(
    openapi.Info(
        title="Stocker API DOCS",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)






router=routers.DefaultRouter()
router.register(r'advisors', AdvisorViewSetWeb, basename='advisors')
router.register(r'authors', AuthorViewSetWeb, basename='authors')
router.register(r'blogs', BlogViewSetWeb, basename='blogs')
router.register(r'services', ServiceViewSetWeb, basename='services')
router.register(r'reviews', ReviewViewSetWeb, basename='reviews')



urlpatterns = [

    path('api-token-auth/', obtain_auth_token),
    path('',include(router.urls)),

]


urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
