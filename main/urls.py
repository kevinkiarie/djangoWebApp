from django.conf.urls import url
from . import views
from django.utils.functional import curry
from django.contrib.sitemaps.views import sitemap
from django.views.defaults import permission_denied, server_error, page_not_found, bad_request
from django.views.defaults import *
handler404 =curry(page_not_found, template_name="404.html")
handler500 = curry(server_error,  template_name="500.html")
handler403 = curry(permission_denied, template_name="403.html")
handler400 = curry(bad_request, template_name="400.html")

urlpatterns = [
	url(r'^index', views.index, name="index"),
	url(r'^home', views.home, name="home"),
	url(r'^search', views.search, name="search"),
	url(r'^register/$', views.register, name='register'),
	url(r'^filtersearch/$', views.advanced_search, name='filtersearch'),
	url(r'^fin_register/$', views.fin_register, name='fin_register'),
	url(r'^signup_login/$', views.signup_login, name='signup_login'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^post/$', views.add_todo, name='add'),
	url(r'^logout/$', views.log_out, name='logout'),
	url(r'^about/$', views.about, name='about'),
	url(r'^help/$', views.help, name='help'),
	
	url(r'^user/password/reset/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/user/password/reset/done/'},name="password_reset"),
	url(r'^user/password/reset/done/$','django.contrib.auth.views.password_reset_done'),
	url(r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : '/user/password/done/'}),
	url(r'^user/password/done/$', 'django.contrib.auth.views.password_reset_complete'),


]
