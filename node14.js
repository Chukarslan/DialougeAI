const convo = [
    {'role': 'system', 'message': 'you are a helpful AI assistant'}
];

// Function to limit the convo length to 20 items while keeping the first "system" message
function limitConvoLength(convo) {
    // Initialize a list to hold the new convo
    const newConvo = [];

    // Initialize a count to keep track of "user" and "assistant" items
    let userAssistantCount = 0;

    // Iterate through the convo
    for (const message of convo) {
        // Add the "system" message directly
        if (message.role === "system") {
            newConvo.push(message);
        }
        // For "user" and "assistant" messages
        else if (["user", "assistant"].includes(message.role)) {
            // Check if the count is less than 2 (max 2 "user" and "assistant" messages)
            if (userAssistantCount < 2) {
                newConvo.push(message);
                userAssistantCount += 1;
            }
        } else {
            // For other roles, add them directly
            newConvo.push(message);
        }

        // If the length of newConvo exceeds 20, break out of the loop
        if (newConvo.length >= 20) {
            break;
        }
    }

    return newConvo;
}

// Call the function to limit the convo length
const limitedConvo = limitConvoLength(convo);

// Print the limited convo
for (const message of limitedConvo) {
    console.log(message);
}
