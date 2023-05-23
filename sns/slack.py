from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from webcam.function_merge_run import message

from sns.token import slack_token

client = WebClient(token=slack_token)

def dm_text(message: str):
    try:
        response_msg = client.chat_postMessage(channel='cbnu-project',
                                               text=f"Candidate Kyu-Sung Han's voice: {message}.")

    except SlackApiError as e:
        print('Error: {}'.format(e.response['error']))


def dm_text_img():
    try:
        response_msg = client.chat_postMessage(channel='cbnu-project',
                                               text=f"Candidate {message.user}'s {message.object} was detected on the screen. please check.")

        response_png = client.files_upload(channels='cbnu-project',
                                           file='/Users/sharekim_hangyuseong/github_repository/Be-Honest/img/screenshot.png',
                                           filename='file.png',
                                           filetype='png')

    except SlackApiError as e:
        print('Error: {}'.format(e.response['error']))

if __name__ == '__main__':
    dm_text_img()