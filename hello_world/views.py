from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import redis


class HelloWorldView(View):

    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

    def get(self, request):
        score = self.r.get('counter')
        data = {
            'message': 'Hello, world!',
            'score': int(score)
        }
        return render(request, 'index.twig', data)


class LikeView(HelloWorldView):

    def get(self, request):
        self.r.incr('counter', 1)
        return HttpResponse(status=200)


class DislikeView(HelloWorldView):
    def get(self, request):
        self.r.decr('counter', 1)
        return HttpResponse(status=200)


class ResetCounterView(HelloWorldView):

    def get(self, request):
        self.r.set('counter', 0)
        return HttpResponse(status=200)
