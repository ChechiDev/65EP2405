from decimal import Decimal, InvalidOperation
from django.shortcuts import render
from .models import Libro

def libro_list(request):
    qs = Libro.objects.select_related('autor').prefetch_related('generos', 'detalle').all()

    genero = request.GET.get('genero', '').strip()
    min_raw = request.GET.get('min', '').strip()
    max_raw = request.GET.get('max', '').strip()

    if genero:
        qs = qs.filter(generos__nombre__icontains=genero)

    def to_decimal(s: str):
        if not s:
            return None
        try:
            return Decimal(s)
        except (InvalidOperation, ValueError):
            return None

    min_price = to_decimal(min_raw)
    max_price = to_decimal(max_raw)

    if min_price is not None and max_price is not None and min_price > max_price:
        min_price, max_price = max_price, min_price

    if min_price is not None:
        qs = qs.filter(_precio__gte=min_price)
    if max_price is not None:
        qs = qs.filter(_precio__lte=max_price)

    context = {
        "libros": qs.order_by('-fecha_creacion')[:200],
        "filtros": {
            "genero": genero,
            "min": min_raw,
            "max": max_raw,
        }
    }
    return render(request, "libros/list.html", context)

