# Ranking-on-Solscan

Wallet-Ranking-Searcher. The purpose of this code is to allow to determine the floor wallet of a token on Solscan. The program is using the Solscan Public API. The defaut
target amount in wallet is 4200 but it can be change by changing the value of "Target" : Uncomment the line 115 and 117. Then, when you'll launch the program, it'll ask you
to chose the target price you aim to reach. 

If you want to keep researching the same amount of token anytime. Keep the line 115 and 117 commented but change the default value of target in the definition of searcher().

The progression will be stored in a CSV file, then, if you use the program another day or week for example, it will compare the new ranking with the one of the last time.
If you want to compare the first ranking found with the latest one, simply add "first" as second argument of increase(). 
Enjoy !
