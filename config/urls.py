from django.contrib import admin
from django.urls import path, include,re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf.urls.static import static
from . import settings

schema_view = get_schema_view(
    openapi.Info(
        title='Bai_Tushum',
        default_version='v1',
        description='TEST'
    ), public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger')),
    path('crm/', include('crm.urls')),
    path('', include('users.urls')),
    # re_path(r'auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
