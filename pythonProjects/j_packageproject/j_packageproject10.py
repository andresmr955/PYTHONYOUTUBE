##PACKAGES 
## Package is a container for multiple modules, in file system terms a package is  a directory or folder.
## We can have modiles for sales, shipping, customer service
##__init__.py when Python interpreter sees a file with this name and name in a directory, it threats this directory as a package  


#This is verbose
##import ecommerce.shipping
#ecommerce.shipping.calc_shipping()

##We can use the second approche, You can import multiple functions like this 
#from ecommerce.shipping import calc_shipping, cal_tax

#calc_shipping()
#cal_tax()

## To import the entire module from a a package

from ecommerce import shipping, caltax

shipping.calc_shipping()
caltax.cal_tax()
##WE USE DJANGO FOR BUILDING WEB APPLICATIONS WITH PYTHON
