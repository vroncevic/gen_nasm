Create Nasm project skeleton
------------------------------

**gen_nasm** is tool for creating Nasm project skeleton.

Developed in `python <https://www.python.org/>`_ code.

The README is used to introduce the tool and provide instructions on
how to install the tool, any machine dependencies it may have and any
other information that should be provided before the tool is installed.

|gen_nasm python checker| |gen_nasm python package| |github issues| |documentation status| |github contributors|

.. |gen_nasm python checker| image:: https://github.com/vroncevic/gen_nasm/actions/workflows/gen_nasm_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_nasm/actions/workflows/gen_nasm_python_checker.yml

.. |gen_nasm python package| image:: https://github.com/vroncevic/gen_nasm/actions/workflows/gen_nasm_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_nasm/actions/workflows/gen_nasm_package.yml

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/gen_nasm.svg
   :target: https://github.com/vroncevic/gen_nasm/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_nasm.svg
   :target: https://github.com/vroncevic/gen_nasm/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen-nasm/badge/?version=latest
   :target: https://gen-nasm.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

🚀 Installation
------------------

|gen_nasm python3 build| |gen_nasm interface checker| |gen_nasm isp checker| |gen_nasm srp checker|

.. |gen_nasm python3 build| image:: https://github.com/vroncevic/gen_nasm/actions/workflows/gen_nasm_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/gen_nasm/actions/workflows/gen_nasm_python3_build.yml

.. |gen_nasm interface checker| image:: https://github.com/vroncevic/gen_nasm/actions/workflows/gen_nasm_interface_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_nasm/actions/workflows/gen_nasm_interface_checker.yml

.. |gen_nasm isp checker| image:: https://github.com/vroncevic/gen_nasm/actions/workflows/gen_nasm_isp_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_nasm/actions/workflows/gen_nasm_isp_checker.yml

.. |gen_nasm srp checker| image:: https://github.com/vroncevic/gen_nasm/actions/workflows/gen_nasm_srp_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_nasm/actions/workflows/gen_nasm_srp_checker.yml


Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_nasm/releases

To install **gen_nasm** type the following

.. code-block:: bash

    tar xvzf gen_nasm-x.y.z.tar.gz
    cd gen_nasm-x.y.z/
    # python3
    wget https://bootstrap.pypa.io/get-pip.py
    python3 get-pip.py 
    python3 -m pip install --upgrade setuptools
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade build
    pip3 install -r requirements.txt
    python3 -m build --no-isolation --wheel
    pip3 install ./dist/gen_nasm-*-py3-none-any.whl
    rm -f get-pip.py

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    # python3
    pip3 install gen_nasm

📦 Dependencies
------------------

**gen_nasm** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

📁 Tool structure
-------------------

**gen_nasm** is based on OOP.

Tool structure

.. code-block:: bash

    gen_nasm/
         ├── core/
         │   ├── __init__.py
         │   ├── model/
         │   │   ├── __init__.py
         │   │   └── project_setup.py
         │   └── service/
         │       ├── engine.py
         │       ├── __init__.py
         │       ├── iservice.py
         │       └── isubprocessor.py
         ├── engine.py
         ├── infrastructure/
         │   ├── cli/
         │   │   ├── engine.py
         │   │   ├── icli.py
         │   │   ├── __init__.py
         │   │   └── setup/
         │   │       ├── bundle.py
         │   │       ├── dep_validator.py
         │   │       ├── dependencies.py
         │   │       ├── factory.py
         │   │       ├── __init__.py
         │   │       ├── keys.py
         │   │       ├── opt_validator.py
         │   │       ├── options.py
         │   │       ├── registry.py
         │   │       └── validator.py
         │   ├── command/
         │   │   ├── command.py
         │   │   ├── gen_nasm_command_definition.py
         │   │   ├── gen_nasm_command_executor.py
         │   │   ├── icommand_definition.py
         │   │   ├── icommand_executor.py
         │   │   └── __init__.py
         │   ├── config/
         │   │   ├── gen_nasm.cfg
         │   │   ├── gen_nasm.logo
         │   │   ├── scheme.json
         │   │   └── templates.tgz
         │   └── subprocessor.py
         ├── __init__.py
         ├── py.typed
         └── setup/
             ├── bundle.py
             ├── dep_validator.py
             ├── dependencies.py
             ├── factory.py
             ├── __init__.py
             ├── keys.py
             ├── opt_validator.py
             ├── options.py
             ├── registry.py
             └── validator.py

     10 directories, 44 files

✨ Features
--------------

* Automatically scaffolds Nasm assembly projects with build/make files.
* Provides a modular and extensible architecture based on OOP and SOLID principles.
* Includes command line interface (CLI) support via a command/executor structure.
* Robust validation of project bundles, dependencies, and options.
* Comes with configurable templates and JSON schema definitions.
* High code quality with full type checking and 100% unit test coverage.

📊 Code coverage
------------------

.. csv-table:: Code coverage
   :file: coverage_table.csv
   :widths: 60, 10, 10, 20
   :header-rows: 1

🛠 Usage
-----------

Install package

.. code-block:: bash

    pip3 install gen_nasm

Prepare main entry point by downloading `main.py` or create your own.

.. code-block:: bash

    wget -O main.py https://raw.githubusercontent.com/vroncevic/gen_nasm/main/main.py

Running tool for creating new Nasm project skeleton

.. code-block:: bash

    python3 main.py create --name mytool --output ./demo/

📚 Docs
---------

More documentation and info at

* `gen_nasm.readthedocs.io <https://gen-nasm.readthedocs.io>`_
* `www.python.org <https://www.python.org/>`_

👥 Contributing
-----------------

`Contributing to gen_nasm <https://github.com/vroncevic/gen_nasm/blob/dev/CONTRIBUTING.md>`_

📄 Copyright and licence
---------------------------

|license gpl v3| |license apache 2.0|

Copyright (C) 2025 - 2026 by `vroncevic.github.io/gen_nasm <https://vroncevic.github.io/gen_nasm>`_

**gen_nasm** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|python software foundation|

|donate|

.. |license gpl v3| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_nasm/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

.. |donate| image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
   :target: https://www.python.org/psf/donations/
