## Porpuse

This website was created to complete the fourth Milestone Project for Code Insitute's Full Stack Software Developer course.
This website is about a real music band, Raizal Duo. It was made based on specific requirements by the members of the band.

Users of this website are able to listen the new EP released by the band, like and comment and check the nexts shows and presentations. 

You can find the link to the live website right


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

![This is an image](/media/website/Nav.png)

**sign up/log in** section:

![This is an image](/media/website/Sign-up.png)


**Footer**

The footer includes social media icons to the users can find the band on spotify, instagram and youtube channel.

![This is an image](/media/website/Social%20media.png)

1. **Home Page**

The home page has a main section with a small text explain the origins of the band. Bellow to this small text there is a video showing the band playing, offering an eye catching content to grab users attention.


![This is an image](/media/website/Main-Video.png)

Below the main section there is a show section. In this section, users can check the upcoming shows and presentations. 


![This is an image](/media/website/Shows.png)

The last section it shows the last EP of the band. There is a post for each song of the album. There is a small text explaining how was recorded

![This is an image](/media/website/Music.png)


2. **Second Page**

When the user clicks on any post on the main page it takes him to the music video of said post. Beside the video there is the comment section; The user can leave a comment and see other user's comments. Below the video the user can like and see other user's likes. 

![This is an image](/media/website/Secondary%20Video.png)


## Testing

During the development process, I was manually testing in the following ways:

I then used the devtools to simulate different screen sizes/devices

The comment form field works: requires entry in body field, only allows comment if the user is authenticated, and the submit button works.

The sign up/sign in form field works: requires entry in every field, only accept and email in the email field, and the submit button works.

## Bugs and Fixes

1. Intended Outcome - A fully responsive main and secondary video suited to all screen sizes.

   Issue Found:
    The video size was fixed, no responsive
    The videos were too small at the largest sizes.
   Solution Used:
    Used CSS flex
2. Intended Outcome - Align the comment section below video

   Issue Found:
    The comment section was overlapping the video
   Soluction Used:
    Used CSS flex

3. Intended Outcome - A footer at the bottom of the page 

  Issue Found:
    The footer was at the middle of the page 
  Soluction Used:
    Used position:fixed


## Post Development Testing

Validators

HTML-[HTML validator ](https://validator.w3.org/)

Issue Found:
![This is an image](/media/website/Screenshot%20(17).png)

All the issues were fixed except for the iframe issue; I do no have access to this element. This element come from the youtube video url uploaded.

CSS-[CSS validator ](https://jigsaw.w3.org/css-validator/validator)

All pages tested, no issues found via URL or file upload.

![This is an image](/media/website/Screenshot%20(20).png)

## Lighthouse Scores

# Test Conditions
I did all lighthouse tests in incognito mode to avoid interference from browser extensions.

I ran the tests for both mobile and desktop.

Desktop Version:

![This is an image](/media/website/Permofance.png)

There were several actions required to get to this score:

Mobile Version:

![This is an image](/media/website/Mobile%20.png)