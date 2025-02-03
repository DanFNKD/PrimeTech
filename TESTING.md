# PrimeTech Testing

## User Story Testing

### Epic: Viewing and navigation
- 1.1 - I know "as a shopper, I can view a list of products so that I can easily browse and choose items to purchase" is completed when I can follow links and use search fields to find different products in specific categories. - PASS
- 1.2 - I know "as a shopper, I can view a specific category of products so that I can quickly find items of interest without searching through all products" when I can select products by category and be shown only those specific products. - PASS
- 1.3 - I know "as a shopper, I can view individual product details so that I can make an informed decision about purchasing an item" when I can click into a product and be provided with information such as it's name, a description and price. - PASS
- 1.4 - I know "as a shopper, I can quickly identify deals and special offers so that I can take advantage of discounts" when I can see discounted products or access a specific filter on the site that takes me to them. - FAIL, NOT THIS TIME
- 1.5 - I know "as a shopper, I can easily view the total of my purchases at any time so that I can stay within my budget" when I can see the value of what is in my basket across site pages. - PASS
- 1.6. - I know "as a shopper, I can find details about the store so that I can learn about their values and policies" when I can visit a specific page that provides me with this information. - PASS
- 1.7 - I know "as a shopper, I can find answers to my questions so that I can make informed decisions before purchasing" when I can visit a specific page providing me with answers to frequently asked questions - PASS

### Epic: Registration and user accounts
- 2.1 - I know "as a site user, I can register for an account so that I can access personalised features like saved addresses and order history" when I can successfully sign up for an account and receive automated emails to complete this process. - PASS
- 2.2 - I know "as a site user, I can login or logout so that I can manage my account securely" when I can easily login or logout. - PASS
- 2.3 - I know "as a site user, I can access my personalised profile so that I can view order history and save payment details" when I can access a profile section, look at previous orders and save various details that can be used for future orders. - PASS

#### Epic: Sorting and searching
- 3.1 - I know "as a site user, I can search for products by name or description so that I can find new items quickly" when I can utilise search functionalit to identify keywords. - PASS
- 3.2 - I know "as a site user, I can sort products so that I can prioritise my preferences like best priced or rating" when I can use a sort feature to sort based on price, rating, name or category. - PASS

#### Epic: Shopping cart management
- 4.1 - I know "as a shopper, I can add, remove and adjust quantities in my shopping cart so that I can finalise my purchase" when I can click to add a product to my bag. I can then navigate to the cart to either remove it if I change my mind or increase/reduce the quantity if my decision has changed. Should I return to another page, the contents should be saved for me to return and complete my purchase. - PASS

#### Epic: Wishlist management
- 5.1 - I know "as a shopper, I can save items to a wishlist so that I can decide whether to purchase them later" when I can select "add to wishlist" from either the core list of products or by clicking on a product individually. When selected, the item is sent to my custom wishlist page and saved until I remove it. - PASS

#### Epic: Email communication
- 6.1 - I know "as a shopper, I receive order confirmation emails so that I can know my purchase was successful" when I automatically receive an email containing information such as my order reference, product details and the total value once I complete a purchase. - PASS

#### Epic: Admin panel functionality
- 7.1 - I know "as an admin, I can add, update and remove products so that the catalogue remains up to date" when I can navigate to the admin panel and add new products, update existing ones and remove ones that are no longer available. - PASS

## Manual feature testing

**All pages**

| **Feature** | **Expected outcome** | **Testing performed** | **result** | **Pass/fail** |
| --- | --- | --- | --- | --- |
| Navigation bar | Responsive | Test on various devices | Collapses on smaller screens | Pass |
| Logo | Leads to Index page when clicked on | Click on the logo | Leads to index page | Pass |
| Navbar links | Lead to relevant pages | Click on the links | Correct pages open | Pass |
| Search bar | Displays search queries | Input query into the form | Shows results for a given query | Pass |
| Basket total | Correct basket total displays | Add Products to basket | Correct basket total displays | Pass |
| All products dropdown | Shows filters | Click on the dropdown | Displays products sorted/filtered as requested | Pass |
| Entertainment dropdown | Displays products for a relevant category | Click on the dropdown links | Displays products for the relevant category | Pass |
| Free delivery banner | Shows a correct free delivery threshold | Open all pages | Free Delivery Threshold displayed | Pass |
| Footer | Displayed on all pages | Open all pages | Footer appears | Pass |

