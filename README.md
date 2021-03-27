## Coinbase Bitcoin Trading Algo

> ### Simply sells bitcoin when its high, and buys it when its low.

>>Sell order executes at 40% over the 50 day moving average. Increases the
the trigger by 20% each time.

>Buy orders are executed when the price meets or falls below the 50 day.
>>The program allows 3 buys, all separated by a day. After the third buy the
loop is broken and the program needs to be run again.
