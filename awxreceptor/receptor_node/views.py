from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ReceptorNode

def index(request):
    return HttpResponse("Hello, enter the node_id or node name")

def render_config(request, param):
    if isinstance(param, int):
        node = get_object_or_404(ReceptorNode, pk=param)
    else:
        node = get_object_or_404(ReceptorNode, name=param)
    return render(request, 'receptor_nodes/render_config.html', {
        'node': node
    }, content_type='application/x-yaml')
