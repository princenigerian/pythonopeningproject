#################################################################################
#    b3.1.3_TR_combo_menu_solution1.py
#    Example solution
################################################################################

# default variables
total = 0.0
selected_a_sandwich = True
selected_a_beverage = True
selected_french_fries = True

# iteration 1
sandwich = input("Would you like a Turkey, beef, or tofu sandwich? ")
if (sandwich == "Turkey"):
  total += 5.25
elif (sandwich == "beef"):
  total += 6.25
elif (sandwich == "tofu"):
  total += 5.75
else:
  selected_a_sandwich = False

if (selected_a_sandwich):
  print("You selected a", sandwich, "sandwich.")
else:
  print("You did not select a sandwich")
  
# iteration 2
french_fries = input("Would you like fries> (yes or no): ")
if (french_fries == "yes"):
  french_fry_size = input("What size french-fries would you like? ")
  if (french_fry_size == "small"):
    mega_size = input("Would you like to MEGA-Size your fies? (yes or no): ")
    if (mega_size == "yes"):
      french_fry_size = "large"
      total += 1.00
    total += 1.00
  elif (french_fry_size == "medium"):
    total += 1.75
  elif (french_fry_size == "large"):
    total += 2.00
  else:
    print ("Error Code 5904: illegal value for french_fry_size")
    selected_french_fries = False
else:
  selected_french_fries = False
  
# iteration 3
beverage = input("Would you like a beverage? (yes or no): ")
if (beverage == "yes"):
  beverage_size = input("What size beverage would you like? ")
  if (beverage_size == "small"):
    total += 1.00
  elif (beverage_size == "medium"):
    total += 1.75
  elif (beverage_size == "large"):
    total += 2.25
  else:
    print ("Error Code 5904: illegal value for french_fry_size")
    selected_a_beverage = False
else:
  selected_a_beverage = False
  
if (selected_a_beverage and selected_french_fries and selected_a_sandwich):
  total -= 1
  
# iteration 4

num_ketchup_packets = int(input("How many ketchup packets would you like? "))
total += 0.25 * num_ketchup_packets

print("Here is your order:")
if (selected_a_sandwich):
  print("A", sandwich, "sandwich")
if (selected_a_beverage):
  print("A", beverage_size, "beverage")
if selected_french_fries:
  print("A", french_fry_size, "fry")
print("And", num_ketchup_packets, "ketchup packets.")

print("Your total comes to: $", total)
