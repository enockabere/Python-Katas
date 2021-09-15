An e-commerce site tracks the purchases made each day. The product that is purchased the most one day is the featured product for the following day. If there is a tie for the product purchased most frequently, those product names are ordered alphabetically ascending and the last name in the list is chosen.

 

Examples

products = [‘redShirt’, ‘greenPants’, ‘redShirt’, ‘orangeShoes’, ‘blackPants’, ‘blackPants’]
greenPants and orangeShoes were purchased once.
redShirt and blackPants were each purchased 2 times on the given day.
After ordering the products alphabetically ascending, redShirt is the last product listed.
redShirt is the featured product for the following day.
 

products = ['yellowShirt', 'redHat', 'blackShirt', 'bluePants', 'redHat',
           'pinkHat', 'blackShirt', 'yellowShirt', 'greenPants', 'greenPants']
pinkHat and yellowPants were each purchased 1 time.
yellowShirt, blackShirt, redHat, and greenPants were each purchased 2 times.
yellowShirt is the last product listed after ordering the products alphabetically ascending: blackShirt, greenPants, redHat, yellowShirt
yellowShirt is the featured product.
Function Description

Create the function featuredProduct in your preferred text editor or IDE. Paste the function in the text editor below when complete.

 

featuredProduct has the following parameter(s):

    string products[n]:  an array of strings where each represents a purchased product

 

Returns:

    string: the name of the featured product

Your answer:
