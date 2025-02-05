from django.contrib import admin
from django.urls import path, include
import logging

logger = logging.getLogger(__name__)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
]

# Debug: Print URL patterns
for pattern in urlpatterns:
    logger.debug(f"Pattern: {pattern}")