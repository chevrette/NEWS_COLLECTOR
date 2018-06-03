from django.shortcuts import redirect, render
from django.http import HttpResponseNotFound
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from users.models import UserProfile
from links.models import Link, Comment, Like

# === Funkcje reprezentujące widoki aplikacji links:  ===
"""
Funkcja zwiększająca liczbę głosów na dany link. Jeśli w bazie danych znajduje 
się już taka para użytkownik-link(obiekt klasy Like), to głos nie zostaje 
oddany.
"""
@login_required
def vote(request, link_id):
    voted_link = Link.objects.get(pk=link_id)
    user = request.user
    author = UserProfile.objects.get(user=user)
    try:
        Like.objects.get(user=author, link=voted_link)
    except Like.DoesNotExist:
        Like.objects.create(
            user=author,
            link=voted_link
            )
        voted_link.votes += 1
        voted_link.save()
    return redirect('main_page')


"""
Funkcja działa analogicznie do funkcji vote, lecz dla komentarzy.
"""
@login_required
def vote_comment(request, com_id):
    voted_comment = Comment.objects.get(pk=com_id)
    com_link = voted_comment.link
    link_id = com_link.id
    user = request.user
    author = UserProfile.objects.get(user=user)
    try:
        Like.objects.get(user=author, comment=voted_comment)
    except Like.DoesNotExist:
        Like.objects.create(
            user=author,
            comment=voted_comment
            )
        voted_comment.votes += 1
        voted_comment.save()
    return redirect('comment', link_id=link_id)


"""
Funkcja generujaca stronę z komentarzami do danego linku. W szablonie comments 
dodawany jest szablon comments_tree, w którym rekurencyjnie tworzy się drzewo 
komentarzy.
"""
def comment(request, link_id):
    link = Link.objects.get(id=link_id)
    comments = Comment.objects.filter(link_id=link.id)
    context = {
        'link': link,
        'comments': comments,
    }
    return render(request, 'links/comments.html', context)


"""
Funkcja służąca do dodawania komentarzy. Jesli wykonywany jest POST, 
z formularza w szablonie pobierane są dane potzrebne do utworzenia komentarza, 
a następnie tworzny jest obiekt klasy Comment.
"""
@login_required
def add_comment(request):
    if request.method == 'POST':
        form_data = request.POST
        link_id = form_data['link_id']
        parent_comment_id = form_data.get('parent_com_id', None)
        parent_comment = Comment.objects.get(
            id=parent_comment_id) if parent_comment_id else None
        comment_text = form_data['text']
        link = Link.objects.get(id=link_id)
        user = request.user
        author = UserProfile.objects.get(user=user)
        comment = Comment(
            link=link,
            text=comment_text,
            published_date=timezone.now(),
            parent_comment=parent_comment,
            author=author
            )
        comment.save()
        return redirect('comment', link_id=link_id)
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')


"""
Funkcja generująca stronę do odpowiedzi na komentarz.
"""
@login_required
def reply_comment(request, com_id):
    comment = Comment.objects.get(id=com_id)
    link = comment.link
    context = {
        'link': link,
        'comment': comment,
    }
    return render(request, 'links/reply.html', context)


"""
Funkcja do dodawania linków na stronie głównej. Jeśli wykonywany jest POST, 
tworzony jest obiekt klasy Link.
"""
@login_required
def add_link(request):
    if request.method == 'POST':
        form_data = request.POST
        link = form_data['link']
        link_title = form_data['link_title']
        user = request.user
        author = UserProfile.objects.get(user=user)
        Link.objects.create(
            url=link,
            title=link_title,
            author=author
        )
    return redirect('main_page')