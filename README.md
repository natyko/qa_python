# qa_python

# 📚 BooksCollector - Unit Tests

This project contains unit tests for the `BooksCollector` class using **pytest**.

## 📝 List of Implemented Tests

### 1️⃣ **Adding a Book**

- ✅ `test_add_new_book_success` - Ensures books can be added if they meet the requirements.
- ✅ `test_add_new_book_failure` - Ensures books **cannot** be added if they exceed 40 characters or are duplicates.

### 2️⃣ **Setting Book Genre**

- ✅ `test_set_book_genre_success` - Successfully assigns a genre to a book.
- ✅ `test_set_book_genre_failure` - Ensures only valid genres can be assigned.

### 3️⃣ **Retrieving Books by Genre**

- ✅ `test_get_books_with_specific_genre` - Returns books of a specific genre.

### 4️⃣ **Children's Book Filter**

- ✅ `test_get_books_for_children` - Returns only books without age restrictions.

### 5️⃣ **Managing Favorites**

- ✅ `test_add_book_in_favorites_success` - Successfully adds a book to favorites.
- ✅ `test_add_book_in_favorites_failure` - Ensures only existing books can be added to favorites.
- ✅ `test_delete_book_from_favorites_success` - Successfully removes a book from favorites.
- ✅ `test_delete_book_from_favorites_failure` - Ensures removing a non-favorite book does nothing.

### 6️⃣ **Retrieving Favorite Books**

- ✅ `test_get_list_of_favorites_books` - Returns a list of favorite books.

## 🚀 Running Tests

To run the tests, use:

```bash
pytest -v