from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse('<html><body>olá mundo</body></html>', content_type='text/html')
