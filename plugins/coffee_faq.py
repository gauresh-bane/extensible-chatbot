try:
    from fuzzywuzzy import process
    FUZZY_LIB = 'fuzzywuzzy'
except ImportError:
    import difflib
    FUZZY_LIB = 'difflib'

def respond(message):
    faqs = {
        "how to clean the coffee machine": "To clean the coffee machine, run a cleaning cycle with water and vinegar, then rinse thoroughly.",
        "how to descale the coffee machine": "Use a descaling solution and follow the manufacturer's instructions for your model.",
        "why is my coffee machine leaking": "Check the water reservoir and seals. Make sure all parts are properly assembled.",
        "how to fix coffee machine not brewing": "Ensure the water tank is filled, filter is clean, and the machine is plugged in.",
        "what coffee beans to use": "You can use any beans, but medium roast is recommended for most machines."
    }
    lowermsg = message.lower().strip()
    questions = list(faqs.keys())
    if FUZZY_LIB == 'fuzzywuzzy':
        match, score = process.extractOne(lowermsg, questions)
        if score >= 75:
            answer = faqs[match]
            return f"Closest match: '{match}'\nAnswer: {answer}"
    else:
        match = difflib.get_close_matches(lowermsg, questions, n=1, cutoff=0.6)
        if match:
            answer = faqs[match[0]]
            return f"Closest match: '{match[0]}'\nAnswer: {answer}"
    return None
