from flask import Flask, render_template, request, redirect, url_for
from Device import Device
from DataOperations import DataOperations

app = Flask(__name__)
data_source = DataOperations()

@app.route('/')
def index():
    # Display all items initially
    devices = data_source.getAllThings()
    return render_template('index.html', devices=devices)

@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['search_query']
    if search_query:
        devices = data_source.search_device(search_query)
    else:
        devices = data_source.getAllThings()
    return render_template('index.html', devices=devices)

@app.route('/new', methods=['POST'])
def new_device():
    if request.method == 'POST':
        # Check if the form is empty. If it is, redirect to the index page
        if not request.form['name'] or not request.form['model'] or not request.form['serial_number'] or not request.form['price'] or not request.form['manufacture_date']:
            return redirect(url_for('index'))
        
        # If the form is not empty, create a new device and redirect to the index page
        name = request.form['name']
        model = request.form['model']
        serial_number = request.form['serial_number']
        price = request.form['price']
        manufacture_date = request.form['manufacture_date']
        data_source.add_device(name, model, serial_number, float(price), manufacture_date)
        return redirect(url_for('index')) 
    
@app.route('/newForm')
def new_device_form():
    return render_template('new.html')

@app.route('/editForm/<int:id>', methods=['GET'])   
def edit_device(id):
    device = data_source.find_device_id(id)
    return render_template('edit.html', device=device)

@app.route('/edit', methods=['POST'])
def edit_device_post():
    id = request.form['id']
    name = request.form['name']
    model = request.form['model']
    serial_number = request.form['serial_number']
    price = request.form['price']
    manufacture_date = request.form['manufacture_date']
    updated_device = Device(id, name, model, serial_number, float(price), manufacture_date)
    data_source.edit_device(updated_device.id, updated_device.name, updated_device.model, updated_device.serial_number, updated_device.price, updated_device.manufacture_date)
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['GET'])
def delete_device(id):
    data_source.remove_device(id)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
