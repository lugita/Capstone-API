from flask import Flask, request 
import pandas as pd 
app = Flask(__name__) 

#home root
@app.route('/')
def homepage():
    return "Hello Worlds"

#mendapatkan buku baru


#mendapatkan buku baru (Endpoint statis)
@app.route('/ambil_buku')
def ambilbuku():
	data = pd.read_csv('data/books_c.csv')
	return (data.to_json())

# buat endpoint yg menghasilkan crosstabulasi dari data books_c.csv
@app.route('/top_rate')
def topratingbook():
    books = pd.read_csv('data/books_c.csv')
    condition = books['average_rating'] == 5
    books = books[condition]
    return books.to_json()

# mendapatkan keseluruhan data dari <data_name>
@app.route('/data/get/<data_name>', methods=['GET']) 
def get_data(data_name): 
    data = pd.read_csv('data/' + str(data_name))
    return (data.to_json())
 

# mendapatkan data dengan filter nilai <value> pada kolom <column>
@app.route('/data/get/equal/<data_name>/<column>/<value>', methods=['GET']) 
def get_data_equal(data_name, column, value): 
    data = pd.read_csv('data/' + str(data_name))
    mask = data[column] == value
    data = data[mask]
    return (data.to_json())

if __name__ == '__main__':
    app.run(debug=True, port=5000) 