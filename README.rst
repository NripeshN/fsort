=======================================
 Function Sorting Hook for Python Code
=======================================

Introduction
============
This project introduces a pre-commit hook named `fsort`, which is designed to 
rearrange Python functions and classes in a logical order. It ensures that your
Python code is structured in a way that enhances readability and maintainability.

The `fsort` hook uses advanced techniques, including dependency graphs, to 
analyze the relationships between different parts of the code. It then rearranges
the elements, such as imports, class definitions, function definitions, and 
assignments, based on these relationships.

Installation
============
To use `fsort`, you need to have `pre-commit` installed in your Python environment.
If you don't have `pre-commit` installed, you can install it using pip:

.. code-block:: bash

    pip install pre-commit

Then, add the following lines to your `.pre-commit-config.yaml` file:

.. code:: yaml

    - repos:
        - repo: https://github.com/unifyai/lint-hook
          rev: main
          hooks:
            - id: fsort

Usage
=====
Once you have added `fsort` to your pre-commit configuration, it will automatically
run whenever you commit your changes. `fsort` will analyze your Python files and 
rearrange the functions and classes as per the logical ordering defined in its 
algorithm.

To manually run `fsort` on all files in the repository, you can use:

.. code-block:: bash

    pre-commit run fsort --all-files

Contributing
============
Contributions to `fsort` are welcome! If you have suggestions for improvements or 
want to contribute code, please feel free to open an issue or a pull request on our 
GitHub repository.