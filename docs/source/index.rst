.. ALeRCE Python Client documentation master file, created by
   sphinx-quickstart on Fri Jul  3 10:37:29 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ALeRCE Python Client's documentation!
================================================
`ALeRCE <http://alerce.science>`_ client is a Python library to interact with ALeRCE services and databases.

Installing ALeRCE Client
========================

The ALeRCE client can be installed through pip with

.. code-block:: bash

    pip install alerce

Usage
===========
.. code-block:: python

    from alerce.core import Alerce
    alerce = Alerce()

    dataframe = alerce.query_objects(
        classifier="light curve", 
        class_name="LPV", 
        format="pandas"
    )

Configuration
==============
By default the `Alerce` object should be ready to use without any external configuration, but in case you need to adjust any parameters then you can configure the Alerce object in different ways.

From object initialization
-----------------------------
You can pass parameters to the `Alerce` class constructor to set the parameters for API connection.

.. code-block:: python

    alerce = Alerce(ZTF_API_URL="https://ztf.alerce.online")

From a dictionary object
--------------------------
You can pass parameters to the `Alerce` class from a dictionary object.

.. code-block:: python

    my_config = {
        "ZTF_API_URL": "https://ztf.alerce.online"
    }
    alerce = Alerce()
    alerce.load_config_from_object(my_config)

From a config file
--------------------------
You can pass parameters to the `Alerce` class from a file

Take for example a ``config.py`` file:

.. code-block:: python
    
    import os

    api_url = os.getenv("API_URL")
    AlerceAPIConfig = {
        "ZTF_API_URL": api_url
    }

Then you can initialize the client like this:

.. code-block:: python

    alerce = Alerce()
    alerce.load_config_from_file("config.py")


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   ztf_api


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
