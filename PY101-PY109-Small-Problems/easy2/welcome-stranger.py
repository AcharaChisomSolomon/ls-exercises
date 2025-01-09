def greetings(names, description):
    name_str = " ".join(names)
    title = description['title']
    occupation = description['occupation']
    return f"Hello, {name_str}! Nice to have a {title} {occupation} around."

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.