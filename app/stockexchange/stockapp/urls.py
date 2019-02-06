from django.urls import path

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('api/users/submit/', TemplateView.as_view(template_name = 'submitform.html')),
    path('api/users/submit/display', views.create_user),
	#path('/api)/users/<int:id>', views.update)
]