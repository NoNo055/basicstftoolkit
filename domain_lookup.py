import whois

def lookup(domain):
    try:
        info = whois.whois(domain)  # Make sure you're calling the function!
        print("Domain:", info.domain_name)
        print("Registrar:", info.registrar)
        print("Creation Date:", info.creation_date)
        print("Expiration Date:", info.expiration_date)
        print("Name Servers:", info.name_servers)
        print("Emails:", info.emails)
    except Exception as e:
        print("Error:", e)

# Example usage:
user_input = input("Enter domain or IP: ")
lookup(user_input)
