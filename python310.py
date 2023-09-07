# Sample convo object
convo = [
    {'role': 'system', 'message': 'you are a helpful AI assistant'}
]

# Function to limit the convo length to 20 items while keeping the first "system" message
def limitConvoLength(convo):
    # Initialize a list to hold the new convo
    newConvo = []

    # Initialize a count to keep track of "user" and "assistant" items
    userAssistantCount = 0

    # Iterate through the convo
    for message in convo:
        # Add the "system" message directly
        if message["role"] == "system":
            newConvo.append(message)
        # For "user" and "assistant" messages
        elif message["role"] in ["user", "assistant"]:
            # Check if the count is less than 2 (max 2 "user" and "assistant" messages)
            if userAssistantCount < 2:
                newConvo.append(message)
                userAssistantCount += 1
        else:
            # For other roles, add them directly
            newConvo.append(message)

        # If the length of newConvo exceeds 20, break out of the loop
        if len(newConvo) >= 20:
            break

    return newConvo

# Replace the entrypoint function according to your cloud function platform here
def your_cloud_function_entrypoint(event, context):
    # Call the function to limit the convo length
    limitedConvo = limitConvoLength(convo)

    # Print the limited convo (or handle it as needed for your cloud function)
    for message in limitedConvo:
        print(message)
