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

package io.swagger.client.request;

import com.android.volley.AuthFailureError;
import com.android.volley.NetworkResponse;
import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyLog;
import com.android.volley.toolbox.HttpHeaderParser;

import org.apache.http.HttpEntity;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class PostRequest extends Request<String> {

  HttpEntity entity;

  private final Response.Listener<String> mListener;

  String contentType;
  Map<String, String> apiHeaders;
  public PostRequest(String url, Map<String, String> apiHeaders, String contentType, HttpEntity entity, Response.Listener<String> listener, Response.ErrorListener errorListener) {
    super(Method.POST, url, errorListener);
    mListener = listener;
    this.entity = entity;
    this.contentType = contentType;
    this.apiHeaders = apiHeaders;
  }

  @Override
  public String getBodyContentType() {
    if(entity == null) {
      return null;
    }
    return entity.getContentType().getValue();
  }

  @Override
  public byte[] getBody() throws AuthFailureError {
    if(entity == null) {
      return null;
    }
    ByteArrayOutputStream bos = new ByteArrayOutputStream();
    try {
      entity.writeTo(bos);
    }
    catch (IOException e) {
      VolleyLog.e("IOException writing to ByteArrayOutputStream");
    }
    return bos.toByteArray();
  }

  @Override
  protected Response<String> parseNetworkResponse(NetworkResponse response) {
    String parsed;
    try {
      parsed = new String(response.data, HttpHeaderParser.parseCharset(response.headers));
    } catch (UnsupportedEncodingException e) {
      parsed = new String(response.data);
    }
    return Response.success(parsed, HttpHeaderParser.parseCacheHeaders(response));
  }

  @Override
  protected void deliverResponse(String response) {
    mListener.onResponse(response);
  }

  /* (non-Javadoc)
   * @see com.android.volley.Request#getHeaders()
   */
  @Override
  public Map<String, String> getHeaders() throws AuthFailureError {
    Map<String, String> headers = super.getHeaders();
    if (headers == null || headers.equals(Collections.emptyMap())) {
        headers = new HashMap<String, String>();
    }
    if (apiHeaders != null && !apiHeaders.equals(Collections.emptyMap())) {
        headers.putAll(apiHeaders);
    }
    if(contentType != null) {
        headers.put("Content-Type", contentType);
    }

    return headers;
  }
}
