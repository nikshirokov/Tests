import pytest
from unittest import TestCase
from main import vote, solution, get_name, get_directory, add, documents, directories, create_folder


def test_vote_1():
    votes = [1, 1, 1, 2, 3]
    expected = 1
    assert vote(votes) == expected


def test_vote_2():
    votes = [1, 2, 3, 2, 2]
    expected = 2
    assert vote(votes) == expected


@pytest.mark.parametrize(
    'votes,expected',
    (
            ([1, 1, 1, 2, 3], 1),
            ([1, 2, 3, 2, 2], 2)
    )
)
def test_vote_with_params(votes, expected):
    result = vote(votes)
    assert result == expected


def test_solution_1():
    a = 1
    b = 8
    c = 15
    expected = (-3.0, -5.0)
    assert solution(a, b, c) == expected


def test_solution_2():
    a = 1
    b = -13
    c = 12
    expected = (12.0, 1.0)
    assert solution(a, b, c) == expected


def test_solution_3():
    a = -4
    b = 28
    c = -49
    expected = 3.5
    assert solution(a, b, c) == expected


def test_solution_4():
    a = 1
    b = 1
    c = 1
    expected = 'корней нет'
    assert solution(a, b, c) == expected


@pytest.mark.parametrize(
    'a, b, c, expected',
    (
            (1, 8, 15, (-3.0, -5.0)),
            (1, -13, 12, (12.0, 1.0)),
            (-4, 28, -49, 3.5),
            (1, 1, 1, 'корней нет')
    )
)
def test_solution_with_params(a, b, c, expected):
    result = solution(a, b, c)
    assert result == expected


class Test_Secretory:
    def setup_method(self):
        document_type = 'international passport'
        number = '311 020203'
        name = 'Александр Пушкин'
        shelf_number = '3'
        add(document_type, number, name, shelf_number)

    def test_add(self):
        assert len(documents) == 5 and len(directories['3']) != []

    def test_get_name_1(self):
        doc_number = '10006'
        expected = 'Аристарх Павлов'
        assert get_name(doc_number) == expected

    def test_get_name_2(self):
        doc_number = '101'
        expected = 'Документ не найден'
        assert get_name(doc_number) == expected

    def test_get_name_3(self):
        doc_number = '311 020203'
        expected = 'Александр Пушкин'
        assert get_name(doc_number) == expected

    def test_get_directory_1(self):
        doc_number = '11-2'
        expected = '1'
        assert get_directory(doc_number) == expected

    def test_get_directory_2(self):
        doc_number = '311 020203'
        expected = '3'
        assert get_directory(doc_number) == expected

    def test_get_directory_3(self):
        doc_number = '311 020204'
        expected = 'Полки с таким документом не найдено'
        assert get_directory(doc_number) == expected


class TestYD(TestCase):
    def test_new_folder(self):
        expected = create_folder('path', 'new folder')
        self.assertIn(expected, (201, 409))

    def test_new_folder_with_params(self):
        for i, (path, folder_name, status) in enumerate([
            ('path', 'новая папка', 201),
            ('path', 'новая папка', 409),
            ('pa', 'новая папка', 400)
        ]):
            with self.subTest(i):
                result = create_folder(path, folder_name)
                self.assertEqual(status, result)
