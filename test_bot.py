from slackclient import SlackClient

oauth_token = 'xoxp-27173653120-27171354980-1264505934583-8dbf2c8036aef342f862ed161a995f10'
bot_token = 'xoxb-27173653120-1274574860293-2z2IzszH8HAh6wT2CqLEn1mA'

slack_client = SlackClient(oauth_token, )

bool = slack_client.rtm_connect(with_team_state=False)
