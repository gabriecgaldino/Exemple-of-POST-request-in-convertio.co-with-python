
import requests

from getGitRepository import links

url = 'https://api.convertio.co/convert'
apikey = 'get you apikey in convertio.co'

for item in links:
    request = requests.post(
        url,
        json={
            "apikey": f"{apikey}",
            "file": f"{item}",
            "outputformat": "jpg"
        }
    )
    print(request.json())

'''
Link URL: https://api.convertio.co/convert
'''
