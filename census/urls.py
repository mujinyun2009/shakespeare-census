from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^editions/(?P<id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^copy$', views.copy, name='copy'),
 	url(r'^provenance$', views.provenance, name='provenance'),
 	url(r'^register$', views.register, name='register'),

	# Jinyun-urls for submission forms
	url(r'^submission$', views.submission, name='submission'),
	url(r'^title/(?P<id>[0-9]+)/$', views.json_editions, name='json_editions'),
	url(r'^edition/(?P<id>[0-9]+)/$', views.json_issues, name='json_issues'),
	url(r'^addTitle$', views.add_title, name='add_title'),
	url(r'^addEdition/(?P<title_id>[0-9]+)/$', views.add_edition, name='add_edition'),
	url(r'^addIssue/(?P<edition_id>[0-9]+)/$', views.add_issue, name='add_issue'),
	url(r'^copy_info/(?P<copy_id>[0-9]+)/$', views.copy_info, name='copy_info'),

	#for viewing transactions related to a copy
	url(r'^transactions/(?P<copy_id>[0-9]+)/$', views.transactions, name='transactions'),

	url(r'^login$', views.login_user, name='login_user'),
	url(r'^accounts/login/$', views.login_user, name='login_user'),
	url(r'^logout$', views.logout_user, name='logout_user'),
	url(r'^homepage$',views.homepage, name='homepage'),
	url(r'^search$', views.search, name='search'),

]
