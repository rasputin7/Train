def citationInfo():
	author = input("Last name of first author ")
	date = input("Date of publication ")
	return(author + date)

name = citationInfo()
print(name)
