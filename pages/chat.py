"""
The Chat Page:
Here, users will be able to interact with ELIZA. The page should simulate a conversation using pattern matching and substitutions.
"""
respons = [{'buy':["What do you look for the most when you decide to buy a new car?","What are your top priorities when you`re looking to buy a new car?"]},
            {'feature':['What kind of features do you have in your main?',"Is there a specific feature would you like to have?"]},
            {'yes':['Why do you think so?','can you elaborate?']},
            {'no':['Why do you think so?','can you elaborate?']},
            {'accessibility' : ["Are you looking for a car with specific accessibility features, such as wheelchair access or adaptive controls?"]},
            {'reliability':['Are you specifically looking for a car with high reliability and low maintenance?']},
            {'maintenance':["Are you interested in cars with technology that helps track maintenance needs?","Are you looking for a car that`s easy to maintain"]}
            ]

def user_input_analysis():
    '''this function suppoes to prepare the input for the generation of eliza response'''
    pass

def response_generation():
    '''
    this function will use the response list and the user analyized input
    return eliza response
    '''