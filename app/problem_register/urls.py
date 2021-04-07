from django.urls import path, include
from django.views.generic import TemplateView


from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='problem_register/home.html'), name='home'),
    path('report', views.ReportView.as_view(), name='report'),
    path('accounts/', include('accounts.urls')),
    path('problems_set', views.problems_dataset, name='problems_data'),
    path('status_set', views.status_dataset, name='status_data'),
    path("problems_list/", views.ProblemsListView.as_view(), name='problems_list'),
    path("problem/<int:pk>/", views.ProblemDetailView.as_view(), name="problem_details"),
]
