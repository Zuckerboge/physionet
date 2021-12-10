from django.conf import settings

from project.models import AccessPolicy


def access_policy(request):
    return {'AccessPolicy': AccessPolicy}


def platform_name(request):
    return {'SITE_NAME': settings.SITE_NAME}


def footer_data(request):
    return {
        'FOOTER_MANAGED_BY': settings.FOOTER_MANAGED_BY,
        'FOOTER_SUPPORTED_BY': settings.FOOTER_SUPPORTED_BY,
        'FOOTER_ACCESSIBILITY_PAGE': settings.FOOTER_ACCESSIBILITY_PAGE,
    }
