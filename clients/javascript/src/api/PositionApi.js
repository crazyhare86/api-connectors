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


import ApiClient from "../ApiClient";
import Error from '../model/Error';
import Position from '../model/Position';

/**
* Position service.
* @module api/PositionApi
* @version 1.2.0
*/
export default class PositionApi {

    /**
    * Constructs a new PositionApi. 
    * @alias module:api/PositionApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the positionGet operation.
     * @callback module:api/PositionApi~positionGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Position>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get your positions.
     * See &lt;a href&#x3D;\&quot;http://www.onixs.biz/fix-dictionary/5.0.SP2/msgType_AP_6580.html\&quot;&gt;the FIX Spec&lt;/a&gt; for explanations of these fields.
     * @param {Object} opts Optional parameters
     * @param {String} opts.filter Table filter. For example, send {\&quot;symbol\&quot;: \&quot;XBTUSD\&quot;}.
     * @param {String} opts.columns Which columns to fetch. For example, send [\&quot;columnName\&quot;].
     * @param {Number} opts.count Number of rows to fetch.
     * @param {module:api/PositionApi~positionGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Position>}
     */
    positionGet(opts, callback) {
      opts = opts || {};
      let postBody = null;


      let pathParams = {
      };
      let queryParams = {
        'filter': opts['filter'],
        'columns': opts['columns'],
        'count': opts['count']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['apiKey', 'apiNonce', 'apiSignature'];
      let contentTypes = ['application/json', 'application/x-www-form-urlencoded'];
      let accepts = ['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'];
      let returnType = [Position];

      return this.apiClient.callApi(
        '/position', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the positionIsolateMargin operation.
     * @callback module:api/PositionApi~positionIsolateMarginCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Position} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Enable isolated margin or cross margin per-position.
     * Users can switch isolate margin per-position. This function allows switching margin isolation (aka fixed margin) on and off.
     * @param {String} symbol Position symbol to isolate.
     * @param {Object} opts Optional parameters
     * @param {Boolean} opts.enabled True for isolated margin, false for cross margin. (default to true)
     * @param {module:api/PositionApi~positionIsolateMarginCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Position}
     */
    positionIsolateMargin(symbol, opts, callback) {
      opts = opts || {};
      let postBody = null;

      // verify the required parameter 'symbol' is set
      if (symbol === undefined || symbol === null) {
        throw new Error("Missing the required parameter 'symbol' when calling positionIsolateMargin");
      }


      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'symbol': symbol,
        'enabled': opts['enabled']
      };

      let authNames = ['apiKey', 'apiNonce', 'apiSignature'];
      let contentTypes = ['application/json', 'application/x-www-form-urlencoded'];
      let accepts = ['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'];
      let returnType = Position;

      return this.apiClient.callApi(
        '/position/isolate', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the positionTransferIsolatedMargin operation.
     * @callback module:api/PositionApi~positionTransferIsolatedMarginCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Position} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Transfer equity in or out of a position.
     * When margin is isolated on a position, use this function to add or remove margin from the position. Note that you cannot remove margin below the initial margin threshold.
     * @param {String} symbol Symbol of position to isolate.
     * @param {Number} amount Amount to transfer, in Satoshis. May be negative.
     * @param {module:api/PositionApi~positionTransferIsolatedMarginCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Position}
     */
    positionTransferIsolatedMargin(symbol, amount, callback) {
      let postBody = null;

      // verify the required parameter 'symbol' is set
      if (symbol === undefined || symbol === null) {
        throw new Error("Missing the required parameter 'symbol' when calling positionTransferIsolatedMargin");
      }

      // verify the required parameter 'amount' is set
      if (amount === undefined || amount === null) {
        throw new Error("Missing the required parameter 'amount' when calling positionTransferIsolatedMargin");
      }


      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'symbol': symbol,
        'amount': amount
      };

      let authNames = ['apiKey', 'apiNonce', 'apiSignature'];
      let contentTypes = ['application/json', 'application/x-www-form-urlencoded'];
      let accepts = ['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'];
      let returnType = Position;

      return this.apiClient.callApi(
        '/position/transferMargin', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the positionUpdateLeverage operation.
     * @callback module:api/PositionApi~positionUpdateLeverageCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Position} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Choose leverage for a position.
     * Users can choose an isolated leverage. This will automatically enable isolated margin.
     * @param {String} symbol Symbol of position to adjust.
     * @param {Number} leverage Leverage value. Send a number between 0.01 and 100 to enable isolated margin with a fixed leverage. Send 0 to enable cross margin.
     * @param {module:api/PositionApi~positionUpdateLeverageCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Position}
     */
    positionUpdateLeverage(symbol, leverage, callback) {
      let postBody = null;

      // verify the required parameter 'symbol' is set
      if (symbol === undefined || symbol === null) {
        throw new Error("Missing the required parameter 'symbol' when calling positionUpdateLeverage");
      }

      // verify the required parameter 'leverage' is set
      if (leverage === undefined || leverage === null) {
        throw new Error("Missing the required parameter 'leverage' when calling positionUpdateLeverage");
      }


      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'symbol': symbol,
        'leverage': leverage
      };

      let authNames = ['apiKey', 'apiNonce', 'apiSignature'];
      let contentTypes = ['application/json', 'application/x-www-form-urlencoded'];
      let accepts = ['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'];
      let returnType = Position;

      return this.apiClient.callApi(
        '/position/leverage', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the positionUpdateRiskLimit operation.
     * @callback module:api/PositionApi~positionUpdateRiskLimitCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Position} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update your risk limit.
     * Risk Limits limit the size of positions you can trade at various margin levels. Larger positions require more margin. Please see the Risk Limit documentation for more details.
     * @param {String} symbol Symbol of position to isolate.
     * @param {Number} riskLimit New Risk Limit, in Satoshis.
     * @param {module:api/PositionApi~positionUpdateRiskLimitCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Position}
     */
    positionUpdateRiskLimit(symbol, riskLimit, callback) {
      let postBody = null;

      // verify the required parameter 'symbol' is set
      if (symbol === undefined || symbol === null) {
        throw new Error("Missing the required parameter 'symbol' when calling positionUpdateRiskLimit");
      }

      // verify the required parameter 'riskLimit' is set
      if (riskLimit === undefined || riskLimit === null) {
        throw new Error("Missing the required parameter 'riskLimit' when calling positionUpdateRiskLimit");
      }


      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'symbol': symbol,
        'riskLimit': riskLimit
      };

      let authNames = ['apiKey', 'apiNonce', 'apiSignature'];
      let contentTypes = ['application/json', 'application/x-www-form-urlencoded'];
      let accepts = ['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'];
      let returnType = Position;

      return this.apiClient.callApi(
        '/position/riskLimit', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }


}
