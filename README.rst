=======
Abathur
=======

.. image:: https://travis-ci.org/yeyuexia/abathur.svg?branch=master
   :target: https://travis-ci.org/yeyuexia/abathur

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

Presume you have a template like this::

  template/src
  ├── main
  │   ├── java
  │   │   └── com
  │   │       └── abathur
  │   │           └── {PROJECT_NAME}
  │   │               └── {PROJECT_NAME_IN_CLASS}Application.java
  │   │                   ├── domain
  │   │                   │   ├── entity
  │   │                   │   │   └── {PROJECT_NAME_IN_CLASS}.java
  │   │                   │   ├── repository
  │   │                   │   │   └── {PROJECT_NAME_IN_CLASS}Repository.java
  │   │                   │   └── service
  │   │                   │       └── {PROJECT_NAME_IN_CLASS}Service.java
  │   │                   ├── facade
  │   │                   │   ├── {PROJECT_NAME_IN_CLASS}DtoMapper.java
  │   │                   │   └── {PROJECT_NAME_IN_CLASS}Facade.java
  │   │                   ├── infrastructure
  │   │                   │   └── persistence
  │   │                   │       ├── {PROJECT_NAME_IN_CLASS}Po.java
  │   │                   │       └── {PROJECT_NAME_IN_CLASS}Repository.java
  │   │                   └── resource
  │   │                      └── {PROJECT_NAME_IN_CLASS}Resource.java
  │   └── resources
  │       └── application.yml
  └── test
      ├── java
      │   └── com
      │       └── abathur
      │           └── {PROJECT_NAME}
      │               └── resource
      │                   └── {PROJECT_NAME_IN_CLASS}ResourceTest.java
      └── resources


You can put all placeholders surrounding with {} like {PROJECT_NAME} and {PROJECT_NAME_IN_CLASS} in the file sources and directory, you can write a file named `.abathur` in the root path like::

  cat .abathur
  PROJECT_NAME_IN_CLASS
  TABLE_NAME

`.abathur` include all keywords used in template and split with \n, abathur will load it and surround the with {}(Abathur would auto add `PROJECT_NAME` into keyword list), then

Create alias::

  abathur add alias ~/template


Build project based on template::

  abathur build -a name project_name

When build project, abathur will let user fix replace the words notified in `.abathur` and replace the placeholders in template.

* You can use --output special the project path.

* You can use --config special a config file auto fill replaceholders

List aliases::

  abathur list

Remove alias::

  abathur remove alias
