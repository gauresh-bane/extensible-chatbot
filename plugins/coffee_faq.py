# Coffee FAQ plugin
# Provides answers to common coffee questions

def get_answer(question):
    faqs = {
        'how to make coffee': 'Add ground coffee to filter, pour hot water, wait 4-5 minutes.',
        'best coffee beans': 'Arabica beans are popular for their smooth flavor.'
    }
    return faqs.get(question.lower(), 'Sorry, I do not have an answer to that question.')
