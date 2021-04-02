import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

class Ticket:
    
    def __init__(self, company):
        self.company = company
        self.ticker = yf.Ticker(self.company)
        
    def plot(self, period):
        df = self.ticker.history(period=period)
        df['Close'].plot(title="Stock Price") #Add name here and decorate
        
    def signal(self, period, small_av = 10, large_av = 50):
        df = self.ticker.history(period=period)
        
        df['MA10'] = df['Close'].rolling(small_av).mean()
        df['MA50'] = df['Close'].rolling(large_av).mean()
        
        df['Long'] = [1 if df.loc[ei, 'MA10']>df.loc[ei, 'MA50'] else -1 
                      for ei in df.index]
        
        if df.iloc[0, 9] ==1:
            print('You should buy now and keep')
        else:
            print('You should sell now and wait')
            
        df['Close'].plot(label='Close')
        df['MA10'].plot(label='MA10')
        df['MA50'].plot(label='MA50')
        plt.legend()
        plt.show()
