import os
import properties as props
import slack_comms


def f1():
    print('hello world')


if __name__ == "__main__":

    text = {
			"color": "#04bf13",
			"blocks": [
				{
					"type": "section",
					"text": {
						"type": "plain_text",
						"text": "Teste brabo.",
						"emoji": True
					}
				},
                {
					"type": "section",
					"text": {
						"type": "plain_text",
						"text": "Teste brabo2.",
						"emoji": True
					}
				}
			]
		}
    
    response = slack_comms.send_msg(text)