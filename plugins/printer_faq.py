import difflib

def respond(message):
    faqs = {
        "how to fix paper jam": "Turn off the printer, gently remove the jammed paper, and restart.",
        "how to connect printer to wifi": "Go to printer settings, select Wi-Fi, and follow the on-screen instructions.",
        "printer not printing": "Check cables, re-add the printer, or reinstall drivers.",
        "how to replace ink": "Open the cartridge compartment and replace the old ink with a new cartridge.",
        "printer prints blank pages": "Check ink/toner levels and clean the print head if necessary."
    }
    lowermsg = message.lower().strip()
    questions = list(faqs.keys())
    match = difflib.get_close_matches(lowermsg, questions, n=1, cutoff=0.7)  # stricter matching
    if match:
        matched_question = match[0]
        answer = faqs[matched_question]
        return f"Closest match: '{matched_question}'\nAnswer: {answer}"
    return None
