# Melbourne Eletronics Store dataset

**This dataset is publicly available [on Kaggle](datasets/muhammadshahrayar/transactional-retail-dataset-of-electronics-store).**

For more information about the dataset, please refer to [Project Plan](project_plan.md) documentation markdown page.

----
## **Data Dictionary**

- `order_id`: A unique id for each order
- `customer_id`: A unique id for each customer
- `date`: The date the order was made, given in YYYY-MM-DD format
- `nearest_warehouse`: A string denoting the name of the nearest warehouse to the customer
- `shopping_cart`: A list of tuples representing the order items: the first element of the tuple is the item ordered, and the second element is the quantity ordered for such item.
- `order_price`: A float denoting the order price in USD. The order price is the price of items before any discounts and/or delivery charges are applied.
- `delivery_charges`: A float representing the delivery charges of the order
- `customer_lat`: Latitude of the customer’s location
- `customer_long`: Longitude of the customer’s location
- `coupondiscount`: An integer denoting the percentage discount to be applied to the orderprice.
- `order_total`: A float denoting the total of the order in USD after all discounts and/or delivery charges are applied.
- `season`: A string denoting the season in which the order was placed.
- `isexpediteddelivery`: A boolean denoting whether the customer has requested an expedited delivery
- `distancetonearest_warehouse`: A float representing the arc distance, in kilometres, between the customer and the nearest warehouse to him/her.
- `latestcustomerreview`: A string representing the latest customer review on his/her most recent order
- `ishappycustomer`: A boolean denoting whether the customer is a happy customer or had an issue with his/her last order.
