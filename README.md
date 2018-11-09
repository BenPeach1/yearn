# yEARN - Independent Contractor Billing Made Easy
This web application provides a streamlined, user-friendly platform for tracking time billing and generating invoices.

# Prerequisites for Running the Application

### _Vagrant Virtual Machine_
This application runs on a Vagrant Virtual Machine. If you do not have Vagrant installed, [You can download it from vagrantup.com.](https://www.vagrantup.com/downloads) Install the version for your operating system.

### _Libraries_
You will need to install the following libraries to run this web application:
 - Flask (```$pip install flask```)
 - SQLAlchemy (```$pip install SQLAlchemy```)
 - Flask-WTF (```$pip install flask-wtf```)

# Running the Woodworking Project Forum App
Once you have logged your terminal into the virtual machine (```$vagrant ssh```), change to the /vagrant/catalog directory by typing (```$cd /vagrant/yearn```). Type (```$ls```) to ensure that you are inside the directory that contains project.py, database_setup.py, and two directories named 'templates' and 'static'

##### _Database Setup_
Now type (```$python database_setup.py```) to initialize the database.

##### _Database Population_
Type (```$python lotsofhours.py```) to populate the database with time billing entries and invoices. (Optional)

##### _Run the Web Application_
Type (```$python project.py```) to run the Flask web server. In your browser visit **http://localhost:8000** to view run the yEARN web app.
