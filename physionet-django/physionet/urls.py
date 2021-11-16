import lightwave.views as lightwave_views
import project.views as project_views
from django.conf import settings
from django.conf.urls import handler404, handler500, include
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from physionet import views
from physionet.settings.base import StorageTypes
from project.projectfiles import ProjectFiles

handler403 = 'physionet.views.error_403'
handler404 = 'physionet.views.error_404'
handler500 = 'physionet.views.error_500'


urlpatterns = [
    # django admin app
    path('admin/', admin.site.urls),
    # management console app
    path('console/', include('console.urls')),
    # user app
    path('', include('user.urls')),
    # project app
    path('projects/', include('project.urls')),
    # notification app
    path('', include('notification.urls')),
    # search app
    path('', include('search.urls')),
    # export app
    path('', include('export.urls')),
    # sso
    path('', include('sso.urls')),

    path('', views.home, name='home'),
    path('ping/', views.ping),

    # about pages
    path('about/publish/', views.about_publish,
        name='about_publish'),
    path('about/', views.about, name='about'),
    path('about/timeline', views.timeline, name='timeline'),
    path('about/licenses/<license_slug>/', views.license_content,
        name='license_content'),
    path('about/citi-course/', views.citi_course, name='citi_course'),

    # # Custom error pages for testing
    # path('403.html', views.error_403, name='error_403'),
    # path('404.html', views.error_404, name='error_404'),
    # path('500.html', views.error_500, name='error_500'),

    # temporary content overview pages
    path('about/content/', views.content_overview,
        name='content_overview'),
    path('about/database/', views.database_overview,
        name='database_overview'),
    path('about/software/', views.software_overview,
        name='software_overview'),
    path('about/challenge/', views.challenge_overview,
        name='challenge_overview'),
    path('about/tutorial/', views.tutorial_overview,
        name='tutorial_overview'),

    # robots.txt for crawlers
    path(
        'robots.txt', lambda x: HttpResponse("User-Agent: *\Allow: /", content_type="text/plain"), name="robots_file"
    ),
]

if ProjectFiles().is_lightwave_supported:
    urlpatterns.append(path('lightwave/', include('lightwave.urls')))
    # backward compatibility for LightWAVE
    urlpatterns.append(path('cgi-bin/lightwave', lightwave_views.lightwave_server))

if settings.DEBUG:
    import debug_toolbar

    # debug toolbar
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
