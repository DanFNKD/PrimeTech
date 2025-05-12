# PrimeTech e-commerce platform

Access the live site [here](https://primetechfnkd-382d679752d9.herokuapp.com/).

## Contents

* [MoSCoW priotisation](#moscow-prioritisation)
* [Features](#features)
  * [Homepage](#homepage)
  * [Products](#products)
  * [Shopping bag and checkout](#shopping-bag-and-checkout)
  * [Registration](#registration)
  * [Authenticated user specific](#authenticated-user-specific)
  * [Other pages](#other-pages)
* [User Experience design](#user-experience-design)
  * [Strategy design](#strategy-design)
  * [Business Plan](#business-plan)
  * [Wireframes](#wireframes)
  * [ERD](#entity-relationship-diagram)
  * [Design choices](#design-choices)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Bugs](#bugs)
* [How to fork and clone](#how-to-fork-and-clone)
* [Deployment](#deployment)
* [Prerequisites](#prerequisites)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

## MoSCoW prioritistation and Kanban board

I used a kanban board timeline [accessed here](https://github.com/users/DanFNKD/projects/5) to track my user stories and prioritise features based on the MoSCoW prioritisation method.

Must Haves:
1. User Accounts and Authentication:
  - Registration (username, email, and password)
  - Login and logout functionality
  - User profile pages with order history and personal details
2. Product Catalogue and Navigation:
  - Viewing a list of products (with pagination or infinite scrolling)
  - Ability to filter and sort products (by price, category, rating, etc.)
  - Viewing individual product details (including multiple images, description, pricing, and related products)
3. Shopping Cart and Checkout:
  - Adding products to the basket, adjusting quantities, and removing items
  - Displaying a cart summary with a total price (including shipping calculation)
  - Secure checkout process integrated with Stripe for payment processing
  - Order confirmation email functionality
4. Basic Search Functionality:
  - Keyword search that returns matching products
5. Deployment and Code Quality:
  - A consistent, clean Django project structure with logical app separation
  - All CRUD operations for products and related models are implemented
  - The final deployed version is secure (with secret keys and credentials stored as environment variables) and free of broken links

Should Haves:
1. Wishlist Functionality:
  - Ability for authenticated users to save items to a wishlist for later purchase
2. Advanced Search and Sorting Options:
  - Combining filters and sorting (e.g., filtering by category and sorting by price or rating)
3. User Reviews and Ratings:
  - Allowing customers to submit and update reviews on products
4. Enhanced User Experience (UX):
  - Responsive design improvements and additional UX touches (e.g., subtle animations or enhanced product card layouts)

Could Haves:
1. Personalisation and Recommendations:
  - Product recommendations based on browsing history or category
  - Customisation options for user preferences (e.g., favorite brands or categories)
2. Marketing and Engagement Features:
  - Newsletter signup form
  - Links to social media platforms such as Facebook Business pages
  - Social media integration for sharing products or promotions
3. Additional Content Features:
  - Extra pages such as “FAQs” or blog articles related to technology and products

Will Not Have Now:
1. Store Access Information:
  - Detailed “About the Store” information is not included in the current user stories
2. Advanced Promotional Features:
  - Features such as dynamic discount systems, flash sales, or extensive analytics that are beyond core e-commerce functionality

## Features

### Homepage

The homepage is scaled back, prompting users to explore other pages to learn more about the site.
![Image](/documentation/media/images/features-home.png)

### Products

#### All products

Users can browse the product catalogue, displayed in a grid layout with images and ratings.
![Image](/documentation/media/images/features-allproducts.png)

#### Product category

Users can search for products dependant on it's category.
![Image](/documentation/media/images/features-category.png)

#### Product sorting

Users can sort products on price, rating, name or category.
![Image](/documentation/media/images/features-allproductssort.png)

#### Product detail

The product detail page provides a comprehensive view of each item, including an image, description, price and rating.
![Image](/documentation/media/images/features-productdetail.png)

#### Product reviews

Users can view reviews from registered users to inform their purchases.
![Image](/documentation/media/images/features-addreview.png)

#### Product search

Search functionality allows users to find products based on keywords.
![Image](/documentation/media/images/features-search.png)

### Shopping bag and checkout

#### Shopping bag

The page allows users to review products before proceeding to checkout. Each item is displayed with its image, quantity selector and price. Users can update product quantities directly from the bag page, automatically updating the price.
![Image](/documentation/media/images/features-addtobag.png)

#### Shopping bag checkout

Users proceed with secure payment options to ensure a smooth transaction.
![Image](/documentation/media/images/features-checkout.png)

#### Transaction completing

Once payment is being processed, the user sees a temporary page before the order is completed.
![Image](/documentation/media/images/features-transactioncompleting.png)

#### Order confirmation

After checkout, users receive an order confirmation page summarising their purchase and an email.
![Image](/documentation/media/images/features-orderconfirmation.png)
![Image](/documentation/media/images/features-orderconfirmationemail.png)

### Registration

#### Sign up

New users create an account by filling in a simple registration form. There is validation and they receive an email once completed.

![Image](/documentation/media/images/features-signup.png)
![Image](/documentation/media/images/features-signupvalidation.png)

#### Sign in

Users can sign in using their verified credentials.
![Image](/documentation/media/images/features-login.png)

#### Sign out

Users can securely log out from the dropdown menu.
![Image](/documentation/media/images/features-logout.png)

### Authenticated user specific

#### Products edit and delete

Authenticated users can edit and delete existing products.
![Image](/documentation/media/images/features-loggedinuseredit.png)
![Image](/documentation/media/images/features-loggedinusereditdelete.png)

#### Reviews

Authenticated users can leave reviews on product pages.
![Image](/documentation/media/images/features-addreview.png)

#### Wishlist

Authenticated users can access a wishlist page that is stored on their account.
![Image](/documentation/media/images/features-wishlist.png)

#### Profile

Authenticated users can save their profile details, as well as view historic orders on site.
![Image](/documentation/media/images/features-profile.png)

### Other pages

#### 404 error page

Users will see an error page if they attempt to access a page that doesn't exist.
![Image](/documentation/media/images/features-404.png)

#### Facebook Business page

Users are encouraged to visit the accompanying Facebook Business page to learn more and connect with the business.
![Image](/documentation/media/images/features-facebook.png)

#### MailChimp marketing

Users are encouraged to sign up and subscribe to more updates from the site.
![Image](/documentation/media/images/features-mailchimp.png)
![Image](/documentation/media/images/features-mailchimp2.png)

## User Experience design

### Strategy design

#### User stories and epics

##### Epic: Viewing and Navigation:
- [1.1](https://github.com/DanFNKD/PrimeTech/issues/1) - As a shopper, I can view a list of products so that I can easily browse and choose items to purchase.
- [1.2](https://github.com/DanFNKD/PrimeTech/issues/2) - As a shopper, I can view a specific category of products so that I can quickly find items of interest without searching through all products.
- [1.3](https://github.com/DanFNKD/PrimeTech/issues/3) - As a shopper, I can view individual product details so that I can make an informed decision about purchasing an item.
- [1.4](https://github.com/DanFNKD/PrimeTech/issues/4) - As a shopper, I can identify deals, clearance items, and special offers so that I can take advantage of discounts.
- [1.5](https://github.com/DanFNKD/PrimeTech/issues/5) - As a shopper, I can view the total of my purchases at any time so that I can stay within my budget.
- [1.6](https://github.com/DanFNKD/PrimeTech/issues/6) - As a shopper, I can find details about the store so that I can learn about their values and policies.
- [1.7](https://github.com/DanFNKD/PrimeTech/issues/7) - As a shopper, I can find answers to questions so that I can make informed decisions before purchasing.
##### Epic: Registration and User Accounts:
- [2.1](https://github.com/DanFNKD/PrimeTech/issues/8) - As a site user, I can easily register for an account so that I can access personalised features like saved addresses and order history.
- [2.2](https://github.com/DanFNKD/PrimeTech/issues/16) - As a site user, I can easily login or logout so that I can manage my account securely.
- [2.3](https://github.com/DanFNKD/PrimeTech/issues/9) - As a site user, I can access my personalised profile so that I can view order history and save payment details.
##### Epic: Sorting and Searching:
- [3.1](https://github.com/DanFNKD/PrimeTech/issues/10) - As a shopper, I can search for products by name or description so that I can find items quickly.
- [3.2](https://github.com/DanFNKD/PrimeTech/issues/11) - As a shopper, I can sort products so that I can prioritise my preferences like best price or rating.
##### Epic: Shopping Cart Management:
- [4.1](https://github.com/DanFNKD/PrimeTech/issues/12) - As a shopper, I can add, remove, and adjust quantities in my shopping cart so that I can finalise my purchase.
##### Epic: Wishlist Management:
- [5.1](https://github.com/DanFNKD/PrimeTech/issues/13) - As a shopper, I can save items to a wishlist so that I can decide whether to purchase them later.
##### Epic: Email Communication:
- [6.1](https://github.com/DanFNKD/PrimeTech/issues/14) - As a shopper, I receive order confirmation emails so that I know my purchase was successful.
##### Epic: Admin Panel Functionality:
- [7.1](https://github.com/DanFNKD/PrimeTech/issues/15) - As an admin, I can add, update, and remove products so that the catalogue remains up to date.

### Business Plan

#### Mission Statement
- PrimeTech offers the best quality, cutting edge technology products. Our range consists of TV’s, radios, gaming consoles and accessories. We serve everyone, from tech enthusiasts to the person buying their very first product! 

#### Demographics
- Age: 18 - 55.

#### USP’s
- Competitive pricing.
- Fast shipping and hassle free returns.
- Simple layout, ensuring anyone can understand the best product for them.

#### Growth strategy
- Expand product offerings to include more specific products e..g VR products. This will help to improve SEO and generate more traction.
- Leverage data and analytics to personalise recommendations for customers.
- Plan the site around the future launch of a mobile App.
- Sustainability strategies such as recycling programs and partnering with ethical manufacturers.

#### Key partners
- Suppliers - Leading manufactures, newer entrants to expand product base.
- Delivery partners - Reliable shipping is crucial to customer satisfaction.
- Internal team - Support and after sales service key to repeat custom and build a strong reputation.

#### Marketing strategies
- Use newsletter providers (such as MailChimp) to increase audience and keep customers up to date.
- Utilise social media (such as Facebook) to promote the brand and engage existing customers.
- Expand social media presence to cover more channels.

### Wireframes

![Home Page](/documentation/media/images/wireframes-home.png)

![Products Page](/documentation/media/images/wireframes-products.png)

![Mobile Page](/documentation/media/images/wireframes-mobile.png)

### Entity Relationship Diagram

![ERD](/documentation/media/images/ux-erd.png)

### Design choices

#### Colour scheme

The PrimeTech site uses a modern, bright colour palette that emphasises contrast and readability:

- **Primary:** - '#000000' (Black)
- **Secondary:** - '#ffffff' (White)
- **Accent Elements:** - '#f8f9fa' (Grey)
- **Success:** - '#28a745' (Green)
- **Brand Highlight:** - '#ffd700' (Gold)(used in delivery banner, links and buttons)

#### Typography

The site uses clean, modern typography to further reinforce readability:

- **Base font:** - 'Lato', loaded in via Google Fonts

## Technologies Used

### Languages

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [jQuery](https://jquery.com/) 
-   [Python](https://www.python.org/)

### Frameworks, Libraries & Programs Used  

-   [Google Fonts:](https://fonts.google.com/) used for the Lato font.
-   [Font Awesome:](https://fontawesome.com/) used for icons.
-   [Bootstrap](https://getbootstrap.com/) used to build responsive web page
-   [Git:](https://git-scm.com/) used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
-   [GitHub:](https://github.com/) used as the repository for the project code after being pushed from Git. Also used for agile development via User Stories and tracking on a Kanban board. 
-   [Django v5.4](https://www.djangoproject.com/) was used as the framework to support rapid and secure development of the application.
s
-   [Django allauth](https://django-allauth.readthedocs.io/en/latest/index.html) used for account registration and authentication.
-   [Pillow](https://pillow.readthedocs.io/en/stable/index.html) - Python Imaging Library used for image handling
-   [Django crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/) used to simplify form rendering.
-   [Stripe](https://js.stripe.com/v3/) used for secure payments (referenced in base.html).
-   [Django Countries](https://pypi.org/project/django-countries/) used on checkout page to pass valid country code to Stripe.
-   [Gunicorn](https://gunicorn.org/) was used as the Web Server to run Django on Heroku.
-   [psycopg2](https://pypi.org/project/psycopg2/) database adapter used to support the connection to the postgres db.
-   [Heroku](https://www.heroku.com) - used to host the deployed application.
-   [Balsamiq:](https://balsamiq.com/) was used to create the wireframes during the design process.
-   [Facebook:](https://www.facebook.com/) was used to create a Facebook business page.
-   [MailChimp:](https://mailchimp.com/?currency=EUR) was used for the purpose of digital marketing.

## Testing

Detailed testing can be found [here.](TESTING.md)

## Bugs

#### TV Category
![Image](/documentation/media/images/bug-category1.png)
![Image](/documentation/media/images/bug-category2.png)
![Image](/documentation/media/images/bug-category3.png)
![Image](/documentation/media/images/bug-category4.png)

Whilst testing, I noticed that nothing was appearing in my TVs category. This was because of a labelling error and was resolved by updating the Category from TVs to TV.

#### Order Total
![Image](/documentation/media/images/bug-ordertotal1.png)
![Image](/documentation/media/images/bug-ordertotal2.png)
![Image](/documentation/media/images/bug-ordertotal3.png)
![Image](/documentation/media/images/bug-ordertotal4.png)
![Image](/documentation/media/images/bug-ordertotal5.png)

Whilst testing, I noticed that the order total wasn't pulling through to the django admin or the profile order history. The model was updated and the issue was resolved.

#### Images
![Image](/documentation/media/images/bug-image1.png)
![Image](/documentation/media/images/bug-image2.png)

Whilst testing, I noticed that images weren't corrected. I moved them into static to help this.

## How to Fork and Clone

### Forking the Repository

1. Log in to your GitHub account.
2. Navigate to the repository for this project - PrimeTech.
3. Click the Fork button in the top right corner of the page to create a copy under your own GitHub account.

### Cloning the Repository

1. After forking, go to your forked version of the PrimeTech repository
2. Click the green Code button and choose your preferred method.
3. Copy the provided URL.
4. Open your terminal or code editor and change to the directory where you'd like to store the project.
5. Type 'git clone' into terminal and then paste the link you copied in step 3.
6. Press Enter. The repository will be cloned to your local machine.

## Deployment

### Deploying to Heroku

1. Create an account on Heroku and log in. 
2. Create a new app and navigate to 'settings'.
3. Click 'Reveal config variables'.
4. Add the following environment variables:
   - `DATABASE_URL` – the Postgres URL
   - `SECRET_KEY` – your Django secret key
   - `CLOUDINARY_URL` – your Cloudinary API key (to display images correctly)
   - `EMAIL_HOST_USER` – your email address
   - `EMAIL_HOST_PASSWORD` – your email password or app password
   - `STRIPE_PUBLIC_KEY` – your Stripe publishable key
   - `STRIPE_SECRET_KEY` – your Stripe secret key
   - `MAILCHIMP_API_KEY` – your Mailchimp API key (if used)
   - `MAILCHIMP_AUDIENCE_ID` – your Mailchimp audience/list ID
5. In the IDE go to your main app's settings file and add the heroku app name to the allowed hosts. Be sure to append `.herokuapp.com` to your app's name. 
6. Add EMAIL_HOST_PASSWORD and the value as the password for the email service.
In the Gitpod terminal, install  `pip3 install dj_database_url==2.2.0 psycopg2`
7. In the Gitpod terminal, run `pip freeze > requirements.txt`
8. In the settings.py file, type in `import dj_database_url` under `import os`
9. In the DATABASES section of the settings.py file, insert the following code: 
```python
DATABASES = {
     'default': dj_database_url.parse('your-database-url-here')
 }
 ```
 10. Do not commit with the database string in the code
 11. In the terminal, run `python3 manage.py showmigrations` to confirm the database is connected
 12. Add the following if statement to the settings.py:
 ```python
    if "DATABASE_URL" in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
            }
        }
```
13. In the terminal, type in `pip3 install gunicorn==23.0.0`
14. In the terminal, run `pip freeze > requirements.txt`
15. Create a Procfile in the root directory and add `web: gunicorn primetech.wsgi --log-file -` 
16. In the terminal, type in `heroku config:set DISABLE_COLLECTSTATIC=1`
17. Commit and push your changes to GitHub.
18. On Heroku, go to the Deploy tab, connect to GitHub and deploy from the main branch.
19. Click "View App" to launch the deployed site.

## Prerequisites

- A **Cloudinary** account will be needed to store and serve media files (e.g. product images). You can create one for free at [https://cloudinary.com](https://cloudinary.com).
  
- An account with an **email service** (such as Gmail or SendGrid) that can be used to send confirmation and notification emails to users. This will be needed to configure `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD`.

- A **Heroku** account is required for cloud deployment. You can sign up at [https://heroku.com](https://heroku.com).

- A **Mailchimp** account (if using newsletter functionality), with an audience/list set up. You'll need the API key and Audience ID.

- A **Stripe** account for handling secure payment processing. You’ll need your publishable key, secret key, and optionally a webhook secret.

- Ensure you have **Python 3**, **Pip**, and **Git** installed locally, or use a cloud IDE like Gitpod.

- A **PostgreSQL database URL** (you can provision this through Heroku Postgres or an external provider).

## Credits

Code Institute [Slack](https://slack.com/intl/en-gb) channel for tips/hints.

Product images [Google](https://images.google.co.uk/).

About us copy written by [ChatGPT](https://chatgpt.com/).

ERD created using [dbdiagram.io](https://dbdiagram.io).

## Acknowledgments

I'd like to thank my girlfriend for putting up with me throughout this process and my new Mentor Daniel Hamilton for his help.

