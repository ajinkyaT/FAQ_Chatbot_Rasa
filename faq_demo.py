import pandas as pd
from fuzzywuzzy import fuzz # visit https://github.com/seatgeek/fuzzywuzzy for more details
from fuzzywuzzy import process

faq_data = pd.read_csv("./data/faq_data.csv")

query = "how to commit"

questions = faq_data['question'].values.tolist()

mathed_question, score = process.extractOne(query, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches

if score > 50: # arbitrarily chosen 50 to exclude matches not relevant to the query
    matched_row = faq_data.loc[faq_data['question'] == mathed_question,]
    
    document = matched_row['link'].values[0]
    page = matched_row['page'].values[0]
    match = matched_row['question'].values[0]
    answer = matched_row['answers'].values[0]
    
    
    print("Here's something I found, \n\n Link: {} \n Page number: {} \n Question: {} \n Answer: {} \n".format(document, page, match, answer))
    
else: print("Sorry I didn't find anything relevant to your query!")