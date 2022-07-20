import requests
from bs4 import BeautifulSoup as bs

def login(username, password):
    payload = {
        'username': str(username),
        'password': str(password),
        'LogIn': 'LOGIN'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }

    base_url = 'http://www.sis.nileuniversity.edu.ng/my/loginAuth.php'


    with requests.Session() as s:
        res = s.post(base_url, data = payload, headers= headers)
        grades_page = 'http://www.sis.nileuniversity.edu).ng/my/index.php?mod=grades'

        res2 = s.get(grades_page, headers = headers)

        soup = bs(res2.text, 'html.parser')

        search = soup.select('td b')
        scores = []
        for x in search:
            if len(x) > 0 :
                scores.append(x.text.strip())

        search2 = soup.select('td')
        credits = []
        for x in search2:
            if x.text.isnumeric() and len(x.text) < 2:
                credits.append(x.text)

    grades = {}

    for x in range(len(scores)):
        if scores[x] in list(grades.keys()):
            grades[scores[x]].append(credits[x])

        else:
            grades[scores[x]] = [credits[x]]

    return grades




