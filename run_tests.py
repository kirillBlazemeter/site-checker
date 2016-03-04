import pytest

if __name__ == '__main__':
    pytest.main(
        args='--alluredir=allure-results test.py')