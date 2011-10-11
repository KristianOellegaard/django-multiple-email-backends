#-*- coding: utf-8 -*-
from django.core.mail.backends.base import BaseEmailBackend
from django.conf import settings
from django.core.mail import get_connection

class CombinedEmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        for backend in getattr(settings, "EMAIL_BACKEND_LIST", []):
            get_connection(backend).send_messages(email_messages)
        return len(email_messages)