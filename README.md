# Rescala
An online practice diary for classical musicians, built with Django.
> Get closer to your musical goals with Rescala.
>
> Rehearse. Record. Repeat.

This project was designed and built as the developer's 4th milestone project for Code Institutes's Diploma in Full Stack Software Development.

![Multi-device mockup](documentation/images/mockup.png)

Key features:

 - Log and review practice sessions, including date, duration, your areas of focus and personal reflections
 - Set and track long term goals
 - View insights from your practice on a bespoke dashboard
 - Read and save articles focused on intentional practice, habit building and personal development

 ## Live Project
[The deployed site is available here.](https://denham-rescala.herokuapp.com/ "Link to open deployed website")

## User Stories
The User Stories for this project were planned and tracked  using [GitHub's Projects Tool.](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects "Link to information on GitHub Projects")

User Stories were categories into Epics and broken down into tasks with clear acceptance criteria. The user stories can be viewd, in full, [here.](https://github.com/users/denham-ed/projects/6 "Link to Rescala User Stories")

Inspired by the Agile methodology and utlising the MoSCoW prioritization, these user stories were assigned to short sprints, as documented on the Projects board. These process allowed for incremental development through iteration.

## Design 
### Wireframes
The layout for Rescala was developed using [Balsamiq](https://balsamiq.com/ "Link to Balsamiq")

The wireframes for Rescala can be found [here.](documentation/diagrams/wireframes.pdf)

### Colour Scheme
Rescala usess the following colours throughout.

![Rescala Colour Sceheme](documentation/images/rescala_colours.png)

The Dark Green and Alice Blue are used as alternatives for black and white. The red is used for error messages and to highlight key information on forms and widgets. The lighter green is used primary for shading and to add additional contrasts.

All four colours are used with varying degrees of opacity to support text/image overlays.
### Typography
Two fonts are used in the application.

**Fraunces** is used for headings and the brand logo in the header. It is used with a font weight of 300.

![Fraunces Font](documentation/images/fraunces.png)

**Work Sans** is used with a font weight of 300 for the majority of text in the body. Occassionally it appears at 400, to add emphasis for subtitles and for headers.

![Fraunces Font](documentation/images/work_sans.png)

## Database Model

### Requirements 
- Each user needs a list of goals. These are unique to the user.
- Each user needs a list of resources. This is a many-to-many relationship.

Therefore, the profile model for this application extends the Django User model.

### Models
![Database Models](documentation/diagrams/rescala_db.png)

## Current Features	

### Layout Features

**Header**

- Appears on every page
- Features the Brand logo in the top left. This acts as link to the Landing Page / Dashboard.

![Logo](documentation/images/logo.png)

- Includes a navigation bar with links to key areas

![Navigation](documentation/images/navigation.png)

- Authenticated users can access the Dashboard, Log Practice and Log Out areas
- Current page is shown to the user
- Anonymous users will only have access to the Resources link

**Footer**

- Appears on every page
- Includes the brand name and slogan

![Branding in Footer](documentation/images/footer_brand.png)

- Includes links the developer's GitHub and LinkedIn page. These open in a new browser tab.

![Socials in Footer](documentation/images/socials.png)

### Landing Page

![Landing Page](documentation/images/landing.png)

- Displays the brands slogan
- Features a large Call-To-Action button
- Authenticated users are redirected to the Dashboard page


### Authentication

The authentication for Rescala is handled by [Django AllAuth.](https://django-allauth.readthedocs.io/en/latest/)

Anonymous (unauthenticated users) can view the landing, sign in and register pages, as well as accessing the Resources section of the site.

The following pages extend and modify the AllAuth templates, adding custom formatting and error messages.
**Register Page**

![Register Page](documentation/images/register.png)

- New users can register for a Rescala account
- Floating labels provide clear instruction to the user
![Errors on Registration Form](documentation/images/register_error.png)

- Registered users are guided to the sign in page
- Invalid form submissions are indiciated with custom error messages

**Sign In Page**

![Sign In](documentation/images/sign_in.png)
- Users with accounts can sign in to Rescala
- Floating labels provide clear instruction to the user
- New users are guided to the Register page
- Valid submission redirects to the Dashboard
- Invalid form submissions are indiciated with custom error messages
- Users can opt for the Remember Me option to by pass this stage next time

**Sign Out Page**

![Sign Out](documentation/images/log_out.png)

 - Users are asked to confirm that they are logging out
 - The confirmation options are in-keeping with the tone for the target user

### Dashboard

The dashboard allows a logged-in user to view aggregated statistics about their logged practices. It also serves as the landing page for authenticated users.

![Dashboard Page](documentation/images/dashboard.png)

The responsive layout of the Dashboard widgets is achieved using [MasonryJS](https://masonry.desandro.com/ 'Link to MasonryJS')

**Recent Practices**
- The most recent 5 logged practice sessions are rendered with the date and the headline.
- Each session is clickable and redirects to the [Session Details ](#session-details) page.

**Goals**
- Users can add long term goals, which can be updated and tracked.
- Progress for each goal can be updated with the Edit button.
- Goals can be removed with the Delete button.
- A spinner is used to show the User that the goal is being updated.

**Moods**
 - Renders a wordcloud from the aggregated Moods from each recorded session. Conditional formatting is applied, reflecting the prevalence of each word.
 - Allows user to identify trends and patterns in their emotions whilst practicing.

**Calendar**
- Renders 30 circles to represent the last 30 days.
- Days where practice has occured are coloured green.
- Allows users to visualise a practice streak, a key factor in habit building.
- Tool-tips allow users to see which date each object represents.

**Focus**
- Displays a Dougnut Chart (Part-To-Whole Relationship) to represent the number of sessions where each focus has occurred.
- Allows the user to track how they are spending their time and areas of focus that may be underserved.

**Total Practice**
- Displays the sum of practice duration for each recorded session for the last 7 days, 30 days and for all sessions.

**User Resources**
- Displays a list of 'favourited' articles by the user
- Each item in the list is a link to the resource.


### Resources

The resources page allows all users to view Rescala's collection of artices on practice, habit-building and self-improvement.

![Resources](documentation/images/resources.png)

**Resource List**
- Resources are ordered by date, so most recent articles are presented to the user first.
- Asymmetric design provides an alternative to the standard list view for blogs.
- Each resource tile is a link to the resource itself.

**Pagination**
- Pagination is handled by Django and renders a maximum of six resources to each page.
- Users can navigate between pages using the Pagination controls underneath the listed resources.

**Excerpt**
- Hovering over the image for each resource displays a summary excerpt as an overlay.

### Individual Resource

![Resource](documentation/images/resource.png)

**Recommendations**
- Users are recommended three additional resources. This will keep users engaged on the site.

![Recommendation](documentation/images/might_like.png)

**Add to Favourites**
- Authenticated users can use the Star icon to mark the resource as a favourite. Favourite articles can be accessed directly from the Dashboard.

### Log Practice
Authenticated Users can log a practice session using the form on this page
![Delete Session](documentation/images/log_practice.png)

- Custom error messages are rendered if the form is not valid when submitted
- After a successful submission, the user is returned to the Dashboard.


### Session Details

Users can view details from a logged a practice including the Reflection, Focus and Moods.

![Session Details](documentation/images/session.png)

- Users can delete a session by clicking the **Delete Practice** button. A modal is used to confirm the request before removing the session and redirecting the user to the dashboard.

![Delete Session](documentation/images/delete_modal.png)

- Users can edit a session by clicking the **Edit Practice** button which redirects them to the [Edit Practice](#edit-practice) page.

### Edit Practice

Users can edit a recorded practice using a prepopulated form.

![Delete Session](documentation/images/edit-practice.png)

- Changes to the practice are saved by clicking the **Update Practice** button.
- Users are redirected to the [Session Details ](#session-details)  page.
- If the form is invalid, custom error messages are rendered for the user.

### Resource Admin

The administration for the Resources is handled by Django's built-in [Admin Interface.](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/ 'Link to Django Admin Docs') 
- This allows administrators to create, update and delete Resources.
- Resources can be drafted first and published at a later date.
- A placeholder image is provided but uploaded images can be added to each resource.
- The slug is automatically provided from the Resource title.

### 404 Page

If any action triggers a 404 error, the User will be shown a custom 404 page.

![Delete Session](documentation/images/404.png)

This replaces the template provided by Django. A button returns the user to the Dashboard.



## Planned Features

## Testing

Rescala has been extensively tested. You can view more about testing, including automated and manual testing, accessibility, validators and more, [here.](documentation/docs/TESTING.md)

## Deployment

## Technologies

### Languages

 - **Python**
 - **Javascript**
 - **HTML5**
 - **CSS3**

### Libraries and Frameworks

 - **Django**
 - **Django AllAuth**
 - **jQuery**
 - **Bootstrap**
 - **Django Crispy Forms**
 - **Summernote**
 - **ChartJS**
 - **MasonryJS**

### Hosting and Storage
 - **Cloudinary**
 - **Heroku**
 - **ElephantSQL**

### Version Control
- **Git**
- **GitHub** 

### Design & Media
Balsamiq
- **Coolors**
- **Google Fonts**
- **Font Awesome**
- **Unsplash**
- **Canva**


### Databases
 - **SQLite** was used for the development database and during unit testing
 - **PostgreSQL**, via Elephant SQL, is used for the production database.

## Credits
### Code
The resources below are were significantly used in the development and deployment of this project. 
Where code has been used verbatim, it is also credited in the code itself.

- [Highlighting Active Page in Django](https://valerymelou.com/blog/2020-05-04-how-to-highlight-active-links-in-your-django-website)
- [Testing Forms in Django](https://adamj.eu/tech/2020/06/15/how-to-unit-test-a-django-form/)
- [Removing Browser Validation from Crispy Forms](https://stackoverflow.com/questions/63539170/how-to-add-action-and-novalidate-attribute-to-form-tag-using-crispy-form)
- [Integrating Crispy Forms in Django](https://www.youtube.com/watch?v=MZwKoi0wu2Q&t=521s)
- [Integrating Summernote in Django](https://djangocentral.com/integrating-summernote-in-django/)
- [Add ChartJS to Django](https://www.section.io/engineering-education/integrating-chart-js-in-django/)
- [Customizing AllAuth Forms pt.1](https://dev.to/danielfeldroy/customizing-django-allauth-signup-forms-2o1m)
- [Customizing AllAuth Forms pt.2](https://gavinwiener.medium.com/modifying-django-allauth-forms-6eb19e77ef56)
- [Extending the Base User Model](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html)
- [W3Schools](https://www.w3schools.com/) was referenced for Python syntax including list comprehension and built-in functions eg. any()
### ChatGPT

[Open AI's ChatGPT ](https://openai.com/blog/chatgpt) was used to accomplish various tasks during this project including:

- writing the practice logs and the the resources for this version of Rescala.
- explaining obscure or verbose error messages, particularly during the the unit testing phase.
- formatting headings and text used in this ReadMe.

### Music Resources
[The Musician's Union Practice Diary](https://musiciansunion.org.uk/working-performing/music-teaching/working-as-a-music-teacher/practice-diaries-and-workbooks) provided inspiration for Rescala

## Acknowledgements
- The support of my mentor Spencer Barriball for his advice, guidance and directions to resources is gratefully acknowledged.
- The Code Institute example read me was used as a template for this document. This includes the instructions for deployment on GitHub Pages which are used in full, above. !!!! CheCK THIS!!!!