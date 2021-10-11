# CarSales
Django Car Sales App to Demonstarte the Django Signal

<h1>Demonstation of the Django Signals</h1>
<ul>
<li>
buyers: user -> buyer, post_save
</li>
<li>
cars: car -> buyer, post_save vs pre_save pre_save vs save
</li>
<li>
orders:order,m2m_changed,order->sale,post_save
</li>
<li>
sales:sale->order,pre_delete
</li>
</ul>

## Steps To Run the Application

<ol>
  <li> git clone project </li>
  <li> go inside project folder </li>
  <li> create an virtual env using  python3 -m venv venv 
 </li>
  <li> Activate the virtual environment source venv/bin/active </li>
  <li> Install dependancies pip install -r requirements.txt </li>
  <li> Migrate the db python manage.py migrate </li>
  <li> Create an super admin user python manage.py createsuperuser </li>
  <li> Run the application python manage.py runserver </li>
  </ol>
   


