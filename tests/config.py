"""
File: config.sample.py
Description: unittest configuration for Python SDK of the Cognitive Face API.

- Copy `config.sample.py` to `config.py`.
- Assign the `KEY` with a valid Subscription Key.
"""
import os

# Subscription Key for calling the Cognitive Face API.
URL = os.environ.get("TA_SWAGGER_URL") or "https://westus.dev.cognitive.microsoft.com/docs/services/TextAnalytics.V2.0/export?DocumentFormat=Swagger&ApiName=Azure%20Machine%20Learning%20-%20Text%20Analytics"

# Can hardcode here or Stored in ENV for CI testing 
KEY = os.environ.get("TA_SUBSCRIPTION_KEY")
