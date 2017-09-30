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
 */

package io.swagger.client.model

import java.util.Date

case class Order (
  orderID: String,
  clOrdID: Option[String],
  clOrdLinkID: Option[String],
  account: Option[Number],
  symbol: Option[String],
  side: Option[String],
  simpleOrderQty: Option[Double],
  orderQty: Option[Number],
  price: Option[Double],
  displayQty: Option[Number],
  stopPx: Option[Double],
  pegOffsetValue: Option[Double],
  pegPriceType: Option[String],
  currency: Option[String],
  settlCurrency: Option[String],
  ordType: Option[String],
  timeInForce: Option[String],
  execInst: Option[String],
  contingencyType: Option[String],
  exDestination: Option[String],
  ordStatus: Option[String],
  triggered: Option[String],
  workingIndicator: Option[Boolean],
  ordRejReason: Option[String],
  simpleLeavesQty: Option[Double],
  leavesQty: Option[Number],
  simpleCumQty: Option[Double],
  cumQty: Option[Number],
  avgPx: Option[Double],
  multiLegReportingType: Option[String],
  text: Option[String],
  transactTime: Option[Date],
  timestamp: Option[Date]
)

