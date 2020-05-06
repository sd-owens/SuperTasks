<h1>SuperTasks</h1>
<h2>A task management web application modeled after ASANA</h2>
<hr>
<h2>CS361 Team 10 Project repo</h2>
<h6>Group Members:</h6>
<ul>
    <li>Kevin Hill</li>
    <li>David Mikulis</li>
    <li>Steven Owens</li>
    <li>Michael Hathaway</li>
    <li>Craig Kelleher</li>
</ul>

<h6>Asana Team Page: https://app.asana.com/0/1167416800657633/overview</h6>

<hr>
<h2>How do I access/run SuperTasks?</h2>

<p> Our project can be accessed publically on the web at: https://osu-cs361-supertasks.appspot.com/ <sup>1</sup> </p>
<p> <sup>1 </sup><sub>Project hosting provided by Google Cloud using the Google App Engine.</sub> </p>

<hr>

<h2>Setup Details</h2>

<ol>
    <li>
        <h5>Created SuperTasks django project</h5>
        <p>created project in  using command "django-admin startproject SuperTasks ."</p>
        <p>This created all the default files in the directory call SuperTasks</p>
    </li>
    <li>
        <h5>Created templates directory and added index.html template</h5>
        <p>In the main project directory I created a directory called templates. This directory contains a file called index.html. index.html is a general template that we can use that containers places to insert a page title, styling, body content, and javascript. I think this will be a good place to put the login and registration templates too.</p>
    </li>
    <li>
        <h5>Created static files directory</h5>
        <p>In the main project directory I created a directory called static with subdirectories CSS, images, and javascript. This is where we can put all of our static files.</p>
    </li>
    <li>
        <h5>Created App called accounts</h5>
        <p>I created an app called account using the command: "django-admin startapp accounts"</p>
        <p>This is where we can put all our code for user accounts, projects, etc</p>
    </li>
    <li>
        <h5>Created templates directory with accounts app</h5>
        <p>I created a subdirectory within the accounts app called templates. within the templates subdirectory I created another subdirectory call  accounts</p>
        <p>This is where we can put our account specific templates</p>
    </li>
    <li>
        <h5>Created test url, view, template</h5>
        <p>I created a sample page by adding a template to the templates/accounts directory, adding a view to accounts/views.py, and adding a URL to accounts/urls.py. This is just a sample so we know how to create new pages. I know we've all probably used slightly different tutorials and there are many similar but slightly different ways to set everything, so I thought this could be helpful for reference. to view the test page: </p>
        <ul>
            <li>start the server with ""python manage.py runserver</li>
            <li>access the page at: "http://127.0.0.1:8000/accounts/test/" </li>
        </ul>
        <p>If an errot occurs when viewing the image on the page, you may need to install the "pillow" module which is used for displaying imagaes. I am using Pillow==7.0.0. install with: pip install pillow </p>
    </li> 
    <li>
        <h5>Added .gitignore </h5>
        <p>
        I took a sample django gitignore for stackoverflow. Additionally I added migrations to the .gitignore. This makes sense to me because until we actually deploy, django automatically creates a sqllite database for us to develop with. by ignoring migrations and the database we just have to focus on the actual code base.
        </p>
        <p>if there are any problems in your local development environment due to migrations or the database, I think you can just delete all the migration files and delete the local database and then run the following commands: </p>
        <ul>
            <li>python manage.py makemigrations</li>
            <li>python manage.py migrate</li>
            <li>python manage.py runserver</li>
        </ul>
        <p>Note: this will delete any data in your local database, but during the development process it shouldn't be hard to create new data as needed. If anyone has any problems with this general method, i'm open to other idea, this just seems like a decent solution to me at the moment
        </p>
    </li>
    
</ol>

<p>Note: when you pull down these changes to your local machine you will need to run the commands:</p>
<ul>
    <li>python manage.py makemigrations</li>
    <li>python manage.py migrate</li>
</ul>

<p>After that if you run the command: "python manage.py runserver" the server should start up fine and youll be able to access the test page at http://127.0.0.1:8000/accounts/test.</p>
<p>If this doesn't work for you please let me know</p>

</li>
    <li>
  Added Account Registration, login, and logout functionality</li>
    <li>
    If there is any issue testing this on your local machine, the following steps should make it work (may not have to do all of them):</li>
    
        easy_install pip
        python -m pip install --upgrade pip
        pip install django
        pip install virtualenv
        ~<source>\Scripts\Activate
        pip install django-widget-tweaks
        python manage.py migrate
        python manage.py runserver
        python manage.py createsuperuser
        python manage.py runserver
        Note: creating a superuser account will allow you to go to 127.0.0.1:8000/admin and see database/edit it
</li>
