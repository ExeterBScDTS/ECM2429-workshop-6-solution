import requests

class BookshopClient:
    def __init__(self, host='http://127.0.0.1:5000'):
        self.__host = host

    def get_books(self):
        url = '/book/list'
        resp = requests.get(self.__host + url)
        return resp.json()

    def get_book(self, isbn):
        url = f'/book/{isbn}'
        resp = requests.get(self.__host + url)
        return resp.json()

    def create_book(self, isbn, title, author, price):
        url = '/book'
        book = {'isbn':isbn, 'title':title, 'author':author, 'price':price}
        resp = requests.post(self.__host + url, json=book)
        return resp.json()

    def update_book(self, isbn, title, author, price):
        url = '/book'
        book = {'isbn':isbn, 'title':title, 'author':author, 'price':price}
        resp = requests.put(self.__host + url, json=book)
        return resp.json()       

    def delete_book(self, isbn):
        url = f'/book/{isbn}'
        resp = requests.delete(self.__host + url)
        return resp.json()


if __name__ == '__main__':
    client = BookshopClient()
    print('\nbook/list')
    books = client.get_books()
    print(books)
    print('\nbook/1')
    book1 = client.get_book(1)
    print(book1)
    print('\nDELETE book/1')
    book1 = client.delete_book(1)
    print(book1)
    print('\nbook/list')
    books = client.get_books()
    print(books)
    print('\nCREATE book')
    newbook = client.create_book(5, 'no title', 'no author', 1.00)
    print(newbook)
    print('\nbook/list')
    books = client.get_books()
    print(books)
