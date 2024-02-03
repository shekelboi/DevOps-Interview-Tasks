ip_list = []

# Read the logs into an array line by line.
with open("logs.txt") as log:
    lines = log.readlines()
    # While reading we split the line by the tabs and get the second part (the IP)
    for line in lines:
        ip_list.append(line.split("\t")[1])


# Create the dotted_quad function
def dotted_quad(ip: str):
    # Remove the "ip-" prefix
    ip = ip[3:]
    parts = []
    # Iterate through with a step of 2, and convert the parts into decimal. Append the parts to a list.
    for i in range(0, len(ip), 2):
        part = ip[i:i + 2]
        parts.append(str(int(part, base=16)))
    # Join the parts by a dot.
    return ".".join(parts)


for ip in ip_list:
    print(dotted_quad(ip))
