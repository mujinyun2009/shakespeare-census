from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.template import Context, Template
from django.shortcuts import render
from django.template import loader
import models
from .models import *
# from.models import Title, Edition, Copy, UserProfile, Provenance, BookPlate
from django.contrib.auth.models import User
from .forms import *
# from .forms import TitleForm, EditionForm, IssueForm, CopyForm, ProvenanceForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.forms import formset_factory
from django.contrib import admin


# Create your views here.

def homepage(request):
    template=loader.get_template('frontpage.html')
    context = {

    }
    return HttpResponse(template.render(context, request))
def search(request):
    query = request.POST.get('qs', '')
    results = Title.objects.filter(title=query) # Your search algo goes here
    return render(request, 'census/index.html', dict(results=results))

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

def trial(request):
	template = loader.get_template('census/trial.html')
	all_titles = Title.objects.all()
	context = {
	'all_titles': all_titles
	}
	return HttpResponse(template.render(context, request))

def all_json_models(request, id):
	current_title = Title.objects.get(pk=id)
	editions = current_title.edition_set.all()
	# editions=Edition.objects.all().filter(title=current_title)
	json_models = serializers.serialize("json", editions)
	return HttpResponse(json_models, mimetype="application/javascript")


@login_required()
def addTitle(request):
	template=loader.get_template('census/addTitle.html')
	if request.method == 'POST':
		title_form= TitleForm(data=request.POST)
		if title_form.is_valid():
			title_form = title_form.save(commit=True)
			return HttpResponseRedirect("/census/submission")
		else:
			print(title_form.errors)
	else:
		title_form=TitleForm()
	context = {
	'title_form': title_form
	}
	return HttpResponse(template.render(context, request))


@login_required()
def submissionForm(request):
	template=loader.get_template('census/submission.html')
	title_dropdown_form=TitleDropDownForm()
	edition_form=EditionDropDownForm()
	# edition_form=EditionForm()
	issue_form=IssueForm()
	copy_form=CopyForm()
	provenance_form=ProvenanceForm()

	if request.method == 'POST':
		title_dropdown_form= TitleDropDownForm(data=request.POST)
		edition_form=EditionDropDownForm(data=request.POST)
		# edition_form = EditionForm(data=request.POST)
		issue_form = IssueForm(data=request.POST)
		copy_form = CopyForm(data=request.POST)
		provenance_form = ProvenanceForm(data=request.POST)

		if title_dropdown_form.is_valid():
			title = title_dropdown_form.cleaned_data['title']

			if edition_form.is_valid():
				edition = edition_form.cleaned_data['edition']
				# edition = edition_form.save(commit=False)
				# edition.title = title
				# edition.save()
				if issue_form.is_valid():
					issue = issue_form.save(commit=False)
					issue.edition = edition
					issue.save()
					if copy_form.is_valid():
						copy = copy_form.save(commit=False)
						copy.issue = issue
						copy.save()
						if provenance_form.is_valid():
							provenance = provenance_form.save(commit=False)
							provenance.copy = copy
							provenance.save()
						else:
							print(provenance_form.errors)
					else:
						print(copy_form.errors)
				else:
					print(issue_form.erros)
				return HttpResponseRedirect("/census/")
			else:
				print(edition_form.errors)
		else:
			print(title_dropdown_form.errors)
			# print(title_form.errors)

	context = {
		'title_dropdown_form': title_dropdown_form,
		# 'title_form': title_form,
		'edition_form': edition_form,
		'issue_form': issue_form,
		'copy_form': copy_form,
		'provenance_form': provenance_form
	}
	return HttpResponse(template.render(context, request))

def transactions(request, copy_id):
	selected_copy = Copy.objects.get(pk=copy_id)
	transactions= selected_copy.transaction_set.all()
	template = loader.get_template('census/transactions.html')
	context = {
		'transactions': transactions
	}
	return HttpResponse(template.render(context,request))


# @login_required()
# def Editionz(request):
# 	template=loader.get_template('submissionedition.html')
# 	if request.method == 'POST':
# 		edition_form = EditionForm(data=request.POST)
# 		if edition_form.is_valid():
# 			edition_form = edition_form.save(commit=False)
# 			edition_form.title=Title.objects.get(pk=1)
# 			edition_form.save()
# 		else:
# 			print(edition_form.errors)
# 	else:
# 		edition_form=EditionForm()
# 	context = {
# 	'edition_form': edition_form
# 	}
# 	return HttpResponse(template.render(context, request))
# @login_required()
# def Copyz(request):
# 	template=loader.get_template('submissioncopy.html')
# 	if request.method == 'POST':
# 		copy_form = CopyForm(data=request.POST)
# 		if copy_form.is_valid():
# 			copy_form = copy_form.save(commit=True)
# 			copy_form.save()
# 		else:
# 			print(copy_form.errors)
# 	else:
# 		copy_form=CopyForm()
# 	context = {
# 	'copy_form': copy_form
# 	}
# 	return HttpResponse(template.render(context, request))
# @login_required()
# def Provenancez(request):
# 	template=loader.get_template('submissionprovenance.html')
# 	if request.method == 'POST':
# 		provenance_form = ProvenanceForm(data=request.POST)
# 		if provenance_form.is_valid():
# 			provenance_form = provenance_form.save(commit=True)
# 			provenance_form.save()
# 		else:
# 			print(provenance_form.errors)
# 	else:
# 		provenance_form=ProvenanceForm()
# 	context = {
# 	'provenance_form': provenance_form
# 	}
# 	return HttpResponse(template.render(context, request))
