# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 20:56:50 2022

@author: charl
"""
import requests
import time
import json
import csv


def checker():
    try:
        with open("Ranking.csv", 'r', newline='') as csvfile:
            csvfile.close()
            return True
    except: 
        with open("Ranking.csv", 'w', newline='') as csvfile:
            fieldnames = ['Rank']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'Rank': 1000000000000})
            csvfile.close()
            return False


def searcher(target=4200,start=0,counter=0):
    checker()
    wallet=1000000000000
    deg=10**(2-counter)
    inc=0
    setoff=0
    limit=deg
    limit=str(limit)
    while(wallet>target):
        time.sleep(0.005)
        setoff=start+deg*inc
        setoff=str(setoff)
        #Le string correspond à l'adresse API, Celle-ci est celle du WLKN, vous pouvez trouver celle du jeton Solana recherché sur Solscan.
        string="https://public-api.solscan.io/token/holders?tokenAddress=EcQCUYv57C4V6RoPxkVUiDwtX1SP8y8FP5AEToYL8Az&offset="+setoff+"&limit="+limit
        requete=requests.get(string)
        content=requete.text
        content=json.loads(content)
        print(content)
        wallet0=content["data"][0]['amount']/1000000000
        wallet=content["data"][-1]['amount']/1000000000
        print(wallet)
        inc+=1        
        if(wallet<target):
            if(((wallet0-wallet)/target)>0.001):
                start=content["data"][0]['rank']
                counter+=1
                if(counter>2):
                    with open('Ranking.csv', 'a', newline='') as csvfile:
                        fieldnames = ['Rank']
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writerow({'Rank': content["data"][-1]['rank']})
                    csvfile.close()
                    return print("\n\n\n\n\n\n\n\n",wallet,"Wallet n°",content["data"][-1]['rank'])
                else:
                    print("\n\n--------------------\n\n  REINCREMENTATION\n\n--------------------\n\n")
                    searcher(target,start,counter)
            else:
                with open('Ranking.csv', 'a', newline='') as csvfile:
                    fieldnames = ['Rank']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)                        
                    writer.writerow({'Rank':content["data"][-1]['rank']})            
                csvfile.close()
                return print("\n\n\n\n\n\n\n\n",wallet,"Wallet n°",content["data"][-1]['rank'])                
    print("\n\n\n",wallet,"Wallet n°",content["data"][-1]['rank'],"\n\n\n\n")   
            
            
def increase(csvname,distance=1):
    listWallet=[]
    token=False
    with open(csvname, 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            listWallet.append(row)
        csvfile.close()
        if(distance=="first"):
            a=int(listWallet[-1][0])-int(listWallet[2][0])
            if(a<-5000000000):
                print("Initialisation, 1er ajout")
            elif(a>0):
                a=(a/int(listWallet[1][0]))*100
            elif(a==0):
                print("Pas de mouvement")
            elif(a<0 and a>-5000000000):
                a=-(a/int(listWallet[1][0]))*100
                token=True
        else:
            a=int(listWallet[-1][0])-int(listWallet[-distance-1][0])
            if(a<-5000000000):
                print("Initialisation, 1er ajout")
            elif(a>0):
                a=(a/int(listWallet[-distance-1][0]))*100
            elif(a==0):
                print("Pas de mouvement")
            elif(a<0 and a>-5000000000):
                a=-(a/int(listWallet[-distance-1][0]))*100
                token=True
    a=round(a,2)
    if(a>0):
        print("Gain de ",a,"%")          
    elif(token):
        print("Perte de ",a,"%")
    
                          

csvname='Ranking.csv'
#target=int(input("La target :"))
searcher(
#    target
    )
increase(csvname)



#checker()




























