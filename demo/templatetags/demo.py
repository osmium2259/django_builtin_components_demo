from django import template
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

register = template.Library()


@register.inclusion_tag('demo/components/sidebar.html', takes_context=True)
def sidebar(context):
    request = context['request']
    links = [
        [_('Home'), reverse('demo:home'), 'bi-house-fill'],
        [_('About'), reverse('demo:about'), 'bi-info-circle-fill'],
        [_('Contact'), reverse('demo:contact'), 'bi-envelope-at-fill'],
    ]

    links[0].append(request.path_info == links[0][1])

    for link in links[1:]:
        link.append(request.path_info.startswith(link[1]))

    return {'request': request, 'links': links}
