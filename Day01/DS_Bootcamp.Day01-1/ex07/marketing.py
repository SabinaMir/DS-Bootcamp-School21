import sys

def get_call_center_list(clients, recipients):
    #Get a list of clients who have not viewed the promotional email.
    return list(set(clients)-set(recipients))

def get_potential_clients_list(clients, participants):
    #Get a list of participants who are not clients.
    return list(set(participants)-set(clients))

def get_loyalty_program_list(clients, participants):
    return list(set(clients)-set(participants))

def main(task):   

    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
    'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
    'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    if task == "call_center":
        result = get_call_center_list(clients, recipients)
        print(result)
    elif task ==  "potential_clients": 
        result = get_potential_clients_list(clients, participants)
        print(result)
    elif  task ==  "loyalty_program":  
        result =  get_loyalty_program_list(clients, participants)
        print(result)
    else:    
        raise ValueError("Invalid task name. Use 'call_center', 'potential_clients', or 'loyalty_program'.")

if __name__ == "__main__":
    if len(sys.argv)!=2:
        print("Usage: python script.py <task_name>")    
    task_name = sys.argv[1]
    try:
        main(task_name)
    except ValueError as e:
        print(e)
        sys.exit(1)       