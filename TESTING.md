# True Brew - Testing

1. [Manual Testing](#manual-testing)
    1. [Testing User Stories](#testing-user-stories)
    2. [Testing Features](#testing-features)
2. [Automated Testing](#automated-testing)
3. [Issues](#issues)
    1. [Resolved](#resolved)
    2. [Unresolved](#unresolved)
4. [Additional Testing](#additional-testing)

## Manual Testing

### Testing User Stories
1. as a first-time user of the website, I want to be able to intuitively browse so that I do not have to hunt around for things
     - This is easily done via the navbar which is always at the top of the browser. The navbar has clearly labelled links to all subpages, and from here the user can get anywhere on the website.
2. as a first-time user, I want to be able to find out what services are offered and who is behind them
    - Info about the business and its services is available as soon as the user gets to the home page. The text on the landing page image sums up what is on offer here, and further down there are two info boxes detailing the services and how the business started.
3. as a first-time user, I want to be able to see what is on offer before registering for an account
    - On this website, a user only has to register for an account once they get to the checkout process, so there is ample opportunity for getting a sense of the products on offer and the business before then. All the different teas available can be reached from the navbar and the home page, so the user does not have to go far to find out what the products are.
4. as a new user who is ready to register, I want to be able to do so quickly and easily
    - To register, a user would only have to click the 'Register' link in the navbar which leads to a simple and easy to fill out registration form. It is only necessary to provide an email address, a username and a password, so the whole process does not take long, and the helper text for each field provided by Django also makes it easy to fill out the form.
5. as a returning user, I want to be able to log in to my account
    - A user can do this at any time by clicking the 'Login' link in the navbar.
6. as a returning user who forgot my password, I want to be able to reset it so that I can log in again
    - This can be done by going to the login page and clicking on the link to reset password under the form. The user will receive an email with a link they need to follow in order to reset their password.
7. as a returning user, I want to be able to add an address so I can checkout faster
    - On the user's account page, they will find a table showing address and contact information. They can click the pen icon and fill out the form that comes up, and when they then go to checkout, the address form will be prepopulated with those details.
8. as a returning customer, I want to be able to see an overview of my previous orders
    - The user will find an overview of all orders they've placed on their account page.
9. as a user who has decided to buy a product, I want to be able to add it to a cart and have easy access to checking the cart
    - Products are easy to add to the cart. The user must go the product page for the tea they are interested in, and there they will find information about the three different subscription types available. They can click the button to add 1 subscription to the cart or adjust the amount before clicking. The cart is always available from the navbar.
10. as a user who has decided to buy a product, I want a quick and easy checkout process
    - The checkout process is very quick and easy. When a user goes to the cart and clicks on the 'Checkout' button, they will be taken to the checkout page where they can see an order summary and fill out a single form to place the order.
11. as a user with items in my cart, I want to be able to adjust the amount or delete from it
    - The user can do this by going to the cart view. Here, they can see how many of a specific subscription they have, and they can adjust the amount or click on the bin icon to remove something completely from the cart.
12. as a user, registered or not, I want a convenient way to get in touch with the business
    - This can be done via the Contact page which is always available from the navbar. The user only needs to fill out their email address (if not logged in already), a subject line and message. When they click the 'Send' button, an email will be sent to the business' email address.
13. as a logged in user who is ready to leave the website, I want to be able to log out so that I do not leave personal information accessible to others
    - The user can do this by clicking on the 'Log out' link in the navbar. The user is then rerouted to the home page and the navbar links change ('Login' and 'Register' instead of 'Log out' and 'Account') showing that the user has indeed been logged out.

### Testing Features
All the following testing has been carried out on smaller screens running both iOS and Android and on larger screens running both macOS and Windows in multiple browsers. In addition, Chrome's developer tools were used extensively to test on all screen sizes including medium size which I did not otherwise have access to.
- **Navbar:** no issues found. Renders and stays in place as intended. All links are working. The correct links are shown for users that are logged in and users not logged in. On small screens the navbar collapsed into dropdown except for the account and cart links which are shown as icons.
- **Home page:** the home page renders as intended across screen sizes and browsers. On small screens everything is stacked, while on medium and up product cards are displayed in rows of 4.\
While testing on a smartphone, I noticed that there was no spacing between the two info boxes in the About Us section, which looked a little cramped. To solve this, I added a little margin at the bottom of the first box.
- **Products page:** the products page renders as intended. On small screens all the product cards are stacked, on medium screens (e.g. iPad) they are shown 2 per row, on large screens (e.g. iPad Pro) there are 3 per row and on extra large screens 4 per row. Images render nicely and all the buttons are working.
- **Product view:** product and subscription cards render with all the necessary info and images, but on medium sized screens the cards were very narrow and long, and it did not look great. I solved this by changing the product div Bootstrap class to `col-md-8` instead of `col-md-6` so that it is broader on medium screens. For the subscription cards, I changed the layout so that there are only 2 per row on medium screens.
- **Contact page:** the contact pages renders as intended. When logged in, the user and email fields are prepopulated as intended. If the 'Send' button is clicked without all the fields filled in, the user is notified of this and the form does not submit.\
On succesfully sending a message, the page refreshes and a success message is displayed. The message is saved in the ContactMessage model.
- **Cart:** the cart renders as intended. If there are no items in the cart, a paragraph is displayed to inform the user of this along with a button to the products page.\
If there are items in the cart, a table is displayed with a row per subscription and options to amend or delete. Both of these worked as intended. Upon amending the number of a particular subscription, the prices are adjusted, and when a subscription is deleted, a flash message shows up to let the user know that it has been removed from the cart. The 'Back to Shopping' and 'Checkout' buttons work as intended.
- **Checkout:** The checkout page renders as intended with an order summary and a checkout form. When not logged in, I got redirected to the login page as intended. The fields in the form were correctly prepopulated with any details available in the UserInfo model.\
I tested the payments both with correct and incorrect card info and they all behaved correctly. Stripe handles most of the validation, so error messages are shown when entering invalid card numbers, CVV numbers, dates etc.\
For testing of the payment form, please use the test card numbers available [here](https://stripe.com/docs/testing). Using any of the 3D Secure card numbers will fail. This is expected since the Stripe Charges API does not support card authentication. A flashed message appears to inform the user that the payment did not go through.\
In case the payment was successful, the user gets redirected to their account page with a message telling them that their order has been placed. 
- **User registration, login and logout:** Login and Registration forms render correctly. Error messages are displayed when needed. After registration, the user is automatically logged in with a success message. Logout works as intended; the user gets redirected to the home page with a success message, and the navbar links change.\
As with the cards on the product page, the authentication forms initially looked very narrow on medium screens. Again, this was remedied by using the Bootstrap `col-md-8` class instead of `col-md-6`.
- **Password reset:** No issues found with this functionality. All password reset views render correctly and are consistent with the website design. The reset link in the email works and the password gets updated.
- **User account page:** Renders as intended. Correctly shows the user's address and contact details along with message and order histories. Editing the details works well and so do the accordions.
- **Messages:** The flash messages render as intended whenever they are needed, and the JavaScript function to remove them after 5 seconds works as well.

## Automated Testing
JavaScript code was run through the [JSHint](https://jshint.com/) analysis tool to check for syntax errors.
In addition, CSS was checked in the [CSS Validator](https://jigsaw.w3.org/css-validator/) and HTML in the [HTML Validator](https://validator.w3.org/).

I also created a number of automated tests for this project (these can be found in the app folders in the repository).\
As I do not have much experience with writing automated tests, they are fairly limited in scope and they by no means cover the whole project, but it was good practice to at least write a few testing forms and urls.

## Issues
### Resolved
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
2. On the account page when clicking the icon to add or edit a user's address details, the DoesNotExist exception was raised. This was because no object had yet been created for that particular user in the UserInfo model where those details are stored.\
The issue was solved by using the `get_or_create()` method instead of just `get()`. This way, an object is created when the user clicks the edit icon for the first time, allowing them to add their address details.
3. I noticed that the order form sometimes rendered without placeholder text in the Full Name input field. I then realised that, due to my code being `'full_name': request.user.first_name + ' ' + request.user.last_name`, the input field actually rendered with just a space in it in cases where there was no `first_name` or `last_name` stored for the user.\
I solved the issue with this if-else statement:
    ```python
    if request.user.first_name and request.user.last_name:
                full_name = request.user.first_name + ' ' + request.user.last_name
            else:
                full_name = ''
    ```
    Now the input field is empty whenever a user does not have both a first and last name stored, and therefore the placeholder text shows up.

### Unresolved
1. For some reason, the emails sent via the contact form to the business mailbox have the business email address as both to address ans from address. This would definitely be a problem in a real life situation since the business would have no way of knowing who the email was sent from and no way of getting in touch with the sender.\
I have gone over the Django documentation for sending emails thoroughly, but at this stage I cannot point to the flaw in my code that is producing this behaviour, as it appears to be identical to what is in the documentation.
2. Running the registration page through the HTML validator returns the error `No p element in scope but a p end tag seen.` However, this comes from the build in Django form and I was therefore not able to resolve the issue.

## Additional Testing
In addition to the testing described above, I asked my partner and my sister to test the website for me. I wrote them a use case to ensure they tested as much of the site's functionality as possible. They both reported back that they did not find any bugs.
