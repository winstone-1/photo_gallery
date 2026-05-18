from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Photo, Tag, Like


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


@login_required
def photo_detail_view(request, pk):
    """Display a single photo with full details."""

    photo = get_object_or_404(Photo, pk=pk)
    user_like = None

    try:
        user_like = Like.objects.get(user=request.user, photo=photo)
    except Like.DoesNotExist:
        pass

    return render(request, 'photo_gallery/photo_detail.html', {
        'photo': photo,
        'user_like': user_like,
    })


@login_required
def like_photo_view(request, pk):
    """Handle like and dislike actions on a photo."""

    if request.method == 'POST':
        photo = get_object_or_404(Photo, pk=pk)
        value = request.POST.get('value')

        if value not in ['like', 'dislike']:
            messages.error(request, 'Invalid action.')
            return redirect('photo_detail', pk=pk)

        like, created = Like.objects.get_or_create(
            user=request.user,
            photo=photo,
            defaults={'value': value}
        )

        if not created:
            if like.value == value:
                # Same vote again — remove it (toggle off)
                like.delete()
                messages.info(request, 'Vote removed.')
            else:
                # Switch vote
                like.value = value
                like.save()
                messages.success(request, 'Vote updated.')
        else:
            messages.success(request, 'Vote recorded.')

    return redirect('photo_detail', pk=pk)