from textnode import TextNode, TextType

# TODO need to set up a bunch of tests

# Ah, let me help you with thinking about test cases for the split_nodes_delimiter function!
# While I didn't specifically give you four bullet points before (perhaps you're thinking of another conversation?),
# I'm happy to suggest some test cases you should consider:
#
# Test with a basic example where the delimiter appears once (like your code block example)
# Test with multiple instances of the same delimiter in a single text node
# Test when the delimiter doesn't exist in the text at all
# Test with different delimiters (backticks, asterisks, underscores)
# Test when a node that's not TextType.TEXT is passed in (should remain unchanged)
# Test the error case when there's no matching closing delimiter
# Remember that your function needs to handle different types of delimiters for inline elements like code (`),
# bold (**), and italic (_). The function should properly split TextNodes and assign the appropriate
# TextType to each part.
#
# Would you like me to explain any of these test cases in more detail? Or would you prefer help with the
# implementation of the function itself?

def split_nodes_delimiter(old_nodes, delimiter, text_type):

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
                interim_list = node.text.split(delimiter)
                print("Here is the interim list")
                print(interim_list)

                for n in range(0,len(interim_list)):
                    if n % 2 == 0:
                        return_list.append(TextNode(interim_list[n], TextType.TEXT))
                    else:
                        return_list.append(TextNode(interim_list[n], text_type))

            else:
                raise ValueError("Unmatched delimiter, invalid markdown")
        else:
            print(f"The node {node} is not TEXT so it will be passed through")
            return_list.append(node)
    return return_list

def main():


    node1 = TextNode("This is text with a `code block` word", TextType.TEXT)
    node2 = TextNode("This is a different text node", TextType.BOLD)
    input_list = [node1, node2]
    new_nodes = split_nodes_delimiter(input_list, "`", TextType.CODE)
    print("Here are the new nodes")
    print(new_nodes)

if __name__ == "__main__":
    main()

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
