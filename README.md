# AVPE -  Materiales Castelar: Warehouse shouldn't receive more than ordered quantity
[Link](https://www.odoo.com/web#id=3364259&cids=3&menu_id=4720&action=4665&active_id=3364224&model=project.task&view_type=form) to task.

There are two ways this task can be completed steps for both the ways are provided.
## Steps to complete the dev (Method 1)
- [X] Create a new Purchase Order and confirm it.
- [X] Check the new receipt created in the inventory section.
- [X] Identify the method called when we press validate button in the receipt section.
- [X] Override the stock.picking.button_validate method
- [X] Find a link between stock_move table and stock_picking table
- [X] Check the condition for each product in the receipt for a particular purchase order
- [X] Raise a User Error if our condition fails
- [X] If condition is passed then call the button_validate method present in the stock_picking to continue with the usual process.

## Steps to complete the dev (Method 2)
- [X] Create a new Purchase Order and confirm it.
- [X] Check the new receipt created in the inventory section.
- [X] Inherit stock.move and add a method with @api.onchange decorator to validate the changes done to stock_move.quantity_done field
- [X] Check the validation condition for each product in the receipt for a particular purchase order
- [X] Raise a User Error if our condition fails


## Issues/Blocking Points
NA

## Topics I need clarification on
NA
      
## Interns who helped me
NA

## Interns I helped
NA
