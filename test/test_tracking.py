from main import read_file

def test_read_file():
    file_content = read_file()
    assert file_content == []