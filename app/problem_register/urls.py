from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'status_set', views.StatusViewSet)
router.register(r'problems_set', views.ProblemLabelGeoJsonViewSet)


urlpatterns = [
    path('', TemplateView.as_view(template_name='problem_register/home.html'), name='home'),
    path('report', views.ReportView.as_view(), name='report'),
    path('accounts/', include('accounts.urls')),
    path('problems_list/', views.ProblemsListView.as_view(), name='problems_list'),
    path('problem/<int:pk>/', views.ProblemDetailView.as_view(), name="problem_details"),
    path('api/', include(router.urls)),
    path('api/problem_detail/<int:pk>/', views.ProblemLabelDetailAPIView.as_view())
]

