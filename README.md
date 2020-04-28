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
6. [Deployment](#deployment)
    1. [Cloning and running the project locally]
    2. (#cloning-and-running-the-project-locally)
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
1. as a first-time user of the website, I want to be able to intuitively browse so that I do not have to hunt around for things
2. as a first-time user, I want to be able to find out what services are offered and who is behind them
3. as a first-time user, I want to be able to see what is on offer before registering for an account
4. as a new user who is ready to register, I want to be able to do so quickly and easily
5. as a returning user, I want to be able to log in to my account
6. as a returning user who forgot my password, I want to be able to reset it so that I can log in again
7. as a returning user, I want to be able to add an address so I can checkout faster
8. as a returning customer, I want to be able to see an overview of my previous orders
9. as a user who has decided to buy a product, I want to be able to add it to a cart and have easy access to checking the cart
10. as a user who has decided to buy a product, I want a quick and easy checkout process
11. as a user, registered or not, I want a convenient way to get in touch with the business
12. as a logged in user who is ready to leave the website, I want to be able to log out so that I do not leave personal information accessible to others

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
- For now, this project uses the Stripe Charges API as it was taught in the course (with some changes due to the project using Stripe V3 and not V2 as in the course), but this is not ideal as it does not handle payments that need card authentication which is widely used in Europe. I would have liked to implement either Stripe Checkout or the Payment Intents API, but I was not able to do so with the time available to me. I am hoping to be able to implement this once I have more time and experience.
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
- [Amazon S3 Bucket](https://aws.amazon.com/s3/) was used to store images
- [Django Storages](https://django-storages.readthedocs.io/en/latest/) and [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) were used to connect Django with S3

## Testing
See the separate [TESTING.md](TESTING.md)

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
- [This guide by Vitor Freitas](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone) was used to help me extend the User model
- [John Elder's Codemy](https://codemy.com/) course on Django user authentication helped me set up the login/registration forms and views.
- [This guide by Dan Kaufhold](https://blog.bitlabstudio.com/ultra-short-guide-to-django-and-amazon-s3-2c5aae805ce4) helped me set up S3 media hosting

### Content and Media
- The texts about the different kinds of tea were adapted from [Republic of Tea](https://www.republicoftea.com/)
- The images for the background and the mixed tea section are free images from [Pixabay](https://pixabay.com/):
  - Background photo from  [dungthuyvunguyen](https://pixabay.com/users/dungthuyvunguyen-5499796/)
  - Mixed teas photo from [gate74](https://pixabay.com/users/gate74-5942741/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=2519551)
- The other photos of the different tea types are from [Nordic Tea](https://nordic-tea.dk/) (For educational use only. No copyright infringement intended.)

### Acknowledgments
- Thank you to Xavier at the Code Institute for pointing me in the right direction with how to relate the Product and Subscription models.

*This website is for educational purposes only. It was created as part of the Code Institute Full Stack Developer course.*