# Objective simulation
a bank

# Element
Customers arrive over time 
Cashiers serve one customers at a time 
Customers may wait in line 

# Starting Startup 
One Cashiers
Customers arrive every 1-3 minutes (random)
Service time is 2-4 minutes (random)
Simulate 60 minutes

# Rule 
1. When a customer arrives:
  i)  If cashier is free -> service starts immediately
  ii) If busy -> customer joins the queue
2. Cashier serves customers one by one
3. Track:
  queue length
  waiting time 
  idle time 

