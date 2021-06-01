from unittest.case import _id

from bson import ObjectId
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from polls.models import Posts


@csrf_exempt
def add_post(request):
    comment = request.POST.get("comment").split(",")
    tags = request.POST.get("tags").split(",")
    user_details = {"first_name": request.POST.get("first_name"), "last_name": request.POST.get("last_name")}
    post = Posts(post_title=request.POST.get("post_title"), post_description=request.POST.get("post_description"),
                 comment=comment, tags=tags, user_details=user_details)
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


def read_post_all(request):
    posts = Posts.object.all()
    stringval = ""
    for post in posts :
        stringval += "First Name : " + post.user_details['first_name'] + " Last Name : " + post.user_details['last_name'] \
                    + " Post Title " + post.post_title + " Comment " + post.comment[0] + "<br>"
    return HttpResponse(stringval)
