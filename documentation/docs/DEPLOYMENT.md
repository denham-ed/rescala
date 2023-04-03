# Rescala - Deployment

## Contents
  * [Create a Gitpod Workspace Using a Template](#create-a-gitpod-workspace-using-a-template)
  * [Create a Local Clone](#create-a-local-clone)
  * [Create a Cloudinary Account](#create-a-cloudinary-account)
  * [Connect to Cloudinary](#connect-to-cloudinary)
  * [Create a Database](#create-a-database)
  * [Connect To Database](#connect-to-database)
  * [Host on Heroku](#host-on-heroku)

## Create a Gitpod Workspace Using a Template
1. Navigate to [Code Institute Gitpod Full Template](https://github.com/Code-Institute-Org/gitpod-full-template)
2. Click 'Use this template' and create a new repository.
3. Open your new repository in Gitpod by clicking the green GitPod button.

## Create a Local Clone
To create a local clone of this project:
1. Create a folder where you want the cloned directory to be stored
2. Open your terminal and navigate to this new directory
3. In the terminal, run `git clone https://github.com/denham-ed/rescala.git`

## Create a Cloudinary Account
Cloudinary is used to host static and media files

1.  Visit the  [Cloudinary website](https://cloudinary.com/)
2.  Click on the  **Sign Up For Free**  button
3.  Provide your name, email address and choose a password
4.  For  **Primary interest**, you can choose  **Programmable Media for image and video API**
5.  _Optional_: edit your assigned cloud name to something more memorable
6.  Click  **Create Account**
7.  Verify your email and you will be brought to the dashboard

**These steps are copied verbatim from the Code Institute *I Think Therefore I Blog* walkthrough**

## Connect to Cloudinary

1. From your Cloudinary account, copy the API Environment variable - you will need this value for deployment in Heroku later.
2. In the GitPod workspace, run `pip3 install dj3-cloudinary-storage`
3. Add `cloudinary_storage` and `cloudinary` to `INSTALLED_APPS` in `settings.py`. NB. `cloudinary_storage` must go above `django.contrib.staticfiles`
4. Add the following code to `settings.py`:
`STATIC_URL = '/static/' STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage' STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')`
5. Add the following code to handle Media Storage:
`MEDIA_URL = '/media/' DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'`

## Create a Database
Django's default configuration uses SQLite but the official documentation recommends switching to PostgreSQL.

1. Log In or Register with [ElephantSQL](https://customer.elephantsql.com/login).
2. Click 'Create New Instance' and add a Name and select a Plan (Tiny Turtle is Free) 
3. Click 'Select a Region' and choose the most appropriate region and data center
4. You will have the opportunity to review before pressing 'Create instance'
5. From the Dashboard, click to view the details of the new instance.
6. Copy the URL; this will be needed to connect your project to the Database.

## Connect To Database
The following steps are necessary to connect your new database to your project. 
During development, the developer used the Django's default configuration before switching to PostgreSQL for the production version.

1. Install dj_database_url and [psycopg2](https://pypi.org/project/psycopg2/) using `pip3 install dj_database_url psycopg2`
2. In `settings.py` replace the `DATABASES` constant with the code below, making sure to insert the URL, copied in the previous steps, as the DATABASE_URL variable
`if DEBUG:
	DATABASES = {
		'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
	}}
else:
	DATABASES = {
		'default': dj_database_url.parse(DATABASE_URL)}`

**Best practice is to store this as a environment variable as it will contain sensitive information and should not be committed to GitHub.**

3.  Run `python manage.py migrate`

Comprehensive guidance can be also found in the [Django documentation](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-DATABASES)

## Host on Heroku
Heroku is a cloud Platform as Service used to deploy and manage apps. This version of Rescala is hosted on Heroku and the following steps can be followed to achieve this.

1. Compile list of dependencies by running  `pip3 freeze > requirements.txt`
2. Sign In or Register with [Heroku](https://www.heroku.com/)
3. Click 'New' and then 'Create New App'
4. Select a name for the app and choose a Region.
5. Click 'Create app'
6. Select your newly created app and select 'Settings'
7. Add four config vars:
	- `DATABASE_URL` as described above
	- `SECRET_KEY` from `settings.py`
	- `CLOUDINARY_URL` as described above	
	- `PORT`, with the value 8000
8. In `settings.py` add the Heroku host name to `ALLOWED_HOSTS` eg. `ALLOWED_HOSTS = ['your-app.heroku.com']`
9. In the root folder of your project, create a file called Procfile with the following content `web: gunicorn YOUR-APP.wsgi:application`
10.  In the Deploy tab, connect Heroku to GitHub by selecting GitHub under Deployment method
 11. Find the relevant GitHub repository
 12.  [Optional] Enable Automatic deploys - this means that every push to the main branch on GitHub will deploy a new version of this app. Alternatively, you can select a manual deployment.
