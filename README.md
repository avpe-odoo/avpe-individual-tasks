# AVPE -  LinkSource Pricing Update
[Link](https://www.odoo.com/web#id=3364280&cids=3&menu_id=4720&action=4665&active_id=3364224&model=project.task&view_type=form) to task.


## Steps to complete the dev (Method 1)
- [X] Create a new Sales Order.
- [X] Notice the behaviour of the Unit Price field when you cahnge the quantity field
- [X] Identfy the function in the sale.order.line which is responsible for calculating the the unit price
- [X] Override the fucntion
- [X] Create a new view by inheriting sale.view_order_form and add a button for each sale order line generated
- [X] Add a function that will be triggred when our recompute button is clicked in the model file
- [X] Test the functionality by repeating the steps mentioned in the task


## Issues/Blocking Points
NA

## Topics I need clarification on
NA
      
## Interns who helped me
NA

## Interns I helped
NA