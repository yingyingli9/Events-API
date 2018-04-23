# reference: https://v2.developer.pagerduty.com/docs/send-an-event-events-api-v2

import requests
import os

# api-endpoint for Event actions
URL = "https://events.pagerduty.com/v2/enqueue"

routing_key = os.environ['routing_key']

# Trigger event
data = {
    "routing_key": routing_key,
    "event_action": "trigger",
    "images": [],
    "links": [],
    "payload": {
        "summary": "Example Trigger Event",
        "source": "Example source",
        "severity": "info"
    }
}

r = requests.post(url=URL, json=data)
print(r.json())

dedup_key = r.json()['dedup_key']

# Acknowledge event
data = {
  "routing_key": routing_key,
  "dedup_key": dedup_key,
  "event_action": "acknowledge"
}
r = requests.post(url=URL, json=data)
print(r.json())

# resolve event
data = {
  "routing_key": routing_key,
  "dedup_key": dedup_key,
  "event_action": "resolve"
}
r = requests.post(url=URL, json=data)
print(r.json())