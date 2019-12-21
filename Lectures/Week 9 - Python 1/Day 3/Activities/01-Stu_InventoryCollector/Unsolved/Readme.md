## Inventory Collector

In this activity, you will create an application that allows its users to create and fill in a store's inventory. It will also print out the inventory to the terminal. 

Use the script file provided and specifically look to the comments to help you code your solution. Some of the code has already been provided as well. 

### Instructions:

 * Create an empty dictionary and call it `inventory`.
    
    * Ask the user how many items they have in their inventory and store it in a variable called `item_count`.
    
    * You will need to create a `for` loop and use `range` to loop over the item count.
    
      * For each item, ask the user what the item is and what the price is.
      
      * Store the item name as a variable called `item_name` and store the item price in a variable called `item_price`.    
          * **Note:** Item prices need to be entered in as integers and not strings.
      
      * Create a dictionary that has for its key/value pairs, the item name and the item price.
      
    * Print the key/value pairs to the console. For each item that is less than five dollars, also indicate that the item is on sale.
    
        * You will need to loop through all the items in the dictionary and print their keys/values to the console.
        
      * Inside of this loop, you will also need to create a conditional that checks the price.
      
  * **Hint:** The file we provided to you guides you step-by-step through the code you will have to create, and some of the above code has already been included.
