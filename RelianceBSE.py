from flask import Flask, render_template
from os import system
from matplotlib import pyplot as plt
import pyodbc

app = Flask(__name__)
try:
        conn = pyodbc.connect('Driver={SQL Server};'
                'Server=DESKTOP-HRFT6U5;'
                'Database=RelianceIndustries;'
                'Trusted_Connection=yes;')
        print('+=========================+')
        print('|  CONNECTED TO DATABASE  |')
        print('+=========================+')
        mycursor=conn.cursor()
except Exception as e:
        system.exit('error',e)
        
@app.route('/')
def show_index():
 return render_template('index.html')

@app.route('/display')
def show_Reliance_data():  
   mycursor.execute ('SELECT TOP (100) [Date],[Open],[High],[Low],[Close],[WAP],[No  of Shares],[No  of Trades],[Total Turnover],[Deliverable Quantity],[% Deli  Qty to Traded Qty],[Spread H-L],[Spread C-O] FROM [RelianceIndustries].[dbo].[BSE-BOM500325]')
   result = mycursor.fetchall()
   return render_template('displayData.html', result=result)   

@app.route('/showGraph')
def show_graph():
        #print('Inside graph')     
        mycursor.execute ('SELECT TOP (5) [Date],[Close] FROM [RelianceIndustries].[dbo].[BSE-BOM500325]')
        result =mycursor.fetchall()
        Date = []
        Close = []
        for i in result:
                Date.append(i[0])
                Close.append(i[1]) 

        # Visulizing Data using Matplotlib
        plt.bar(Date, Close)
        plt.ylim(0, 5)
        plt.xlabel("Date")
        plt.ylabel("Close")
        plt.title("Close v/s Date")
        plt.show()
        return      

if __name__ == '__main__':
   app.run(debug=True,port=5001)

