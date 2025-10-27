Here's the recommended updated README.md content you should use. This will keep all the old structure but add clarity and detail for the new features:

-----

# Extensible Chatbot

A modular and extensible Python chatbot project featuring:
- Plugin architecture for new FAQ domains and features
- **Advanced fuzzy matching (difflib or fuzzywuzzy)**
- **REST API with authentication** (`app.py` using Flask)
- **Logging of all activity** (`chatbot.log`)
- Easily extendable via Python plugins

## Features

- **Plugin-based Architecture:** Add new FAQ or feature plugins in the `plugins/` directory.
- **Advanced Fuzzy Matching:** Uses fuzzy string matching (difflib, fuzzywuzzy optional for stronger results) in FAQ plugins.
- **Multiple FAQ Domains:** Includes `coffee_faq.py` and new `printer_faq.py` plugin examples.
- **Production-ready:** Dockerfile included. Can run as a CLI or REST API server.
- **REST API:** Start `app.py` with Flask for HTTP access to the bot (`/chat` endpoint).
- **Authentication:** Simple API key for API access. Set `CHATBOT_API_KEY` in environment.
- **Logging:** All queries, responses, and security warnings are logged to `chatbot.log`.
- **Easy to Extend:** Drop new `.py` files in `plugins/`, see `printer_faq.py` as example.

## Usage

- **CLI:** Run `python chatbot.py` to interact in terminal.
- **API:** Run `python app.py` to serve chatbot on `/chat`.

**Sample REST call:**
```bash
curl -X POST http://localhost:5000/chat \
  -H "Authorization: Bearer test-api-key" \
  -H "Content-Type: application/json" \
  -d '{"message": "how to fix paper jam"}'
```

## Plugins (FAQ Domains)
- **plugins/coffee_faq.py:** Answers on coffee machines
- **plugins/printer_faq.py:** Answers on printers

## Installation & Setup
- Make sure Python 3.x is installed
- (Optional) Install fuzzywuzzy for best fuzzy matching: `pip install fuzzywuzzy python-Levenshtein`
- Add new plugins with a `respond(message)` function
- REST API requires Flask: `pip install flask`

## Authentication
- Set `CHATBOT_API_KEY` in your environment (default is `test-api-key`)
- All API calls must send header `Authorization: Bearer <YOUR_API_KEY>`

## Logging
- All chats and warnings are saved in `chatbot.log`

## Extending
- Copy or modify plugin scripts in `/plugins` for new FAQ topics

## Example Plugin (printer_faq.py)
```python
import difflib

def respond(message):
    faqs = {
        "how to fix paper jam": "Turn off the printer, gently remove the jammed paper, and restart.",
        "how to connect printer to wifi": "Go to printer settings, select Wi-Fi, and follow on-screen instructions.",
        # ... additional printer FAQ entries
    }
    match = difflib.get_close_matches(message.lower(), faqs.keys(), n=1, cutoff=0.7)
    if match:
        question = match[0]
        return f"Closest match: '{question}'\nAnswer: {faqs[question]}"
```

## License
MIT License
