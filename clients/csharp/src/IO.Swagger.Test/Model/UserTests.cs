/* 
 * BitMEX API
 *
 * ## REST API for the BitMEX Trading Platform  [View Changelog](/app/apiChangelog)    #### Getting Started   ##### Fetching Data  All REST endpoints are documented below. You can try out any query right from this interface.  Most table queries accept `count`, `start`, and `reverse` params. Set `reverse=true` to get rows newest-first.  Additional documentation regarding filters, timestamps, and authentication is available in [the main API documentation](https://www.bitmex.com/app/restAPI).  *All* table data is available via the [Websocket](/app/wsAPI). We highly recommend using the socket if you want to have the quickest possible data without being subject to ratelimits.  ##### Return Types  By default, all data is returned as JSON. Send `?_format=csv` to get CSV data or `?_format=xml` to get XML data.  ##### Trade Data Queries  *This is only a small subset of what is available, to get you started.*  Fill in the parameters and click the `Try it out!` button to try any of these queries.  * [Pricing Data](#!/Quote/Quote_get)  * [Trade Data](#!/Trade/Trade_get)  * [OrderBook Data](#!/OrderBook/OrderBook_getL2)  * [Settlement Data](#!/Settlement/Settlement_get)  * [Exchange Statistics](#!/Stats/Stats_history)  Every function of the BitMEX.com platform is exposed here and documented. Many more functions are available.  ##### Swagger Specification  [⇩ Download Swagger JSON](swagger.json)    ## All API Endpoints  Click to expand a section. 
 *
 * OpenAPI spec version: 1.2.0
 * Contact: support@bitmex.com
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */


using NUnit.Framework;

using System;
using System.Linq;
using System.IO;
using System.Collections.Generic;
using IO.Swagger.Api;
using IO.Swagger.Model;
using IO.Swagger.Client;
using System.Reflection;
using Newtonsoft.Json;

namespace IO.Swagger.Test
{
    /// <summary>
    ///  Class for testing User
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by Swagger Codegen.
    /// Please update the test case below to test the model.
    /// </remarks>
    [TestFixture]
    public class UserTests
    {
        // TODO uncomment below to declare an instance variable for User
        //private User instance;

        /// <summary>
        /// Setup before each test
        /// </summary>
        [SetUp]
        public void Init()
        {
            // TODO uncomment below to create an instance of User
            //instance = new User();
        }

        /// <summary>
        /// Clean up after each test
        /// </summary>
        [TearDown]
        public void Cleanup()
        {

        }

        /// <summary>
        /// Test an instance of User
        /// </summary>
        [Test]
        public void UserInstanceTest()
        {
            // TODO uncomment below to test "IsInstanceOfType" User
            //Assert.IsInstanceOfType<User> (instance, "variable 'instance' is a User");
        }


        /// <summary>
        /// Test the property 'Id'
        /// </summary>
        [Test]
        public void IdTest()
        {
            // TODO unit test for the property 'Id'
        }
        /// <summary>
        /// Test the property 'OwnerId'
        /// </summary>
        [Test]
        public void OwnerIdTest()
        {
            // TODO unit test for the property 'OwnerId'
        }
        /// <summary>
        /// Test the property 'Firstname'
        /// </summary>
        [Test]
        public void FirstnameTest()
        {
            // TODO unit test for the property 'Firstname'
        }
        /// <summary>
        /// Test the property 'Lastname'
        /// </summary>
        [Test]
        public void LastnameTest()
        {
            // TODO unit test for the property 'Lastname'
        }
        /// <summary>
        /// Test the property 'Username'
        /// </summary>
        [Test]
        public void UsernameTest()
        {
            // TODO unit test for the property 'Username'
        }
        /// <summary>
        /// Test the property 'Email'
        /// </summary>
        [Test]
        public void EmailTest()
        {
            // TODO unit test for the property 'Email'
        }
        /// <summary>
        /// Test the property 'Phone'
        /// </summary>
        [Test]
        public void PhoneTest()
        {
            // TODO unit test for the property 'Phone'
        }
        /// <summary>
        /// Test the property 'Created'
        /// </summary>
        [Test]
        public void CreatedTest()
        {
            // TODO unit test for the property 'Created'
        }
        /// <summary>
        /// Test the property 'LastUpdated'
        /// </summary>
        [Test]
        public void LastUpdatedTest()
        {
            // TODO unit test for the property 'LastUpdated'
        }
        /// <summary>
        /// Test the property 'Preferences'
        /// </summary>
        [Test]
        public void PreferencesTest()
        {
            // TODO unit test for the property 'Preferences'
        }
        /// <summary>
        /// Test the property 'TFAEnabled'
        /// </summary>
        [Test]
        public void TFAEnabledTest()
        {
            // TODO unit test for the property 'TFAEnabled'
        }
        /// <summary>
        /// Test the property 'AffiliateID'
        /// </summary>
        [Test]
        public void AffiliateIDTest()
        {
            // TODO unit test for the property 'AffiliateID'
        }
        /// <summary>
        /// Test the property 'PgpPubKey'
        /// </summary>
        [Test]
        public void PgpPubKeyTest()
        {
            // TODO unit test for the property 'PgpPubKey'
        }
        /// <summary>
        /// Test the property 'Country'
        /// </summary>
        [Test]
        public void CountryTest()
        {
            // TODO unit test for the property 'Country'
        }

    }

}
