<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chatbot Interface</title>
    <style>
        body {
            font-family: 'Arial', sans-serif; /* Default font */
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }

        .chat-container {
            width: 100%;
            max-width: 600px;
            margin: 50px auto;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
        }

        .chat-header {
            font-family: 'Georgia', serif; /* Change font for header */
            font-size: 24px;
            font-weight: bold;
            color: #333;
            margin-bottom: 20px;
        }

        .chat-messages {
            font-family: 'Courier New', monospace; /* Change font for chat messages */
            font-size: 16px;
            color: #555;
            max-height: 300px;
            overflow-y: auto;
            margin-bottom: 20px;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }

        .chat-input {
            width: 100%;
            font-family: 'Verdana', sans-serif; /* Change font for input */
            font-size: 16px;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }

        .chat-button {
            margin-top: 10px;
            width: 100%;
            font-family: 'Tahoma', sans-serif; /* Change font for button */
            font-size: 16px;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        .chat-button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="chat-header">
            Medicore Chatbot
        </div>
        <div class="chat-messages">
            <p>User: Hi!</p>
            <p>Medicore: Hello! How can I assist you today?</p>
        </div>
        <input type="text" class="chat-input" placeholder="Type a message...">
        <button class="chat-button">Send</button>
    </div>
</body>
</html>
