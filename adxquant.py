

import os
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import requests
import math
from tvDatafeed import TvDatafeed, Interval
from telegram_notifier import TelegramNotifier
from pathlib import Path
from scipy.signal import argrelextrema
import pygsheets
import pathlib
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import socket
import talib as ta
import simplejson
import json
from scipy.stats import linregress

from icecream import ic

from stockdata.quant import Quant


class AdxQuant:
    def get_slowmovingaverage(af):
            emaopen = Quant.ema(af["open"], 10)
            emaclose = Quant.ema(af["close"], 10)
            emahigh = Quant.ema(af["high"], 10)
            emalow = Quant.ema(af["low"], 10)

            af['emaopen'] = emaopen
            af['emaclose'] = emaclose
            af['emahigh'] = emahigh
            af['emalow'] = emalow

            af['ema1'] = Quant.ema(af["close"], 21)
            af['ema2'] = Quant.ema(af["close"], 41)

            len2= 10
            o2=Quant.ema(af['emaopen'], len2)
            c2=Quant.ema(af['emaclose'], len2)
            h2=Quant.ema(af['emahigh'], len2)
            l2=Quant.ema(af['emalow'], len2)

            af['o2'] = o2
            af['c2'] = c2
            af['h2'] = h2
            af['l2'] = l2

            af['doji'] = ta.CDLDOJI(o2, h2, l2, c2)
            af['doji'] = np.where(af['doji'] > 0, af['c2'], 0)
            
            return af
        
    def pullback_avg(af, slowanchorma,veryslowanchorma):
        
        af['fastma'] = Quant.ema(af["c2"], 5)
        af['slowma'] = Quant.ema(af["c2"], 15)
        af['signalma'] = Quant.ema(af["c2"], 60)
        # af['fastanchorma'] = Quant.ema(af["c2"], 41)
        # af['mediumanchorma'] = Quant.ema(af["c2"], 60)
        af['slowanchorma'] = Quant.ema(af["c2"], 100)
        af['superslowanchorma'] = Quant.ema(af["c2"], slowanchorma)
        af['veryslowanchorma'] = Quant.ema(af["c2"], veryslowanchorma)
        
        af['smasell'] = ((af['c2'] < af['signalma']) & (af['c2'].shift(1) > af['signalma'].shift(1)))
        af['smabuy'] = ((af['c2'] > af['signalma']) & (af['c2'].shift(1) < af['signalma'].shift(1)))
        af['smasell'] = np.where(af['smasell'] > 0, af["c2"], 0)
        af['smabuy'] = np.where(af['smabuy'] > 0, af["c2"], 0)


        lastposition = 0
        for i, row in af.iterrows():
            if af.loc[i, "smabuy"] > 0:
                positionvalue = i - lastposition
                if positionvalue < 100:
                    af.loc[i, "smabuy"] = "NaN"
                else:
                    positionvalue = i



        af['anchorsell'] = ((af['close'] < af['slowanchorma']) & (af['close'].shift(1) > af['slowanchorma'].shift(1)))
        af['anchorbuy'] = ((af['close'] >= af['slowanchorma']) & (af['close'].shift(1) < af['slowanchorma'].shift(1)))
        af['anchorsell'] = np.where(af['anchorsell'] > 0, af["close"], 0)
        af['anchorbuy'] = np.where(af['anchorbuy'] > 0, af["close"], 0)

        return af
        
    def standarddeviation(df,deviationfactor):

        df = df.iloc[-1000:]
        df_len = len(df)
        df['number'] = np.arange(df_len)+1
        slope, intercept, r_value, p_value, std_err = linregress(df['number'], df['close'])
        deviation = df['close'].std() * float(deviationfactor)
        deviationx1 = deviation * 2
        for i, row in df.iterrows():
            df.loc[i, "middle"] = intercept + slope* df.loc[i, "number"]
            df.loc[i, "uppertwo"] = (intercept + slope* df.loc[i, "number"]) + deviationx1
            df.loc[i, "upper"] = (intercept + slope* df.loc[i, "number"]) + deviation
            df.loc[i, "lower"] = (intercept + slope* df.loc[i, "number"]) - deviation
            df.loc[i, "lowertwo"] = (intercept + slope* df.loc[i, "number"]) - deviationx1

        print("slope: %f, intercept: %f" % (slope, intercept))
        print("R-squared: %f" % r_value**2)
        print("Deviation : %f" % deviation)
        df.index.rename('index',inplace=True)
        df = df.reset_index()
        df_newlen = len(df) 
        print("df_newlen", df_newlen)
        return df


    def new_indicators(af):

        # fastk, fastd = ta.STOCHRSI(af["close"], timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
        # af['slowk'] = fastk
        # af['slowd'] = fastd
        # # RSI
        # af['rsi'] = ta.RSI(af["c2"])

        # # Inverse Fisher transform on RSI, values [-1.0, 1.0] (https://goo.gl/2JGGoy)
        # rsi = 0.1 * (af['rsi'] - 50)
        # af['fisher_rsi'] = (np.exp(2 * rsi) - 1) / (np.exp(2 * rsi) + 1)

        # Bollinger bands
        # bollinger = qtpylib.bollinger_bands(qtpylib.typical_price(af["close"]), window=20, stds=2)
        
        

        # # SAR Parabol
        # af['sar'] = ta.SAR(af["h2"],af["l2"])

        # Hammer: values [0, 100]
        
        return af

    def analysis1(af,meantrade):

        upperband, middleband, lowerband = ta.BBANDS(af["fastma"], timeperiod=21, nbdevup=5, nbdevdn=5, matype=0)

        af['bb_middleband'] = middleband
        af['bb_lowerband'] = lowerband
        af['bb_upperband'] = upperband

        af['bbema1'] = Quant.ema(af['bb_upperband'], 10)
        af['bbwma1'] = AdxQuant.wma(af['bb_upperband'], 10)
        af['distance'] = af['bb_upperband'] - af['bb_lowerband']
        af['meandistance'] = af['distance'].mean() * meantrade


        af['bbsell'] = ((af['close'] < af['bb_upperband']) & (af['close'].shift(1) > af['bb_upperband'].shift(1)))
        af['bbsell'] = np.where(af['bbsell'] > 0, af["close"], 0)
        for i, row in af.iterrows():
            if af.loc[i, "bbsell"] > 0 and af.loc[i,'distance'] > af.loc[i, "meandistance"]:
                if af.loc[i,'close'] > af.loc[i, "bb_middleband"]:
                    af.loc[i, "sbbsell"] = af.loc[i, "bbsell"]

        af['bbbuy'] = ((af['bb_lowerband'] < af['close']) & (af['bb_lowerband'].shift(1) > af['close'].shift(1)))
        af['bbbuy'] = np.where(af['bbbuy'] > 0, af["close"], 0)
        for i, row in af.iterrows():
            if af.loc[i, "bbbuy"] > 0 and  af.loc[i, "bbbuy"] < af.loc[i, "slowanchorma"] and af.loc[i,'distance'] > af.loc[i, "meandistance"]:
                if af.loc[i,'close'] < af.loc[i, "bb_middleband"]:
                    af.loc[i, "sbbbuy"] = af.loc[i, "bbbuy"]


        for i, row in af.iterrows():
            if af.loc[i, "sbbsell"] > 0:
                af.loc[i, "touchpoint"] = af.loc[i, "close"]
        
        for i, row in af.iterrows():
            if af.loc[i, "sbbbuy"] > 0:
                af.loc[i, "touchpoint"] = af.loc[i, "close"]

        af['ssuperbuy'] = ((af['slowanchorma'] < af['slowma']) & (af['slowanchorma'].shift(1) > af['slowma'].shift(1)))
        af['ssupersell'] = ((af['slowanchorma'] > af['slowma']) & (af['slowanchorma'].shift(1) < af['slowma'].shift(1)))
        af['ssuperbuy'] = np.where(af['ssuperbuy'] > 0, af["c2"], 0)
        af['ssupersell'] = np.where(af['ssupersell'] > 0, af["c2"], 0)

        
        af['vssuperbuy'] = ((af['c2'] > af['veryslowanchorma']) & (af['veryslowanchorma'].shift(2) > af['c2'].shift(2)))
        af['vssupersell'] = ((af['veryslowanchorma'] > af['c2']) & (af['veryslowanchorma'].shift(1) < af['c2'].shift(1)))
        af['superbuy'] = np.where(af['vssuperbuy'] > 0, af["c2"], 0)
        af['supersell'] = np.where(af['vssupersell'] > 0, af["c2"], 0)


        
        af['tsuperbuy'] = ((af['veryslowanchorma'] < af['slowanchorma']) & (af['veryslowanchorma'].shift(1) > af['slowanchorma'].shift(1)))
        af['tsupersell'] = ((af['veryslowanchorma'] > af['slowanchorma']) & (af['veryslowanchorma'].shift(1) < af['slowanchorma'].shift(1)))
        af['tsuperbuy'] = np.where(af['tsuperbuy'] > 0, af["veryslowanchorma"], 0)
        af['tsupersell'] = np.where(af['tsupersell'] > 0, af["veryslowanchorma"], 0)



        # for i, row in af.iterrows():
        #     if af.loc[i, "ssupersell"] > 0 and af.loc[i,'distance'] > (af.loc[i, "meandistance"] * meantrade ) :
        #         af.loc[i,'supersell'] = af.loc[i, "ssupersell"]
            
        #     if af.loc[i, "ssuperbuy"] > 0 and af.loc[i,'distance'] > (af.loc[i, "meandistance"] * meantrade ) :
        #         af.loc[i,'superbuy'] = af.loc[i, "ssuperbuy"]
                    

        # af["slowzigzag"] = peak_valley_pivots(af["slowanchorma"],0.003,-0.003)
        for i, row in af.iterrows():
            if af.loc[i, "tsuperbuy"] >  0 :
                    af.loc[i, "cmin"] =   af.loc[i, "c2"]
            elif af.loc[i, "tsupersell"] > 0 :
                af.loc[i, "cmax"] =  af.loc[i, "c2"]

        trend = 0
        for i, row in af.iterrows():
            if trend == 0 :
                af.loc[i, "trend"] = 0
                if float(af.loc[i, "tsuperbuy"]) > 0 :
                    trend = 1
            elif trend == 1:
                af.loc[i, "trend"] = 1
                if float(af.loc[i, "tsupersell"]) > 0:
                    trend = 2
            elif trend == 2:
                af.loc[i, "trend"] = 2
                if float(af.loc[i, "tsuperbuy"]) > 0:
                    trend = 1

        for i, row in af.iterrows():
            if af.loc[i, "trend"] == 1:
                af.loc[i, "ptrend"] = af.loc[i, "c2"]
            elif af.loc[i, "trend"] == 2:
                af.loc[i, "ntrend"] = af.loc[i, "c2"]


        return af

    def wma(s, period):
        a = s.rolling(period)
        x = 0
        x = np.arange(period) + 1 * x
        x1 = x.sum()
        y = np.arange(period) + 1
        y1 = y.sum()
        wma = s.rolling(period).apply(
            lambda x: ((np.arange(period) + 1) * x).sum()
            / (np.arange(period) + 1).sum(),
            raw=True,
        )
        return wma



    def supertrend(df, atr_period=18, multiplier=3):
        atr_period = float(atr_period)
        multiplier = float(multiplier)
        # issue with forex --

        minclose = df["close"].iloc[-1]
        if minclose < 2:
            high = df["high"] = df["high"] * 1000
            low = df["low"] = df["low"] * 1000
            close = df["close"] = df["close"] * 1000
        else:
            high = df["high"]
            low = df["low"]
            close = df["close"]
        # calculate ATR
        price_diffs = [high - low, high - close.shift(), close.shift() - low]
        tr = pd.concat(price_diffs, axis=1)
        tr = tr.abs().max(axis=1)

        df["tr"] = tr
        df["atr"] = atr = df["tr"].ewm(alpha=1 / atr_period, min_periods=atr_period).mean()

        # df["ema1"] = tradeindicators.ema(df["close"], 100)
        # df["ema2"] = tradeindicators.ema(df["close"], 200)

        # HL2 is simply the average of high and low prices
        df["hl2"] = hl2 = (high + low) / 2
        final_upperband = upperband = hl2 + (multiplier * atr)
        final_lowerband = lowerband = hl2 - (multiplier * atr)
        supertrend = [True] * len(df)
        trade = [True] * len(df)

        for i in range(1, len(df.index)):
            curr, prev = i, i - 1

            # if current close price crosses above upperband
            if close[curr] > final_upperband[prev]:
                supertrend[curr] = 1
            # if current close price crosses below lowerband
            elif close[curr] < final_lowerband[prev]:
                supertrend[curr] = 0
            # else, the trend continues
            else:
                supertrend[curr] = supertrend[prev]
                # adjustment to the final bands
                if supertrend[curr] == 1 and final_lowerband[curr] < final_lowerband[prev]:
                    final_lowerband[curr] = final_lowerband[prev]
                if supertrend[curr] == 0 and final_upperband[curr] > final_upperband[prev]:
                    final_upperband[curr] = final_upperband[prev]

                # remove bands depending on the trend direction for visualization
                if supertrend[curr] == 1:
                    final_upperband[curr] = np.nan
                else:
                    final_lowerband[curr] = np.nan

        df["supertrend"] = supertrend
        df["supertrend1"] = df["supertrend"].shift(periods=1)

        df["final_lowerband"] = final_lowerband
        df["final_upperband"] = final_upperband

        df = pd.DataFrame(df)
        df.reset_index(inplace=True)

        return df


    def supertrendc2(df, atr_period, multiplier):

        atr_period = float(atr_period)
        multiplier = float(multiplier)
        # issue with forex --

        minclose = df.loc[0, "c2"]
        if minclose < 2:
            high = df["h2"] = df["h2"] * 1000
            low = df["l2"] = df["l2"] * 1000
            close = df["c2"] = df["c2"] * 1000
        else:
            high = df["h2"]
            low = df["l2"]
            close = df["c2"]
        # calculate ATR
        price_diffs = [high - low, high - close.shift(), close.shift() - low]
        tr = pd.concat(price_diffs, axis=1)
        tr = tr.abs().max(axis=1)

        df["tr"] = tr
        df["atr"] = atr = df["tr"].ewm(alpha=1 / atr_period, min_periods=atr_period).mean()

        # df["ema1"] = tradeindicators.ema(df["close"], 100)
        # df["ema2"] = tradeindicators.ema(df["close"], 200)

        # HL2 is simply the average of high and low prices
        df["hl2"] = hl2 = (high + low) / 2
        final_upperband = upperband = hl2 + (multiplier * atr)
        final_lowerband = lowerband = hl2 - (multiplier * atr)
        supertrend = [True] * len(df)
        trade = [True] * len(df)

        for i in range(1, len(df.index)):
            curr, prev = i, i - 1

            # if current close price crosses above upperband
            if close[curr] > final_upperband[prev]:
                supertrend[curr] = 1
            # if current close price crosses below lowerband
            elif close[curr] < final_lowerband[prev]:
                supertrend[curr] = 0
            # else, the trend continues
            else:
                supertrend[curr] = supertrend[prev]
                # adjustment to the final bands
                if supertrend[curr] == 1 and final_lowerband[curr] < final_lowerband[prev]:
                    final_lowerband[curr] = final_lowerband[prev]
                if supertrend[curr] == 0 and final_upperband[curr] > final_upperband[prev]:
                    final_upperband[curr] = final_upperband[prev]

                # remove bands depending on the trend direction for visualization
                if supertrend[curr] == 1:
                    final_upperband[curr] = np.nan
                else:
                    final_lowerband[curr] = np.nan
        df["supertrendc2"] = supertrend
        df["supertrend1"] = df["supertrend"].shift(periods=1)
        df["finalc2_lowerband"] = final_lowerband
        df["finalc2_upperband"] = final_upperband
        df = pd.DataFrame(df)
        df.reset_index(inplace=True)

        return df

    def minmaxc2(df):

        price = df.loc[0,"c2"]
        position = 1
        high2 = 0
        for i in range(10, len(df.index)):
            prev1, prev2,prev3,prev4, prev5 = i - 1, i-2, i-3,i-4, i - 5 

            if df.loc[i,"c2"] < df.loc[prev1,"c2"] < df.loc[prev2,"c2"] > df.loc[prev3,"c2"] > df.loc[prev5,"c2"] and df.loc[i,'distance'] > df.loc[i, "meandistance"]:
                price = df.loc[prev5,"c2"]
                df.loc[i,"high2"] = round(price,2)

        return df