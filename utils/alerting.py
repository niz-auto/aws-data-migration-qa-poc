import requests

def send_alert(message):

    webhook = "https://hooks.slack.com/services/xxxxx"

    requests.post(webhook, json={"text": message})