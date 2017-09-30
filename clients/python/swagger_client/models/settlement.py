# coding: utf-8

"""
    BitMEX API

    ## REST API for the BitMEX Trading Platform  [View Changelog](/app/apiChangelog)    #### Getting Started   ##### Fetching Data  All REST endpoints are documented below. You can try out any query right from this interface.  Most table queries accept `count`, `start`, and `reverse` params. Set `reverse=true` to get rows newest-first.  Additional documentation regarding filters, timestamps, and authentication is available in [the main API documentation](https://www.bitmex.com/app/restAPI).  *All* table data is available via the [Websocket](/app/wsAPI). We highly recommend using the socket if you want to have the quickest possible data without being subject to ratelimits.  ##### Return Types  By default, all data is returned as JSON. Send `?_format=csv` to get CSV data or `?_format=xml` to get XML data.  ##### Trade Data Queries  *This is only a small subset of what is available, to get you started.*  Fill in the parameters and click the `Try it out!` button to try any of these queries.  * [Pricing Data](#!/Quote/Quote_get)  * [Trade Data](#!/Trade/Trade_get)  * [OrderBook Data](#!/OrderBook/OrderBook_getL2)  * [Settlement Data](#!/Settlement/Settlement_get)  * [Exchange Statistics](#!/Stats/Stats_history)  Every function of the BitMEX.com platform is exposed here and documented. Many more functions are available.  ##### Swagger Specification  [⇩ Download Swagger JSON](swagger.json)    ## All API Endpoints  Click to expand a section. 

    OpenAPI spec version: 1.2.0
    Contact: support@bitmex.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Settlement(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'timestamp': 'datetime',
        'symbol': 'str',
        'settlement_type': 'str',
        'settled_price': 'float',
        'bankrupt': 'float',
        'tax_base': 'float',
        'tax_rate': 'float'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'symbol': 'symbol',
        'settlement_type': 'settlementType',
        'settled_price': 'settledPrice',
        'bankrupt': 'bankrupt',
        'tax_base': 'taxBase',
        'tax_rate': 'taxRate'
    }

    def __init__(self, timestamp=None, symbol=None, settlement_type=None, settled_price=None, bankrupt=None, tax_base=None, tax_rate=None):
        """
        Settlement - a model defined in Swagger
        """

        self._timestamp = None
        self._symbol = None
        self._settlement_type = None
        self._settled_price = None
        self._bankrupt = None
        self._tax_base = None
        self._tax_rate = None
        self.discriminator = None

        self.timestamp = timestamp
        self.symbol = symbol
        if settlement_type is not None:
          self.settlement_type = settlement_type
        if settled_price is not None:
          self.settled_price = settled_price
        if bankrupt is not None:
          self.bankrupt = bankrupt
        if tax_base is not None:
          self.tax_base = tax_base
        if tax_rate is not None:
          self.tax_rate = tax_rate

    @property
    def timestamp(self):
        """
        Gets the timestamp of this Settlement.

        :return: The timestamp of this Settlement.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this Settlement.

        :param timestamp: The timestamp of this Settlement.
        :type: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")

        self._timestamp = timestamp

    @property
    def symbol(self):
        """
        Gets the symbol of this Settlement.

        :return: The symbol of this Settlement.
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """
        Sets the symbol of this Settlement.

        :param symbol: The symbol of this Settlement.
        :type: str
        """
        if symbol is None:
            raise ValueError("Invalid value for `symbol`, must not be `None`")

        self._symbol = symbol

    @property
    def settlement_type(self):
        """
        Gets the settlement_type of this Settlement.

        :return: The settlement_type of this Settlement.
        :rtype: str
        """
        return self._settlement_type

    @settlement_type.setter
    def settlement_type(self, settlement_type):
        """
        Sets the settlement_type of this Settlement.

        :param settlement_type: The settlement_type of this Settlement.
        :type: str
        """

        self._settlement_type = settlement_type

    @property
    def settled_price(self):
        """
        Gets the settled_price of this Settlement.

        :return: The settled_price of this Settlement.
        :rtype: float
        """
        return self._settled_price

    @settled_price.setter
    def settled_price(self, settled_price):
        """
        Sets the settled_price of this Settlement.

        :param settled_price: The settled_price of this Settlement.
        :type: float
        """

        self._settled_price = settled_price

    @property
    def bankrupt(self):
        """
        Gets the bankrupt of this Settlement.

        :return: The bankrupt of this Settlement.
        :rtype: float
        """
        return self._bankrupt

    @bankrupt.setter
    def bankrupt(self, bankrupt):
        """
        Sets the bankrupt of this Settlement.

        :param bankrupt: The bankrupt of this Settlement.
        :type: float
        """

        self._bankrupt = bankrupt

    @property
    def tax_base(self):
        """
        Gets the tax_base of this Settlement.

        :return: The tax_base of this Settlement.
        :rtype: float
        """
        return self._tax_base

    @tax_base.setter
    def tax_base(self, tax_base):
        """
        Sets the tax_base of this Settlement.

        :param tax_base: The tax_base of this Settlement.
        :type: float
        """

        self._tax_base = tax_base

    @property
    def tax_rate(self):
        """
        Gets the tax_rate of this Settlement.

        :return: The tax_rate of this Settlement.
        :rtype: float
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        """
        Sets the tax_rate of this Settlement.

        :param tax_rate: The tax_rate of this Settlement.
        :type: float
        """

        self._tax_rate = tax_rate

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Settlement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
