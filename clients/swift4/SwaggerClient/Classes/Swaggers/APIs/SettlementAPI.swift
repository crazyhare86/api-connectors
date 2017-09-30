//
// SettlementAPI.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation
import Alamofire



open class SettlementAPI {
    /**
     Get settlement history.
     
     - parameter symbol: (query) Instrument symbol. Send a bare series (e.g. XBU) to get data for the nearest expiring contract in that series.  You can also send a timeframe, e.g. &#x60;XBU:monthly&#x60;. Timeframes are &#x60;daily&#x60;, &#x60;weekly&#x60;, &#x60;monthly&#x60;, &#x60;quarterly&#x60;, and &#x60;biquarterly&#x60;. (optional)
     - parameter filter: (query) Generic table filter. Send JSON key/value pairs, such as &#x60;{\&quot;key\&quot;: \&quot;value\&quot;}&#x60;. You can key on individual fields, and do more advanced querying on timestamps. See the [Timestamp Docs](https://www.bitmex.com/app/restAPI#timestamp-filters) for more details. (optional)
     - parameter columns: (query) Array of column names to fetch. If omitted, will return all columns.  Note that this method will always return item keys, even when not specified, so you may receive more columns that you expect. (optional)
     - parameter count: (query) Number of results to fetch. (optional, default to 100)
     - parameter start: (query) Starting point for results. (optional, default to 0)
     - parameter reverse: (query) If true, will sort results newest first. (optional, default to false)
     - parameter startTime: (query) Starting date filter for results. (optional)
     - parameter endTime: (query) Ending date filter for results. (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func settlementGet(symbol: String? = nil, filter: String? = nil, columns: String? = nil, count: Double? = nil, start: Double? = nil, reverse: Bool? = nil, startTime: Date? = nil, endTime: Date? = nil, completion: @escaping ((_ data: [Settlement]?,_ error: Error?) -> Void)) {
        settlementGetWithRequestBuilder(symbol: symbol, filter: filter, columns: columns, count: count, start: start, reverse: reverse, startTime: startTime, endTime: endTime).execute { (response, error) -> Void in
            completion(response?.body, error);
        }
    }


    /**
     Get settlement history.
     - GET /settlement
     - examples: [{contentType=application/json, example=[ {
  "settlementType" : "settlementType",
  "symbol" : "symbol",
  "taxRate" : 5.962133916683182,
  "settledPrice" : 0.8008281904610115,
  "bankrupt" : 6.02745618307040320615897144307382404804229736328125,
  "timestamp" : "2000-01-23T04:56:07.000+00:00",
  "taxBase" : 1.46581298050294517310021547018550336360931396484375
}, {
  "settlementType" : "settlementType",
  "symbol" : "symbol",
  "taxRate" : 5.962133916683182,
  "settledPrice" : 0.8008281904610115,
  "bankrupt" : 6.02745618307040320615897144307382404804229736328125,
  "timestamp" : "2000-01-23T04:56:07.000+00:00",
  "taxBase" : 1.46581298050294517310021547018550336360931396484375
} ]}]
     
     - parameter symbol: (query) Instrument symbol. Send a bare series (e.g. XBU) to get data for the nearest expiring contract in that series.  You can also send a timeframe, e.g. &#x60;XBU:monthly&#x60;. Timeframes are &#x60;daily&#x60;, &#x60;weekly&#x60;, &#x60;monthly&#x60;, &#x60;quarterly&#x60;, and &#x60;biquarterly&#x60;. (optional)
     - parameter filter: (query) Generic table filter. Send JSON key/value pairs, such as &#x60;{\&quot;key\&quot;: \&quot;value\&quot;}&#x60;. You can key on individual fields, and do more advanced querying on timestamps. See the [Timestamp Docs](https://www.bitmex.com/app/restAPI#timestamp-filters) for more details. (optional)
     - parameter columns: (query) Array of column names to fetch. If omitted, will return all columns.  Note that this method will always return item keys, even when not specified, so you may receive more columns that you expect. (optional)
     - parameter count: (query) Number of results to fetch. (optional, default to 100)
     - parameter start: (query) Starting point for results. (optional, default to 0)
     - parameter reverse: (query) If true, will sort results newest first. (optional, default to false)
     - parameter startTime: (query) Starting date filter for results. (optional)
     - parameter endTime: (query) Ending date filter for results. (optional)

     - returns: RequestBuilder<[Settlement]> 
     */
    open class func settlementGetWithRequestBuilder(symbol: String? = nil, filter: String? = nil, columns: String? = nil, count: Double? = nil, start: Double? = nil, reverse: Bool? = nil, startTime: Date? = nil, endTime: Date? = nil) -> RequestBuilder<[Settlement]> {
        let path = "/settlement"
        let URLString = SwaggerClientAPI.basePath + path
        let parameters: [String:Any]? = nil

        let url = NSURLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems(values:[
            "symbol": symbol, 
            "filter": filter, 
            "columns": columns, 
            "count": count, 
            "start": start, 
            "reverse": reverse, 
            "startTime": startTime?.encodeToJSON(), 
            "endTime": endTime?.encodeToJSON()
        ])
        

        let requestBuilder: RequestBuilder<[Settlement]>.Type = SwaggerClientAPI.requestBuilderFactory.getBuilder()

        return requestBuilder.init(method: "GET", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false)
    }

}
