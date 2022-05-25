text = "X-DSPAM-Confidence:    0.8475"
s=text.find(":")
q=text[s+1:].lstrip()
p=float(q)
print(p)
