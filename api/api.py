from ninja import NinjaAPI,Schema
from .models import URL
import secrets

api = NinjaAPI()

class Url(Schema):
    original_url: str
    key: str = None
    secret_key: float = None
    is_active: bool = True
    clicks: int = 0

@api.get("/")
def hello(request):
    return "Welcome to THE Url Shortening Application"

@api.post("/url")
def create(request,url: str):

    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    key = "".join(secrets.choice(chars) for _ in range(5))
    secret_key = "".join(secrets.choice(chars) for _ in range(8))

    url = URL.objects.create(original_url=url,key = key, secret_key = secret_key)
    return f'shortyurl.io/{key}'



@api.get("/{url_key}")
def redirect(request, url_key):
    s_key=url_key
    URL.objects.get(secret_key={url_key})


@api.get("/admin/{secret_key}")
def create(request, item: Url):
    return item

@api.delete("/admin/{secret_key}")
def create(request, item: Url):
    return item










