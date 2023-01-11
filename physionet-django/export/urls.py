from django.urls import path, re_path

from export import views


urlpatterns = [
    # API V1 Routes
    path('v1/published', views.PublishedProjectList.as_view(), name='Published_project_list'),
    path('v1/published/<str:slug>/<str:version>', views.PublishedProjectDetail.as_view(),
         name='Published_project_detail'),
]
