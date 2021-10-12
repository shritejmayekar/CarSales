# CarSales App
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


## Django Signal Description
  
<pre> The Django Signals is a strategy to allow decoupled applications to get notified when certain events occur. Let’s say you want to invalidate a cached page everytime a given model instance is updated, but there are several places in your code base that this model can be updated. You can do that using signals, hooking some pieces of code to be executed everytime this specific model’s save method is trigged.

Another common use case is when you have extended the Custom Django User by using the Profile strategy through a one-to-one relationship. What we usually do is use a “signal dispatcher” to listen for the User’s post_save event to also update the Profile instance as well.

<h3>When Should I Use It?</h3>
Before we move forward, know when you should use it:
<ul>
<li>When many pieces of code may be interested in the same events;</li>
<li>When you need to interact with a decoupled application, e.g.:</li>
<li>A Django core model;</li>
<li>A model defined by a third-party app.</li>
</ul>

</pre>

## How it Works ?
<pre>
If you are familiar with the Observer Design Pattern, this is somewhat how Django implements it. Or at least serves for the same purpose.

There are two key elements in the signals machinary: the senders and the receivers. As the name suggests, the sender is the one responsible to dispatch a signal, and the receiver is the one who will receive this signal and then do something.

A receiver must be a function or an instance method which is to receive signals.

A sender must either be a Python object, or None to receive events from any sender.

The connection between the senders and the receivers is done through “signal dispatchers”, which are instances of Signal, via the connect method.

The Django core also defines a ModelSignal, which is a subclass of Signal that allows the sender to be lazily specified as a string of the app_label.ModelName form. But, generally speaking, you will always want to use the Signal class to create custom signals.

So to receive a signal, you need to register a receiver function that gets called when the signal is sent by using the Signal.connect() method.
</pre>
   


