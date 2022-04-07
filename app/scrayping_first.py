import requests
from bs4 import BeautifulSoup

# requestsのgetメソッドで、指定されたURLの情報を取ってくる
r = requests.get('https://karuppi.jp/')


# print("ステータスコードを表示:")
# print(r.status_code)
# print()
# print("HTTPヘッダーの辞書を取得:")
# print(r.headers['content-type'])
# print()
# print("エンコーディングを表示:")
# print(r.encoding)
# print()
# print("htmlの中身を表示:")
# print(r.text)


soup = BeautifulSoup(r.text, 'html.parser')

print(f'soup.h1 => {soup.h1}')
print(f'soup.h1.name => {soup.h1.name}')
print(f'soup.h1.string => {soup.h1.string}')

a = soup.find_all('a')
print(f'soup.find_all(\'a\') => {a}')