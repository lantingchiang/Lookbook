# Lookbook

## Installation
Make sure you have [`pipenv`](https://docs.pipenv.org/en/latest/) installed.

### Setting up the Django Backend
1. `git clone https://github.com/lantingchiang/Lookbook.git` to clone the repository to your local machine
2. `pipenv install` to install all project dependencies
3. `pipenv shell` to activate the virtual environment
In the virtual environment...
4. `./manage.py makemigrations`
5. `./manage.py migrate`
6. `./manage.py runserver` and follow the url in the console

## Ongoing development
1. `git pull origin master` to get the most up to date code
2. `git branch [branchname]` to create a new branch
3. `git checkout [branchname]` to switch to new branch
4. Start developing :)
5. `git push origin [branchname]` to push local commits to remote repository
6. Make a pull request and request 1 reviewer in order to merge to master

## Documentation
### API Routes
<table>
  <tr>
    <th>Route</th>
    <th>Request Method</th>
    <th>Parameters</th>
    <th>Response</th>
  </tr>
  <tr>
    <td>"/"</td>
    <td><code>GET</code></td>
    <td>NA</td>
    <td>Serves static page <code>home.html</code></td>
  </tr>
</table>
### Accessing the admin site
[See official documentation here](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/)
<ol>
  <li>Run `./manage.py createsuperuser` to create credentials for logging into admin site</li>
  <li>Enter username and password in command line as prompted</li>
  <li>Start the server by running `./manage.py runserver`</li>
  <li>Access the admin site at http://127.0.0.1:8000/admin/</li>
  <li>Log in and create model instances!</li>
</ol>

