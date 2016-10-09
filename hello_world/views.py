from django.shortcuts import render
from django.http import HttpResponse
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)


def index(request):
    score = r.get('counter')
    return render(request, 'index.twig', {
        'message': 'Hello, world!',
        'score': score
    })


def like(request):
    r.incr('counter', 1)
    return HttpResponse(status=200)


def dislike(request):
    r.decr('counter', 1)
    return HttpResponse(status=200)
