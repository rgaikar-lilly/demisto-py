# coding: utf-8

"""
    Demisto API

    This is the public REST API to integrate with the demisto server. HTTP request can be sent using any HTTP-client.  For an example dedicated client take a look at: https://github.com/demisto/demisto-py.  Requests must include API-key that can be generated in the Demisto web client under 'Settings' -> 'Integrations' -> 'API keys'   Optimistic Locking and Versioning\\:  When using Demisto REST API, you will need to make sure to work on the latest version of the item (incident, entry, etc.), otherwise, you will get a DB version error (which not allow you to override a newer item). In addition, you can pass 'version\\: -1' to force data override (make sure that other users data might be lost).  Assume that Alice and Bob both read the same data from Demisto server, then they both changed the data, and then both tried to write the new versions back to the server. Whose changes should be saved? Alice’s? Bob’s? To solve this, each data item in Demisto has a numeric incremental version. If Alice saved an item with version 4 and Bob trying to save the same item with version 3, Demisto will rollback Bob request and returns a DB version conflict error. Bob will need to get the latest item and work on it so Alice work will not get lost.  Example request using 'curl'\\:  ``` curl 'https://hostname:443/incidents/search' -H 'content-type: application/json' -H 'accept: application/json' -H 'Authorization: <API Key goes here>' --data-binary '{\"filter\":{\"query\":\"-status:closed -category:job\",\"period\":{\"by\":\"day\",\"fromValue\":7}}}' --compressed ```  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from demisto_client.demisto_api.models.arg_filter import ArgFilter  # noqa: F401,E501
from demisto_client.demisto_api.models.arg_transformer import ArgTransformer  # noqa: F401,E501


class ComplexArg(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'accessor': 'str',
        'filters': 'list[ArgFilter]',
        'root': 'str',
        'transformers': 'list[ArgTransformer]'
    }

    attribute_map = {
        'accessor': 'accessor',
        'filters': 'filters',
        'root': 'root',
        'transformers': 'transformers'
    }

    def __init__(self, accessor=None, filters=None, root=None, transformers=None):  # noqa: E501
        """ComplexArg - a model defined in Swagger"""  # noqa: E501

        self._accessor = None
        self._filters = None
        self._root = None
        self._transformers = None
        self.discriminator = None

        if accessor is not None:
            self.accessor = accessor
        if filters is not None:
            self.filters = filters
        if root is not None:
            self.root = root
        if transformers is not None:
            self.transformers = transformers

    @property
    def accessor(self):
        """Gets the accessor of this ComplexArg.  # noqa: E501


        :return: The accessor of this ComplexArg.  # noqa: E501
        :rtype: str
        """
        return self._accessor

    @accessor.setter
    def accessor(self, accessor):
        """Sets the accessor of this ComplexArg.


        :param accessor: The accessor of this ComplexArg.  # noqa: E501
        :type: str
        """

        self._accessor = accessor

    @property
    def filters(self):
        """Gets the filters of this ComplexArg.  # noqa: E501


        :return: The filters of this ComplexArg.  # noqa: E501
        :rtype: list[ArgFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this ComplexArg.


        :param filters: The filters of this ComplexArg.  # noqa: E501
        :type: list[ArgFilter]
        """

        self._filters = filters

    @property
    def root(self):
        """Gets the root of this ComplexArg.  # noqa: E501


        :return: The root of this ComplexArg.  # noqa: E501
        :rtype: str
        """
        return self._root

    @root.setter
    def root(self, root):
        """Sets the root of this ComplexArg.


        :param root: The root of this ComplexArg.  # noqa: E501
        :type: str
        """

        self._root = root

    @property
    def transformers(self):
        """Gets the transformers of this ComplexArg.  # noqa: E501


        :return: The transformers of this ComplexArg.  # noqa: E501
        :rtype: list[ArgTransformer]
        """
        return self._transformers

    @transformers.setter
    def transformers(self, transformers):
        """Sets the transformers of this ComplexArg.


        :param transformers: The transformers of this ComplexArg.  # noqa: E501
        :type: list[ArgTransformer]
        """

        self._transformers = transformers

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ComplexArg, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ComplexArg):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
