from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.template import Context, Template
from django.shortcuts import render, get_object_or_404
from django.template import loader
import models
from .models import *
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.forms import formset_factory
from django.db.models import Q
from django.contrib import admin
from django.core.paginator import Paginator, PageNotAnInteger
from itertools import chain
from django.core import serializers
from django.forms.models import model_to_dict
import json
from django.urls import reverse

# Create your views here.
def search(request):
	template=loader.get_template('results.html')
	query1 = request.GET.get('a')
	query2 = request.GET.get('b')
	query3 = request.GET.get('c')
	query4 = request.GET.get('d')
	category1 = request.GET.get('j')
	category2 = request.GET.get('k')
	category3 = request.GET.get('l')
	category4 = request.GET.get('z')
	copy_list = Copy.objects.all()
	if query1 and not query2 and not query3 and not query4:
		results_list = copy_list.filter(Q(**{category1: query1}))
		result_list = list(chain(results_list))
		context = {
		'result_list': result_list
		}
		return HttpResponse(template.render(context, request))
	if query1 and query2 and not query3 and not query4:
		results_list = copy_list.filter(Q(**{category1: query1})|Q(**{category2: query2}))
		result_list = list(chain(results_list))
		context = {
		'result_list': result_list
		}
		return HttpResponse(template.render(context, request))
	if query1 and query2 and query3 and not query4:
		results_list = copy_list.filter(Q(**{category1: query1})|Q(**{category2: query2})|Q(**{category3: query3}))
		result_list = list(chain(results_list))
		context = {
		'result_list': result_list
		}
		return HttpResponse(template.render(context, request))
	if query1 and query2 and query3 and query4:
		results_list = copy_list.filter(Q(**{category1: query1})|Q(**{category2: query2})|Q(**{category4: query4}))
		result_list = list(chain(results_list))
		context = {
		'result_list': result_list
		}
		return HttpResponse(template.render(context, request))
	if not query1 and not query2 and not query3 and not query4:
		template=loader.get_template('frontpage.html')
		results_list = copy_list.filter(Q(**{category1: query1})|Q(**{category2: query2})|Q(**{category4: query4}))
		result_list = list(chain(results_list))
		context = {
		'result_list': result_list
		}
		return HttpResponse(template.render(context, request))
	else:
		print('Whoops!')

def homepage(request):
    template=loader.get_template('frontpage.html')
    queryset_list = Title.objects.all()
    query = request.GET.get('q')
    if query:
    	queryset_list = queryset_list.filter(title__icontains=query)

    paginator= Paginator(queryset_list, 10)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
    	queryset = paginator.page(page)
    except PageNotAnInteger:
    	queryset = paginator.page(1)
	context = {
		"object_list": queryset,
		"title": "List",
		"page_request_var": page_request_var,
	}
	return HttpResponse(template.render(context, request))

def index(request):
	title = Title.objects.all()
	template = loader.get_template('census/index.html')
	context = {
		'titles': title
	}
	return HttpResponse(template.render(context, request))

def detail(request, id):
	selected_title=Title.objects.get(pk=id)
	editions = selected_title.edition_set.all()
	template = loader.get_template('census/detail.html')
	context = {
		'editions': editions
	}
	return HttpResponse(template.render(context, request))

def copy(request):
	copies = Copy.objects.all()
	template = loader.get_template('census/copy.html')
	context = {
		'copies': copies
	}
	return HttpResponse(template.render(context,request))


def provenance(request):
	provenances= Provenance.objects.all()
	template = loader.get_template('census/provenance.html')
	context = {
		'provenances': provenances
	}
	return HttpResponse(template.render(context,request))

def transactions(request, copy_id):
	selected_copy = Copy.objects.get(pk=copy_id)
	transactions= selected_copy.transaction_set.all()
	template = loader.get_template('census/transactions.html')
	context = {
		'transactions': transactions
	}
	return HttpResponse(template.render(context,request))

def register(request):
	template = loader.get_template('census/register.html')
	if request.method == 'POST':
		user_form = LoginForm(data=request.POST)
		if user_form.is_valid():
			# save the new user
			new_user = User.objects.create_user(
				username=user_form.cleaned_data['username'],
				first_name=user_form.cleaned_data['first_name'],
				last_name=user_form.cleaned_data['last_name'],
				email=user_form.cleaned_data['email'],
				password=user_form.cleaned_data['password1'],
				)
			new_user.save()
			return HttpResponseRedirect("/census/")
		else:
			print(user_form.errors)
	else:
		user_form = LoginForm()
	return HttpResponse(template.render({'user_form': user_form}, request))

def login_user(request):
	template = loader.get_template('census/login.html')
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		user_account = authenticate(username=username, password=password)
		if user_account is not None:
			login(request, user_account)
			next_url = request.POST.get('next',default=request.GET.get('next', 'login.html'))
			return HttpResponseRedirect(next_url)
		else:
			return HttpResponse(template.render({'failed': True}, request))
	else:
		return HttpResponse(template.render({'next': request.GET.get('next', '/census')}, request))

def logout_user(request):
	template = loader.get_template('census/logout.html')
	logout(request)
	context = {}
	return HttpResponse(template.render(context,request))

#Jinyun - dependent dropdowns and popups start here:

#expected to be called when a new copy is submitted; displaying the copy info
def copy_info(request, copy_id):
	template=loader.get_template('census/copy_info.html')
	selected_copy=get_object_or_404(Copy, pk=copy_id)
	selected_issue=selected_copy.issue
	selected_edition=selected_issue.edition
	context={
		'selected_edition': selected_edition,
		'selected_copy': selected_copy,
	}
	return HttpResponse(template.render(context,request))

