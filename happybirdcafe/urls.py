"""happybirdcafe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'', include('home.urls', namespace='home')),
    url(r'^birdie_talks/', include('birdie_talks.urls', namespace='birdie_talks')),
    url(r'^your_feeders/', include('your_feeders.urls', namespace='your_feeders')),
    url(r'^our_feeders/', include('our_feeders.urls', namespace='our_feeders')),
    url(r'^food/', include('food.urls', namespace='food')),
    url(r'^contacts/', include('contacts.urls', namespace='contacts')),
    # url(r'^admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    url(r'^admin/', admin.site.urls),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
