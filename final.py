import openai

#use your own OpenAI API key
openai.api_key = 'YOU_API_KEY'


#add query to the original string
def process_keyword(mykeyword):
    # use query of your choice
    query = ''
    final_query = mykeyword +  query 
    return str(final_query)

#OpenAI completes your keywords
def grab_completed_text(stext):
        response = openai.Completion.create(
          engine="text-davinci-002",
          prompt=stext,
          temperature=0.7,
          max_tokens=200,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0
        )
        return response['choices'][0]['text']





chosen_keywords = []


file_open_paan = open('people-also-ask.txt', 'r')
chosen_keywords = file_open_paan.read().splitlines()
original_keyword_untrimmed = chosen_keywords[0].split(' ')
original_keyword =  original_keyword_untrimmed[1]
introduction = 'Introduction about ' + original_keyword
conclusion = 'Conclusion about ' + original_keyword
chosen_keywords.pop(0)
chosen_keywords.insert(0, introduction)
chosen_keywords.append(conclusion)

for keyword in chosen_keywords: 
    processed_keyword = process_keyword(keyword)
    completed_text = grab_completed_text(processed_keyword)
    file_open = open("openai-completed-description.txt", 'a')
    file_open.write(f'<b>{processed_keyword}</b>\n\n')

    file_open.write(completed_text)
    file_open.write("\n\n")
