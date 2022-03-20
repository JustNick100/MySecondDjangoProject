from django.shortcuts import render

# Create your views here.
def users(request):
	return render(request,"admin/users.html")

def agents(request):
	return render(request,"admin/agents.html")

def categories(request):
	return render(request,"admin/categories.html")

def categories_suggestions(request):
	return render(request,"admin/categories_suggestions.html")

def transcripts(request):
	return render(request,"admin/transcripts.html")

def transcripts_messages(request):
	return render(request,"admin/transcripts_messages.html")

def clients(request):
	return render(request,"admin/clients.html")

def languages(request):
	return render(request,"admin/languages.html")

def language_translations(request):
	return render(request,"admin/language_translations.html")

def services(request):
	return render(request,"admin/services.html")