def submission(request):
	template = loader.get_template('census/submission.html')
	all_titles = Title.objects.all()
	copy_form = CopyForm()
	if request.method=='POST':
		issue_id=request.POST.get('issue')
		selected_issue=Issue.objects.get(pk=issue_id)
		copy_form=CopyForm(data=request.POST)
		if copy_form.is_valid():
			copy=copy_form.save(commit=False)
			copy.issue=selected_issue
			copy.save()
			return HttpResponseRedirect(reverse('copy_info', args=(copy.id,)))
	else:
		copy_form=CopyForm()

	context = {
	'all_titles': all_titles,
	'copy_form': copy_form,
	}

	return HttpResponse(template.render(context, request))

def edit_copy_submission(request, copy_id):
	template = loader.get_template('census/submission.html')
	all_titles = Title.objects.all()
	copy_to_edit=Copy.objects.get(pk=copy_id)

	data={"thumbnail_URL": copy_to_edit.thumbnail_URL,
			"NSC": copy_to_edit.NSC,
			"Owner": copy_to_edit.Owner,
			"Shelfmark": copy_to_edit.Shelfmark,
			"Height": copy_to_edit.Height,
			"Width": copy_to_edit.Width,
			"Marginalia": copy_to_edit.Marginalia,
			"Condition": copy_to_edit.Condition,
			"Binding": copy_to_edit.Binding,
			"Binder": copy_to_edit.Binder,
			"Bookplate":copy_to_edit.Bookplate,
			"Bookplate_Location": copy_to_edit.Bookplate_Location,
			"Barlett1939": copy_to_edit.Barlett1939,
			"Barlet1939_Notes": copy_to_edit.Barlet1939_Notes,
			"Barlet1916": copy_to_edit.Barlet1916,
			"Barlet1916_Notes": copy_to_edit.Barlet1916_Notes,
			"Lee_Notes": copy_to_edit.Lee_Notes,
			"Library_Notes": copy_to_edit.Library_Notes,}

	# copy_form =CopyForm(instance=Copy.objects.get(pk=copy_id))
	if request.method=='POST':
		issue_id=request.POST.get('issue')
		selected_issue=Issue.objects.get(pk=issue_id)
		copy_form=CopyForm(request.POST)
		if copy_form.is_valid():
			copy_to_edit.NSC = copy_form.cleaned_data['NSC']
			copy_to_edit.issue=selected_issue
			return HttpResponseRedirect(reverse('copy_info', args=(copy_id,)))
	else:
		copy_form=CopyForm(initial=data)

	context = {
	'all_titles': all_titles,
	'copy_form': copy_form,
	}
	return HttpResponse(template.render(context, request))

def copy_submission_success(request):
	template=loader.get_template('census/copysubmissionsuccess.html')
	context={}
	return HttpResponse(template.render(context, request))

def cancel_copy_submission(request, copy_id):
	copy_to_delete=Copy.objects.get(pk=copy_id)
	copy_to_delete.delete()
	return HttpResponseRedirect(reverse('homepage'))

def json_editions(request, id):
	current_title = Title.objects.get(pk=id)
	editions = current_title.edition_set.all()
	data = []
	for edition in editions:
		data.append(model_to_dict(edition))
	return HttpResponse(json.dumps(data), content_type='application/json')

def json_issues(request, id):
	current_edition = Edition.objects.get(pk=id)
	issues = current_edition.issue_set.all()
	data = []
	for issue in issues:
		data.append(model_to_dict(issue))
	return HttpResponse(json.dumps(data), content_type='application/json')

@login_required()
def add_title(request):
	template=loader.get_template('census/addTitle.html')
	if request.method == 'POST':
		title_form= TitleForm(data=request.POST)
		if title_form.is_valid():
			title = title_form.save(commit=True)
			myScript = '<script type="text/javascript">opener.dismissAddAnotherTitle(window, "%s", "%s");</script>' % (title.id, title.title)
			return HttpResponse(myScript)
		else:
			print(title_form.errors)
	else:
		title_form=TitleForm()

	context = {
	   'title_form': title_form
	}
	return HttpResponse(template.render(context, request))

@login_required()
def add_edition(request, title_id):
	template=loader.get_template('census/addEdition.html')
	selected_title =Title.objects.get(pk=title_id)

	if request.method=='POST':
		edition_form=EditionForm(data=request.POST)
		if edition_form.is_valid():
			edition=edition_form.save(commit=False)
			edition.title=selected_title
			edition.save()
			myScript = '<script type="text/javascript">opener.dismissAddAnotherEdition(window, "%s", "%s");</script>' % (edition.id, edition.Edition_number)
			return HttpResponse(myScript)
		else:
			print(edition_form.errors)
	else:
		edition_form=EditionForm()

	context={
		'edition_form':edition_form,
		'title_id': title_id,
	}
	return HttpResponse(template.render(context, request))

@login_required()
def add_issue(request, edition_id):
	template=loader.get_template('census/addIssue.html')
	selected_edition =Edition.objects.get(pk=edition_id)

	if request.method=='POST':
		issue_form=IssueForm(data=request.POST)
		if issue_form.is_valid():
			issue=issue_form.save(commit=False)
			issue.edition=selected_edition
			issue.save()
			myScript = '<script type="text/javascript">opener.dismissAddAnotherIssue(window, "%s", "%s");</script>' % (issue.id, issue.STC_Wing)
			return HttpResponse(myScript)
		else:
			print(issue_form.errors)
	else:
		issue_form=IssueForm()

	context={
		'issue_form':issue_form,
		'edition_id': edition_id,
	}
	return HttpResponse(template.render(context, request))
#dependent dropdowns and popups trials end here
