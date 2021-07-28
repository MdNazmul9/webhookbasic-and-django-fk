from django.shortcuts import render

from  django.views.generic import TemplateView


import json
from django.http import HttpResponse
from django.views.generic import View
from braces.views import CsrfExemptMixin
# from braces.views import LoginRequiredMixin, SuperuserRequiredMixin

class  ProcessWebhookView(CsrfExemptMixin, View):
    def post(self, request, *args, **kwargs):
        print(json.loads(request.body))
        return HttpResponse("success")



class  PayloadView(TemplateView):
    template_name = 'webhook/payload.html'




