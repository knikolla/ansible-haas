import ast
import pytest
import subprocess

project1 = 'foo'


class TestCLI:
    def test_add_list_delete_projects(self):
        output = subprocess.check_output(['haas', 'list_projects'])
        projects = ast.literal_eval(output)
        size = len(projects)

        subprocess.check_call(['haas', 'project_create', project1])
        output = subprocess.check_output(['haas', 'list_projects'])
        projects = ast.literal_eval(output)
        assert project1 in projects
        assert len(projects) == size + 1

        subprocess.check_call(['haas', 'project_delete', project1])
        output = subprocess.check_output(['haas', 'list_projects'])
        projects = ast.literal_eval(output)
        assert project1 not in projects
        assert len(projects) == size
