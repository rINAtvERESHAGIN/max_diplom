from unittest.case import _id
from django.http.response import HttpResponse, JsonResponse, HttpResponseBadRequest
from bson import ObjectId
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from polls.serializers import AddNewMusicSerializer
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from polls.models import Posts
from polls.models import Music


class AddNewMusic(APIView):
    def post(self, request):
        def get_response_music():
            musics = Music.object.all()
            response_data = []

            for music in musics:
                response_data.append({
                    "composer": music.composer,
                    "executor": music.executor,
                    "genre": music.genre,
                    "label": music.label,
                    "nominations": music.nominations,
                    "release_date": music.release_date,
                    "songwriter": music.songwriter,
                })
            return response_data

        print(request.data)
        serializer = AddNewMusicSerializer(data=request.data)

        print('serializer.is_valid()', serializer.is_valid())

        print('SSSSS', serializer.data.pop('composer'))
        print('SSSSS', serializer.data.keys())
        if serializer.is_valid():
            music = Music(
                composer=serializer.data.pop("composer"),
                executor=serializer.data.pop("executor"),
                genre=serializer.data.pop("genre"),
                label=serializer.data.pop("label"),
                nominations=serializer.data.pop("nominations"),
                release_date=serializer.data.pop("release_date"),
                songwriter=serializer.data.pop("songwriter"),
                file_in_binary=serializer.data.pop("file_in_binary"),
            )
            music.save()
            return JsonResponse(data=get_response_music(), safe=False)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def add_music(request):
    print(request.POST)
    print(request.POST.get("composer"))
    print(request.data)

    music = Music(
        composer=request.POST.get("composer"),
        executor=request.POST.get("executor"),
        genre=request.POST.get("genre"),
        label=request.POST.get("label"),
        nominations=request.POST.get("nominations"),
        release_date=request.POST.get("release_date"),
        songwriter=request.POST.get("songwriter"),
        file_in_binary=request.POST.get("file_in_binary"))
    music.save()
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
    musics = Music.object.all()
    responseData = []

    for music in musics:
        responseData.append({
            "composer": music.composer,
            "executor": music.executor,
            "genre": music.genre,
            "label": music.label,
            "nominations": music.nominations,
            "release_date": music.release_date,
            "songwriter": music.songwriter,
        })

    print(responseData)
    return JsonResponse(data=responseData, safe=False)
