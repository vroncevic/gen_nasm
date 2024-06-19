Create nasm project skeleton
-----------------------------

**gen_nasm** is tool for creating nasm project skeleton.

Developed in `python <https://www.python.org/>`_ code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

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

Installation
-------------

|gen_nasm python3 build|

.. |gen_nasm python3 build| image:: https://github.com/vroncevic/gen_nasm/actions/workflows/gen_nasm_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/gen_nasm/actions/workflows/gen_nasm_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_nasm/releases

To install this set of modules type the following

.. code-block:: bash

    tar xvzf gen_nasm-x.y.z.tar.gz
    cd gen_nasm-x.y.z
    #python3
    pip3 install -r requirements.txt
    python3 setup.py install_lib
    python3 setup.py install_egg_info
    python3 setup.py install_data

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    #python3
    pip3 install gen_nasm

Dependencies
-------------

**gen_nasm** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Tool structure
------------------

**gen_nasm** is based on OOP

Code structure

.. code-block:: bash

    gen_nasm/
        ├── conf/
        │   ├── gen_nasm.cfg
        │   ├── gen_nasm.logo
        │   ├── gen_nasm_util.cfg
        │   ├── project.yaml
        │   └── template/
        │       ├── asmflags.template
        │       ├── ldflags.template
        │       ├── main.template
        │       ├── makefile.template
        │       ├── objects.template
        │       └── sources.template
        ├── __init__.py
        ├── log/
        │   └── gen_nasm.log
        ├── pro/
        │   ├── __init__.py
        │   ├── read_template.py
        │   └── write_template.py
        ├── py.typed
        └── run/
            └── gen_nasm_run.py
    
    6 directories, 17 files

Copyright and licence
----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg
   :target: https://opensource.org/licenses/apache-2.0

Copyright (C) 2024 by `vroncevic.github.io/gen_nasm <https://vroncevic.github.io/gen_nasm>`_

**gen_nasm** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_nasm/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_us/i/btn/btn_donatecc_lg.gif
   :target: https://www.python.org/psf/donations/

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
