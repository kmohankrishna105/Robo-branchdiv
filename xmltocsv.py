from xml.etree import ElementTree
import csv
import xml.sax

tree = ElementTree.parse('order_new1.xml')
root = tree.findall('order')

for t in root:
	order_num=t.attrib['order-no']
	created=t.find('created-by').text
	org_order=t.find('original-order-no').text
	curr=t.find('currency').text
	cust_local=t.find('customer-locale').text
	tax=t.find('taxation').text
	invoice=t.find('invoice-no').text
	print(order_num,created,org_order,curr,tax,invoice)

	for product in t.find('product-lineitems'):
		net_price=product.find('net-price').text
		tax = product.find('tax').text
		gross_price = product.find('gross-price').text
		base_price = product.find('base-price').text

		position=product.find('position').text
		print(product)
		item = product.find('tax').text
		id=product.find('product-id').text
		product_name=product.find('product-name').text
		unitcount=product.find('quantity').attrib['unit']
		print(net_price,item,id,product_name,unitcount)

	for customer in t.find('customer'):
		print(customer)
		cust=t[7][1].text
		print(cust)
		#customer_name=customer.find('customer-name')
		#print(customer_name)
		customer_email = customer.find('customer-email').text
		for baddress in customer.find('billing-address'):
			first_name = baddress.find('first-name').text
			last_name = baddress.find('last-name').text
			address1 = baddress.find('address1').text
			city=baddress.find('city').text




		with open('share.csv', 'a+') as csvfile:
			filewriter = csv.writer(csvfile, delimiter=',',quotechar='|')
			filewriter.writerow([order_num,created,curr,cust_local,tax,invoice,net_price,tax,gross_price,base_price,position,item,id,product_name,unitcount])
			#order_num,created,curr,cust_local,tax,invoice,net_price,tax,gross_price,base_price,position,item,id,product_name,unitcount