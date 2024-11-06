import urllib
import urllib.request
import json

def ask_url(url):
    head = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / "
                      "80.0.3987.122  Safari / 537.36"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

def ask_url_post(url, data):
    head = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / "
                      "80.0.3987.122  Safari / 537.36"
    }
    request = urllib.request.Request(url, headers=head, data=urllib.parse.urlencode(data).encode("utf-8"))
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

def ask_url_post_as_dict(url, data):
    response = ask_url_post(url, data)
    try:
        response_dict = json.loads(response)
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        response_dict = {}
    return response_dict

def get_last_word_of_url(url):
    index = -1
    if url.endswith("/"):
        index = -2
    return url.split("/")[index]
    
