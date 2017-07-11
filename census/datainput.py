from .models import *
import csv

def create_title(title_name):
	return Title.objects.create(title=title_name)

def create_edition(new_title, number):
	return Edition.objects.create(title=new_title, Edition_number=number)

def create_issue(new_edition, new_date, new_STC_Wing, new_ESTC, new_notes):
	return Issue.objects.create(edition=new_edition, year=new_date, STC_Wing=new_STC_Wing, ESTC=new_ESTC, notes=new_notes)

def create_copy(new_issue, library, shelfmark, copy_note, provinfo):
	return Copy.objects.create(issue=new_issue, Owner=library, Shelfmark=shelfmark, copynote=copy_note, prov_info=provinfo)

def remove_all_titles():
	titles=Title.objects.all()
	for title in titles:
		title.delete()

def remove_all_editions():
	editions=Edition.objects.all()
	for edition in editions:
		edition.delete()

def remove_all_issues():
	issues=Issue.objects.all()
	for issue in issues:
		issue.delete()

def remove_all_copies():
	copies=Copy.objects.all()
	for copy in copies:
		copy.delete()

def read_issue_file(csv_file_path):
	with open(csv_file_path, 'rU') as csvfile:
		reader=csv.reader(csvfile)

		for row in reader:
			if row[0] =='Title':
				continue
			related_title=list(Title.objects.filter(title=row[0]))
			if related_title:
				new_title=related_title[0]
			else:
				new_title=create_title(row[0])

			related_edition=list(Edition.objects.filter(title=new_title, Edition_number=row[1]))
			if related_edition:
				new_edition=related_edition[0]
			else:
				new_edition=create_edition(new_title, row[1])

			new_issue=create_issue(new_edition, row[2], row[3], row[4], row[5])
	return "success"

def read_copy_file(csv_file_path):
	with open(csv_file_path, 'rU') as csvfile:
		reader=csv.reader(csvfile)

		for row in reader:
			if row[0]=='ESTC number':
				continue;

			related_issue=list(Issue.objects.filter(ESTC=row[0]))
			library=row[1]
			shelfmark=row[3]
			copynote=row[4]
			if copynote=='null':
				copynote=''

			prov_info=row[5]
			if prov_info=='null':
				prov_info=''

			create_copy(related_issue[0], library, shelfmark, copynote, prov_info)
	return "success"
