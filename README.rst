fsort pre-commit hook
==========================


Installation
------------
To install the pre-commit hooks, add this to your `.pre-commit-config.yaml`:

.. code-block:: yaml

    - repos:
        - repo: https://github.com/NripeshN/fsort
            rev: main
            hooks:
            - id: fsort
