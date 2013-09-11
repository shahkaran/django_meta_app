# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context,RequestContext
from bs4 import BeautifulSoup
from meta.models import *
import urllib2
import json


def hello(request):
	return HttpResponse("Hello world")

def home(request):
	return render(request,'index.html');


def getInfo(request):
	url=request.POST["url"]
	website = urllib2.urlopen(url)
	op=website.read()
	soup=BeautifulSoup(op)
	title=soup.title.string
	response_data={}
	meta_desc=""
	meta_keywords=""
	meta = soup.find_all('meta')
        for tag in meta:
		if 'name' in tag.attrs and tag.attrs['name'].lower() == 'description':
			meta_desc=tag.attrs['content']
		elif 'name' in tag.attrs and tag.attrs['name'].lower() =='keywords':
			meta_keywords=tag.attrs['content']

	response_data["title"]=title
	response_data["desc"]=meta_desc
	response_data["keywords"]=meta_keywords

	return HttpResponse(json.dumps(response_data), mimetype="application/json");

def saved(request):
	t=get_template('index.html')
	return HttpResponse(t.render(RequestContext(request,{'saved':True})));

def saveInfo(request):
	meta_url=request.POST["url"]
	meta_title=request.POST["title"]
	keywords=request.POST["keywords"]
	desc=request.POST["desc"]
	new_entry=url_info(url=meta_url,title=meta_title,meta_desc=desc,meta_keywords=keywords)
	new_entry.save()
	return HttpResponseRedirect("/saved")


