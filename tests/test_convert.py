import unittest
from pathlib import Path

import toml

from requirements.convert import RequirementsConverter


def write_dependencies(items: dict[str, str]) -> None:
    source_path = Path(".").resolve() / "tests" / "pyproject.toml"
    if not source_path.exists():
        raise FileNotFoundError
    content = toml.load(str(source_path))
    content["tool"]["poetry"]["dependencies"] = items
    with source_path.open("w") as file:
        toml.dump(content, file)


def read_requirements() -> list[str]:
    output_path = Path(".").resolve() / "tests" / "requirements.txt"
    if not output_path.exists():
        raise FileNotFoundError
    with output_path.open("r") as file:
        result = file.read().split("\n")
    return result


class TestRequirementsConverter(unittest.TestCase):
    def __check_conversions(self, mapping: dict[str, str]) -> None:
        converted = {}
        for dependency in list(mapping.keys()):
            package, version = dependency.split(" = ", maxsplit=1)
            converted[package] = version.strip(r"\"'")
        write_dependencies(converted)
        RequirementsConverter("tests").write_requirements()
        self.assertListEqual(read_requirements(), list(mapping.values()))

    def test_regular(self):
        self.__check_conversions(
            {'click = "8.0.0"': "click==8.0.0", 'toml = "0.10.2"': "toml==0.10.2"}
        )

    def test_exact(self):
        self.__check_conversions({'requests = "=2.13.0"': "requests==2.13.0"})

    def test_caret(self):
        self.__check_conversions({'requests = "^2.13.0"': "requests==2.13.0"})

    def test_local(self):
        inputs = ["python-jose = {extras = ['cryptography'], version = '^3.3.0'}"]
        expected = ["python-jose[cryptography]==3.3.0"]
        self.__check_conversions(dict(zip(inputs, expected)))

    def test_extras(self):
        inputs = ["mylib = {path = 'libs/mylib-3.0.4-py3-none-any.whl'}"]
        expected = ["libs/mylib-3.0.4-py3-none-any.whl"]
        self.__check_conversions(dict(zip(inputs, expected)))


if __name__ == "__main__":
    unittest.main()
