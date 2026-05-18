from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Photo, Tag


@login_required
def gallery_view(request):
    """Display all photos, optionally filtered by tag."""
    
    photos = Photo.objects.all()
    tags = Tag.objects.all()
    selected_tag = None

    tag_name = request.GET.get('tag')
    if tag_name:
        photos = photos.filter(tags__name=tag_name)
        selected_tag = tag_name

    return render(request, 'photo_gallery/gallery.html', {
        'photos': photos,
        'tags': tags,
        'selected_tag': selected_tag,
    })