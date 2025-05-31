from .base import *  # noqa
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

###################################################################
# General
###################################################################

DEBUG = False

###################################################################
# Django security
###################################################################

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = [
    "https://example.com",
    "https://muhammadjabborov.jprq.app",
    "https://admin.icc-kimyo.uz",
    "https://icc-kimyo.uz",
    "https://reklama.icc-kimyo.uz",
]

###################################################################
# CORS
###################################################################

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ["*"]

sentry_sdk.init(
    dsn="https://9f68fecfd41476bf342235ab224cfa79@o4507672631902208.ingest.us.sentry.io/4507772537208832",
    integrations=[
        DjangoIntegration(),
    ],
    traces_sample_rate=1.0,
    send_default_pii=True
)
