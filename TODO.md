
# Top prioritiy

1. Build new item screen, test DB write


# Database Updates


1. Modify item import logic:
   - If imported `icon-path` exists → use it
   - If it does not exist → set `icon_path = NULL` (safe fallback)


# New Inventory Item Screen

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

1. Add EDIT button with proper enable/disable logic
2. Add New Item button that opens the new item screen
3. Ensure selected item's details panel is updating using the new weight + icon system

# Inventory Interaction

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