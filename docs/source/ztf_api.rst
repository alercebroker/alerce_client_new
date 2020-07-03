ZTF API Access
====================

The ALeRCE ZTF API Wrapper gives an easy access to our database through the `ALeRCE ZTF API`_ service with Python.

.. _`ALeRCE ZTF API`: https://ztf.alerce.online

Usage
###########
.. code-block:: python

    from alerce.core import AlerceAPI
    alerce = AlerceAPI()

    dataframe = alerce.query_objects(
        classifier="light curve", 
        class_name="LPV", 
        format="pandas"
    )

Configuration
###################
By default the `AlerceAPI` object should be ready to use without any external configuration, but in case you need to adjust any parameters then you can configure the AlerceAPI object in different ways.

From object initialization
-----------------------------
You can pass parameters to the `AlerceAPI` class constructor to set the parameters for API connection.

.. code-block:: python

    alerce = AlerceAPI(ZTF_API_URL="https://ztf.alerce.online")

From a dictionary object
--------------------------
You can pass parameters to the `AlerceAPI` class from a dictionary object.

.. code-block:: python

    my_config = {
        "ZTF_API_URL": "https://ztf.alerce.online"
    }
    alerce = AlerceAPI()
    alerce.load_config_from_object(my_config)

From a config file
--------------------------
You can pass parameters to the `AlerceAPI` class from a file

Take for example a ``config.py`` file:

.. code-block:: python
    
    import os

    api_url = os.getenv("API_URL")
    AlerceAPIConfig = {
        "ZTF_API_URL": api_url
    }

Then you can initialize the client like this:

.. code-block:: python

    alerce = AlerceAPI()
    alerce.load_config_from_file("config.py")

ZTF API Documentation
------------------------
.. autoclass:: alerce.core.AlerceAPI
    :members: