/**
 * BitMEX API
 * ## REST API for the BitMEX Trading Platform  [View Changelog](/app/apiChangelog)    #### Getting Started   ##### Fetching Data  All REST endpoints are documented below. You can try out any query right from this interface.  Most table queries accept `count`, `start`, and `reverse` params. Set `reverse=true` to get rows newest-first.  Additional documentation regarding filters, timestamps, and authentication is available in [the main API documentation](https://www.bitmex.com/app/restAPI).  *All* table data is available via the [Websocket](/app/wsAPI). We highly recommend using the socket if you want to have the quickest possible data without being subject to ratelimits.  ##### Return Types  By default, all data is returned as JSON. Send `?_format=csv` to get CSV data or `?_format=xml` to get XML data.  ##### Trade Data Queries  *This is only a small subset of what is available, to get you started.*  Fill in the parameters and click the `Try it out!` button to try any of these queries.  * [Pricing Data](#!/Quote/Quote_get)  * [Trade Data](#!/Trade/Trade_get)  * [OrderBook Data](#!/OrderBook/OrderBook_getL2)  * [Settlement Data](#!/Settlement/Settlement_get)  * [Exchange Statistics](#!/Stats/Stats_history)  Every function of the BitMEX.com platform is exposed here and documented. Many more functions are available.  ##### Swagger Specification  [⇩ Download Swagger JSON](swagger.json)    ## All API Endpoints  Click to expand a section. 
 *
 * OpenAPI spec version: 1.2.0
 * Contact: support@bitmex.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 *
 */


import ApiClient from '../ApiClient';





/**
* The Position model module.
* @module model/Position
* @version 1.2.0
*/
export default class Position {
    /**
    * Constructs a new <code>Position</code>.
    * Summary of Open and Closed Positions
    * @alias module:model/Position
    * @class
    * @param account {Number} 
    * @param symbol {String} 
    * @param currency {String} 
    */

    constructor(account, symbol, currency) {
        

        
        

        this['account'] = account;this['symbol'] = symbol;this['currency'] = currency;

        
    }

    /**
    * Constructs a <code>Position</code> from a plain JavaScript object, optionally creating a new instance.
    * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
    * @param {Object} data The plain JavaScript object bearing properties of interest.
    * @param {module:model/Position} obj Optional instance to populate.
    * @return {module:model/Position} The populated <code>Position</code> instance.
    */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Position();

            
            
            

            if (data.hasOwnProperty('account')) {
                obj['account'] = ApiClient.convertToType(data['account'], 'Number');
            }
            if (data.hasOwnProperty('symbol')) {
                obj['symbol'] = ApiClient.convertToType(data['symbol'], 'String');
            }
            if (data.hasOwnProperty('currency')) {
                obj['currency'] = ApiClient.convertToType(data['currency'], 'String');
            }
            if (data.hasOwnProperty('underlying')) {
                obj['underlying'] = ApiClient.convertToType(data['underlying'], 'String');
            }
            if (data.hasOwnProperty('quoteCurrency')) {
                obj['quoteCurrency'] = ApiClient.convertToType(data['quoteCurrency'], 'String');
            }
            if (data.hasOwnProperty('commission')) {
                obj['commission'] = ApiClient.convertToType(data['commission'], 'Number');
            }
            if (data.hasOwnProperty('initMarginReq')) {
                obj['initMarginReq'] = ApiClient.convertToType(data['initMarginReq'], 'Number');
            }
            if (data.hasOwnProperty('maintMarginReq')) {
                obj['maintMarginReq'] = ApiClient.convertToType(data['maintMarginReq'], 'Number');
            }
            if (data.hasOwnProperty('riskLimit')) {
                obj['riskLimit'] = ApiClient.convertToType(data['riskLimit'], 'Number');
            }
            if (data.hasOwnProperty('leverage')) {
                obj['leverage'] = ApiClient.convertToType(data['leverage'], 'Number');
            }
            if (data.hasOwnProperty('crossMargin')) {
                obj['crossMargin'] = ApiClient.convertToType(data['crossMargin'], 'Boolean');
            }
            if (data.hasOwnProperty('deleveragePercentile')) {
                obj['deleveragePercentile'] = ApiClient.convertToType(data['deleveragePercentile'], 'Number');
            }
            if (data.hasOwnProperty('rebalancedPnl')) {
                obj['rebalancedPnl'] = ApiClient.convertToType(data['rebalancedPnl'], 'Number');
            }
            if (data.hasOwnProperty('prevRealisedPnl')) {
                obj['prevRealisedPnl'] = ApiClient.convertToType(data['prevRealisedPnl'], 'Number');
            }
            if (data.hasOwnProperty('prevUnrealisedPnl')) {
                obj['prevUnrealisedPnl'] = ApiClient.convertToType(data['prevUnrealisedPnl'], 'Number');
            }
            if (data.hasOwnProperty('prevClosePrice')) {
                obj['prevClosePrice'] = ApiClient.convertToType(data['prevClosePrice'], 'Number');
            }
            if (data.hasOwnProperty('openingTimestamp')) {
                obj['openingTimestamp'] = ApiClient.convertToType(data['openingTimestamp'], 'Date');
            }
            if (data.hasOwnProperty('openingQty')) {
                obj['openingQty'] = ApiClient.convertToType(data['openingQty'], 'Number');
            }
            if (data.hasOwnProperty('openingCost')) {
                obj['openingCost'] = ApiClient.convertToType(data['openingCost'], 'Number');
            }
            if (data.hasOwnProperty('openingComm')) {
                obj['openingComm'] = ApiClient.convertToType(data['openingComm'], 'Number');
            }
            if (data.hasOwnProperty('openOrderBuyQty')) {
                obj['openOrderBuyQty'] = ApiClient.convertToType(data['openOrderBuyQty'], 'Number');
            }
            if (data.hasOwnProperty('openOrderBuyCost')) {
                obj['openOrderBuyCost'] = ApiClient.convertToType(data['openOrderBuyCost'], 'Number');
            }
            if (data.hasOwnProperty('openOrderBuyPremium')) {
                obj['openOrderBuyPremium'] = ApiClient.convertToType(data['openOrderBuyPremium'], 'Number');
            }
            if (data.hasOwnProperty('openOrderSellQty')) {
                obj['openOrderSellQty'] = ApiClient.convertToType(data['openOrderSellQty'], 'Number');
            }
            if (data.hasOwnProperty('openOrderSellCost')) {
                obj['openOrderSellCost'] = ApiClient.convertToType(data['openOrderSellCost'], 'Number');
            }
            if (data.hasOwnProperty('openOrderSellPremium')) {
                obj['openOrderSellPremium'] = ApiClient.convertToType(data['openOrderSellPremium'], 'Number');
            }
            if (data.hasOwnProperty('execBuyQty')) {
                obj['execBuyQty'] = ApiClient.convertToType(data['execBuyQty'], 'Number');
            }
            if (data.hasOwnProperty('execBuyCost')) {
                obj['execBuyCost'] = ApiClient.convertToType(data['execBuyCost'], 'Number');
            }
            if (data.hasOwnProperty('execSellQty')) {
                obj['execSellQty'] = ApiClient.convertToType(data['execSellQty'], 'Number');
            }
            if (data.hasOwnProperty('execSellCost')) {
                obj['execSellCost'] = ApiClient.convertToType(data['execSellCost'], 'Number');
            }
            if (data.hasOwnProperty('execQty')) {
                obj['execQty'] = ApiClient.convertToType(data['execQty'], 'Number');
            }
            if (data.hasOwnProperty('execCost')) {
                obj['execCost'] = ApiClient.convertToType(data['execCost'], 'Number');
            }
            if (data.hasOwnProperty('execComm')) {
                obj['execComm'] = ApiClient.convertToType(data['execComm'], 'Number');
            }
            if (data.hasOwnProperty('currentTimestamp')) {
                obj['currentTimestamp'] = ApiClient.convertToType(data['currentTimestamp'], 'Date');
            }
            if (data.hasOwnProperty('currentQty')) {
                obj['currentQty'] = ApiClient.convertToType(data['currentQty'], 'Number');
            }
            if (data.hasOwnProperty('currentCost')) {
                obj['currentCost'] = ApiClient.convertToType(data['currentCost'], 'Number');
            }
            if (data.hasOwnProperty('currentComm')) {
                obj['currentComm'] = ApiClient.convertToType(data['currentComm'], 'Number');
            }
            if (data.hasOwnProperty('realisedCost')) {
                obj['realisedCost'] = ApiClient.convertToType(data['realisedCost'], 'Number');
            }
            if (data.hasOwnProperty('unrealisedCost')) {
                obj['unrealisedCost'] = ApiClient.convertToType(data['unrealisedCost'], 'Number');
            }
            if (data.hasOwnProperty('grossOpenCost')) {
                obj['grossOpenCost'] = ApiClient.convertToType(data['grossOpenCost'], 'Number');
            }
            if (data.hasOwnProperty('grossOpenPremium')) {
                obj['grossOpenPremium'] = ApiClient.convertToType(data['grossOpenPremium'], 'Number');
            }
            if (data.hasOwnProperty('grossExecCost')) {
                obj['grossExecCost'] = ApiClient.convertToType(data['grossExecCost'], 'Number');
            }
            if (data.hasOwnProperty('isOpen')) {
                obj['isOpen'] = ApiClient.convertToType(data['isOpen'], 'Boolean');
            }
            if (data.hasOwnProperty('markPrice')) {
                obj['markPrice'] = ApiClient.convertToType(data['markPrice'], 'Number');
            }
            if (data.hasOwnProperty('markValue')) {
                obj['markValue'] = ApiClient.convertToType(data['markValue'], 'Number');
            }
            if (data.hasOwnProperty('riskValue')) {
                obj['riskValue'] = ApiClient.convertToType(data['riskValue'], 'Number');
            }
            if (data.hasOwnProperty('homeNotional')) {
                obj['homeNotional'] = ApiClient.convertToType(data['homeNotional'], 'Number');
            }
            if (data.hasOwnProperty('foreignNotional')) {
                obj['foreignNotional'] = ApiClient.convertToType(data['foreignNotional'], 'Number');
            }
            if (data.hasOwnProperty('posState')) {
                obj['posState'] = ApiClient.convertToType(data['posState'], 'String');
            }
            if (data.hasOwnProperty('posCost')) {
                obj['posCost'] = ApiClient.convertToType(data['posCost'], 'Number');
            }
            if (data.hasOwnProperty('posCost2')) {
                obj['posCost2'] = ApiClient.convertToType(data['posCost2'], 'Number');
            }
            if (data.hasOwnProperty('posCross')) {
                obj['posCross'] = ApiClient.convertToType(data['posCross'], 'Number');
            }
            if (data.hasOwnProperty('posInit')) {
                obj['posInit'] = ApiClient.convertToType(data['posInit'], 'Number');
            }
            if (data.hasOwnProperty('posComm')) {
                obj['posComm'] = ApiClient.convertToType(data['posComm'], 'Number');
            }
            if (data.hasOwnProperty('posLoss')) {
                obj['posLoss'] = ApiClient.convertToType(data['posLoss'], 'Number');
            }
            if (data.hasOwnProperty('posMargin')) {
                obj['posMargin'] = ApiClient.convertToType(data['posMargin'], 'Number');
            }
            if (data.hasOwnProperty('posMaint')) {
                obj['posMaint'] = ApiClient.convertToType(data['posMaint'], 'Number');
            }
            if (data.hasOwnProperty('posAllowance')) {
                obj['posAllowance'] = ApiClient.convertToType(data['posAllowance'], 'Number');
            }
            if (data.hasOwnProperty('taxableMargin')) {
                obj['taxableMargin'] = ApiClient.convertToType(data['taxableMargin'], 'Number');
            }
            if (data.hasOwnProperty('initMargin')) {
                obj['initMargin'] = ApiClient.convertToType(data['initMargin'], 'Number');
            }
            if (data.hasOwnProperty('maintMargin')) {
                obj['maintMargin'] = ApiClient.convertToType(data['maintMargin'], 'Number');
            }
            if (data.hasOwnProperty('sessionMargin')) {
                obj['sessionMargin'] = ApiClient.convertToType(data['sessionMargin'], 'Number');
            }
            if (data.hasOwnProperty('targetExcessMargin')) {
                obj['targetExcessMargin'] = ApiClient.convertToType(data['targetExcessMargin'], 'Number');
            }
            if (data.hasOwnProperty('varMargin')) {
                obj['varMargin'] = ApiClient.convertToType(data['varMargin'], 'Number');
            }
            if (data.hasOwnProperty('realisedGrossPnl')) {
                obj['realisedGrossPnl'] = ApiClient.convertToType(data['realisedGrossPnl'], 'Number');
            }
            if (data.hasOwnProperty('realisedTax')) {
                obj['realisedTax'] = ApiClient.convertToType(data['realisedTax'], 'Number');
            }
            if (data.hasOwnProperty('realisedPnl')) {
                obj['realisedPnl'] = ApiClient.convertToType(data['realisedPnl'], 'Number');
            }
            if (data.hasOwnProperty('unrealisedGrossPnl')) {
                obj['unrealisedGrossPnl'] = ApiClient.convertToType(data['unrealisedGrossPnl'], 'Number');
            }
            if (data.hasOwnProperty('longBankrupt')) {
                obj['longBankrupt'] = ApiClient.convertToType(data['longBankrupt'], 'Number');
            }
            if (data.hasOwnProperty('shortBankrupt')) {
                obj['shortBankrupt'] = ApiClient.convertToType(data['shortBankrupt'], 'Number');
            }
            if (data.hasOwnProperty('taxBase')) {
                obj['taxBase'] = ApiClient.convertToType(data['taxBase'], 'Number');
            }
            if (data.hasOwnProperty('indicativeTaxRate')) {
                obj['indicativeTaxRate'] = ApiClient.convertToType(data['indicativeTaxRate'], 'Number');
            }
            if (data.hasOwnProperty('indicativeTax')) {
                obj['indicativeTax'] = ApiClient.convertToType(data['indicativeTax'], 'Number');
            }
            if (data.hasOwnProperty('unrealisedTax')) {
                obj['unrealisedTax'] = ApiClient.convertToType(data['unrealisedTax'], 'Number');
            }
            if (data.hasOwnProperty('unrealisedPnl')) {
                obj['unrealisedPnl'] = ApiClient.convertToType(data['unrealisedPnl'], 'Number');
            }
            if (data.hasOwnProperty('unrealisedPnlPcnt')) {
                obj['unrealisedPnlPcnt'] = ApiClient.convertToType(data['unrealisedPnlPcnt'], 'Number');
            }
            if (data.hasOwnProperty('unrealisedRoePcnt')) {
                obj['unrealisedRoePcnt'] = ApiClient.convertToType(data['unrealisedRoePcnt'], 'Number');
            }
            if (data.hasOwnProperty('simpleQty')) {
                obj['simpleQty'] = ApiClient.convertToType(data['simpleQty'], 'Number');
            }
            if (data.hasOwnProperty('simpleCost')) {
                obj['simpleCost'] = ApiClient.convertToType(data['simpleCost'], 'Number');
            }
            if (data.hasOwnProperty('simpleValue')) {
                obj['simpleValue'] = ApiClient.convertToType(data['simpleValue'], 'Number');
            }
            if (data.hasOwnProperty('simplePnl')) {
                obj['simplePnl'] = ApiClient.convertToType(data['simplePnl'], 'Number');
            }
            if (data.hasOwnProperty('simplePnlPcnt')) {
                obj['simplePnlPcnt'] = ApiClient.convertToType(data['simplePnlPcnt'], 'Number');
            }
            if (data.hasOwnProperty('avgCostPrice')) {
                obj['avgCostPrice'] = ApiClient.convertToType(data['avgCostPrice'], 'Number');
            }
            if (data.hasOwnProperty('avgEntryPrice')) {
                obj['avgEntryPrice'] = ApiClient.convertToType(data['avgEntryPrice'], 'Number');
            }
            if (data.hasOwnProperty('breakEvenPrice')) {
                obj['breakEvenPrice'] = ApiClient.convertToType(data['breakEvenPrice'], 'Number');
            }
            if (data.hasOwnProperty('marginCallPrice')) {
                obj['marginCallPrice'] = ApiClient.convertToType(data['marginCallPrice'], 'Number');
            }
            if (data.hasOwnProperty('liquidationPrice')) {
                obj['liquidationPrice'] = ApiClient.convertToType(data['liquidationPrice'], 'Number');
            }
            if (data.hasOwnProperty('bankruptPrice')) {
                obj['bankruptPrice'] = ApiClient.convertToType(data['bankruptPrice'], 'Number');
            }
            if (data.hasOwnProperty('timestamp')) {
                obj['timestamp'] = ApiClient.convertToType(data['timestamp'], 'Date');
            }
            if (data.hasOwnProperty('lastPrice')) {
                obj['lastPrice'] = ApiClient.convertToType(data['lastPrice'], 'Number');
            }
            if (data.hasOwnProperty('lastValue')) {
                obj['lastValue'] = ApiClient.convertToType(data['lastValue'], 'Number');
            }
        }
        return obj;
    }

    /**
    * @member {Number} account
    */
    account = undefined;
    /**
    * @member {String} symbol
    */
    symbol = undefined;
    /**
    * @member {String} currency
    */
    currency = undefined;
    /**
    * @member {String} underlying
    */
    underlying = undefined;
    /**
    * @member {String} quoteCurrency
    */
    quoteCurrency = undefined;
    /**
    * @member {Number} commission
    * @default 0.0
    */
    commission = 0.0;
    /**
    * @member {Number} initMarginReq
    * @default 0.0
    */
    initMarginReq = 0.0;
    /**
    * @member {Number} maintMarginReq
    * @default 0.0
    */
    maintMarginReq = 0.0;
    /**
    * @member {Number} riskLimit
    */
    riskLimit = undefined;
    /**
    * @member {Number} leverage
    * @default 0.0
    */
    leverage = 0.0;
    /**
    * @member {Boolean} crossMargin
    */
    crossMargin = undefined;
    /**
    * @member {Number} deleveragePercentile
    * @default 0.0
    */
    deleveragePercentile = 0.0;
    /**
    * @member {Number} rebalancedPnl
    */
    rebalancedPnl = undefined;
    /**
    * @member {Number} prevRealisedPnl
    */
    prevRealisedPnl = undefined;
    /**
    * @member {Number} prevUnrealisedPnl
    */
    prevUnrealisedPnl = undefined;
    /**
    * @member {Number} prevClosePrice
    * @default 0.0
    */
    prevClosePrice = 0.0;
    /**
    * @member {Date} openingTimestamp
    */
    openingTimestamp = undefined;
    /**
    * @member {Number} openingQty
    */
    openingQty = undefined;
    /**
    * @member {Number} openingCost
    */
    openingCost = undefined;
    /**
    * @member {Number} openingComm
    */
    openingComm = undefined;
    /**
    * @member {Number} openOrderBuyQty
    */
    openOrderBuyQty = undefined;
    /**
    * @member {Number} openOrderBuyCost
    */
    openOrderBuyCost = undefined;
    /**
    * @member {Number} openOrderBuyPremium
    */
    openOrderBuyPremium = undefined;
    /**
    * @member {Number} openOrderSellQty
    */
    openOrderSellQty = undefined;
    /**
    * @member {Number} openOrderSellCost
    */
    openOrderSellCost = undefined;
    /**
    * @member {Number} openOrderSellPremium
    */
    openOrderSellPremium = undefined;
    /**
    * @member {Number} execBuyQty
    */
    execBuyQty = undefined;
    /**
    * @member {Number} execBuyCost
    */
    execBuyCost = undefined;
    /**
    * @member {Number} execSellQty
    */
    execSellQty = undefined;
    /**
    * @member {Number} execSellCost
    */
    execSellCost = undefined;
    /**
    * @member {Number} execQty
    */
    execQty = undefined;
    /**
    * @member {Number} execCost
    */
    execCost = undefined;
    /**
    * @member {Number} execComm
    */
    execComm = undefined;
    /**
    * @member {Date} currentTimestamp
    */
    currentTimestamp = undefined;
    /**
    * @member {Number} currentQty
    */
    currentQty = undefined;
    /**
    * @member {Number} currentCost
    */
    currentCost = undefined;
    /**
    * @member {Number} currentComm
    */
    currentComm = undefined;
    /**
    * @member {Number} realisedCost
    */
    realisedCost = undefined;
    /**
    * @member {Number} unrealisedCost
    */
    unrealisedCost = undefined;
    /**
    * @member {Number} grossOpenCost
    */
    grossOpenCost = undefined;
    /**
    * @member {Number} grossOpenPremium
    */
    grossOpenPremium = undefined;
    /**
    * @member {Number} grossExecCost
    */
    grossExecCost = undefined;
    /**
    * @member {Boolean} isOpen
    */
    isOpen = undefined;
    /**
    * @member {Number} markPrice
    * @default 0.0
    */
    markPrice = 0.0;
    /**
    * @member {Number} markValue
    */
    markValue = undefined;
    /**
    * @member {Number} riskValue
    */
    riskValue = undefined;
    /**
    * @member {Number} homeNotional
    * @default 0.0
    */
    homeNotional = 0.0;
    /**
    * @member {Number} foreignNotional
    * @default 0.0
    */
    foreignNotional = 0.0;
    /**
    * @member {String} posState
    */
    posState = undefined;
    /**
    * @member {Number} posCost
    */
    posCost = undefined;
    /**
    * @member {Number} posCost2
    */
    posCost2 = undefined;
    /**
    * @member {Number} posCross
    */
    posCross = undefined;
    /**
    * @member {Number} posInit
    */
    posInit = undefined;
    /**
    * @member {Number} posComm
    */
    posComm = undefined;
    /**
    * @member {Number} posLoss
    */
    posLoss = undefined;
    /**
    * @member {Number} posMargin
    */
    posMargin = undefined;
    /**
    * @member {Number} posMaint
    */
    posMaint = undefined;
    /**
    * @member {Number} posAllowance
    */
    posAllowance = undefined;
    /**
    * @member {Number} taxableMargin
    */
    taxableMargin = undefined;
    /**
    * @member {Number} initMargin
    */
    initMargin = undefined;
    /**
    * @member {Number} maintMargin
    */
    maintMargin = undefined;
    /**
    * @member {Number} sessionMargin
    */
    sessionMargin = undefined;
    /**
    * @member {Number} targetExcessMargin
    */
    targetExcessMargin = undefined;
    /**
    * @member {Number} varMargin
    */
    varMargin = undefined;
    /**
    * @member {Number} realisedGrossPnl
    */
    realisedGrossPnl = undefined;
    /**
    * @member {Number} realisedTax
    */
    realisedTax = undefined;
    /**
    * @member {Number} realisedPnl
    */
    realisedPnl = undefined;
    /**
    * @member {Number} unrealisedGrossPnl
    */
    unrealisedGrossPnl = undefined;
    /**
    * @member {Number} longBankrupt
    */
    longBankrupt = undefined;
    /**
    * @member {Number} shortBankrupt
    */
    shortBankrupt = undefined;
    /**
    * @member {Number} taxBase
    */
    taxBase = undefined;
    /**
    * @member {Number} indicativeTaxRate
    * @default 0.0
    */
    indicativeTaxRate = 0.0;
    /**
    * @member {Number} indicativeTax
    */
    indicativeTax = undefined;
    /**
    * @member {Number} unrealisedTax
    */
    unrealisedTax = undefined;
    /**
    * @member {Number} unrealisedPnl
    */
    unrealisedPnl = undefined;
    /**
    * @member {Number} unrealisedPnlPcnt
    * @default 0.0
    */
    unrealisedPnlPcnt = 0.0;
    /**
    * @member {Number} unrealisedRoePcnt
    * @default 0.0
    */
    unrealisedRoePcnt = 0.0;
    /**
    * @member {Number} simpleQty
    * @default 0.0
    */
    simpleQty = 0.0;
    /**
    * @member {Number} simpleCost
    * @default 0.0
    */
    simpleCost = 0.0;
    /**
    * @member {Number} simpleValue
    * @default 0.0
    */
    simpleValue = 0.0;
    /**
    * @member {Number} simplePnl
    * @default 0.0
    */
    simplePnl = 0.0;
    /**
    * @member {Number} simplePnlPcnt
    * @default 0.0
    */
    simplePnlPcnt = 0.0;
    /**
    * @member {Number} avgCostPrice
    * @default 0.0
    */
    avgCostPrice = 0.0;
    /**
    * @member {Number} avgEntryPrice
    * @default 0.0
    */
    avgEntryPrice = 0.0;
    /**
    * @member {Number} breakEvenPrice
    * @default 0.0
    */
    breakEvenPrice = 0.0;
    /**
    * @member {Number} marginCallPrice
    * @default 0.0
    */
    marginCallPrice = 0.0;
    /**
    * @member {Number} liquidationPrice
    * @default 0.0
    */
    liquidationPrice = 0.0;
    /**
    * @member {Number} bankruptPrice
    * @default 0.0
    */
    bankruptPrice = 0.0;
    /**
    * @member {Date} timestamp
    */
    timestamp = undefined;
    /**
    * @member {Number} lastPrice
    * @default 0.0
    */
    lastPrice = 0.0;
    /**
    * @member {Number} lastValue
    */
    lastValue = undefined;








}


