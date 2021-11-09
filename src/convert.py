#!/usr/bin/env python3
"""
Convert pyproject.toml to requirements.txt
"""
from pathlib import Path

import toml
import click


class RequirementsConverter:
    """
    @description: a class containing scripts for conversion
    """
    def __init__(self, project_dir: str) -> None:
        self.__project_dir = Path(project_dir).resolve(strict=True)
        self.__source = self.__project_dir / 'pyproject.toml'
        self.__target = self.__project_dir / 'requirements.txt'
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
        print(f"requirements.txt has been stored in {self.__project_dir}")


@click.command()
@click.argument('project_dir', default='.')
def main(project_dir):
    """
    @description: main function to perform the conversion
    """
    converter = RequirementsConverter(project_dir)
    converter.write_requirements()


if __name__ == '__main__':
    main()
