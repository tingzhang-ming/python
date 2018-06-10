import connexion
import six

from swagger_server.models.book import Book  # noqa: E501
from swagger_server import util


def add_book(book):  # noqa: E501
    """Add a new book to the store

     # noqa: E501

    :param book: Pet object that needs to be added to the store
    :type book: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        book = Book.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_book(book):  # noqa: E501
    """Add a new book to the store

     # noqa: E501

    :param book: Pet object that needs to be added to the store
    :type book: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        book = Book.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def find_book_by_status(state):  # noqa: E501
    """Finds Book by status

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param state: Status values that need to be considered for filter
    :type state: List[str]

    :rtype: None
    """
    return 'do some magic!'
