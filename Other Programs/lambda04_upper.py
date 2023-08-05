# to transform all elements of a list to upper case using lambda and map function

company=['dell','hp','logitech','tops','asus','google','accenture','oracle']
uppered_company=list(map(lambda company: company.upper(),company))
print(uppered_company)

title_company=list(map(lambda company: company.title(),company))
print(title_company)


