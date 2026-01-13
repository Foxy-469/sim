# Simulation Documentation: Single-Cashier Queue System

## 1. Purpose
The simulation models a **bank queue with a single cashier**. It helps analyze:
- Waiting times for customers
- Cashier idle time
- How random arrival and service times affect queue length

## 2. Simulation Model
- **Time:** Simulated in discrete minutes (0–60).
- **Entities:** Customers arriving randomly and a single cashier serving them.
- **Queue:** First-in-first-out (FIFO) system.

### Parameters
- **Customer Arrival:** Random between 1–3 minutes.
- **Service Time:** Random between 2–4 minutes.
- **Simulation Duration:** 60 minutes.

## 3. Variables
| Variable | Description |
|----------|-------------|
| `t`      | Virtual simulation time in minutes |
| `c_state`| Cashier state (0 = idle, 1 = busy) |
| `c_id`   | Unique customer identifier |
| `c_time` | Next customer arrival time |
| `s_time` | Next service completion time |
| `i_time` | Total idle time of cashier |
| `q`      | Queue object storing customer IDs and waiting times |

## 4. Simulation Logic
1. **Initialization:**
   - Set cashier idle (`c_state = 0`)
   - Set time `t = 0`
   - Schedule first customer arrival

2. **Each minute:**
   - Check if a **customer arrives** (`t == c_time`).
     - If cashier idle → start service immediately.
     - Else → add to queue.
     - Schedule next customer arrival.
   - Check if **service completes** (`t == s_time`).
     - Remove customer from queue.
     - Start service for next customer in queue if any.
   - Update **idle time** if cashier is free.

3. **Repeat** until simulation ends (`t = 60`).

## 5. Output
- **Customer waiting times:** `{customer_id: waiting_time}`
- **Cashier idle time:** total minutes idle
- **Average waiting time:** `sum(waiting_times)/number_of_customers`

## 6. Assumptions
1. Service times and arrivals are independent random variables.
2. Only one cashier is available.
3. Queue has unlimited length (no customer is turned away).
4. Time is discrete (1-minute intervals).

## 7. Observations
- Early-arriving customers may experience **no waiting**.
- When multiple customers arrive in quick succession, the **queue grows**, and waiting times increase.
- Idle time occurs when **no customers are in the system**.
- Randomness leads to **variable waiting times and idle periods** each simulation run.

## 8. Possible Extensions
1. **Multiple cashiers** → reduce queue lengths.
2. **Limited queue size** → model rejected customers.
3. **Priority customers** → urgent service first.
4. **Variable simulation duration** → longer-term analysis.
