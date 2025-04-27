from htmlnode import HTMLNode

test_dict = {
        "href": "https://www.google.com",
        "target": "_blank"
        }

return_string = ""

for key, value in test_dict.items():
    print(key, value)
    formatted_string = f' {key}="{value}"'
    return_string += formatted_string

print(return_string)
