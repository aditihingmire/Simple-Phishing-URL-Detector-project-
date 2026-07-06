url = input("Enter URL: ")

# Suspicious words
suspicious = ["login", "verify", "secure", "update", "bank", "@", "-", ".xyz"]

found = False

for word in suspicious:
    if word in url.lower():
        found = True
        break

if found:
    print(" Suspicious URL")
else:
    print(" Safe URL")