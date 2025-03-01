from typing import Annotated
from django.core.exceptions import ImproperlyConfigured
from pydantic import BaseModel

class DjaggerConfig(BaseModel):
    """Djagger configuration schema"""
    global_prefix: Annotated[str, ""]

try:
    from django.conf import settings
    djagger_config = DjaggerConfig.model_validate(settings.DJAGGER_CONFIG)

except (ImproperlyConfigured, AttributeError):
    djagger_config = DjaggerConfig() # type: ignore
