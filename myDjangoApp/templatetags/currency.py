from decimal import Decimal
from django import template

register = template.Library()


@register.filter
def pesos(value):
    try:
        value = Decimal(value)
        value = value.quantize(Decimal("1"))
        return f"${value:,.0f}".replace(",", ".")
    except (ValueError, TypeError, ArithmeticError):
        return value
