from django.urls import path
# import from the same folder as the urls.py file is in
from . import views


urlpatterns = [
    # Our path is just January. The second argument is a pointer at the view function that should be executed when a request reaches that URL.

    # `views.index` is pointing at the index function defined in the views.py file.

    # With that, we're basically telling Django if a request reaches `/january`, then execute this index view function.

    # Now that's a first step, but it's not everything. This creates a so-called URLconfig, or often all called URLconf. We configured the URLs we wants to support in this application and which views should be triggered for the incoming requests.

    # Now, this will not be enough though, because this is now a URLconfig defined in our challenges app, which is a part of the overall monthly_challenges project. Therefore we now need to connect this challenges app to the entire project. We need to make the entire URLconfig aware of the URLconfig for this specific app.
    path("january", views.january),
    path("february", views.february),
]
