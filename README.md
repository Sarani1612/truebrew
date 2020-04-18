[![Build Status](https://travis-ci.org/Sarani1612/truebrew.svg?branch=master)](https://travis-ci.org/Sarani1612/truebrew)

## Table of Contents
1. [True Brew](#true-brew)
2. [UX](#ux)
    1. [User Stories](#user-stories)
    2. [Wireframes](#wireframes)
3. [Features](#features)
    1. [Design and Layout](#design-and-layout)
    2. [Wireframe Differences](#wireframe-differences)
    3. [Existing Features](#existing-features)
    4. [Features Left to Implement](#features-left-to-implement) 
4. [Technologies and Tools Used](#techonolies-and-tools-used)
5. [Testing](#testing)
    1. [Testing User Stories](#testing-user-stories)
    3. [Additional Testing](#additional-testing)
    4. [Unit Testing](#unit-testing)
    5. [Issues](#issues)
        1. [Resolved](#resolved)
6. [Deployment](#deployment)
    1. [Cloning and running the project locally](#cloning-and-running-the-project-locally)
7. [Credits](#credits)
    1. [Code](#code)
    2. [Content and Media](#content-and-media)
    3. [Acknowledgments](#acknowledgments)

# True Brew

## UX
### User Stories
### Wireframes
Differences between the wireframes and the actual layout are discussed in the [Features](#wireframe-differences) section below.

## Features
### Design and Layout
#### Wireframe Differences
### Existing Features
### Features Left to Implement

## Technologies and Tools Used
- HTML, CSS, JavaScript and Python were used to build the webpage
- The [Django framework](https://palletsprojects.com/p/flask/)
- The [Bootstrap](https://getbootstrap.com/) framework was used to set up a responsive layout
- [Gitpod](https://www.gitpod.io/) was used as the IDE for this Project
- [Git](https://git-scm.com/) and [GitHub](https://github.com/) were used for version control and repository hosting
- [Heroku](https://www.heroku.com/) was used as the platform for deployment of the website
- [Autoprefixer](https://autoprefixer.github.io/) was used to add vendor prefixes to CSS code
- [Google Fonts](https://fonts.google.com/) provided the fonts used throughout the website
- [Canva](https://www.canva.com/) was used to design the website logo and [Favicon.io](https://favicon.io/) to turn it into a favicon
- [Font Awesome](https://fontawesome.com/) provided all icons used throughout the website
- [Balsamiq](https://balsamiq.com/) was used to create wireframes for the project

## Testing
JavaScript code was run through the [JSHint](https://jshint.com/) analysis tool to check for syntax errors.
In addition, CSS was checked in the [CSS Validator](https://jigsaw.w3.org/css-validator/) and HTML in the [HTML Validator](https://validator.w3.org/).

All the following testing has been carried out on smaller screens running both iOS and Android and on larger screens
running both macOS and Windows in multiple browsers. In addition, Chrome's developer tools were used extensively to test on all screen sizes
including medium size which I did not otherwise have access to.

### Testing User Stories
### Additional Testing
### Unit Testing
### Issues
#### Resolved
1. I encountered a problem with my add_to_cart function where adding more of a product already in the cart would overwrite the quantity insteading of adding the new quantity to the old. In the view I added print statements to the if-else clause:
    ```python
    def add_to_cart(request, id):
        ''' adds a subscription and the quantity chosen to the cart '''
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})

        if id in cart:
            print('Already in cart')
            cart[id] = cart[id] + quantity
        else:
            print('Not in cart')
            cart[id] = cart.get(id, quantity)

        request.session['cart'] = cart
        return redirect('cart')
    ```
    I also printed the cart to see what was in it. I then added 2 of the product with the id 3 to the cart, and then tried adding another 4, so that the total should have been 6. Instead the total was 4. The 'else' print statement was printed, indicating that the product already in the cart was not recognized, and printing cart resulted in `{'3' : 2, 3 : 4}`. It was then clear that the product was not being found because its id was stored as a string while it was being added as an integer.\
    I solved the issue by removing `int:` from the paths in the urls file so that they read `path('adjust/<id>/', ...)` instead of `path('adjust/<int:id>/, ...)'`.
#### Not resolved


## Deployment
This project was developed in Gitpod and pushed regularly to the GitHub repository via git commands in the terminal.\
The website was deployed on Heroku via the following steps:
1. I created an app on Heroku and connected to it on Gitpod in the terminal
2. I set the necessary config vars in the Heroku Settings tab (secret key, MongoDB name, MongoDB URI, IP and PORT)
3. I regularly pushed code from Gitpod to Heroku via the command line (later I set up automatic deploys from the master branch
in the Heroku Deploy tab)
4. The app was then available on ...

### Cloning and running the project locally
Follow these steps if you wish to run the project locally:
- go to the [repository page](https://github.com/Sarani1612/truebrew) on GitHub
- click the "clone or download" button on the right-hand side
- copy the URL that shows up
- in Terminal, change the current working directory to the location where you want the cloned directory to be made
- type 'git clone' and paste the URL from step 2
- press enter
- the local clone will be created

These instructions and more info can be found at [this GitHub Help Page](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

## Credits

### Code:
- [This article by Vitor Freitas](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone) was used to help me extend the User model

### Content and Media
- The texts about the different kinds of tea were adapted from [Republic of Tea](https://www.republicoftea.com/)

### Acknowledgments
- Thank you to Xavier at the Code Institute for pointing me in the right direction with how to relate the Product and Subscription models.

*This website is for educational purposes only. It was created as part of the Code Institute Full Stack Developer course.*