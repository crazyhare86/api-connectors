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


class Execution(object):
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
        'exec_id': 'str',
        'order_id': 'str',
        'cl_ord_id': 'str',
        'cl_ord_link_id': 'str',
        'account': 'float',
        'symbol': 'str',
        'side': 'str',
        'last_qty': 'float',
        'last_px': 'float',
        'underlying_last_px': 'float',
        'last_mkt': 'str',
        'last_liquidity_ind': 'str',
        'simple_order_qty': 'float',
        'order_qty': 'float',
        'price': 'float',
        'display_qty': 'float',
        'stop_px': 'float',
        'peg_offset_value': 'float',
        'peg_price_type': 'str',
        'currency': 'str',
        'settl_currency': 'str',
        'exec_type': 'str',
        'ord_type': 'str',
        'time_in_force': 'str',
        'exec_inst': 'str',
        'contingency_type': 'str',
        'ex_destination': 'str',
        'ord_status': 'str',
        'triggered': 'str',
        'working_indicator': 'bool',
        'ord_rej_reason': 'str',
        'simple_leaves_qty': 'float',
        'leaves_qty': 'float',
        'simple_cum_qty': 'float',
        'cum_qty': 'float',
        'avg_px': 'float',
        'commission': 'float',
        'trade_publish_indicator': 'str',
        'multi_leg_reporting_type': 'str',
        'text': 'str',
        'trd_match_id': 'str',
        'exec_cost': 'float',
        'exec_comm': 'float',
        'home_notional': 'float',
        'foreign_notional': 'float',
        'transact_time': 'datetime',
        'timestamp': 'datetime'
    }

    attribute_map = {
        'exec_id': 'execID',
        'order_id': 'orderID',
        'cl_ord_id': 'clOrdID',
        'cl_ord_link_id': 'clOrdLinkID',
        'account': 'account',
        'symbol': 'symbol',
        'side': 'side',
        'last_qty': 'lastQty',
        'last_px': 'lastPx',
        'underlying_last_px': 'underlyingLastPx',
        'last_mkt': 'lastMkt',
        'last_liquidity_ind': 'lastLiquidityInd',
        'simple_order_qty': 'simpleOrderQty',
        'order_qty': 'orderQty',
        'price': 'price',
        'display_qty': 'displayQty',
        'stop_px': 'stopPx',
        'peg_offset_value': 'pegOffsetValue',
        'peg_price_type': 'pegPriceType',
        'currency': 'currency',
        'settl_currency': 'settlCurrency',
        'exec_type': 'execType',
        'ord_type': 'ordType',
        'time_in_force': 'timeInForce',
        'exec_inst': 'execInst',
        'contingency_type': 'contingencyType',
        'ex_destination': 'exDestination',
        'ord_status': 'ordStatus',
        'triggered': 'triggered',
        'working_indicator': 'workingIndicator',
        'ord_rej_reason': 'ordRejReason',
        'simple_leaves_qty': 'simpleLeavesQty',
        'leaves_qty': 'leavesQty',
        'simple_cum_qty': 'simpleCumQty',
        'cum_qty': 'cumQty',
        'avg_px': 'avgPx',
        'commission': 'commission',
        'trade_publish_indicator': 'tradePublishIndicator',
        'multi_leg_reporting_type': 'multiLegReportingType',
        'text': 'text',
        'trd_match_id': 'trdMatchID',
        'exec_cost': 'execCost',
        'exec_comm': 'execComm',
        'home_notional': 'homeNotional',
        'foreign_notional': 'foreignNotional',
        'transact_time': 'transactTime',
        'timestamp': 'timestamp'
    }

    def __init__(self, exec_id=None, order_id=None, cl_ord_id=None, cl_ord_link_id=None, account=None, symbol=None, side=None, last_qty=None, last_px=None, underlying_last_px=None, last_mkt=None, last_liquidity_ind=None, simple_order_qty=None, order_qty=None, price=None, display_qty=None, stop_px=None, peg_offset_value=None, peg_price_type=None, currency=None, settl_currency=None, exec_type=None, ord_type=None, time_in_force=None, exec_inst=None, contingency_type=None, ex_destination=None, ord_status=None, triggered=None, working_indicator=None, ord_rej_reason=None, simple_leaves_qty=None, leaves_qty=None, simple_cum_qty=None, cum_qty=None, avg_px=None, commission=None, trade_publish_indicator=None, multi_leg_reporting_type=None, text=None, trd_match_id=None, exec_cost=None, exec_comm=None, home_notional=None, foreign_notional=None, transact_time=None, timestamp=None):
        """
        Execution - a model defined in Swagger
        """

        self._exec_id = None
        self._order_id = None
        self._cl_ord_id = None
        self._cl_ord_link_id = None
        self._account = None
        self._symbol = None
        self._side = None
        self._last_qty = None
        self._last_px = None
        self._underlying_last_px = None
        self._last_mkt = None
        self._last_liquidity_ind = None
        self._simple_order_qty = None
        self._order_qty = None
        self._price = None
        self._display_qty = None
        self._stop_px = None
        self._peg_offset_value = None
        self._peg_price_type = None
        self._currency = None
        self._settl_currency = None
        self._exec_type = None
        self._ord_type = None
        self._time_in_force = None
        self._exec_inst = None
        self._contingency_type = None
        self._ex_destination = None
        self._ord_status = None
        self._triggered = None
        self._working_indicator = None
        self._ord_rej_reason = None
        self._simple_leaves_qty = None
        self._leaves_qty = None
        self._simple_cum_qty = None
        self._cum_qty = None
        self._avg_px = None
        self._commission = None
        self._trade_publish_indicator = None
        self._multi_leg_reporting_type = None
        self._text = None
        self._trd_match_id = None
        self._exec_cost = None
        self._exec_comm = None
        self._home_notional = None
        self._foreign_notional = None
        self._transact_time = None
        self._timestamp = None
        self.discriminator = None

        self.exec_id = exec_id
        if order_id is not None:
          self.order_id = order_id
        if cl_ord_id is not None:
          self.cl_ord_id = cl_ord_id
        if cl_ord_link_id is not None:
          self.cl_ord_link_id = cl_ord_link_id
        if account is not None:
          self.account = account
        if symbol is not None:
          self.symbol = symbol
        if side is not None:
          self.side = side
        if last_qty is not None:
          self.last_qty = last_qty
        if last_px is not None:
          self.last_px = last_px
        if underlying_last_px is not None:
          self.underlying_last_px = underlying_last_px
        if last_mkt is not None:
          self.last_mkt = last_mkt
        if last_liquidity_ind is not None:
          self.last_liquidity_ind = last_liquidity_ind
        if simple_order_qty is not None:
          self.simple_order_qty = simple_order_qty
        if order_qty is not None:
          self.order_qty = order_qty
        if price is not None:
          self.price = price
        if display_qty is not None:
          self.display_qty = display_qty
        if stop_px is not None:
          self.stop_px = stop_px
        if peg_offset_value is not None:
          self.peg_offset_value = peg_offset_value
        if peg_price_type is not None:
          self.peg_price_type = peg_price_type
        if currency is not None:
          self.currency = currency
        if settl_currency is not None:
          self.settl_currency = settl_currency
        if exec_type is not None:
          self.exec_type = exec_type
        if ord_type is not None:
          self.ord_type = ord_type
        if time_in_force is not None:
          self.time_in_force = time_in_force
        if exec_inst is not None:
          self.exec_inst = exec_inst
        if contingency_type is not None:
          self.contingency_type = contingency_type
        if ex_destination is not None:
          self.ex_destination = ex_destination
        if ord_status is not None:
          self.ord_status = ord_status
        if triggered is not None:
          self.triggered = triggered
        if working_indicator is not None:
          self.working_indicator = working_indicator
        if ord_rej_reason is not None:
          self.ord_rej_reason = ord_rej_reason
        if simple_leaves_qty is not None:
          self.simple_leaves_qty = simple_leaves_qty
        if leaves_qty is not None:
          self.leaves_qty = leaves_qty
        if simple_cum_qty is not None:
          self.simple_cum_qty = simple_cum_qty
        if cum_qty is not None:
          self.cum_qty = cum_qty
        if avg_px is not None:
          self.avg_px = avg_px
        if commission is not None:
          self.commission = commission
        if trade_publish_indicator is not None:
          self.trade_publish_indicator = trade_publish_indicator
        if multi_leg_reporting_type is not None:
          self.multi_leg_reporting_type = multi_leg_reporting_type
        if text is not None:
          self.text = text
        if trd_match_id is not None:
          self.trd_match_id = trd_match_id
        if exec_cost is not None:
          self.exec_cost = exec_cost
        if exec_comm is not None:
          self.exec_comm = exec_comm
        if home_notional is not None:
          self.home_notional = home_notional
        if foreign_notional is not None:
          self.foreign_notional = foreign_notional
        if transact_time is not None:
          self.transact_time = transact_time
        if timestamp is not None:
          self.timestamp = timestamp

    @property
    def exec_id(self):
        """
        Gets the exec_id of this Execution.

        :return: The exec_id of this Execution.
        :rtype: str
        """
        return self._exec_id

    @exec_id.setter
    def exec_id(self, exec_id):
        """
        Sets the exec_id of this Execution.

        :param exec_id: The exec_id of this Execution.
        :type: str
        """
        if exec_id is None:
            raise ValueError("Invalid value for `exec_id`, must not be `None`")

        self._exec_id = exec_id

    @property
    def order_id(self):
        """
        Gets the order_id of this Execution.

        :return: The order_id of this Execution.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """
        Sets the order_id of this Execution.

        :param order_id: The order_id of this Execution.
        :type: str
        """

        self._order_id = order_id

    @property
    def cl_ord_id(self):
        """
        Gets the cl_ord_id of this Execution.

        :return: The cl_ord_id of this Execution.
        :rtype: str
        """
        return self._cl_ord_id

    @cl_ord_id.setter
    def cl_ord_id(self, cl_ord_id):
        """
        Sets the cl_ord_id of this Execution.

        :param cl_ord_id: The cl_ord_id of this Execution.
        :type: str
        """

        self._cl_ord_id = cl_ord_id

    @property
    def cl_ord_link_id(self):
        """
        Gets the cl_ord_link_id of this Execution.

        :return: The cl_ord_link_id of this Execution.
        :rtype: str
        """
        return self._cl_ord_link_id

    @cl_ord_link_id.setter
    def cl_ord_link_id(self, cl_ord_link_id):
        """
        Sets the cl_ord_link_id of this Execution.

        :param cl_ord_link_id: The cl_ord_link_id of this Execution.
        :type: str
        """

        self._cl_ord_link_id = cl_ord_link_id

    @property
    def account(self):
        """
        Gets the account of this Execution.

        :return: The account of this Execution.
        :rtype: float
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this Execution.

        :param account: The account of this Execution.
        :type: float
        """

        self._account = account

    @property
    def symbol(self):
        """
        Gets the symbol of this Execution.

        :return: The symbol of this Execution.
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """
        Sets the symbol of this Execution.

        :param symbol: The symbol of this Execution.
        :type: str
        """

        self._symbol = symbol

    @property
    def side(self):
        """
        Gets the side of this Execution.

        :return: The side of this Execution.
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """
        Sets the side of this Execution.

        :param side: The side of this Execution.
        :type: str
        """

        self._side = side

    @property
    def last_qty(self):
        """
        Gets the last_qty of this Execution.

        :return: The last_qty of this Execution.
        :rtype: float
        """
        return self._last_qty

    @last_qty.setter
    def last_qty(self, last_qty):
        """
        Sets the last_qty of this Execution.

        :param last_qty: The last_qty of this Execution.
        :type: float
        """

        self._last_qty = last_qty

    @property
    def last_px(self):
        """
        Gets the last_px of this Execution.

        :return: The last_px of this Execution.
        :rtype: float
        """
        return self._last_px

    @last_px.setter
    def last_px(self, last_px):
        """
        Sets the last_px of this Execution.

        :param last_px: The last_px of this Execution.
        :type: float
        """

        self._last_px = last_px

    @property
    def underlying_last_px(self):
        """
        Gets the underlying_last_px of this Execution.

        :return: The underlying_last_px of this Execution.
        :rtype: float
        """
        return self._underlying_last_px

    @underlying_last_px.setter
    def underlying_last_px(self, underlying_last_px):
        """
        Sets the underlying_last_px of this Execution.

        :param underlying_last_px: The underlying_last_px of this Execution.
        :type: float
        """

        self._underlying_last_px = underlying_last_px

    @property
    def last_mkt(self):
        """
        Gets the last_mkt of this Execution.

        :return: The last_mkt of this Execution.
        :rtype: str
        """
        return self._last_mkt

    @last_mkt.setter
    def last_mkt(self, last_mkt):
        """
        Sets the last_mkt of this Execution.

        :param last_mkt: The last_mkt of this Execution.
        :type: str
        """

        self._last_mkt = last_mkt

    @property
    def last_liquidity_ind(self):
        """
        Gets the last_liquidity_ind of this Execution.

        :return: The last_liquidity_ind of this Execution.
        :rtype: str
        """
        return self._last_liquidity_ind

    @last_liquidity_ind.setter
    def last_liquidity_ind(self, last_liquidity_ind):
        """
        Sets the last_liquidity_ind of this Execution.

        :param last_liquidity_ind: The last_liquidity_ind of this Execution.
        :type: str
        """

        self._last_liquidity_ind = last_liquidity_ind

    @property
    def simple_order_qty(self):
        """
        Gets the simple_order_qty of this Execution.

        :return: The simple_order_qty of this Execution.
        :rtype: float
        """
        return self._simple_order_qty

    @simple_order_qty.setter
    def simple_order_qty(self, simple_order_qty):
        """
        Sets the simple_order_qty of this Execution.

        :param simple_order_qty: The simple_order_qty of this Execution.
        :type: float
        """

        self._simple_order_qty = simple_order_qty

    @property
    def order_qty(self):
        """
        Gets the order_qty of this Execution.

        :return: The order_qty of this Execution.
        :rtype: float
        """
        return self._order_qty

    @order_qty.setter
    def order_qty(self, order_qty):
        """
        Sets the order_qty of this Execution.

        :param order_qty: The order_qty of this Execution.
        :type: float
        """

        self._order_qty = order_qty

    @property
    def price(self):
        """
        Gets the price of this Execution.

        :return: The price of this Execution.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this Execution.

        :param price: The price of this Execution.
        :type: float
        """

        self._price = price

    @property
    def display_qty(self):
        """
        Gets the display_qty of this Execution.

        :return: The display_qty of this Execution.
        :rtype: float
        """
        return self._display_qty

    @display_qty.setter
    def display_qty(self, display_qty):
        """
        Sets the display_qty of this Execution.

        :param display_qty: The display_qty of this Execution.
        :type: float
        """

        self._display_qty = display_qty

    @property
    def stop_px(self):
        """
        Gets the stop_px of this Execution.

        :return: The stop_px of this Execution.
        :rtype: float
        """
        return self._stop_px

    @stop_px.setter
    def stop_px(self, stop_px):
        """
        Sets the stop_px of this Execution.

        :param stop_px: The stop_px of this Execution.
        :type: float
        """

        self._stop_px = stop_px

    @property
    def peg_offset_value(self):
        """
        Gets the peg_offset_value of this Execution.

        :return: The peg_offset_value of this Execution.
        :rtype: float
        """
        return self._peg_offset_value

    @peg_offset_value.setter
    def peg_offset_value(self, peg_offset_value):
        """
        Sets the peg_offset_value of this Execution.

        :param peg_offset_value: The peg_offset_value of this Execution.
        :type: float
        """

        self._peg_offset_value = peg_offset_value

    @property
    def peg_price_type(self):
        """
        Gets the peg_price_type of this Execution.

        :return: The peg_price_type of this Execution.
        :rtype: str
        """
        return self._peg_price_type

    @peg_price_type.setter
    def peg_price_type(self, peg_price_type):
        """
        Sets the peg_price_type of this Execution.

        :param peg_price_type: The peg_price_type of this Execution.
        :type: str
        """

        self._peg_price_type = peg_price_type

    @property
    def currency(self):
        """
        Gets the currency of this Execution.

        :return: The currency of this Execution.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this Execution.

        :param currency: The currency of this Execution.
        :type: str
        """

        self._currency = currency

    @property
    def settl_currency(self):
        """
        Gets the settl_currency of this Execution.

        :return: The settl_currency of this Execution.
        :rtype: str
        """
        return self._settl_currency

    @settl_currency.setter
    def settl_currency(self, settl_currency):
        """
        Sets the settl_currency of this Execution.

        :param settl_currency: The settl_currency of this Execution.
        :type: str
        """

        self._settl_currency = settl_currency

    @property
    def exec_type(self):
        """
        Gets the exec_type of this Execution.

        :return: The exec_type of this Execution.
        :rtype: str
        """
        return self._exec_type

    @exec_type.setter
    def exec_type(self, exec_type):
        """
        Sets the exec_type of this Execution.

        :param exec_type: The exec_type of this Execution.
        :type: str
        """

        self._exec_type = exec_type

    @property
    def ord_type(self):
        """
        Gets the ord_type of this Execution.

        :return: The ord_type of this Execution.
        :rtype: str
        """
        return self._ord_type

    @ord_type.setter
    def ord_type(self, ord_type):
        """
        Sets the ord_type of this Execution.

        :param ord_type: The ord_type of this Execution.
        :type: str
        """

        self._ord_type = ord_type

    @property
    def time_in_force(self):
        """
        Gets the time_in_force of this Execution.

        :return: The time_in_force of this Execution.
        :rtype: str
        """
        return self._time_in_force

    @time_in_force.setter
    def time_in_force(self, time_in_force):
        """
        Sets the time_in_force of this Execution.

        :param time_in_force: The time_in_force of this Execution.
        :type: str
        """

        self._time_in_force = time_in_force

    @property
    def exec_inst(self):
        """
        Gets the exec_inst of this Execution.

        :return: The exec_inst of this Execution.
        :rtype: str
        """
        return self._exec_inst

    @exec_inst.setter
    def exec_inst(self, exec_inst):
        """
        Sets the exec_inst of this Execution.

        :param exec_inst: The exec_inst of this Execution.
        :type: str
        """

        self._exec_inst = exec_inst

    @property
    def contingency_type(self):
        """
        Gets the contingency_type of this Execution.

        :return: The contingency_type of this Execution.
        :rtype: str
        """
        return self._contingency_type

    @contingency_type.setter
    def contingency_type(self, contingency_type):
        """
        Sets the contingency_type of this Execution.

        :param contingency_type: The contingency_type of this Execution.
        :type: str
        """

        self._contingency_type = contingency_type

    @property
    def ex_destination(self):
        """
        Gets the ex_destination of this Execution.

        :return: The ex_destination of this Execution.
        :rtype: str
        """
        return self._ex_destination

    @ex_destination.setter
    def ex_destination(self, ex_destination):
        """
        Sets the ex_destination of this Execution.

        :param ex_destination: The ex_destination of this Execution.
        :type: str
        """

        self._ex_destination = ex_destination

    @property
    def ord_status(self):
        """
        Gets the ord_status of this Execution.

        :return: The ord_status of this Execution.
        :rtype: str
        """
        return self._ord_status

    @ord_status.setter
    def ord_status(self, ord_status):
        """
        Sets the ord_status of this Execution.

        :param ord_status: The ord_status of this Execution.
        :type: str
        """

        self._ord_status = ord_status

    @property
    def triggered(self):
        """
        Gets the triggered of this Execution.

        :return: The triggered of this Execution.
        :rtype: str
        """
        return self._triggered

    @triggered.setter
    def triggered(self, triggered):
        """
        Sets the triggered of this Execution.

        :param triggered: The triggered of this Execution.
        :type: str
        """

        self._triggered = triggered

    @property
    def working_indicator(self):
        """
        Gets the working_indicator of this Execution.

        :return: The working_indicator of this Execution.
        :rtype: bool
        """
        return self._working_indicator

    @working_indicator.setter
    def working_indicator(self, working_indicator):
        """
        Sets the working_indicator of this Execution.

        :param working_indicator: The working_indicator of this Execution.
        :type: bool
        """

        self._working_indicator = working_indicator

    @property
    def ord_rej_reason(self):
        """
        Gets the ord_rej_reason of this Execution.

        :return: The ord_rej_reason of this Execution.
        :rtype: str
        """
        return self._ord_rej_reason

    @ord_rej_reason.setter
    def ord_rej_reason(self, ord_rej_reason):
        """
        Sets the ord_rej_reason of this Execution.

        :param ord_rej_reason: The ord_rej_reason of this Execution.
        :type: str
        """

        self._ord_rej_reason = ord_rej_reason

    @property
    def simple_leaves_qty(self):
        """
        Gets the simple_leaves_qty of this Execution.

        :return: The simple_leaves_qty of this Execution.
        :rtype: float
        """
        return self._simple_leaves_qty

    @simple_leaves_qty.setter
    def simple_leaves_qty(self, simple_leaves_qty):
        """
        Sets the simple_leaves_qty of this Execution.

        :param simple_leaves_qty: The simple_leaves_qty of this Execution.
        :type: float
        """

        self._simple_leaves_qty = simple_leaves_qty

    @property
    def leaves_qty(self):
        """
        Gets the leaves_qty of this Execution.

        :return: The leaves_qty of this Execution.
        :rtype: float
        """
        return self._leaves_qty

    @leaves_qty.setter
    def leaves_qty(self, leaves_qty):
        """
        Sets the leaves_qty of this Execution.

        :param leaves_qty: The leaves_qty of this Execution.
        :type: float
        """

        self._leaves_qty = leaves_qty

    @property
    def simple_cum_qty(self):
        """
        Gets the simple_cum_qty of this Execution.

        :return: The simple_cum_qty of this Execution.
        :rtype: float
        """
        return self._simple_cum_qty

    @simple_cum_qty.setter
    def simple_cum_qty(self, simple_cum_qty):
        """
        Sets the simple_cum_qty of this Execution.

        :param simple_cum_qty: The simple_cum_qty of this Execution.
        :type: float
        """

        self._simple_cum_qty = simple_cum_qty

    @property
    def cum_qty(self):
        """
        Gets the cum_qty of this Execution.

        :return: The cum_qty of this Execution.
        :rtype: float
        """
        return self._cum_qty

    @cum_qty.setter
    def cum_qty(self, cum_qty):
        """
        Sets the cum_qty of this Execution.

        :param cum_qty: The cum_qty of this Execution.
        :type: float
        """

        self._cum_qty = cum_qty

    @property
    def avg_px(self):
        """
        Gets the avg_px of this Execution.

        :return: The avg_px of this Execution.
        :rtype: float
        """
        return self._avg_px

    @avg_px.setter
    def avg_px(self, avg_px):
        """
        Sets the avg_px of this Execution.

        :param avg_px: The avg_px of this Execution.
        :type: float
        """

        self._avg_px = avg_px

    @property
    def commission(self):
        """
        Gets the commission of this Execution.

        :return: The commission of this Execution.
        :rtype: float
        """
        return self._commission

    @commission.setter
    def commission(self, commission):
        """
        Sets the commission of this Execution.

        :param commission: The commission of this Execution.
        :type: float
        """

        self._commission = commission

    @property
    def trade_publish_indicator(self):
        """
        Gets the trade_publish_indicator of this Execution.

        :return: The trade_publish_indicator of this Execution.
        :rtype: str
        """
        return self._trade_publish_indicator

    @trade_publish_indicator.setter
    def trade_publish_indicator(self, trade_publish_indicator):
        """
        Sets the trade_publish_indicator of this Execution.

        :param trade_publish_indicator: The trade_publish_indicator of this Execution.
        :type: str
        """

        self._trade_publish_indicator = trade_publish_indicator

    @property
    def multi_leg_reporting_type(self):
        """
        Gets the multi_leg_reporting_type of this Execution.

        :return: The multi_leg_reporting_type of this Execution.
        :rtype: str
        """
        return self._multi_leg_reporting_type

    @multi_leg_reporting_type.setter
    def multi_leg_reporting_type(self, multi_leg_reporting_type):
        """
        Sets the multi_leg_reporting_type of this Execution.

        :param multi_leg_reporting_type: The multi_leg_reporting_type of this Execution.
        :type: str
        """

        self._multi_leg_reporting_type = multi_leg_reporting_type

    @property
    def text(self):
        """
        Gets the text of this Execution.

        :return: The text of this Execution.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this Execution.

        :param text: The text of this Execution.
        :type: str
        """

        self._text = text

    @property
    def trd_match_id(self):
        """
        Gets the trd_match_id of this Execution.

        :return: The trd_match_id of this Execution.
        :rtype: str
        """
        return self._trd_match_id

    @trd_match_id.setter
    def trd_match_id(self, trd_match_id):
        """
        Sets the trd_match_id of this Execution.

        :param trd_match_id: The trd_match_id of this Execution.
        :type: str
        """

        self._trd_match_id = trd_match_id

    @property
    def exec_cost(self):
        """
        Gets the exec_cost of this Execution.

        :return: The exec_cost of this Execution.
        :rtype: float
        """
        return self._exec_cost

    @exec_cost.setter
    def exec_cost(self, exec_cost):
        """
        Sets the exec_cost of this Execution.

        :param exec_cost: The exec_cost of this Execution.
        :type: float
        """

        self._exec_cost = exec_cost

    @property
    def exec_comm(self):
        """
        Gets the exec_comm of this Execution.

        :return: The exec_comm of this Execution.
        :rtype: float
        """
        return self._exec_comm

    @exec_comm.setter
    def exec_comm(self, exec_comm):
        """
        Sets the exec_comm of this Execution.

        :param exec_comm: The exec_comm of this Execution.
        :type: float
        """

        self._exec_comm = exec_comm

    @property
    def home_notional(self):
        """
        Gets the home_notional of this Execution.

        :return: The home_notional of this Execution.
        :rtype: float
        """
        return self._home_notional

    @home_notional.setter
    def home_notional(self, home_notional):
        """
        Sets the home_notional of this Execution.

        :param home_notional: The home_notional of this Execution.
        :type: float
        """

        self._home_notional = home_notional

    @property
    def foreign_notional(self):
        """
        Gets the foreign_notional of this Execution.

        :return: The foreign_notional of this Execution.
        :rtype: float
        """
        return self._foreign_notional

    @foreign_notional.setter
    def foreign_notional(self, foreign_notional):
        """
        Sets the foreign_notional of this Execution.

        :param foreign_notional: The foreign_notional of this Execution.
        :type: float
        """

        self._foreign_notional = foreign_notional

    @property
    def transact_time(self):
        """
        Gets the transact_time of this Execution.

        :return: The transact_time of this Execution.
        :rtype: datetime
        """
        return self._transact_time

    @transact_time.setter
    def transact_time(self, transact_time):
        """
        Sets the transact_time of this Execution.

        :param transact_time: The transact_time of this Execution.
        :type: datetime
        """

        self._transact_time = transact_time

    @property
    def timestamp(self):
        """
        Gets the timestamp of this Execution.

        :return: The timestamp of this Execution.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this Execution.

        :param timestamp: The timestamp of this Execution.
        :type: datetime
        """

        self._timestamp = timestamp

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
        if not isinstance(other, Execution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
