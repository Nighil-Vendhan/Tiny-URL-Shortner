"""
URL shorten with TinyURL API
"""
import requests
import sys
import traceback
import urllib


class UrlShortenTinyurl:
    URL = "http://tinyurl.com/api-create.php"

    def shorten(self, url_long):
        try:
            url = self.URL + "?" \
                + urllib.parse.urlencode({"url": url_long})
            res = requests.get(url)
            print("STATUS CODE:", res.status_code)
            print("   LONG URL:", url_long)
            print("  SHORT URL:", res.text)
        except Exception as e:
            raise


if __name__ == '__main__':
    url_long = "https://www.mk-mode.com/octopress/2018/02/25/python-napier-computation/"
    try:
        obj = UrlShortenTinyurl()
        obj.shorten(url_long)
    except Exception as e:
        traceback.print_exc()
