ZTF API Access
====================

The ALeRCE ZTF API Wrapper gives an easy access to our database through the `ALeRCE ZTF API`_ service with Python.

.. _`ALeRCE ZTF API`: https://ztf.alerce.online

Usage
###########
.. code-block:: python

    from alerce.core import Alerce
    alerce = Alerce()

    dataframe = alerce.query_objects(
        classifier="light curve", 
        class_name="LPV", 
        format="pandas"
    )

Configuration
###################
The available options and default values for ZTF API Client are:

.. code-block:: python

    "ZTF_API_URL": "http://3.212.59.238:8082",
    "ZTF_ROUTES": {
        "objects": "/objects",
        "single_object": "/objects/%s",
        "detections": "/objects/%s/detections",
        "non_detections": "/objects/%s/non_detections",
        "lightcurve": "/objects/%s/lightcurve",
        "magstats": "/objects/%s/magstats",
        "probabilities": "/objects/%s/probabilities"
    }

Making Queries
################
Making queries using the alerce client is easy. With your instance of `Alerce` class you have access to 
many methods that will allow you to make queries to one of the `ALeRCE ZTF API`_ routes.

For example, getting all the objects classified as LPV could be done like this:

.. code-block:: python

    from alerce.core import Alerce
    alerce = Alerce()

    dataframe = alerce.query_objects(
        classifier="light curve", 
        class_name="LPV",
        format="pandas"
    )

You can specify one of the following return formats: `pandas | votable | json` with json being the default.

There are other kind of queries, that are related to a specific object like *lightcurve*, *probabilities* and *magnitude statistics* queries. This queries require an object id to retrieve the data.

.. code-block:: python

    data = alerce.query_lightcurve("ZTF18abbuksn", format="json")

Notice that you can still specify a format.

Error Handling
##############
The ALeRCE Client has some useful error messages that you can manage when something goes wrong. If you specify a wrong search criteria or no objects were found with your query, then you will get one of the following errors:

- ZTFAPIError (code -1): this is the default error
- ParseError (code 400): this error is raised when there's an error with search parameters
- ObjectNotFoundError (code 404): this error is raised when no objects were returned in your query
- FormatValidationError (code 500): this error is raised when you set a not allowed return format

This errors usually give useful data on what you need to fix with your query.
In case you want to do something when an error happens you can capture the error as a regular python exception handling.

.. code-block:: python

    try:
        data = alerce.query_objects(**my_filters)
    except ObjectNotFoundError as e:
        print(e.message)
        # do something else

ZTF API Documentation
#####################
.. autoclass:: alerce.core.Alerce
    :members:
    :inherited-members: