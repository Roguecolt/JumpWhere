sampledict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}


key_to_remove = input("Enter key to remove")


if key_to_remove in sampledict:
    del sampledict[key_to_remove]
    print(f"Key '{key_to_remove}' removed successfully.")
else:
    print(f"Key '{key_to_remove}' not found in the dictionary.")


print("Updated dictionary:", sampledict)
