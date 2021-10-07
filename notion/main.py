# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json
from requests.sessions import Session
import requests

def get_html(url):
    _html = ""
    resp = requests.get(url)
    if resp.status_code == 200:
        _html = resp.text
    return _html


PAGE_URL = 'URL '


def setTestPage():
    response = requests.post(PAGE_URL, headers={'Content-Type': 'application/json',
                                                'Authorization': 'ADD - KEY',
                                                'Notion-Version': '2021-05-13'},
                             json={

                                 "filter": {
                                     "property": "작성일",
                                     "date": {
                                         "on_or_after": "2021-10-07"
                                     }
                                 }

                             }
                             )
    print("The title is:", response)
    response.encoding = 'euc-kr'
    print("The title is:", response.encoding)

    my_json = response.content.decode('utf8').replace("'", '"')

    print(type(my_json))
    data = json.loads(my_json)
    print(type(data))
    # print(data)

    print(data['results'][0]['properties'])

    # print(data[,,])
    s = json.dumps(data, indent=4, sort_keys=True)
    # print(s)
    print(type(s))


if __name__ == '__main__':
    session_data = requests.session()  # type: Session
    print("[START]")
    setTestPage()
    print('[END]')
