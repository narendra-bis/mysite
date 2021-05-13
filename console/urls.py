from django.conf.urls import url
from . import views
from django.views.generic import RedirectView

app_name = "console"

urlpatterns = [
	url(r'^$',views.home,name='home'),
	# url(r'^console/',RedirectView.as_view(pattern_name='home', permanent=False)),
	url(r'signup',views.signupview, name='signup'),
	# (?# url(r'^signup/$',views.SignUpView.as_view(),name='signup'),)
	url(r'^ajax/validate_username/$',views.validate_username,name='validate_username'),
	url(r'login',views.signin, name = 'login'),
	url(r'logout',views.signout,name='logout')

]
