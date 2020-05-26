## Question: design a vending machine

1. ask questions:

a vending machine can accept cash, dispense items, the design and code to be extensible

Requirements:
        1. vending machine can keep track of the inventory
        2. a person should be able to inert cash into the machine and choose and  choose an item
        3. confirm the inserted cash with the price of the selected item
        4. the machine must display an error in case of the insufficient cash or unavailable item
        5. all the above steps succeed then the user gets the selected item

Design:
two actors:
    machine: take the action
    user: issue command 

States:
- ready  : machine is ready for the 
- cash collected: the user can select item or cancel the transaction
- dispense the change : give back the the change to the user
- dispense the item: dispense the item upon successful validation of entered cash and the price of the selected invevtory 
- transacion canceled: if the user cancels the transaction, return the cash 

```commandline

```