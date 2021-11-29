from flask import Flask, render_template
import pandas as pd
from matplotlib import pyplot as plt
#import sqlite3
from os import system
app = Flask(__name__)

plt.style.use('seaborn')

"""df = pd.read_csv('F:\\Office task\\web app task\\BSE-BOM500325.csv')
df.head(100)"""

@app.route('/plot')
def show_data():
  import pyodbc
  try:
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-HRFT6U5;'
                      'Database=RelianceIndustries;'
                      'Trusted_Connection=yes;')
        print('+=========================+')
        print('|  CONNECTED TO DATABASE  |')
        print('+=========================+')
  except Exception as e:
        system.exit('error',e)
   
cursor=conn.cursor()
cursor.execute ('SELECT [Date],[Close] FROM [RelianceIndustries].[dbo].[BSE-BOM500325]')
result = cursor.fetchall()

df = pd.DataFrame(result, columns = ['Date','Close'])
print (df)
          
                    

#conn.commit()
x = df['Date']
y = df['Close']

plt.plot(x,y) 

plt.title('Close Date vs ')       #(title of the plot)
plt.xlabel('Date')                #(lable for x-axis)
plt.ylabel('Close')               #(lable for y-axis)

plt.tight_layout()
plt.show()
