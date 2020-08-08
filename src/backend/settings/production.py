"""Settings for running RACTF backend locally."""

# flake8: noqa

from . import *

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


SEND_MAIL = True

ALLOWED_HOSTS.extend(("ractf.co.uk", "api-elite.ractf.co.uk"))

TEMPLATES.insert(0, {
    "BACKEND": "django.template.backends.jinja2.Jinja2",
    "DIRS": [os.path.join(BASE_DIR, 'templates')],
    "APP_DIRS": True,
})

MAIL = {
    "SEND_ADDRESS": "no-reply@ractf.co.uk",
    "SEND_NAME": "RACTF",
    "SEND": True,
}

sentry_sdk.init(
    dsn="https://beaf099a91144f74afac77c0afe70518@o430159.ingest.sentry.io/5378144",
    integrations=[DjangoIntegration()],
    send_default_pii=True
)

REST_FRAMEWORK["DEFAULT_THROTTLE_RATES"].update({
    "challenges": "4/second",
    "leaderboard": "4/second",
    "self": "4/second",
    "member": "4/second",
    "team": "4/second",
    "config": "4/second",
    "announcement": "4/second",
})