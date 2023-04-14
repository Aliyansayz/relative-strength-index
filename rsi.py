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
     
def shift(self, array , place):
    array = np.array(array , dtype= np.float16 )
    array =  array.astype(np.float16)
    shifted = np.roll(array, place)
    shifted[0:place] = np.nan

    return shifted

    
def rsi(self , bar  , period ):
    import numpy as np
    # highs , lows =   np.array(abs(bar.High - self.shift( array=bar.High , place=1 )) , dtype=np.float16 ) , 
    # np.array(abs( self.shift(array=bar.Low , place=1 ) - bar.Low ) , dtype=np.float16 )

    diff =  np.array( bar.Close - self.shift( array=bar.Close , place=1 )   , dtype=np.float16 )
    gain = np.where(diff > 0.0 , diff , 0.0 )
    loss = np.where(diff < 0.0 , abs(diff) , 0.0 )

    avg_gain =  self.sma( gain , period )
    avg_loss =  self.sma( loss , period )
    rs =  np.round(avg_gain / avg_loss , 2)
    relative_strength_index = np.round( 100 - 100/(1+rs) , 2 )
    return relative_strength_index
