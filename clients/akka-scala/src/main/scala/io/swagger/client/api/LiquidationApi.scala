/**
 * NOTE: This class is auto generated by the akka-scala (beta) swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen
 * For any issue or feedback, please open a ticket via https://github.com/swagger-api/swagger-codegen/issues/new
 */
package io.swagger.client.api

import org.joda.time.DateTime
import io.swagger.client.model.Error
import io.swagger.client.model.Liquidation
import io.swagger.client.core._
import io.swagger.client.core.CollectionFormats._
import io.swagger.client.core.ApiKeyLocations._

object LiquidationApi {

  /**
   * 
   * 
   * Expected answers:
   *   code 200 : Seq[Liquidation] (Request was successful)
   *   code 400 : Error (Parameter Error)
   *   code 401 : Error (Unauthorized)
   *   code 404 : Error (Not Found)
   * 
   * @param symbol Instrument symbol. Send a bare series (e.g. XBU) to get data for the nearest expiring contract in that series.  You can also send a timeframe, e.g. &#x60;XBU:monthly&#x60;. Timeframes are &#x60;daily&#x60;, &#x60;weekly&#x60;, &#x60;monthly&#x60;, &#x60;quarterly&#x60;, and &#x60;biquarterly&#x60;.
   * @param filter Generic table filter. Send JSON key/value pairs, such as &#x60;{\&quot;key\&quot;: \&quot;value\&quot;}&#x60;. You can key on individual fields, and do more advanced querying on timestamps. See the [Timestamp Docs](https://www.bitmex.com/app/restAPI#timestamp-filters) for more details.
   * @param columns Array of column names to fetch. If omitted, will return all columns.  Note that this method will always return item keys, even when not specified, so you may receive more columns that you expect.
   * @param count Number of results to fetch.
   * @param start Starting point for results.
   * @param reverse If true, will sort results newest first.
   * @param startTime Starting date filter for results.
   * @param endTime Ending date filter for results.
   */
  def liquidation.get(symbol: Option[String] = None, filter: Option[String] = None, columns: Option[String] = None, count: Option[Double], start: Option[Double], reverse: Option[Boolean], startTime: Option[DateTime] = None, endTime: Option[DateTime] = None): ApiRequest[Seq[Liquidation]] =
    ApiRequest[Seq[Liquidation]](ApiMethods.GET, "https://localhost/api/v1", "/liquidation", "application/json")
      .withQueryParam("symbol", symbol)
      .withQueryParam("filter", filter)
      .withQueryParam("columns", columns)
      .withQueryParam("count", count)
      .withQueryParam("start", start)
      .withQueryParam("reverse", reverse)
      .withQueryParam("startTime", startTime)
      .withQueryParam("endTime", endTime)
      .withSuccessResponse[Seq[Liquidation]](200)
      .withErrorResponse[Error](400)
      .withErrorResponse[Error](401)
      .withErrorResponse[Error](404)
      

}

