

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