**Index Page**

| **Feature** | **Expected outcome** | **Testing performed** | **result** | **Pass/fail** |
| --- | --- | --- | --- | --- |
| Background | Displays on load | Go to the index page | Appears | Pass |
| Mission statement | Displays on load | Go to the index page | Text appears | Pass |

**All products page**

| **Feature** | **Expected outcome** | **Testing performed** | **result** | **Pass/fail** |
| --- | --- | --- | --- | --- |
| Product cards | Displays product image | Open the all products Page | Images appear | Pass |
| Product cards | Display product title and price | Open the all products Page | titles and prices appear | Pass |
| Product image | Clicking on the image opens a product detail page | Click on the image | Correct product detail page opens | Pass |
| Admin buttons | Appear to the superuser | Log in as superuser | Edit and delete buttons appear | Pass |
| Edit button | Opens a product edit page | Click on the button | Edit product page opens for the correct product | Pass |
| Delete button | Deletes a product | Click on the button | Product deleted | Pass |
| Dropdown | Sort products | Select different sorting options | Products sorted correctly | Pass |
| Category page | Appears when clicked on a category name | Click a category name on a product card | Correct product(s) appear | Pass |
| Product count | Shows the amount of products within the category | Click a category name on a product card | Correct number of products appears | Pass |
| Product query | Shows relevant products | Type a query into the search bar | Correct products appear | Pass |
| Back to the top button | Takes user back to the top of the page | Click on the button | Works as expected | Pass |

**Product detail page**

| **Feature** | **Expected outcome** | **Testing performed** | **result** | **Pass/fail** |
| --- | --- | --- | --- | --- |
| Product detail page | Displays correct product information | Go to the product detail page for any product | Correct information displayed | Pass |
| Add to basket button | Adds product to basket | Click on the button | Product added | Pass |
| Quantity selector | Select quantity | Add to basket | Correct quantity added | Pass |
| Add to basket button | Min value is 1, max value is 99 | Try to add less than 1 or more than 99 products | Impossible to add | Pass |
| Add to wishlist icon | Adds or removes from wishlist | Click on the icon | Works as expected | Pass |
| Edit button | Opens a product edit page | Click on the button | Edit product page opens for the correct product | Pass |
| Delete button | Deletes a product | Click on the button | Product deleted | Pass |

**Add product page**

| **Feature** | **Expected outcome** | **Testing performed** | **result** | **Pass/fail** |
| --- | --- | --- | --- | --- |
| Product form | Loads all the fields | Go to the product management page | Works as expected | Pass |
| Image field | Image title appears | Add image | Works as expected | Pass |
| Product form | Adds a new product | Fill out the form and click submit | New product added | Pass |

**Edit product page**

| **Feature** | **Expected outcome** | **Testing performed** | **result** | **Pass/fail** |
| --- | --- | --- | --- | --- |
| Product form | Fields prepopulated with existing information | Go to the edit product page | Works as expected | Pass |
| Image field | Current image displayed | Go to the product page | Works as expected | Pass |
| Product form | Updates the product | Fill out the form and click submit | Product updated | Pass |

**Bag page**

| **Feature** | **Expected outcome** | **Testing performed** | **result** | **Pass/fail** |
| --- | --- | --- | --- | --- |
| Table | Display product image, title, price, quantity and subtotal | Add product to basket | Works as expected | Pass |
| Quantity selector | Updates product quantity | Change quantity and click update | Works as expected | Pass |
| Quantity selector | Min value is 1, max value is 99 | Try to add less than 1 or more than 99 products | Impossible to add | Pass |
| Remove link | Removes product from basket | Click on | Works as expected | Pass |
| Prices | Subtotal, basket Total, Delivery and Grand Total show the correct amount | Add products to basket | Works as expected | Pass |
| Secure Checkout button | Opens the checkout page | Click on the button | Works as expected | Pass |

**Checkout page**

