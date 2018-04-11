from .models import RequestListener

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


class RequestListenerMiddleware(MiddlewareMixin):

    def process_request(self, request):
        value = request.build_absolute_uri()
        request_instance = RequestListener(request_value=value)
        request_qty = RequestListener.objects.all().count()
        if request_qty >= 20:
            RequestListener.objects.all().first().delete()
        request_instance.save()
        return None
