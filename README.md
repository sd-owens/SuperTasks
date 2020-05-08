<h1>SuperTasks - A task management web application modeled after ASANA</h1>

<h2>CS361 Team 10 Project repository</h2>
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
<p> Or if desired, a local instance can be setup as follows:</p>
<p> <sup>1 </sup><sub>Project hosting provided by Google Cloud using the Google App Engine.</sub> </p>

<hr>

<h2>Setting up a local development environment</h2>

<h3>Note: if python3 is not aliased to python on your machine, replace “python” with “python3” in all of the references that follow</h3>

<p><em>Requirements:</em></p>

<ul>
    <li>Python3 installed  https://www.python.org/downloads/</li>
    <li>Verify PIP installed with Python3:  <strong>pip -V</strong></li>
    <li>If not, install the lastest version with Python3:  <strong>python pip -m install –upgrade pip</strong></li>
    <li>Setup a virtual environment for the project:  <strong>pip install virtualenv</strong></li>>
</ul>

     
<p><em>Clone the repo to your local machine.</em></p>
<ul>
    <li><strong>git clone git@github.com:craigkelleher/CS361-Team-10-Project-repository.git</strong></li>
    <li>(optional) rename to something simpler:  <strong>mv ./CS361-Team-10-Project-repository/ ./SuperTasks</strong></li>
    <li>Switch over the project root directory:  <strong>cd SuperTasks/</strong></li>
</ul>

<p><em>Install the modules for all dependencies in local-requirements.txt</em></p>
<ul>
    <li><strong>python -m pip install -r local-requirements.txt</strong></li>
    <li>note: requirements.txt with the local prefix contains dependencies for the production version only and should not be used for local development unless mySQL server and a mySQL test database are setup. </li>
</ul>

<p><em>Setup development SQlite Database</em></p>
<ul>
    <li><strong>python manage.py makemigrations</strong> </li>
    <li><strong>python manage.py migrate</strong></li>
</ul>

<p><em>Run the application</em></p>
<ul>
    <li><strong>python manage.py runserver</strong> </li>
    <li>Navigate to <strong>localhost:8000</strong> in your web browser of choice.</li>
</ul>

<p><em>(optional)</em></p>
<ul>
    <li><strong>python manage.py createsuperuser</strong></li>
    <li>Allows creation of a superuser account allowing access to <strong>localhost:8000/admin</strong> to view the development database.</li>
</ul>


