import pandas as pd
import yfinance as yf
import matplotlib as plt
from FinanceTicket.Ticket import Ticket

test = Ticket("AAPL")
test.signal('2y', large_av = 40)
