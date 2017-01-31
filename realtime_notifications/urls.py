"""realtime_notifications URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

import notifications.urls

from django.conf.urls import url, include

from django.contrib import admin
from django.contrib.auth.views import login, logout

admin.autodiscover()

from rn.views import home, send_notification, mark_as_read, home_realtime, ajax_send_notification, ajax_mask_as_read

urlpatterns = [
	url(r"", include("user_sessions.urls", "user_sessions")),
    url(r'^admin/', admin.site.urls),
    url(r'^inbox/notifications/', include(notifications.urls)),

    url(r"^$", home, name="home"),
    url(r"^send_notification/$", send_notification, name= "send_notification"),
    url(r"^mark_as_read/$", mark_as_read, name= "mark_as_read"),
    url(r"^accounts/login/$", login, {"template_name": "admin/login.html"}),
    url(r"^accounts/logout/$", logout, {"next_page": "/"}, name= "logout"),

    url(r'^realtime/$', home_realtime, name='home_realtime'),
	url(r'^ajax_send_notification/$', ajax_send_notification, name='ajax_send_notification'),
	url(r'^ajax_mark_as_read/$', ajax_mask_as_read, name='ajax_mark_as_read')
]
