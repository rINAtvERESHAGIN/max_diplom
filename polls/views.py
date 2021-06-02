from unittest.case import _id

from bson import ObjectId
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from polls.models import Posts
from polls.models import Music


@csrf_exempt
def add_music(request):
    post = Posts(composer=request.POST.get("composer"),
                 executor=request.POST.get("executor"),
                 genre=request.POST.get("genre"),
                 label=request.POST.get("label"),
                 nominations=request.POST.get("nominations"),
                 release_date=request.POST.get("release_date"),
                 songwriter=request.POST.get("songwriter"),
                 file_in_binary=request.POST.get("file_in_binary"))
    post.save()
    return HttpResponse("inserted")


@csrf_exempt
def update_post(request, id):
    post = Posts.object.get(_id=ObjectId(id))
    post.user_details['first_name'] = request.POST.get('first_name')
    post.save()
    return HttpResponse("Post Updated")


def delete_post(request, id):
    post = Posts.object.get(_id=ObjectId(id))
    post.delete()
    return HttpResponse("Post Deleted")


def read_post(request, id):
    print(Posts)
    post = Posts.object.get(_id=ObjectId(id))
    # post = Posts.objects.get(_id=ObjectId(id))
    stringval = "First Name : " + post.user_details['first_name'] + " Last Name : " + post.user_details['last_name'] \
                + " Post Title " + post.post_title + " Comment " + post.comment[0]
    return HttpResponse(stringval)


def get_all_music(request):
    posts = Music.object.all()
    stringval = ""
    for post in posts:
        stringval += "composer" + post.composer + "executor " + post.executor + "genre " + post.genre + "label " + \
                     post.label + "nominations " + post.nominations + "release_date " + post.genre + "songwriter " + \
                     post.label + "file_in_binary" + post.file_in_binary + "<br>"
    return HttpResponse(stringval)
