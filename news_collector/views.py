from django.shortcuts import render
from links.models import Link


# === Funkcja reprezentująca widok strony głównej:  ===

"""
Domyślnie zostaje załadowany widok z linkami posortowanymi wg daty.
W przypadku wyboru danego sortowania, za pomocą metody GET pobrana zostaje 
wartość parametru sort. Jej wartośc zostaje przypisana do pola filter.
"""
def main_page(request):
    sort_by = '-published_date'
    filter = request.GET.get('sort')
    if filter == 'date':
        sort_by = '-published_date'
    elif filter == 'votes':
        sort_by = '-votes'
    latest_links = Link.objects.order_by(sort_by)[:15]
    context = {
        'latest_links': latest_links,
    }
    return render(request, 'news_collector/main_page.html', context)
