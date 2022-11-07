from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from sns.token import slack_token

client = WebClient(token=slack_token)

try:
    response_msg = client.chat_postMessage(channel='cbnu-project',
                                           text='Test message from python slack api')

    # response_xlsx = client.files_upload(channels='cbnu-project',
    #                                       file='item_sample_1.xlsx',
    #                                       filename='item_sample_1_share.xlsx',
    #                                       filetype='xlsx')
    #
    # response_csv = client.files_upload(channels='cbnu-project',
    #                                       file='item_sample_2.csv',
    #                                       filename='item_sample_2_share.csv',
    #                                       filetype='csv')
    #
    response_png = client.files_upload(channels='cbnu-project',
                                          file='/Users/sharekim_hangyuseong/github_repository/Be-Honest/img/test.png',
                                          filename='test.png',
                                          filetype='png')

    # response_jpg = client.files_upload(channels='cbnu-project',
    #                                    file='item_sample_2.jpg',
    #                                    filename='item_sample_2_share.jpg',
    #                                    filetype='jpg')

    print(response_msg['ok'])
    # print(response_xlsx['ok'])
    # print(response_csv['ok'])
    print(response_png['ok'])
    # print(response_jpg['ok'])

except SlackApiError as e:
    print('Error: {}'.format(e.response['error']))