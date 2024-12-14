email=input("Please Enter Your Email: ").strip()
username=email[:email.index("@")]
domain_name=email[email.index("@")+1:]
print(f"Yor Username is '{username}' and domain name is '{domain_name}'")