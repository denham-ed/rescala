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
[Rescala is available to view here](https://denham-rescala.herokuapp.com/ "Link to open deployed website")

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

Link to database model drawing

## Current Features	

### Landing Page

![Landing Page](documentation/images/landing.png)

- Displays the brands slogan
- Features a large Call-To-Action button


**Header**

- Appears on every page
- Features the Brand logo in the top left

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

### Authentication

The authentication for Rescala is handled by Django AllAuth..

**Register Page**

**Sign In Page**

**Log Out Page**

### Dashboard

**Recent Practices**
**Goals**
**Moods**
**Calendar**
**Focus**
**Total Practice**
**User Resources**

## Planned Features

## Testing
### Accessibility 
### Validators
### Manual Testing
### Automated Testing
### Responsiveness

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

### Hosting and Storage
 - **Cloudinary**
 - **Heroku**
 - **ElephantSQL**

### Version Control
- **Git**
- **GitHub** 

### Design & Media
- **Coolors**
- **Google Fonts**
- **Font Awesome**
- **Unsplash**
- **Canva**


### Databases
 - **SQLite** was used for the development database and during unit testing
 - **PostgreSQL**, via Elephant SQL, is used for the production database.
### Credits
### Chat GPT

## Acknowledgements