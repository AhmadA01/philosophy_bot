# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 22:50:49 2021

@author: ahmed
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 20:07:52 2021

@author: ahmed
"""
#import docx2txt 
#doc = docx2txt.process(r"C:\Users\ahmed\Desktop\PhD\felsefe\yeni test -2020-01.docx")
#doc2 = docx2txt.process(r"C:\Users\ahmed\Desktop\PhD\felsefe\felsefe500.docx")
import pickle
import os
PORT = int(os.environ.get('PORT', 5000))
#pickle.dump(doc, open("doc1.pk", "wb"))
#pickle.dump(doc2, open("doc2.pk", "wb"))
doc=pickle.load(open("doc1.pk", "rb"))
doc2=pickle.load(open("doc2.pk", "rb"))
sual_n= [str(i)+"." for i in range(1,501)]
suallar=[]
prevv=0
nextt=0
for i in range(1,len(doc)):
    if doc[i:i+4] in sual_n:
        suallar.append(doc[prevv:i-1])
        sual_n.remove(doc[i:i+4])
        prevv=i
    elif doc[i:i+3] in sual_n:
        suallar.append(doc[prevv:i-1])
        sual_n.remove(doc[i:i+3])
        prevv=i
    elif doc[i:i+2] in sual_n:
        #print(doc[i:i+2], prevv, i-1)
        suallar.append(doc[prevv:i-1])
        sual_n.remove(doc[i:i+2])
        prevv=i
    if i==(len(doc)-1):
        suallar.append(doc[prevv:len(doc)])
suallar.pop(10)        
cavablar=[]   
import emoji
for i in range(1,len(doc2)):
        if doc2[i]=='√':
            s=doc2[i:i+300]
            tmp= s.split("\n\n\t\t")[0].split("\n\n•\n\n")[0]
            fin =emoji.emojize(' :key: ')
            fin+=tmp
            fin=fin.replace('√',"")
            cavablar.append(fin)
import numpy as np
n=np.random.randint(1,501)
print(suallar[n])
print(cavablar[n])
import pandas as pd
felsefe= pd.DataFrame()
felsefe['sual']=suallar
felsefe['cavab']=cavablar
felsefe.to_pickle("suallar.pkl")
foo = list(range(1,501))
  
selected = np.random.choice(foo)
foo.remove(selected)
def get_sual():
#    n=np.random.randint(1,501)
    n = np.random.choice(foo)
    foo.remove(n)
    sual= suallar[n]
    sual2=sual.split("\n\n")
    variantlar=sual2[1].split('•')
    var_final=[]
    for i in variantlar:
        if i!="":
            a=i.split("  ")
            for t in a:
              var_final.append(t.strip())  
#    print(cavablar[n][1:].lstrip())
    return [var_final,cavablar[n][1:].lstrip(), sual2[0].strip()]
def get_sual2():
#    n=np.random.randint(1,501)
    n = np.random.choice(foo)
    foo.remove(n)    
    sual= suallar[n]
    sual2=sual.split("\n\n")
    for kk in range(len(sual2)):
        sual2[kk]=" ".join(sual2[kk].split()) 
    variantlar=("•".join(sual2[1:])).split('•')
    sual_text=[]
    sual_text.append(sual2[0].strip())
    var_final=[]
    nn=1
    for i in variantlar:
        if i!="":
            a=i.split("  ")
            for t in a:
              var_final.append(t.strip()) 
              sual_text.append(emoji.emojize(' :key: ')+t.strip())
              nn+=1
    sual_text2=[]
    if len(sual_text)<6:
        anss=cavablar[n][2:].strip()
        sual_text2.append(sual_text[0])
        for h in sual_text[1:]:
            if anss in h:
                tmp = h.split()
                sual_text2.append(h.replace(anss,""))
                sual_text2.append(emoji.emojize(' :key: ')+anss)
            else:
                sual_text2.append(h)
        sual_text=sual_text2
#    print(cavablar[n][1:].lstrip())
    return [sual_text,cavablar[n].strip()]
temp = get_sual2()
print(emoji.emojize('Python is :unlock:'))
def get_sual3(n):
    sual= suallar[n]
    sual2=sual.split("\n\n")
    for kk in range(len(sual2)):
        sual2[kk]=" ".join(sual2[kk].split()) 
    variantlar=("•".join(sual2[1:])).split('•')
    sual_text=[]
    sual_text.append(sual2[0].strip())
    var_final=[]
    nn=1
    for i in variantlar:
            if i!="":
                a=i.split("  ")
                for t in a:
                  var_final.append(t.strip()) 
                  sual_text.append(emoji.emojize(' :key: ')+t.strip())
                  nn+=1
    sual_text2=[]
    if len(sual_text)<6:
        anss=cavablar[n][2:].strip()
        sual_text2.append(sual_text[0])
        for h in sual_text[1:]:
            if anss in h:
                tmp = h.split()
                sual_text2.append(h.replace(anss,""))
                sual_text2.append(emoji.emojize(' :key: ')+anss)
            else:
                sual_text2.append(h)
        sual_text=sual_text2
#    print(cavablar[n][1:].lstrip())
    return [sual_text,cavablar[n].strip()]
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from random import seed
from telegram.ext import Updater, CommandHandler,MessageHandler, Filters
from telegram import File

import sqlite3
import pandas as pd

#record = sqlite3.connect("phd.db")
#cur = record.cursor()

#sql1="select * from  t1"
#cur.execute(sql1)
#results = cur.fetchall()
#results

#cur.execute("select * from t1")
#results = cur.fetchall()
#results
#record = sqlite3.connect("phd.db")
#cur = record.cursor()
#cur.execute("create table t2 (user_id,last_sual, last_sual_num)")
#cur.execute('commit')
#record.close()

#last_sual=""
#last_sual_num=1
def get_link(update,context):
    try:
#        print(update) 
        link = update.message.text
        if last_sual.startswith(link):
            update.message.reply_text("Düz tapdınız 😊")
            update.message.reply_text("Əvvəlki sual - /previous")
            
            update.message.reply_text("Yeni sual - /random")
        elif (emoji.emojize(':key: ')+last_sual).startswith(link):
            update.message.reply_text("Düz tapdınız 😊")
            update.message.reply_text("Əvvəlki sual - /previous")
            
            update.message.reply_text("Yeni sual - /random")
            
        else:
            update.message.reply_text("Səhv tapdınız")
            update.message.reply_text("Əvvəlki sual - /previous")
            update.message.reply_text("Əvvəlki sualın cavabı - /answer")
            update.message.reply_text("Yeni sual - /random")
            

    except Exception as e:
        update.message.reply_text(str(e))
        print(str(e), "problem")

def startt(update, context):
#    print(update)
    update.message.reply_text("Salam "+ str(update['message']['chat']['first_name'])+" 😊")
    update.message.reply_text("Aşağıdakı komandalardan istifadə edə bilərsiniz")
    update.message.reply_text("Yeni sual əldə etmək- /random")
    update.message.reply_text("Əvvəlki suala qayitmaq- /previous")
    update.message.reply_text("Sualın cavabına baxmaq- /answer")

def start(update, context):
    #print(update)
    my_sual= get_sual2()
    #global last_sual
    #global last_sual_num
    ind=my_sual[0][0].index(".")
    last_sual=my_sual[1]
    last_sual_num=int(my_sual[0][0][:ind])
    record = sqlite3.connect("phd.db")
    cur = record.cursor()
    
    sql1="select * from  t1 where user_id=?"
    task1= (str(update['message']['chat']['first_name']),)
    #task1= (str(1324),)
    cur.execute(sql1,task1)
    results = cur.fetchall()
    record.close()
    record = sqlite3.connect("phd.db")
    cur = record.cursor()
    if len(results)>0:
        #print(i)
        sql="update t1 set last_sual =?, last_sual_num=? where user_id=?"
        task=(last_sual,last_sual_num,str(update['message']['chat']['first_name']))
    else:
        sql = ''' insert into t1 (user_id,last_sual, last_sual_num)
              VALUES(?,?,?) '''
        task =(str(update['message']['chat']['first_name']), last_sual, last_sual_num)
    #task =(str(1324), last_sual, last_sual_num)
    cur.execute(sql, task)
    cur.execute('commit')
    record.close()
          
   # cur.execute("insert into t1 (user_id,last_sual, last_sual_num) values ('naber', 'malekzadeh')")
    
    #all_text=""
    #for i in my_sual[0]:
        #all_text+=i
        #update.message.reply_text(i)
    update.message.reply_text("\n".join(my_sual[0]))
    update.message.reply_text("Sualın cavabı - /answer")
def start2(update, context):
#    print(update)
    sql1="select * from  t1 where user_id=?"
    task1= (str(update['message']['chat']['first_name']),)
    record = sqlite3.connect("phd.db")
    cur = record.cursor()
    #task1= (str(1324),)
    cur.execute(sql1,task1)
    results = cur.fetchall()
    #results[0][-1]==243
    my_sual= get_sual3(results[0][-1]-1)
    sql2="update t1 set last_sual =? where user_id=?"
    task2=(my_sual[1],str(update['message']['chat']['first_name']))
    cur.execute(sql2,task2)
    cur.execute('commit')
    record.close()
    #global last_sual
    #last_sual=my_sual[1]
    #for i in my_sual[0]:
    #    update.message.reply_text(i)
    update.message.reply_text("\n".join(my_sual[0]))
    update.message.reply_text("Sualın cavabı - /answer")
def start3(update, context):
    sql3="select * from  t1 where user_id=?"
    task3= (str(update['message']['chat']['first_name']),)
    record = sqlite3.connect("phd.db")
    cur = record.cursor()
    #task1= (str(1324),)
    cur.execute(sql3,task3)
    results = cur.fetchall()
    #results[0][-1]==243
    last_sual1= results[0][1]
    record.close()
    update.message.reply_text(last_sual1)
    update.message.reply_text("Yeni sual - /random")
def main():
    updater = Updater("1911649371:AAHCRahT-rpWGhdxHFZ4ddDqZIHyxjHzc0Q", use_context=True)
    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', startt))
    dp.add_handler(CommandHandler('random', start))
    dp.add_handler(CommandHandler('previous', start2))
    dp.add_handler(CommandHandler('answer', start3))
    #dp.add_handler(MessageHandler(Filters.text, get_link))
    #updater.start_polling()
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path='1911649371:AAHCRahT-rpWGhdxHFZ4ddDqZIHyxjHzc0Q')
    updater.bot.setWebhook('https://philosophy1.herokuapp.com/' + '1911649371:AAHCRahT-rpWGhdxHFZ4ddDqZIHyxjHzc0Q')
    updater.idle()
    
if __name__=='__main__':
    main()
    
