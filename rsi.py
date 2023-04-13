import numpy as np
"""
rsi = rsi(bar  , period= 14 )

rsi = rsi(bar  , period= 2 ) # below 30 / 45 tells oversold above 70 / 55 tells overbought

"""
def sma (array, period ):

    sma = np.empty_like(array)
    sma = np.full( sma.shape , np.nan)
    # Calculate the EMA for each window of 14 values
    for i in range(period, len(array)+1 ):
          sma[i-1] = np.mean(array[i-period:i] , dtype=np.float16)
    return sma 
     

def rsi(bar  , period):
    highs , lows =   np.array(abs(bar["High"] - bar["High"].shift(1)), dtype=np.float16)  
    , np.array(abs(bar["Low"].shift(1) - bar["Low"]), dtype=np.float16 )

    diff =  np.array( bar['Close'] -  bar['Close'].shift(1) , dtype=np.float16 )
    gain = np.where(diff > 0.0 , diff , 0.0 )
    loss = np.where(diff < 0.0 , diff , 0.0 )

    avg_gain =  sma(array= gain , period )
    avg_loss =  sma(array= loss , period )
    rs =  round(avg_gain / avg_loss , 2)
    relative_strength_index = round( 100 - 100/(1+rs) , 2 )
    return relative_strength_index
