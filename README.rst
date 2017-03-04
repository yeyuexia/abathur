=======
Abathur
=======

.. image:: https://travis-ci.org/yeyuexia/dummie.svg?branch=master
   :target: https://travis-ci.org/yeyuexia/dummie

Simple Template manager to manage template and create project based on template.

Requirements
------------

* Python 3.6+
* Works on Linux, Windows, Mac OSX, BSD

Install
-------

pip::

  pip install abathur

Usage
-----

Create alias::

  abathur alias name ~/template

* You can put a file named .abathur indicate placeholders split with \n, abathur will load it and surrend the with {}. When build project, abathur will let user fix replace words and replace the placeholders in template.

Build project based on template::

  abathur build -a name project_name


* You can use --output special the project path.

* You can use --config special a config file auto fill replaceholders