| **Feature** | **Expected outcome** | **Testing performed** | **result** | **Pass/fail** |
| --- | --- | --- | --- | --- |
| Order summary | Displays correct details | Add products to basket and go to checkout | Works as expected | Pass |
| Delivery info | Loads correct fields | Go to checkout | Works as expected | Pass |
| Save delivery info | Saves delivery info | Check the checkbox and go to the profile | Works as expected | Pass |
| Stripe payment | Make a payment | Input stripe testing card details | Works as expected | Pass |
| Loading spinner overlay | Appears when payment is being processed | Click complete order | Works as expected | Pass |

**Checkout success page**

| **Feature** | **Expected outcome** | **Testing performed** | **result** | **Pass/fail** |
| --- | --- | --- | --- | --- |
| Checkout success page | Appears when an order is successfully placed | Place an order | Works as expected | Pass |
| Email | Displays the correct user email | Place an order | Works as expected | Pass |
| Order number | Displays an order number | Place an order | Works as expected | Pass |

**Profile page**

| **Feature** | **Expected outcome** | **Testing performed** | **result** | **Pass/fail** |
| --- | --- | --- | --- | --- |
| Default delivery information form | Displays correct fields | Go to the profile page | Works as expected | Pass |
| Default delivery information form | Shows saved delivery info | Save delivery info and go to the profile page | Works as expected | Pass |
| Default delivery information form | Updates default delivery info | Click update information | Works as expected | Pass |
| Order history | Shows previous orders' details | Place orders and go to the profile page | Works as expected | Pass |
| Order number | Displays past order confirmation when clicked on | Click on the order number | Works as expected | Pass |

**Wishlist page**

| **Feature** | **Expected outcome** | **Testing performed** | **result** | **Pass/fail** |
| --- | --- | --- | --- | --- |
| Wishlist page | Displays products added to wishlist by the user | Add products to wishlist | Works as expected | Pass |
| Add to wishlist button | Changes icon | Click the button | Works as expected | Pass |
| Remove from wishlist button | Changes icon | Click the button | Works as expected | Pass |

**Register page**

| **Feature** | **Expected outcome** | **Testing performed** | **result** | **Pass/fail** |
| --- | --- | --- | --- | --- |
| Register form | Displays correct fields | Go to the register page | Works as expected | Pass |
| Back to login button | Redirects to the login page | Click on the button | Works as expected | Pass |
| Sign in link | Redirects to the login page | Click on the link | Works as expected | Pass |
| Confirmation email | Received when a new account is created | Create a new account | Works as expected | Pass |

**Login page**

| **Feature** | **Expected outcome** | **Testing performed** | **result** | **Pass/fail** |
| --- | --- | --- | --- | --- |
| Login form | Displays correct fields | Go to the Login page | Works as expected | Pass |
| Sign up link | Redirects to the register page | Click on the link | Works as expected | Pass |
| Home button | Redirects to the index page | Click on the button | Works as expected | Pass |
| Forgot password link | Redirects to the forgot password page | Click on the link | Works as expected | Pass |
| Sign in button | Logs the user in | Click on the button | Works as expected | Pass |

**Logout page**

| **Feature** | **Expected outcome** | **Testing performed** | **result** | **Pass/fail** |
| --- | --- | --- | --- | --- |
| Cancel button | Redirects to the index page | Click on the button | Works as expected | Pass |
| Logout button | Logs the user out | Click on the button | Works as expected | Pass |

**Forgotten password page**

| **Feature** | **Expected outcome** | **Testing performed** | **result** | **Pass/fail** |
| --- | --- | --- | --- | --- |
| Forgot password form | Displays the email field | Go to the forgot password | Works as expected | Pass |
| Back to login button | Redirects to the Log in page | Click on the button | Works as expected | Pass |
| Reset password button | Send a reset password email | Click on the button | Works as expected | Pass |

**Error page**

| **Feature** | **Expected outcome** | **Testing performed** | **result** | **Pass/fail** |
| --- | --- | --- | --- | --- |
| Custom error Page | Displays a correct error number | Manually trigger error | Works as expected | Pass |
| Go Home button | Redirects to the index page | Click on the button | Works as expected | Pass |

