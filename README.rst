Welcome to Fabric Interface
===========================

This project is work in progress, there's no production-ready release available yet. Want to speed things up? This is an open-source project with a spare time budget. Donations are very welcome and will be used solely to improve Fabric Interface :-)


.. image:: https://travis-ci.org/Hedde/fabric_interface.svg?branch=develop
    :alt: status
    :scale: 100%
    :target: https://travis-ci.org/Hedde/fabric_interface

.. image:: http://img.shields.io/paypal/donate.png?color=blue
    :alt: paypal donate
    :scale: 100%
    :target: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=AU4TBGECBV7PN

Documentation for this repository can be found at readthedocs.org_

.. _readthedocs.org: http://fabric-interface.readthedocs.org/en/latest/


Quickstart
----------

1. Install::

    $ git clone https://github.com/Hedde/fabric_interface
    $ cd fabric_interface
    $ virtualenv venv
    $ . venv/bin/activate
    $ (venv)pip install -r requirements.txt

2. Migrate db::

    $ (venv)python manage.py migrate
    
3. Start Redis::

    $ redis-server  (or overwrite cache settings in a local_settings.py)

4. Run::

    $ (venv)python manage.py runserver


Screenshots
-----------

.. image:: http://s9.postimg.org/8bworvcov/example_2.jpg
    :alt: project screen
    :scale: 100%
    
.. image:: http://s23.postimg.org/gaaszcl17/example_1.jpg
    :alt: user permissions screen
    :scale: 100%
