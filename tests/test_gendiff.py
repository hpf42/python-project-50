import pytest

from gendiff.scripts.generate_diff import generate_diff
from gendiff.scripts.file_parser import read_file


@pytest.mark.parametrize('file_path_1, file_path_2, expected_result', [
    ('tests/test_data/file_1.json',
     'tests/test_data/file_2.json',
     'tests/test_data/expected_result_json.txt'),
    ('tests/test_data/file_1.yaml',
     'tests/test_data/file_2.yaml',
     'tests/test_data/expected_result_yaml.txt')])
def test_generate_diff(file_path_1, file_path_2, expected_result):
    diff = generate_diff(file_path_1, file_path_2)
    expected = read_file(expected_result).strip()
    assert diff.strip() == expected