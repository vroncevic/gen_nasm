# Create nasm project skeleton

<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_nasm/dev/docs/gen_nasm_logo.png" width="25%">

**gen_nasm** is tool for creating nasm project skeleton.

Developed in **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![gen_nasm python checker](https://github.com/vroncevic/gen_nasm/actions/workflows/gen_nasm_python_checker.yml/badge.svg)](https://github.com/vroncevic/gen_nasm/actions/workflows/gen_nasm_python_checker.yml) [![gen_nasm package checker](https://github.com/vroncevic/gen_nasm/actions/workflows/gen_nasm_package_checker.yml/badge.svg)](https://github.com/vroncevic/gen_nasm/actions/workflows/gen_nasm_package.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_nasm.svg)](https://github.com/vroncevic/gen_nasm/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_nasm.svg)](https://github.com/vroncevic/gen_nasm/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Tool structure](#tool-structure)
- [Docs](#docs)
- [Contributing](#contributing)
- [Copyright and Licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Used next development environment

![debian linux os](https://raw.githubusercontent.com/vroncevic/gen_nasm/dev/docs/debtux.png)

[![gen_nasm python3 build](https://github.com/vroncevic/gen_nasm/actions/workflows/gen_nasm_python3_build.yml/badge.svg)](https://github.com/vroncevic/gen_nasm/actions/workflows/gen_nasm_python3_build.yml)

Currently there are four ways to install framework
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

Python is located at **[pypi.org](https://pypi.org/project/gen_nasm/)**.

You can install by using pip

```bash
#python3
pip3 install gen_nasm
```

##### Install using build

Navigate to **[release page](https://github.com/vroncevic/gen_nasm/releases)** download and extract release archive.

To install **gen-nasm** run

```bash
tar xvzf gen-nasm-x.y.z.tar.gz
cd gen-nasm-x.y.z
# python3
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py 
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
pip3 install -r requirements.txt
python3 -m build -s --no-isolation --wheel
pip3 install dist/gen-nasm-x.y.z-py3-none-any.whl
rm -f get-pip.py
```

##### Install using py setup

Navigate to release **[page](https://github.com/vroncevic/gen_nasm/releases/)** download and extract release archive.

To install **gen_nasm** type the following

```bash
tar xvzf gen_nasm-x.y.z.tar.gz
cd gen_nasm-x.y.z/
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_data
python3 setup.py install_egg_info
```

##### Install using docker

You can use Dockerfile to create image/container.

### Dependencies

**gen_nasm** requires next modules and libraries

* [ats-utilities - Python App/Tool/Script Utilities](https://vroncevic.github.io/gen_nasm)

### Tool structure

**gen_nasm** is based on OOP

Generator structure

```bash
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
```

### Code coverage

| Name | Stmts | Miss | Cover |
|------|-------|------|-------|
| `gen_nasm/__init__.py` | 71 | 12 | 83% |
| `gen_nasm/pro/__init__.py` | 59 | 2 | 97% |
| `gen_nasm/pro/read_template.py` | 53 | 2 | 96% |
| `gen_nasm/pro/write_template.py` | 60 | 3 | 95% |
| **Total** | 243 | 19 | 92% |

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen_nasm/badge/?version=latest)](https://gen-nasm.readthedocs.io/en/latest/?badge=latest)

More documentation and info at

* [gen_nasm.readthedocs.io](https://gen-nasm.readthedocs.io)
* [www.python.org](https://www.python.org/)

### Contributing

[Contributing to gen_nasm](CONTRIBUTING.md)

### Copyright and Licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2024 by [vroncevic.github.io/gen_nasm](https://vroncevic.github.io/gen_nasm/)

**gen_nasm** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_nasm/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)
