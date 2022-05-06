"""Views.py"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

from bookmarks.common.decorators import ajax_required
from .forms import ImageCreateForm
from .models import Image
# Create your views here.
@login_required
def image_create(request):
    """Image upload view"""
    if request.method == "POST":
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            messages.success(request, "Image added Successfully")
            return redirect(new_item.get_absolute_url())
    else:
        form = ImageCreateForm(data=request.GET)

    return render(request, "images/image/create.html",{"section":"images","form":form})

@login_required
def image_detail(request, id, slug):
    """Getting absolute URL of page."""
    image = get_object_or_404(Image, id = id, slug = slug)
    return render(request, "images/image/detail.html", {"section":"images", "image":image})

@ajax_required
@login_required
@require_POST
def image_like(request):
    """Tracking user likes"""
    image_id = request.POST.get("id")
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id = image_id)
            if action == "like":
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({"status":"ok"})
        except:
            pass
    return JsonResponse({"status":"error"})

@login_required
def image_list(request):
    """Internal view"""
    images = Image.objects.all()
    paginator = Paginator(images, 8)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            return HttpResponse('')
        images = paginator.page(paginator.num_pages)
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return render(request, "images/image/list_ajax.html",{'section':'images','images':images})
    return render(request, "images/image/list.html", {'section':"images",'images':images})
