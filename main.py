from messageprocessor import MessageProcessor
from userprocessor import UserProcessor
from datetime import datetime


if __name__ == '__main__':

    RAW_FOLDER_PATH = "data/processed/"

    filepath = RAW_FOLDER_PATH + "users/%s.json" % (datetime.today().strftime('%Y-%m-%d'))
    url = "https://619ca0ea68ebaa001753c9b0.mockapi.io/evaluation/dataengineer/jr/v1/users"
    processor = UserProcessor()
    if processor.process(url, filepath):
        print('processed the users and subscriptions')
    else:
        print('error while processing users and subscriptions')

    filepath = RAW_FOLDER_PATH + "messages/%s.json" % (datetime.today().strftime('%Y-%m-%d'))
    url = "https://619ca0ea68ebaa001753c9b0.mockapi.io/evaluation/dataengineer/jr/v1/messages"
    processor = MessageProcessor()
    if processor.process(url, filepath):
        print('processed the messages')
    else:
        print('error while processing messages')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
