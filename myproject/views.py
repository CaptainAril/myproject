from django.http import JsonResponse


# Create your views here.
def status(request):
    """
    Returns the status of the server.
    """
    return JsonResponse({"status": "ok"})
