import ast
import inspect
import os
import re


def generate_markdown(file_path):
    # Read the Python script
    with open(file_path, 'r') as f:
        code = f.read()

    # Parse the code into an AST
    tree = ast.parse(code)

    # Get the classes, methods, and functions
    classes = []
    methods = []
    functions = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            classes.append(node)
        elif isinstance(node, ast.FunctionDef):
            functions.append(node)
        elif isinstance(node, ast.MethodDef):
            methods.append(node)

    # Generate the Markdown document
    markdown = ''
    for cls in classes:
        markdown += f'\n## Class {cls.name}\n\n'
        if cls.docstring:
            markdown += cls.docstring + '\n\n'
        for method in methods:
            if method.name.startswith(cls.name):
                markdown += f'### Method {method.name}\n\n'
                if method.docstring:
                    markdown += method.docstring + '\n\n'
    for function in functions:
        markdown += f'\n## Function {function.name}\n\n'
        if function.docstring:
            markdown += function.docstring + '\n\n'

    # Save the Markdown document
    base_name, _ = os.path.splitext(file_path)
    markdown_path = base_name + '.md'
    with open(markdown_path, 'w') as f:
        f.write(markdown)


# Example usage
file_path = 'monthinfo/monthinfo.py'
generate_markdown(file_path)
