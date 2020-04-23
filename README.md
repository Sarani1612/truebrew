[![Build Status](https://travis-ci.org/Sarani1612/truebrew.svg?branch=master)](https://travis-ci.org/Sarani1612/truebrew)

## Table of Contents
1. [True Brew](#true-brew)
2. [UX](#ux)
    1. [User Stories](#user-stories)
    2. [Wireframes](#wireframes)
3. [Features](#features)
    1. [Design and Layout](#design-and-layout)
        1. [Wireframe Differences](#wireframe-differences)
    2. [Existing Features](#existing-features)
    3. [Features Left to Implement](#features-left-to-implement) 
4. [Technologies and Tools Used](#technologies-and-tools-used)
5. [Testing](#testing)
    1. [Testing User Stories](#testing-user-stories)
    3. [Additional Testing](#additional-testing)
    4. [Unit Testing](#unit-testing)
    5. [Issues](#issues)
        1. [Resolved](#resolved)
        2. [Unresolved](#unresolved)
6. [Deployment](#deployment)
    1. [Cloning and running the project locally](#cloning-and-running-the-project-locally)
7. [Credits](#credits)
    1. [Code](#code)
    2. [Content and Media](#content-and-media)
    3. [Acknowledgments](#acknowledgments)

# True Brew
True Brew is my final milestone project for the Code Institute Full-Stack Web Development course making use of the programming languages and frameworks taught in all the modules throughout the course.
It is an e-commerce site where users can register for an account and buy loose-leaf tea subscription boxes.\
The live site can be found at [True Brew](https://truebrew.herokuapp.com/)
## UX
The target audience for this website are people who are passionate tea-drinkers and who are interested in buying and drinking tea of a better quality and with more varieties than what can usually be found in supermarkets.\
The website also caters to people with a sense of adventure and who like the element of suprise given that they do not have full control over which products they are going to receive in the boxes.\
A user's goals/needs would include:
- finding a subscription box with a type of tea they like
- finding a gift for a tea-drinker in their life
- browsing all products and reading descriptions of each kind of tea
- keeping track of account and order details

With these user goals in mind, I came up with the following user stories and then created the wireframes below for a blueprint of how best to meet the needs of the users.

### User Stories
### Wireframes
I created wireframes for small, medium and large screens for the following pages on the website:
- [Home](wireframes/about.pdf)
- [About](wireframes/about.pdf)
- [User Account](wireframes/account.pdf)
- [Login](wireframes/login.pdf)
- [Register](wireframes/register.pdf)
- [Product view](wireframes/product.pdf)
- [Cart](wireframes/cart.pdf)
- [Checkout](wireframes/checkout.pdf)
- [Payment](wireframes/payment.pdf)
- [Order Confirmation](wireframes/order-confirmation.pdf)
- [Contact](wireframes/contact.pdf)

Differences between the wireframes and the actual layout are discussed in the [Features](#wireframe-differences) section below.

## Features
### Design and Layout
#### Wireframe Differences
### Existing Features
### Features Left to Implement
### Databases/Models
While developing the app, the SQL database used was the **sqlite3** database that comes with Django.\
In production I used the **PostgreSQL** database available on Heroku.

#### Accounts app models
I used the **User** model provided by Django for letting users register and log in. In addition, I created a custom **UserInfo** model:
| Key             | Field Type | Validation                |
|-----------------|------------|---------------------------|
| user            | OneToOne   | on_delete=models.CASCADE  |
| street_address1 | CharField  | max_length=40, blank=True |
| street_address2 | CharField  | max_length=40, blank=True |
| town_or_city    | CharField  | max_length=40, blank=True |
| postcode        | CharField  | max_length=20, blank=True |
| county          | CharField  | max_length=40, blank=True |
| country         | CharField  | max_length=40, blank=True |
| phone_number    | CharField  | max_length=20, blank=True |

An object in this model has a one-to-one relationship with a User object, and the user can store address and contact info here for faster checkouts. Apart from the user field, all the fields are allowed to be blank because users are not required to enter their details in the database if they do not want to.

#### Checkout app models
the **Order** model:
| Key             | Field Type | Validation                 |
|-----------------|------------|----------------------------|
| user            | OneToOne   | on_delete=models.CASCADE   |
| full_name       | CharField  | max_length=50              |
| street_address1 | CharField  | max_length=40              |
| street_address2 | CharField  | max_length=40, blank=True  |
| town_or_city    | CharField  | max_length=40              |
| postcode        | CharField  | max_length=20, blank=True  |
| county          | CharField  | max_length=40, blank=True  |
| country         | CharField  | max_length=40              |
| email           | EmailField |                            |
| phone_number    | CharField  | max_length=20              |
| date            | DateField  |                            |

This model is used for storing orders. Each order object is related to a user on a one-to-one basis, so they can be retrieved and displayed on the user's account page. **street_address2**, **postcode** and **county** are allowed to be blank as they are not necessarily used in all countries in the world.

The **OrderLineItem** model:
| Key          | Field Type   | Validation               |
|--------------|--------------|--------------------------|
| order        | ForeignKey   | on_delete=models.CASCADE |
| subscription | ForeignKey   | on_delete=models.CASCADE |
| quantity     | IntegerField |                          |

This model stores an object for each item in an order. Each object relates to an Order and represents a particular subscription object in the Subscription model (Products app).

#### Pages app models
The **ContactMessage** model:
| Key             | Field Type | Validation                 |
|-----------------|------------|----------------------------|
| user            | ForeignKey | on_delete=models.CASCADE, blank=True, null=True|
| email           | EmailField    |                         |
| title           | CharField     | max_length=150          |
| message_body    | TextField     |                         |
| date_sent       | DateTimeField | auto_now_add=True       |

This model stores all messages sent through the Contact page form. If it was sent by a logged in user, the message has a ForeignKey to that user, allowing it to be retrieved and displayed on the user's account page. The user input field is not shown on the contact form.

#### Products app models
The **Product** model:
| Key               | Field Type | Validation                 |
|-------------------|------------|----------------------------|
| title             | CharField  | max_length=50              |
| category          | CharField  | max_length=20, choices=TEA_CHOICES,default=BLACK_TEA   |
| image             | ImageField |                            |
| description       | TextField  |                            |
| short_description | TextField  |                            |

This model stores an object for each tea available in the store.

The **Subscription** model:
| Key               | Field Type   | Validation                         |
|-------------------|--------------|------------------------------------|
| frequency         | CharField    | max_length=15                      |
| description       | TextField    |                                    |
| unit_price        | DecimalField | max_digits=6, decimal_places=2     |
| practical_info    | CharField    | max_length=200                     |
| product           | ForeignKey   | on_delete=models.CASCADE, null=True|

Each object in this database is a specific subscription related to a specific object in the Product database.

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
#### Unresolved


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
- The images for the background and the mixed tea section are free images from [Pixabay](https://pixabay.com/):
  - Background photo from  [dungthuyvunguyen](https://pixabay.com/users/dungthuyvunguyen-5499796/)
  - Mixed teas photo from [gate74](https://pixabay.com/users/gate74-5942741/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=2519551)
- The other photos of the different tea types are from [Nordic Tea](https://nordic-tea.dk/) (For educational use only. No copyright infringement intended.)

### Acknowledgments
- Thank you to Xavier at the Code Institute for pointing me in the right direction with how to relate the Product and Subscription models.

*This website is for educational purposes only. It was created as part of the Code Institute Full Stack Developer course.*