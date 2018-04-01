def request_string(instance, value):
        request_instance = instance(request_value=value)
        request_qty = instance.objects.all().count()
        if request_qty >= 20:
            instance.objects.all().first().delete()
        request_instance.save()