## Code validation

### HTML

#### Index page

![Product detail](/documentation/media/testing/validator/htmlvalidator-index.png)

#### Signup

![Product detail](/documentation/media/testing/validator/htmlvalidator-signup.png)

#### Login

![Product detail](/documentation/media/testing/validator/htmlvalidator-login.png)

#### Logout

![Product detail](/documentation/media/testing/validator/htmlvalidator-logout.png)

#### Profile

![Product detail](/documentation/media/testing/validator/htmlvalidator-profile.png)

#### Bag

![Product detail](/documentation/media/testing/validator/htmlvalidator-bag.png)

#### Products

![Product detail](/documentation/media/testing/validator/htmlvalidator-products.png)

#### Product detail

![Product detail](/documentation/media/testing/validator/htmlvalidator-productdetail.png)

#### Add products

![Product detail](/documentation/media/testing/validator/htmlvalidator-productsadd.png)

#### Edit products

![Product detail](/documentation/media/testing/validator/htmlvalidator-productsedit.png)

#### Wishlist

![Product detail](/documentation/media/testing/validator/htmlvalidator-wishlist.png)

#### About

![Product detail](/documentation/media/testing/validator/htmlvalidator-about.png)

#### FAQ

![Product detail](/documentation/media/testing/validator/htmlvalidator-faq.png)

### CSS

https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fprimetechfnkd-382d679752d9.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en

### Python

#### Bag - Contexts
![Bag Contexts](/documentation/media/testing/plinter-bagcontexts.png)

#### Bag - Urls
![Bag Urls](/documentation/media/testing/plinter-bagurls.png)

#### Checkout - Admin
![Checkout Admin](/documentation/media/testing/plinter-checkoutadmin.png)

#### Checkout - Apps
![Checkout Apps](/documentation/media/testing/plinter-checkoutapps.png)

#### Checkout - Forms
![Checkout Forms](/documentation/media/testing/plinter-checkoutforms.png)

#### Checkout - Models
![Checkout Models](/documentation/media/testing/plinter-checkoutmodels.png)

#### Checkout - Signals
![Checkout Signals](/documentation/media/testing/plinter-checkoutsignals.png)

#### Checkout - URLs
![Checkout URLs](/documentation/media/testing/plinter-checkouturls.png)

#### Checkout - Views
![Checkout Views](/documentation/media/testing/plinter-checkoutviews.png)

#### Checkout - Webhook Handlers
![Checkout Webhook Handlers](/documentation/media/testing/plinter-checkoutwebhookhandlers.png)

#### Checkout - Webhooks
![Checkout Webhooks](/documentation/media/testing/plinter-checkoutwebhooks.png)

#### FAQ - Models
![FAQ Models](/documentation/media/testing/plinter-faqmodels.png)

#### PrimeTech - Settings
![PrimeTech Settings](/documentation/media/testing/plinter-primetechsettings.png)

#### PrimeTech - URLs
![PrimeTech URLs](/documentation/media/testing/plinter-primetechurls.png)

#### Products - Admin
![Products - Admin](/documentation/media/testing/plinter-productsadmin.png)

#### Products - Forms
![Products - Forms](/documentation/media/testing/plinter-productsforms.png)

#### Products - Models
![Products - Models](/documentation/media/testing/plinter-productsmodels.png)

#### Products - URLs
![Products - URLs](/documentation/media/testing/plinter-productsurls.png)

#### Products - Views
![Products - Views](/documentation/media/testing/plinter-productsviews.png)

#### Profiles - Forms
![Profiles - Forms](/documentation/media/testing/plinter-profilesforms.png)

#### Profiles - Models
![Profiles - Models](/documentation/media/testing/plinter-profilesmodels.png)

#### Profiles - Views
![Profiles - Views](/documentation/media/testing/plinter-profilesviews.png)

### JavaScript

#### Checkout - Stripe elements
![Checkout - Stripe elements](/documentation/media/testing/jshint-stripe_elements.png)

#### Profiles - Countryfield
![Profiles - Countryfield](/documentation/media/testing/jshint-countryfield.png)

#### Lighthouse
![Lighthouse](/documentation/media/testing/lighthouse.png)
