from textnode import TextNode, TextType
from htmlnode import HTMLNode

# It takes a list of "old nodes", a delimiter, and a text type.
# It should return a new list of nodes, where any "text" type nodes in the input list
# are (potentially) split into multiple nodes based on the syntax.
#
# For example, given the following input:
#
# node = TextNode("This is text with a `code block` word", TextType.TEXT)
# new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
#
# [
#     TextNode("This is text with a ", TextType.TEXT),
#     TextNode("code block", TextType.CODE),
#     TextNode(" word", TextType.TEXT),
# ]

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # old nodes is a list of TEXTNode objects
    # delimiter is the string being searched for - in the example `
    # text_type is the TextType to assign to the content between delimiters

    # Function should look at each node in the input list
    # If it is not TextType.TEXT then pass it through to the return list as it is
    # If it is TextType.TEXT then search for matched pairs of the delimiter
    # When you find a matched pair then split that node into multiple nodes
    # Text before delimiter stays as TextType.TEXT
    # Text between the delimiters becomes the specified TextType (code in our example)
    # # Text after the delimiter stays as TextType.TEXT

    return_list = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            print(f"Here is the node, Text Node is TEXT {node}")
            print("processing ....")
            num_delimiters = node.text.count(delimiter)
            print(f"I have found {num_delimiters} occurrences of the delimiter {delimiter}")
            if num_delimiters % 2 == 0:
                print("An even number of delimiters has been found")
                # calculate number of pairs
                num_pairs = num_delimiters // 2
                print(f"There are {num_pairs} pairs")
                interim_list = node.text.split("`")
                print("Here is the interim list")
                print(interim_list)

                for n in range(0,len(interim_list)-1,3):
                    return_list.append(TextNode(f'"{interim_list[n]}"', TextType.TEXT))
                    return_list.append(TextNode(f'"{interim_list[n+1]}"', TextType.CODE))
                    return_list.append(TextNode(f'"{interim_list[n+2]}"', TextType.TEXT))

            else:
                return_list.append(node)
        else:
            print(f"The node {node} is not TEXT so it will be passed through")
            return_list.append(node)
    return return_list



def main():
    # list_of_nodes = [
    #     TextNode("oh how plain this is", TextType.TEXT),
    #     TextNode("same text", TextType.BOLD),
    #     TextNode("same text", TextType.ITALIC),
    #     TextNode("same text", TextType.CODE),
    #     TextNode("This is some link anchor text", TextType.LINK, "google.com"),
    #     TextNode("This is some image anchor text", TextType.IMAGE, "google.com")
    # ]
    #
    # for each_node in list_of_nodes:
    #     processed_node = text_node_to_html_node(each_node)

    node1 = TextNode("This is text with a `code block` word", TextType.TEXT)
    node2 = TextNode("This is a different text node", TextType.BOLD)
    input_list = [node1]
    new_nodes = split_nodes_delimiter(input_list, "`", TextType.CODE)
    print("Here are the new nodes")
    print(new_nodes)

if __name__ == "__main__":
    main()
