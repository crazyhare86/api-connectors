//
// Position.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation


/** Summary of Open and Closed Positions */

open class Position: Codable {

    public var account: Double
    public var symbol: String
    public var currency: String
    public var underlying: String?
    public var quoteCurrency: String?
    public var commission: Double?
    public var initMarginReq: Double?
    public var maintMarginReq: Double?
    public var riskLimit: Double?
    public var leverage: Double?
    public var crossMargin: Bool?
    public var deleveragePercentile: Double?
    public var rebalancedPnl: Double?
    public var prevRealisedPnl: Double?
    public var prevUnrealisedPnl: Double?
    public var prevClosePrice: Double?
    public var openingTimestamp: Date?
    public var openingQty: Double?
    public var openingCost: Double?
    public var openingComm: Double?
    public var openOrderBuyQty: Double?
    public var openOrderBuyCost: Double?
    public var openOrderBuyPremium: Double?
    public var openOrderSellQty: Double?
    public var openOrderSellCost: Double?
    public var openOrderSellPremium: Double?
    public var execBuyQty: Double?
    public var execBuyCost: Double?
    public var execSellQty: Double?
    public var execSellCost: Double?
    public var execQty: Double?
    public var execCost: Double?
    public var execComm: Double?
    public var currentTimestamp: Date?
    public var currentQty: Double?
    public var currentCost: Double?
    public var currentComm: Double?
    public var realisedCost: Double?
    public var unrealisedCost: Double?
    public var grossOpenCost: Double?
    public var grossOpenPremium: Double?
    public var grossExecCost: Double?
    public var isOpen: Bool?
    public var markPrice: Double?
    public var markValue: Double?
    public var riskValue: Double?
    public var homeNotional: Double?
    public var foreignNotional: Double?
    public var posState: String?
    public var posCost: Double?
    public var posCost2: Double?
    public var posCross: Double?
    public var posInit: Double?
    public var posComm: Double?
    public var posLoss: Double?
    public var posMargin: Double?
    public var posMaint: Double?
    public var posAllowance: Double?
    public var taxableMargin: Double?
    public var initMargin: Double?
    public var maintMargin: Double?
    public var sessionMargin: Double?
    public var targetExcessMargin: Double?
    public var varMargin: Double?
    public var realisedGrossPnl: Double?
    public var realisedTax: Double?
    public var realisedPnl: Double?
    public var unrealisedGrossPnl: Double?
    public var longBankrupt: Double?
    public var shortBankrupt: Double?
    public var taxBase: Double?
    public var indicativeTaxRate: Double?
    public var indicativeTax: Double?
    public var unrealisedTax: Double?
    public var unrealisedPnl: Double?
    public var unrealisedPnlPcnt: Double?
    public var unrealisedRoePcnt: Double?
    public var simpleQty: Double?
    public var simpleCost: Double?
    public var simpleValue: Double?
    public var simplePnl: Double?
    public var simplePnlPcnt: Double?
    public var avgCostPrice: Double?
    public var avgEntryPrice: Double?
    public var breakEvenPrice: Double?
    public var marginCallPrice: Double?
    public var liquidationPrice: Double?
    public var bankruptPrice: Double?
    public var timestamp: Date?
    public var lastPrice: Double?
    public var lastValue: Double?


    // Encodable protocol methods

