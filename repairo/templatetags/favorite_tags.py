from django import template

register = template.Library()


@register.filter(name='has_favorite')
def has_favorite(car, user):
    return car.favorites.filter(user=user).exists()
