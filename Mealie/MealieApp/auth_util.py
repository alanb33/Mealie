from django.http import HttpResponseRedirect
from django.urls import reverse

def redirect(request, level):
    match level:
        case "superuser":
            return superuser_redirect(request)
        case "auth":
            return authenticated_redirect(request)
        case _:
            return authenticated_redirect(request)

# Redirect the user to the index if they are not a superuser.
def superuser_redirect(request):
    authenticated_redirect(request)
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse("Mealie:index"))

# Redirect the user to the login screen if they are not authenticated.
def authenticated_redirect(request):
    if not request.user.is_authenticated:
        print("Not authenticated")
        return HttpResponseRedirect(reverse("Mealie:login"))