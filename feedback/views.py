from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic.list_detail import object_list
from models import *



def index(request):
    if request.method == 'POST':
        feedback = Feedback()
        feedback.ip_address = request.META['REMOTE_ADDR']
        feedback.kind = request.POST['kind']
        feedback.version = request.POST['version']
        feedback.text = request.POST['feedback']
        feedback.save()
        return HttpResponseRedirect(feedback.get_absolute_url())
    else:
        return render_to_response("feedback/index.html",
            context_instance=RequestContext(request=request))

def show_list(request, filter_by, page=1):
    for item in FEEDBACK_CHOICE:
        if item[1] == filter_by:
            kind_short = item[0]
            break
    else:
            raise Http404
    feedback = Feedback.objects.filter(kind=kind_short).order_by('-pub_date')
    return object_list(request, queryset=feedback, page=page, allow_empty=True, extra_context={'kind': filter_by})