    public func encode(to encoder: Encoder) throws {

        var container = encoder.container(keyedBy: String.self)

        try container.encode(account, forKey: "account")
        try container.encode(symbol, forKey: "symbol")
        try container.encode(currency, forKey: "currency")
        try container.encodeIfPresent(underlying, forKey: "underlying")
        try container.encodeIfPresent(quoteCurrency, forKey: "quoteCurrency")
        try container.encodeIfPresent(commission, forKey: "commission")
        try container.encodeIfPresent(initMarginReq, forKey: "initMarginReq")
        try container.encodeIfPresent(maintMarginReq, forKey: "maintMarginReq")
        try container.encodeIfPresent(riskLimit, forKey: "riskLimit")
        try container.encodeIfPresent(leverage, forKey: "leverage")
        try container.encodeIfPresent(crossMargin, forKey: "crossMargin")
        try container.encodeIfPresent(deleveragePercentile, forKey: "deleveragePercentile")
        try container.encodeIfPresent(rebalancedPnl, forKey: "rebalancedPnl")
        try container.encodeIfPresent(prevRealisedPnl, forKey: "prevRealisedPnl")
        try container.encodeIfPresent(prevUnrealisedPnl, forKey: "prevUnrealisedPnl")
        try container.encodeIfPresent(prevClosePrice, forKey: "prevClosePrice")
        try container.encodeIfPresent(openingTimestamp, forKey: "openingTimestamp")
        try container.encodeIfPresent(openingQty, forKey: "openingQty")
        try container.encodeIfPresent(openingCost, forKey: "openingCost")
        try container.encodeIfPresent(openingComm, forKey: "openingComm")
        try container.encodeIfPresent(openOrderBuyQty, forKey: "openOrderBuyQty")
        try container.encodeIfPresent(openOrderBuyCost, forKey: "openOrderBuyCost")
        try container.encodeIfPresent(openOrderBuyPremium, forKey: "openOrderBuyPremium")
        try container.encodeIfPresent(openOrderSellQty, forKey: "openOrderSellQty")
        try container.encodeIfPresent(openOrderSellCost, forKey: "openOrderSellCost")
        try container.encodeIfPresent(openOrderSellPremium, forKey: "openOrderSellPremium")
        try container.encodeIfPresent(execBuyQty, forKey: "execBuyQty")
        try container.encodeIfPresent(execBuyCost, forKey: "execBuyCost")
        try container.encodeIfPresent(execSellQty, forKey: "execSellQty")
        try container.encodeIfPresent(execSellCost, forKey: "execSellCost")
        try container.encodeIfPresent(execQty, forKey: "execQty")
        try container.encodeIfPresent(execCost, forKey: "execCost")
        try container.encodeIfPresent(execComm, forKey: "execComm")
        try container.encodeIfPresent(currentTimestamp, forKey: "currentTimestamp")
        try container.encodeIfPresent(currentQty, forKey: "currentQty")
        try container.encodeIfPresent(currentCost, forKey: "currentCost")
        try container.encodeIfPresent(currentComm, forKey: "currentComm")
        try container.encodeIfPresent(realisedCost, forKey: "realisedCost")
        try container.encodeIfPresent(unrealisedCost, forKey: "unrealisedCost")
        try container.encodeIfPresent(grossOpenCost, forKey: "grossOpenCost")
        try container.encodeIfPresent(grossOpenPremium, forKey: "grossOpenPremium")
        try container.encodeIfPresent(grossExecCost, forKey: "grossExecCost")
        try container.encodeIfPresent(isOpen, forKey: "isOpen")
        try container.encodeIfPresent(markPrice, forKey: "markPrice")
        try container.encodeIfPresent(markValue, forKey: "markValue")
        try container.encodeIfPresent(riskValue, forKey: "riskValue")
        try container.encodeIfPresent(homeNotional, forKey: "homeNotional")
        try container.encodeIfPresent(foreignNotional, forKey: "foreignNotional")
        try container.encodeIfPresent(posState, forKey: "posState")
        try container.encodeIfPresent(posCost, forKey: "posCost")
        try container.encodeIfPresent(posCost2, forKey: "posCost2")
        try container.encodeIfPresent(posCross, forKey: "posCross")
        try container.encodeIfPresent(posInit, forKey: "posInit")
        try container.encodeIfPresent(posComm, forKey: "posComm")
        try container.encodeIfPresent(posLoss, forKey: "posLoss")
        try container.encodeIfPresent(posMargin, forKey: "posMargin")
        try container.encodeIfPresent(posMaint, forKey: "posMaint")
        try container.encodeIfPresent(posAllowance, forKey: "posAllowance")
        try container.encodeIfPresent(taxableMargin, forKey: "taxableMargin")
        try container.encodeIfPresent(initMargin, forKey: "initMargin")
        try container.encodeIfPresent(maintMargin, forKey: "maintMargin")
        try container.encodeIfPresent(sessionMargin, forKey: "sessionMargin")
        try container.encodeIfPresent(targetExcessMargin, forKey: "targetExcessMargin")
        try container.encodeIfPresent(varMargin, forKey: "varMargin")
        try container.encodeIfPresent(realisedGrossPnl, forKey: "realisedGrossPnl")
        try container.encodeIfPresent(realisedTax, forKey: "realisedTax")
        try container.encodeIfPresent(realisedPnl, forKey: "realisedPnl")
        try container.encodeIfPresent(unrealisedGrossPnl, forKey: "unrealisedGrossPnl")
        try container.encodeIfPresent(longBankrupt, forKey: "longBankrupt")
        try container.encodeIfPresent(shortBankrupt, forKey: "shortBankrupt")
        try container.encodeIfPresent(taxBase, forKey: "taxBase")
        try container.encodeIfPresent(indicativeTaxRate, forKey: "indicativeTaxRate")
        try container.encodeIfPresent(indicativeTax, forKey: "indicativeTax")
        try container.encodeIfPresent(unrealisedTax, forKey: "unrealisedTax")
        try container.encodeIfPresent(unrealisedPnl, forKey: "unrealisedPnl")
        try container.encodeIfPresent(unrealisedPnlPcnt, forKey: "unrealisedPnlPcnt")
        try container.encodeIfPresent(unrealisedRoePcnt, forKey: "unrealisedRoePcnt")
        try container.encodeIfPresent(simpleQty, forKey: "simpleQty")
        try container.encodeIfPresent(simpleCost, forKey: "simpleCost")
        try container.encodeIfPresent(simpleValue, forKey: "simpleValue")
        try container.encodeIfPresent(simplePnl, forKey: "simplePnl")
        try container.encodeIfPresent(simplePnlPcnt, forKey: "simplePnlPcnt")
        try container.encodeIfPresent(avgCostPrice, forKey: "avgCostPrice")
        try container.encodeIfPresent(avgEntryPrice, forKey: "avgEntryPrice")
        try container.encodeIfPresent(breakEvenPrice, forKey: "breakEvenPrice")
        try container.encodeIfPresent(marginCallPrice, forKey: "marginCallPrice")
        try container.encodeIfPresent(liquidationPrice, forKey: "liquidationPrice")
        try container.encodeIfPresent(bankruptPrice, forKey: "bankruptPrice")
        try container.encodeIfPresent(timestamp, forKey: "timestamp")
        try container.encodeIfPresent(lastPrice, forKey: "lastPrice")
        try container.encodeIfPresent(lastValue, forKey: "lastValue")
    }

