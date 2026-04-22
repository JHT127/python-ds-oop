
from linked_queue import LinkedQueue

# Customer Service System
customer_queue = LinkedQueue()

def customer_arrives(customer_name):
    customer_queue.enqueue(customer_name)
    print(f"Arriving: {customer_name}")

def serve_customer():
    if not customer_queue.is_empty():
        served_customer = customer_queue.dequeue()
        print(f"Serving: {served_customer}")
    else:
        print("All customers served")

# Simulate customer arrivals and service
customer_arrives("Alice")
customer_arrives("Bob")
customer_arrives("Carol")

serve_customer()
serve_customer()
serve_customer()
serve_customer()  # This will print "All customers served"