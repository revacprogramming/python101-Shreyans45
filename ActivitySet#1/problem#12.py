fname = input("Enter file name")
fh = open(fname)
counts = dict()
lst = []
for line in fh:
    if not line.startswith("From "):
        continue
    line = line.rstrip().split()
    emails = line[1]
    lst.append(emails)
for email in lst:
    counts[email] = counts.get(email, 0) +1
print(emails, counts[email])