    // Decodable protocol methods
    
    public required init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: String.self)

        account = try container.decode(Double.self, forKey: "account")
        symbol = try container.decode(String.self, forKey: "symbol")
        currency = try container.decode(String.self, forKey: "currency")
        underlying = try container.decodeIfPresent(String.self, forKey: "underlying")
        quoteCurrency = try container.decodeIfPresent(String.self, forKey: "quoteCurrency")
        commission = try container.decodeIfPresent(Double.self, forKey: "commission")
        initMarginReq = try container.decodeIfPresent(Double.self, forKey: "initMarginReq")
        maintMarginReq = try container.decodeIfPresent(Double.self, forKey: "maintMarginReq")
        riskLimit = try container.decodeIfPresent(Double.self, forKey: "riskLimit")
        leverage = try container.decodeIfPresent(Double.self, forKey: "leverage")
        crossMargin = try container.decodeIfPresent(Bool.self, forKey: "crossMargin")
        deleveragePercentile = try container.decodeIfPresent(Double.self, forKey: "deleveragePercentile")
        rebalancedPnl = try container.decodeIfPresent(Double.self, forKey: "rebalancedPnl")
        prevRealisedPnl = try container.decodeIfPresent(Double.self, forKey: "prevRealisedPnl")
        prevUnrealisedPnl = try container.decodeIfPresent(Double.self, forKey: "prevUnrealisedPnl")
        prevClosePrice = try container.decodeIfPresent(Double.self, forKey: "prevClosePrice")
        openingTimestamp = try container.decodeIfPresent(Date.self, forKey: "openingTimestamp")
        openingQty = try container.decodeIfPresent(Double.self, forKey: "openingQty")
        openingCost = try container.decodeIfPresent(Double.self, forKey: "openingCost")
        openingComm = try container.decodeIfPresent(Double.self, forKey: "openingComm")
        openOrderBuyQty = try container.decodeIfPresent(Double.self, forKey: "openOrderBuyQty")
        openOrderBuyCost = try container.decodeIfPresent(Double.self, forKey: "openOrderBuyCost")
        openOrderBuyPremium = try container.decodeIfPresent(Double.self, forKey: "openOrderBuyPremium")
        openOrderSellQty = try container.decodeIfPresent(Double.self, forKey: "openOrderSellQty")
        openOrderSellCost = try container.decodeIfPresent(Double.self, forKey: "openOrderSellCost")
        openOrderSellPremium = try container.decodeIfPresent(Double.self, forKey: "openOrderSellPremium")
        execBuyQty = try container.decodeIfPresent(Double.self, forKey: "execBuyQty")
        execBuyCost = try container.decodeIfPresent(Double.self, forKey: "execBuyCost")
        execSellQty = try container.decodeIfPresent(Double.self, forKey: "execSellQty")
        execSellCost = try container.decodeIfPresent(Double.self, forKey: "execSellCost")
        execQty = try container.decodeIfPresent(Double.self, forKey: "execQty")
        execCost = try container.decodeIfPresent(Double.self, forKey: "execCost")
        execComm = try container.decodeIfPresent(Double.self, forKey: "execComm")
        currentTimestamp = try container.decodeIfPresent(Date.self, forKey: "currentTimestamp")
        currentQty = try container.decodeIfPresent(Double.self, forKey: "currentQty")
        currentCost = try container.decodeIfPresent(Double.self, forKey: "currentCost")
        currentComm = try container.decodeIfPresent(Double.self, forKey: "currentComm")
        realisedCost = try container.decodeIfPresent(Double.self, forKey: "realisedCost")
        unrealisedCost = try container.decodeIfPresent(Double.self, forKey: "unrealisedCost")
        grossOpenCost = try container.decodeIfPresent(Double.self, forKey: "grossOpenCost")
        grossOpenPremium = try container.decodeIfPresent(Double.self, forKey: "grossOpenPremium")
        grossExecCost = try container.decodeIfPresent(Double.self, forKey: "grossExecCost")
        isOpen = try container.decodeIfPresent(Bool.self, forKey: "isOpen")
        markPrice = try container.decodeIfPresent(Double.self, forKey: "markPrice")
        markValue = try container.decodeIfPresent(Double.self, forKey: "markValue")
        riskValue = try container.decodeIfPresent(Double.self, forKey: "riskValue")
        homeNotional = try container.decodeIfPresent(Double.self, forKey: "homeNotional")
        foreignNotional = try container.decodeIfPresent(Double.self, forKey: "foreignNotional")
        posState = try container.decodeIfPresent(String.self, forKey: "posState")
        posCost = try container.decodeIfPresent(Double.self, forKey: "posCost")
        posCost2 = try container.decodeIfPresent(Double.self, forKey: "posCost2")
        posCross = try container.decodeIfPresent(Double.self, forKey: "posCross")
        posInit = try container.decodeIfPresent(Double.self, forKey: "posInit")
        posComm = try container.decodeIfPresent(Double.self, forKey: "posComm")
        posLoss = try container.decodeIfPresent(Double.self, forKey: "posLoss")
        posMargin = try container.decodeIfPresent(Double.self, forKey: "posMargin")
        posMaint = try container.decodeIfPresent(Double.self, forKey: "posMaint")
        posAllowance = try container.decodeIfPresent(Double.self, forKey: "posAllowance")
        taxableMargin = try container.decodeIfPresent(Double.self, forKey: "taxableMargin")
        initMargin = try container.decodeIfPresent(Double.self, forKey: "initMargin")
        maintMargin = try container.decodeIfPresent(Double.self, forKey: "maintMargin")
        sessionMargin = try container.decodeIfPresent(Double.self, forKey: "sessionMargin")
        targetExcessMargin = try container.decodeIfPresent(Double.self, forKey: "targetExcessMargin")
        varMargin = try container.decodeIfPresent(Double.self, forKey: "varMargin")
        realisedGrossPnl = try container.decodeIfPresent(Double.self, forKey: "realisedGrossPnl")
        realisedTax = try container.decodeIfPresent(Double.self, forKey: "realisedTax")
        realisedPnl = try container.decodeIfPresent(Double.self, forKey: "realisedPnl")
        unrealisedGrossPnl = try container.decodeIfPresent(Double.self, forKey: "unrealisedGrossPnl")
        longBankrupt = try container.decodeIfPresent(Double.self, forKey: "longBankrupt")
        shortBankrupt = try container.decodeIfPresent(Double.self, forKey: "shortBankrupt")
        taxBase = try container.decodeIfPresent(Double.self, forKey: "taxBase")
        indicativeTaxRate = try container.decodeIfPresent(Double.self, forKey: "indicativeTaxRate")
        indicativeTax = try container.decodeIfPresent(Double.self, forKey: "indicativeTax")
        unrealisedTax = try container.decodeIfPresent(Double.self, forKey: "unrealisedTax")
        unrealisedPnl = try container.decodeIfPresent(Double.self, forKey: "unrealisedPnl")
        unrealisedPnlPcnt = try container.decodeIfPresent(Double.self, forKey: "unrealisedPnlPcnt")
        unrealisedRoePcnt = try container.decodeIfPresent(Double.self, forKey: "unrealisedRoePcnt")
        simpleQty = try container.decodeIfPresent(Double.self, forKey: "simpleQty")
        simpleCost = try container.decodeIfPresent(Double.self, forKey: "simpleCost")
        simpleValue = try container.decodeIfPresent(Double.self, forKey: "simpleValue")
        simplePnl = try container.decodeIfPresent(Double.self, forKey: "simplePnl")
        simplePnlPcnt = try container.decodeIfPresent(Double.self, forKey: "simplePnlPcnt")
        avgCostPrice = try container.decodeIfPresent(Double.self, forKey: "avgCostPrice")
        avgEntryPrice = try container.decodeIfPresent(Double.self, forKey: "avgEntryPrice")
        breakEvenPrice = try container.decodeIfPresent(Double.self, forKey: "breakEvenPrice")
        marginCallPrice = try container.decodeIfPresent(Double.self, forKey: "marginCallPrice")
        liquidationPrice = try container.decodeIfPresent(Double.self, forKey: "liquidationPrice")
        bankruptPrice = try container.decodeIfPresent(Double.self, forKey: "bankruptPrice")
        timestamp = try container.decodeIfPresent(Date.self, forKey: "timestamp")
        lastPrice = try container.decodeIfPresent(Double.self, forKey: "lastPrice")
        lastValue = try container.decodeIfPresent(Double.self, forKey: "lastValue")
    }
}

