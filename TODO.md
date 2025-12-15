
# Top prioritiy

1. Build new item screen, test DB write


# Database Updates


1. Modify item import logic:
   - If imported `icon-path` exists → use it
   - If it does not exist → set `icon_path = NULL` (safe fallback)


# Add/Modify Inventory Item Screen

This page is specifically for adding items to the inventory that currently do not exist in the inventory. Outstanding items on the page are as follows:

  
1. Need to add an icon viewing for the item itself
2. Fix the CSS on the stat viewing, maybe we should make some sort of list
3. Users should be able to "edit" the selected item
4. Users can "select" how many of the said item they want to add
5. Press "add button"
   1. This should add some transactions to the database
   2. How can we reflect these changes? Is there anyway to reselect the item after we do the "push" to the DB? Refreshing the page? Not sure how this would work.
6. Create a "remove item from DB"
   1. This will remove the item from the entire database and would impact other characters
   2. There should be a check on the other characters
   3. Ensure we delete from the actual inventory - check the PRAGMA command and cascading rules in the DB


# New Inventory Item Screen

This page is specifically for adding items to the database that do not exist. This should exist over the add/modify inventory item screen, I'm thinking about a pop-up similar to the inventory thing that we have.

1. Create page
2. Screen must include:
  - Name
  - Icon selection panel
  - Category/tag dropdown
  - Stats input section
  - Weight input
3. Ensure UI validates: name, weight, category
4. On save → insert into DB with string `icon_path`

# Edit Inventory Item Screen

This page is going to be similar to the new inventory item screen, but is going to be a slightly different module. The "Edit" is going to popover the current screen but as a slide in and nothing really aggressive. You can overwrite the item or "create a new item" -- you will have to change the name though. The actual data doesn't get edited though.

If the overwrite button is pressed, then you have to ensure the item name changes. If you press "overwrite item" it will update the CK of the item.

These items are *shared between characters*...maybe this isn't something we want to do but I'd imagine items are something you'd want to be able to share between characters and campaigns. 

1. Create a second full-screen page similar to the `New Inventory Item Screen`
2. Pre-populate all fields
  - name
  - icon_path
  - stats
  - category
  - weight
3. Save updates back to DB
4. Add an EDIT button on the main inventory page:
  - Disabled if no item is selected
  - Opens this screen

# Main Inventory Page

This is the primary page for the application.

1. Add EDIT button with proper enable/disable logic
2. Add New Item button that opens the new item screen
3. Ensure selected item's details panel is updating using the new weight + icon system

# Inventory Interaction

This is just side stuff.

1. Add/Remove quantity buttons in details panel
2. Decide behavior when quantity hits zero
  - Delete item from DB?
3. Add "Drop All" button to set the quantity of the item to zero
  - Requires modal confirmation

# Categorization System

1. Define fixed category list (non-custom)
2. Add category field to item table
3. Add category tabs to the inventory UI

# Stats system

1. Ensure item stats table exists and references items properly with the proper PK and FK relationship
2. Support stats input in both create/edit screens
3. Link stats visually to the item detail panel

# Future, not Urgent

1. Character screen (lightweight for now until v1 is deployed)
  - Name + Max Weight
  - Weight calculation summarizing carried load
2. Potential weight summary box added below the details section
3. Export items
4. Export characters