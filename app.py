from flask import Flask, request, render_template 
import pandas as pd 
import sqlite3

app = Flask(__name__,template_folder='template') 

#home root
@app.route('/')
def homepage():
    return render_template("home.html")

#documentation
@app.route('/docs')
def docs():
    return render_template("docs.html")

#mendapatkan data rata-rata umur perjabatan (statis)
@app.route('/average_age_title')
def average():
    conn = sqlite3.connect("data/chinook.db")
    query = "SELECT LastName, FirstName,BirthDate,Title FROM employees" # select (columns) from (table)
    employee = pd.read_sql_query(query, conn)
    employee['BirthDate'] = employee['BirthDate'].astype('datetime64')
    this_year=2020
    born_year = employee['BirthDate'].dt.year
    employee['Age'] = this_year - born_year
    employee_age_mean = employee.groupby(['Title']).mean()
    return (employee_age_mean.to_json())

#menentukan genre apa yang paling banyak digemari i suatu negara (statis)
@app.route('/fav_genre/country')
def fav_gen():
    conn = sqlite3.connect("data/chinook.db")
    query = """
    SELECT i.InvoiceId,Country,BillingCity,tracks.Name as Tracks,Milliseconds,Bytes,genres.Name as Genre,InvoiceDate,Total
    FROM customers
    LEFT JOIN invoices as i ON i.CustomerId = customers.CustomerId
    LEFT JOIN invoice_items as ii ON ii.InvoiceLineId = i.InvoiceId
    LEFT JOIN tracks ON tracks.trackid = ii.trackid
    LEFT JOIN genres ON genres.genreid = tracks.genreid
    """
    data = pd.read_sql_query(query, conn)
    gen_in_country = pd.crosstab(
    index = [data['Country'],data['Genre']],
    columns = 'Jml Penggemar',
    ).sort_values(by='Jml Penggemar', ascending=False)
    return (gen_in_country.to_json())

#mendapatkan data penjualan genre di setiap negara (dinamis)
@app.route('/<inv_country>', methods=['GET'])
def country_gen(inv_country):
    conn = sqlite3.connect("data/chinook.db")
    query = """
    SELECT i.InvoiceId,Country,BillingCity,tracks.Name as Tracks,Milliseconds,Bytes,genres.Name as Genre,InvoiceDate,Total
    FROM customers
    LEFT JOIN invoices as i ON i.CustomerId = customers.CustomerId
    LEFT JOIN invoice_items as ii ON ii.InvoiceLineId = i.InvoiceId
    LEFT JOIN tracks ON tracks.trackid = ii.trackid
    LEFT JOIN genres ON genres.genreid = tracks.genreid
    """
    data = pd.read_sql_query(query, conn)
    country = data.groupby(['Country','Genre']).sum().drop(['InvoiceId'], axis=1)
    country[['Milliseconds','Bytes','Total']] = (country[['Milliseconds','Bytes','Total']]).fillna(0)
    country_new=country.unstack(level=0).stack(level=0)
    country_gen = country_new[inv_country]
    return (country_gen.to_json())

if __name__ == '__main__':
    app.run(debug=True, port=5000) 