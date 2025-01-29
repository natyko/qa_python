import pytest
from main import BooksCollector


# Fixture для инициализации объекта
@pytest.fixture
def books_collector():
    return BooksCollector()


# Тесты для add_new_book
@pytest.mark.parametrize("book_name", ["Книга1", "Очень длинное название книги, которое содержит 39 символов"])
def test_add_new_book_success(books_collector, book_name):
    books_collector.add_new_book(book_name)
    assert book_name in books_collector.get_books_genre()
    assert books_collector.get_books_genre()[book_name] == ""


@pytest.mark.parametrize("book_name", ["", "Очень длинное название книги, которое содержит более 40 символов"])
def test_add_new_book_failure(books_collector, book_name):
    books_collector.add_new_book(book_name)
    assert book_name not in books_collector.get_books_genre()


# Тесты для set_book_genre
@pytest.mark.parametrize("book_name, genre", [("Книга1", "Фантастика"), ("Книга2", "Комедии")])
def test_set_book_genre_success(books_collector, book_name, genre):
    books_collector.add_new_book(book_name)
    books_collector.set_book_genre(book_name, genre)
    assert books_collector.get_book_genre(book_name) == genre


@pytest.mark.parametrize("book_name, genre", [("Книга1", "Неизвестный жанр"), ("Несуществующая книга", "Фантастика")])
def test_set_book_genre_failure(books_collector, book_name, genre):
    books_collector.add_new_book("Книга1")
    books_collector.set_book_genre(book_name, genre)
    assert books_collector.get_book_genre(book_name) != genre


# Тесты для get_books_with_specific_genre
def test_get_books_with_specific_genre(books_collector):
    books_collector.add_new_book("Книга1")
    books_collector.add_new_book("Книга2")
    books_collector.set_book_genre("Книга1", "Фантастика")
    books_collector.set_book_genre("Книга2", "Комедии")
    assert books_collector.get_books_with_specific_genre("Фантастика") == ["Книга1"]


# Тесты для get_books_for_children
def test_get_books_for_children(books_collector):
    books_collector.add_new_book("Книга1")
    books_collector.add_new_book("Книга2")
    books_collector.set_book_genre("Книга1", "Фантастика")
    books_collector.set_book_genre("Книга2", "Ужасы")
    assert books_collector.get_books_for_children() == ["Книга1"]


# Тесты для add_book_in_favorites
def test_add_book_in_favorites_success(books_collector):
    books_collector.add_new_book("Книга1")
    books_collector.add_book_in_favorites("Книга1")
    assert books_collector.get_list_of_favorites_books() == ["Книга1"]


def test_add_book_in_favorites_failure(books_collector):
    books_collector.add_book_in_favorites("Несуществующая книга")
    assert books_collector.get_list_of_favorites_books() == []


# Тесты для delete_book_from_favorites
def test_delete_book_from_favorites_success(books_collector):
    books_collector.add_new_book("Книга1")
    books_collector.add_book_in_favorites("Книга1")
    books_collector.delete_book_from_favorites("Книга1")
    assert books_collector.get_list_of_favorites_books() == []


def test_delete_book_from_favorites_failure(books_collector):
    books_collector.add_new_book("Книга1")
    books_collector.delete_book_from_favorites("Книга1")
    assert books_collector.get_list_of_favorites_books() == []


# Тесты для get_list_of_favorites_books
def test_get_list_of_favorites_books(books_collector):
    books_collector.add_new_book("Книга1")
    books_collector.add_new_book("Книга2")
    books_collector.add_book_in_favorites("Книга1")
    assert books_collector.get_list_of_favorites_books() == ["Книга1"]
