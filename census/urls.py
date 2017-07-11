from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^$', views.homepage, name='homepage'),
	url(r'^titles', views.index, name='index'),
	url(r'^editions/(?P<id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^copy/(?P<id>[0-9]+)/$', views.copy, name='copy'),
	url(r'^copy', views.copylist, name='copylist'),
	url(r'^issue/(?P<id>[0-9]+)/$', views.issue, name='issue'),
 	url(r'^provenance$', views.provenance, name='provenance'),
 	url(r'^register$', views.register, name='register'),

	# Jinyun-urls for submission forms
	url(r'^submission$', views.submission, name='submission'),
	url(r'^title/(?P<id>[0-9]+)/$', views.json_editions, name='json_editions'),
	url(r'^edition/(?P<id>[0-9]+)/$', views.json_issues, name='json_issues'),
	url(r'^addTitle$', views.add_title, name='add_title'),
	url(r'^addEdition/(?P<title_id>[0-9]+)/$', views.add_edition, name='add_edition'),
	url(r'^addIssue/(?P<edition_id>[0-9]+)/$', views.add_issue, name='add_issue'),

	#reviewing submitted copy-info, having edit, confirm, and cancel buttons
	url(r'^copy_info/(?P<copy_id>[0-9]+)/$', views.copy_info, name='copy_info'),

	#displaying copy info for all
	url(r'^copy_detail/(?P<copy_id>[0-9]+)/$', views.copy_detail, name='copy_detail'),

	url(r'^copysubmissionsuccess$', views.copy_submission_success, name='copy_success'),
	url(r'^cancelcopysubmission/(?P<copy_id>[0-9]+)/$', views.cancel_copy_submission, name='cancel_copy_submission'),
	url(r'^editcopysubmission/(?P<copy_id>[0-9]+)/$', views.edit_copy_submission, name='edit_copy_submission'),

	#for viewing transactions related to a copy
	url(r'^transactions/(?P<copy_id>[0-9]+)/$', views.transactions, name='transactions'),

	url(r'^login$', views.login_user, name='login_user'),
	url(r'^accounts/login/$', views.login_user, name='login_user'),
	url(r'^logout$', views.logout_user, name='logout_user'),
	url(r'^homepage$',views.homepage, name='homepage'),
	url(r'^search/$', views.search, name='search_for_something'),

	#for viewing user's profile
	url(r'^profile$', views.display_user_profile, name='profile'),
	
	#for viewing user's history (submitted copies & editted copies)
	url(r'^user_history$', views.user_history, name='user_history'),

	url(r'^editProfile$', views.edit_profile, name='edit_profile'),
]
