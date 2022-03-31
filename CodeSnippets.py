# Inputing citation info example
# Should change citation dictionary
# How to change dictionary to hdf5 metadata
from typing import Union, Any


def citationInfo():
	author = input("Last name of first author ")
	date = input("Data of publication ")
	dic1 = author + date
	return dic1

name = citationInfo()
