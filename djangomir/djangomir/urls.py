from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path("admin/", admin.site.urls),
    path(r'rest-auth/', include('rest_auth.urls')),
    path(r'rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path(r'api/auth/', include('accounts.api.urls'), name='api-auth'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'accounts/', include('accounts.api.urls'), name='api-auth'),
    path('upload/', include('upload.api.urls')),
    path('tabs/', include('tabs.api.urls')),
    # Upload

]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
