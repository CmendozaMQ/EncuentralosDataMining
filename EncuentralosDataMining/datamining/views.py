# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from .fb_get_posts_page_multiple import *
# from tempa import *
from .secrets import FACEBOOK_APP_ID, FACEBOOK_APP_SECRET
from .models import *
import pandas as pd
import numpy as np
import os
import csv
from django.http import HttpResponse
from .models import savePosts
import urllib

# keyInformation=[
# "desaparecido",
# "desaparecida",
# "desaparecidos",
# "desaparecidas",
# "extraviados",
# "buscamos",
# "desaparecio",
# "buscando",
# "Encontrada",
# "búsqueda",
# "encontrados",
# "Comparte"]

#export data information
def export_post_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Lista_de_posts.csv"'
    writer = csv.writer(response)
    writer.writerow(['Status id', 'Status message', 'Link name', 'Status type', 'Status link', 'Status published'])
    posts_csv = savePosts.objects.all().values_list('status_id', 'status_message', 'link_name', 'status_type', 'status_link', 'status_published')
    for post in posts_csv:
        writer.writerow(post)

    return response
#end export data information

def cleanFilesCSV():
    mydir = '..\..\..\EncuentralosDataMining\EncuentralosDataMining'
    filelist = [f for f in os.listdir(mydir) if f.endswith(".csv")]
    for f in filelist:
        os.remove(os.path.join(mydir, f))

def isNaN(num):
    return num != num


def home(request):
    return render(request, 'accounts/login.html')


def home_setup(request):
    return render(request, 'datamining/home_setup.html')


def scrapeData(request):
    access_token_in = FACEBOOK_APP_ID + "|" + FACEBOOK_APP_SECRET
    group_id_in = request.GET.getlist('groupId')
    keyInformation = request.GET.getlist('KeyWord')
    print(group_id_in)
    print(keyInformation)
    since_date = request.GET['since_date_in']
    until_date = request.GET['until_date_in']
    cleanFilesCSV()
    scrapdata.objects.all().delete()
    scrapdataMessageBlank.objects.all().delete()
    for group_ids in group_id_in:
        print(group_ids)
        if group_ids != '':
            scrapeFacebookPageFeedStatus(group_ids, access_token, since_date, until_date)
            dataset = pd.read_csv('../EncuentralosDataMining/'+group_ids+'_facebook_statuses.csv')
            csvRows = dataset.iloc[:, :-9].values
            for datacsv in csvRows:
                if (isNaN(datacsv[1]) is False):
                    datacsv[1] = datacsv[1].lower()
                    datacsv_info = list(datacsv[1].split())
                    datacsv_value = list(set(datacsv_info).intersection(set(keyInformation)))
                    # print(datacsv_value)
                    if not datacsv_value:
                        print(True)
                        infocsv = np.asarray(datacsv)
                        p = scrapdata(status_id=infocsv[0], status_message=infocsv[1], link_name=infocsv[2],
                                          status_type=infocsv[3], status_link=infocsv[4],
                                          status_published=infocsv[5], found_post=False)
                        p.save()
                    else:
                        print(False)
                        infocsv = np.asarray(datacsv)
                       # infocsv_message = infocsv[1].split()
                        q = scrapdata(status_id=infocsv[0], status_message=infocsv[1], link_name=infocsv[2],
                                          status_type=infocsv[3], status_link=infocsv[4],
                                          status_published=infocsv[5], found_post=True)
                        q.save()
                else:
                    print("blank")
                    infocsv = np.asarray(datacsv)
                    p = scrapdata(status_id=infocsv[0], status_message=infocsv[1], link_name=infocsv[2],
                                          status_type=infocsv[3], status_link=infocsv[4],
                                          status_published=infocsv[5], found_post=False)
                    p.save()
    datainfo =scrapdata.objects.all().filter(found_post=True).order_by('-status_published')
    SDBCount_sd = scrapdata.objects.filter(found_post=True).count()
    print(SDBCount_sd)
    return render(request, 'datamining/scrapeData.html', {'datainfo':datainfo, 'SDBCount':SDBCount_sd})


def scrapeDataBlank(request):
    datainfoBlank = scrapdata.objects.all().filter(found_post=False).order_by('-status_published')
    SDBCount = scrapdata.objects.filter(found_post=False).count()
    print(SDBCount)
    return render(request, 'datamining/scrapeDataBlank.html', {'datainfoBlank':datainfoBlank, 'SDBCount':SDBCount})


def scrapeData_page(request):
    scrapdata_info = scrapdata.objects.all().filter(found_post=True).order_by('-status_published')
    SDBCount_sd = scrapdata.objects.filter(found_post=True).count()
    return render(request, 'datamining/scrapeData.html', {'datainfo':scrapdata_info, 'SDBCount':SDBCount_sd})


def savePost_page(request):
    post_info = savePosts.objects.all()
    return render(request, 'datamining/savePost_page.html', {'post_info': post_info})


def about(request):
    return render(request, 'datamining/about.html')


def save_post(request):
    if request.method == 'POST':
        if request.POST['id']:
            id_post = request.POST['id']
            postData = scrapdata.objects.get(id=id_post)
            posts = savePosts()
            posts.status_id = postData.status_id
            posts.status_message = postData.status_message
            posts.link_name = postData.link_name
            posts.status_type = postData.status_type
            posts.status_link = postData.status_link
            posts.status_published = postData.status_published
            posts.save()
            postData.delete()
            datainfoBlank = scrapdata.objects.all().filter(found_post=False).order_by('-status_published')
            SDBCount = scrapdata.objects.filter(found_post=False).count()
            print(SDBCount)
        return render(request, 'datamining/scrapeDataBlank.html', {'datainfoBlank':datainfoBlank, 'SDBCount':SDBCount})


def save_post_data(request):
    if request.method == 'POST':
        if request.POST['id']:
            id_post = request.POST['id']
            postData = scrapdata.objects.get(id=id_post)
            posts = savePosts()
            posts.status_id = postData.status_id
            posts.status_message = postData.status_message
            posts.link_name = postData.link_name
            posts.status_type = postData.status_type
            posts.status_link = postData.status_link
            posts.status_published = postData.status_published
            posts.save()
            postData.delete()
            datainfo_s = scrapdata.objects.all().filter(found_post=True).order_by('-status_published')
            SDBCount_s = scrapdata.objects.filter(found_post=True).count()
            print(SDBCount_s)
        return render(request, 'datamining/scrapeData.html', {'datainfo':datainfo_s, 'SDBCount':SDBCount_s})