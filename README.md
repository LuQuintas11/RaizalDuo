## Purp0se

This website was created to complete the fourth Milestone Project for Code Insitute's Full Stack Software Developer course. It is about a real music band, Raizal Duo. It was made based on specific requirements by the members of the band.

Users of this website are able to listen the new EP released by the band, like and comment and check the nexts shows and presentations. 

You can find the link to the live website right  [here ](https://raizalduo.herokuapp.com/)

![This is an image](/static/media/images/responsive.png)


## Technologies used

HTML, CSS, JavaScript, Python+Django

## Frameworks, Libraries, Programmes and Tools

* Django web framework - used to build the project

* Bootstrap - for responsiveness, layout, modals, and general frontend style

* django-allauth - for user registration and authentication

* Code Institute Template - to display and run the command line terminal in the browser

* Favicon.io - to create a favicon for the site

* sLighthouse - to audit the site for performance, accessibility, SEO and best practices


## Agile thinking

This project was made for a real customer so I tried to follow as many as agile principles I could:

   * Satisfy the customer through early and continuous delivery of valuable software.

   * Welcome Chanching Requirements 

   * Working software is the primary measure of progress

   * Create the simplest software solution

   # Agile tool

I used Github user stories to keep track of the features that were already done and the ones I had to do


![This is an image](/static/media/images/user%20stories.png)

## User Experience

**As a Site User** I can view a list of posts so that **I can select one to listen to**.

**As a Site User** I can click on a song so that **I can listen to it**.

**As a Site User** I can register an account so that **I can comment and like**.

**As a Site User** I can leave comments on a song so that **I can be involved in the conversation**.

**As a Site User** I can like or unlike a song so that **I can interact with the content**.

**As a Site User / Admin** I can view comments on an individual song so that **I can read the conversation**.

**As a Site Admin** I can create, read, update and delete comments.

**As a Site User / Admin** I can view the number of likes on each song so that **I can see which is the most popular or viral**.

**As a Site User** I can register an account so that **I can comment and like**.

**As a Site Admin** I can approve or disapprove comments so that **I can filter out objectionable comments**.


## Features

This website two pages:

1. Home page: main video section, music section
2. Second page: music section video, comment section 

The navigation and footer features are present in the three pages:

**Navigation**

Feature at the top of the page, the navigation shows the name of the music band in the center: Raizal. To the left of the name shows  **home** and **sign up/log in** links. To the right of the name shows social media links 

![This is an image](/static/media/images/Nav.png)

**sign up/log in** section:

![This is an image](/static/media/images/Sign-up.png)


**Footer**

The footer includes social media icons to the users can find the band on spotify, instagram and youtube channel.

![This is an image](/static/media/images/Social%20media.png)

1. **Home Page**

The home page has a main section with a small text explain the origins of the band. Bellow to this small text there is a video showing the band playing, offering an eye catching content to grab users attention.


![This is an image](/static/media/images/Main-Video.png)

Below the main section there is a show section. In this section, users can check the upcoming shows and presentations. 


![This is an image](/static/media/images/Shows.png)

The last section it shows the last EP of the band. There is a post for each song of the album. There is a small text explaining how was recorded

![This is an image](/static/media/images/Music.png)


2. **Second Page**

When the user clicks on any post on the main page it takes him to the music video of said post. Beside the video there is the comment section; The user can leave/update or delete a comment and see other user's comments. Below the video the user can like and see other user's likes. 

![This is an image](/static/media/images/Secondary%20Video.png)

![This is an image](/static/media/images/CRUD.png)


## Testing

During the development process, I was manually testing in the following ways:

* I then used the devtools to simulate different screen sizes/devices

* The comment form field works: requires entry in body field, only allows comment if the user is authenticated, and the submit button works.

* The sign up/sign in form field works: requires entry in every field, only accept and email in the email field, and the submit button works.

## Bugs and Fixes

1. **Intended Outcome** - A fully responsive main and secondary video suited to all screen sizes.

  *Issue Found*:
    The video size was fixed, no responsive
    The videos were too small at the largest sizes.
   *Solution Used*:
    Used CSS flex
2. **Intended Outcome** - Align the comment section below video

   *Issue Found*:
    The comment section was overlapping the video
   *Soluction Used*:
    Used CSS flex

3. **Intended Outcome** - A footer at the bottom of the page 

  *Issue Found*:
    The footer was at the middle of the page 
  *Soluction Used*:
    Used position:fixed

4. **Intended Outcome** - Set DEBUG=False to deploy project

*Issue Found*:
  Static and media was not loaded in the deployed project
*Solution Used*:
 Set Cloudinary variable in heroku and upload pictures again in admin


## Post Development Testing

**Validators**

HTML-[HTML validator ](https://validator.w3.org/)

*Issue Found*:
Post_detail.html
![This is an image](/static/media/images/base.html.png)

Base.html:

![This is an image](/static/media/images/postdetail.html.png)

All the issues were fixed except for the iframe issue; I do no have access to this element. This element come from the youtube video url uploaded.

createComment.html and updateComment.html:

![This is an image](/static/media/images/createComment.html.png)

CSS-[CSS validator ](https://jigsaw.w3.org/css-validator/validator)



Pycodestyle was run on every python code:
No big issues found, just too long line that were left like that for a readability issues

![This is a image](/static/media/images/pycodestyle.png)

## Lighthouse Scores


I did all lighthouse tests in incognito mode to avoid interference from browser extensions.

I ran the tests for both mobile and desktop.

**Desktop Version**:

![This is an image](/static/media/images/desktopper.png)


There were several actions required to get to this score:
  The initial Performance was 78. I read [Perfomance Django Documentation ](https://docs.djangoproject.com/en/4.1/topics/performance/) to know how to improve the performance. The sujestion were:

    1. Reduce unused JavaScript code: I do not have unused code in my project

    2. Use an appropriate size for images: The images were reduce more than 7 times

    3. Remove resources that block rendering: it suggests tagging stylesheet link with disable or media attribute but this brings consequences when I want to render the website. It also suggests tagging the script link with defer attribute. I did this and the perfomance improved

    4. Reduce server response time: DJango documentation suggests several things to improve this like:
         Use caching: I did set caching in the setting file. This improve the perfomance but I have to remove it because it was compromising the log in. The perfomance score it stayed good enough 
         Reduce Queries: I run django-debug-tool to check the project queries. The majority of queries that are affecting the run time are this:
         ![this is a image](/static/media/images/time.png)
         ![this is image](/static/media/images/queries.png)
         I do not have access to this queries
  
The Accecibility score is 94. It suggest to improve it:

  Background and foreground colors do not have a sufficient contrast ratio: This was improved several times. I consider there is a good contrast 

 frame or iframe elements do not have a title: I do not have access to this element 


**Mobile Version**:

![This is an image](/static/media/images/performance.png)

The same issues mentioned before ( desktop score ) were found and the same actions were taken 

## Deployment

The project was deployed on Heroku. Here are the steps to achieve this:

1. Clicked on "Create new app" on Heroku account and named app 'raizalduo' and selected region as 'Europe'.
2. In resources, select Heroku Postgres on the Hobby Dev setting.
3. Add config vars in settings, including PORT, DATABASE_URL and SECRET_KEY.
4. Make sure Debug is set to False in your settings.py file in your code.
5. Connect GitHub repository in Deploy section and either automatically or manually deploy.
4. The site should deploy after these steps.

## Credits 

#### Media and content

* The icons in the footer were taken from Font Awesome  https://fontawesome.com/start
* The font-family was imported from https://fonts.google.com/
* The images and videos were given for Raizal Duo band. 
* I want to give credits to my tutor Sandeep Aggarwal. 




