import requests
import hashlib

# gofile url
url = ''

# optional
password = ''

# =================================

def gofile_dl(url):
    api_uri = 'https://api.gofile.io'
    client = requests.Session()
    res = client.get(api_uri+'/createAccount').json()
    
    data = {
        'contentId': url.split('/')[-1],
        'token': res['data']['token'],
        'websiteToken': 'websiteToken',
        'cache': 'true',
        'password': hashlib.sha256(password.encode('utf-8')).hexdigest()
    }
    res = client.get(api_uri+'/getContent', params=data).json()

    content = []
    for item in res['data']['contents'].values():
        content.append(item)
    
    return {
        'accountToken': data['token'],
        'files': content
    }

# =================================

print(gofile_dl(url))

# =================================

'''
SAMPLE OUTPUT:
{
    accountToken: 'xxxxx' (to be used as a cookie if ddl doesn't work)
    files: [
        {
            'id': 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX', 
            'type': 'file', 
            'name': 'XXX', 
            'parentFolder': 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX', 
            'createTime': 1837708755, 
            'size': 11851111419,
            'downloadCount': 442, 
            'md5': '509d4472ea7e00000000000000008bd3', 
            'mimetype': 'application/vnd.rar', 
            'serverChoosen': 'store1', 
            'directLink': 'https://store1.gofile.io/download/XYZ', 
            'link': 'https://store1.gofile.io/download/XYZ'
        },
        {
            # more objects for multi-files
        }
    ]
}
'''
