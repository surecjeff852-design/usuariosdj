from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q
from .models import Posts, ProductMetaLookup

def productos(request):

    q = request.GET.get("q", "")

    productos = Posts.objects.filter(
        post_type__in=['product', 'product_variation'],
        post_status='publish'
    ).select_related('meta')

    if q:
        palabras = q.split()
        filtro_base = Q()

        for palabra in palabras:
            filtro_base |= Q(post_title__icontains=palabra)
            filtro_base |= Q(post_excerpt__icontains=palabra)
            filtro_base |= Q(ID__icontains=palabra)
            filtro_base |= Q(meta_values__meta_value__icontains=palabra)

        productos = productos.filter(filtro_base).distinct()

    productos = sorted(
        productos,
        key=lambda p: 0 if p.post_excerpt and p.post_excerpt.strip() else 1
    )

    paginator = Paginator(productos, 50)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    for p in page_obj:

        stock_obj = p.meta_values.filter(
            meta_key__in=["_stock", "_stock_quantity", "stock_quantity"]
        ).first()

        p.stock = stock_obj.meta_value if stock_obj else "Agotado" 
        p.descripcion = p.post_excerpt if p.post_excerpt else "No disponible"

        if hasattr(p, "meta") and p.meta:
            p.sku = p.meta.sku
            p.global_unique_id = p.meta.global_unique_id
            p.virtual = p.meta.virtual
            p.downloadable = p.meta.downloadable
            p.min_price = p.meta.min_price
            p.max_price = p.meta.max_price
            p.onsale = p.meta.onsale
            p.stock_quantity = p.meta.stock_quantity
            p.stock_status = p.meta.stock_status
            p.rating_count = p.meta.rating_count
            p.average_rating = p.meta.average_rating
            p.total_sales = p.meta.total_sales
            p.tax_status = p.meta.tax_status
            p.tax_class = p.meta.tax_class
        else:
            p.sku = "No definido"
            p.global_unique_id = "No definido"
            p.virtual = "No definido"
            p.downloadable = "No definido"
            p.min_price = "No definido"
            p.max_price = "No definido"
            p.onsale = "No definido"
            p.stock_quantity = "No definido"
            p.stock_status = "No definido"
            p.rating_count = "No definido"
            p.average_rating = "No definido"
            p.total_sales = "No definido"
            p.tax_status = "No definido"
            p.tax_class = "No definido"

    return render(request, 'reportes/productos.html', {
        'page_obj': page_obj,
        'q': q,
    })
