#!/usr/bin/env python3
"""
Convert pyproject.toml to requirements.txt
"""
import toml


class RequirementsConverter:
    """
    @description: a class containing scripts for conversion
    """
    def __init__(self) -> None:
        self.__source = 'pyproject.toml'
        self.__target = 'requirements.txt'
        self.__dependencies = self.__load_dependencies()
        self.__requirements = self.__make_requirements()

    def __load_dependencies(self) -> dict[str, str]:
        """
        @description: get a list of dependencies from pyproject.toml
        """
        content = toml.load(self.__source)
        packages = content['tool']['poetry']['dependencies']
        packages.pop('python', None)
        return packages

    def __make_requirements(self) -> str:
        """
        @description: convert the list of dependencies to requirements format
        """
        items = [f'{package}=={version}'
                 for package, version in self.__dependencies.items()]
        return '\n'.join(items)

    def get_dependencies(self) -> dict[str, str]:
        """
        @description: getter for dependencies in pyproject.toml
        """
        return self.__dependencies

    def get_requirements(self) -> str:
        """
        @description: getter for requirements
        """
        return self.__requirements

    def write_requirements(self) -> None:
        """
        @description: write requirements to requirements.txt
        """
        with open(self.__target, 'w', encoding='UTF-8') as file:
            file.write(self.__requirements)


if __name__ == '__main__':
    converter = RequirementsConverter()
    converter.write_requirements()
