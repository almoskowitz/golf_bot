from slackclient import SlackClient
from config import get_env

class SlackHelper:

    def __init__(self):
        self.slack_token = '' #which token?
        self.slack_client = SlackClient(self.slack_token)
        self.slack_channel = '' #slack channel?

    def post_message(self, msg, recipient):
        return self.slack_client.api_call(
        method="chat.PostMessage",
        channel = recipient,
        text = msg,
        as_user = True)

    def post_message_to_channel(self, msg):
        return self.slack_client.api_call(
        method = "chat.postMessage",
        channel = self.slack_channel,
        text = msg,
        username = 'test_bot',
        parse = 'full',
        as_user = False
        )

    def 
