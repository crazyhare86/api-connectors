//
// OrderBookAPI.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation
import Alamofire



open class OrderBookAPI {
    /**
     Get current orderbook [deprecated, use /orderBook/L2].
     
     - parameter symbol: (query) Instrument symbol. Send a series (e.g. XBT) to get data for the nearest contract in that series. 
     - parameter depth: (query) Orderbook depth. (optional, default to 25)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func orderBookGet(symbol: String, depth: Double? = nil, completion: @escaping ((_ data: [OrderBook]?,_ error: Error?) -> Void)) {
        orderBookGetWithRequestBuilder(symbol: symbol, depth: depth).execute { (response, error) -> Void in
            completion(response?.body, error);
        }
    }


    /**
     Get current orderbook [deprecated, use /orderBook/L2].
     - GET /orderBook
     - examples: [{contentType=application/json, example=[ {
  "symbol" : "symbol",
  "askPrice" : 5.962133916683182,
  "level" : 0.80082819046101150206595775671303272247314453125,
  "bidSize" : 6.02745618307040320615897144307382404804229736328125,
  "bidPrice" : 1.4658129805029452,
  "askSize" : 5.63737665663332876420099637471139430999755859375,
  "timestamp" : "2000-01-23T04:56:07.000+00:00"
}, {
  "symbol" : "symbol",
  "askPrice" : 5.962133916683182,
  "level" : 0.80082819046101150206595775671303272247314453125,
  "bidSize" : 6.02745618307040320615897144307382404804229736328125,
  "bidPrice" : 1.4658129805029452,
  "askSize" : 5.63737665663332876420099637471139430999755859375,
  "timestamp" : "2000-01-23T04:56:07.000+00:00"
} ]}]
     
     - parameter symbol: (query) Instrument symbol. Send a series (e.g. XBT) to get data for the nearest contract in that series. 
     - parameter depth: (query) Orderbook depth. (optional, default to 25)

     - returns: RequestBuilder<[OrderBook]> 
     */
    open class func orderBookGetWithRequestBuilder(symbol: String, depth: Double? = nil) -> RequestBuilder<[OrderBook]> {
        let path = "/orderBook"
        let URLString = SwaggerClientAPI.basePath + path
        let parameters: [String:Any]? = nil

        let url = NSURLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems(values:[
            "symbol": symbol, 
            "depth": depth
        ])
        

        let requestBuilder: RequestBuilder<[OrderBook]>.Type = SwaggerClientAPI.requestBuilderFactory.getBuilder()

        return requestBuilder.init(method: "GET", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false)
    }

    /**
     Get current orderbook in vertical format.
     
     - parameter symbol: (query) Instrument symbol. Send a series (e.g. XBT) to get data for the nearest contract in that series. 
     - parameter depth: (query) Orderbook depth per side. Send 0 for full depth. (optional, default to 25)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func orderBookGetL2(symbol: String, depth: Double? = nil, completion: @escaping ((_ data: [OrderBookL2]?,_ error: Error?) -> Void)) {
        orderBookGetL2WithRequestBuilder(symbol: symbol, depth: depth).execute { (response, error) -> Void in
            completion(response?.body, error);
        }
    }


    /**
     Get current orderbook in vertical format.
     - GET /orderBook/L2
     - examples: [{contentType=application/json, example=[ {
  "symbol" : "symbol",
  "side" : "side",
  "size" : 6.02745618307040320615897144307382404804229736328125,
  "price" : 1.4658129805029452,
  "id" : 0.80082819046101150206595775671303272247314453125
}, {
  "symbol" : "symbol",
  "side" : "side",
  "size" : 6.02745618307040320615897144307382404804229736328125,
  "price" : 1.4658129805029452,
  "id" : 0.80082819046101150206595775671303272247314453125
} ]}]
     
     - parameter symbol: (query) Instrument symbol. Send a series (e.g. XBT) to get data for the nearest contract in that series. 
     - parameter depth: (query) Orderbook depth per side. Send 0 for full depth. (optional, default to 25)

     - returns: RequestBuilder<[OrderBookL2]> 
     */
    open class func orderBookGetL2WithRequestBuilder(symbol: String, depth: Double? = nil) -> RequestBuilder<[OrderBookL2]> {
        let path = "/orderBook/L2"
        let URLString = SwaggerClientAPI.basePath + path
        let parameters: [String:Any]? = nil

        let url = NSURLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems(values:[
            "symbol": symbol, 
            "depth": depth
        ])
        

        let requestBuilder: RequestBuilder<[OrderBookL2]>.Type = SwaggerClientAPI.requestBuilderFactory.getBuilder()

        return requestBuilder.init(method: "GET", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false)
    }

}
