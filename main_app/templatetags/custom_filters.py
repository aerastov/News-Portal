from django import template

register = template.Library()
censorwords = ["сука", "блять", "пиздец", "охуенная", "хуй", "ебать"]

@register.filter(name='censor')
def censor(value):
    for a in censorwords:
        b = str(a + ",")
        с = str(b.title())
        value = value.replace(a, "<CEN>")
        value = value.replace(b, "<CEN>")
        value = value.replace(с, "<CEN>")
    return value
