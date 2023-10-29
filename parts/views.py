from django.shortcuts import render
from .models import *

# Create your views here.


def get_component_tree(request):
    components = Details.objects.all()

    def build_tree(node):
        children = Details.objects.filter(parent_components__in=[node])
        return {'component': node, 'children': [build_tree(child) for child in children]}

    root_components = Details.objects.filter(parent_components=None)
    tree = [build_tree(root) for root in root_components]

    return render(request, 'parts/component-tree.html', {'tree': tree})