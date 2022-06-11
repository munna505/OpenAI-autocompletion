import openai

#use your own OpenAI API key
# openai.api_key = 'YOU_API_KEY'

openai.api_key = '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'



#OpenAI completes your keywords
def grab_completed_text(stext):
        response = openai.Completion.create(
          engine="text-davinci-002",
          prompt=stext,
          temperature=0.7,
          max_tokens=4000,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0
        )
        return response['choices'][0]['text']




# stores queries here
chosen_keywords = []


# opens the people-also-ask.txt file to read the quesitons
file_open_paan = open('people-also-ask.txt', 'r')
chosen_keywords = file_open_paan.read().splitlines()
original_keyword_untrimmed = chosen_keywords[0].split(' ')
original_keyword =  " ".join(original_keyword_untrimmed[1:])
chosen_keywords.pop(0)

#removes previous texts from the file 'openai-completed-descriptions.txt'
open('openai-completed-description.txt', 'w').close()

# completes the introduction query
introduction_query = "Write an article introduction about "  + original_keyword
processed_keyword =  introduction_query + original_keyword
openai_completed_introduction =  grab_completed_text(processed_keyword)
file_open = open("openai-completed-description.txt", 'a')
file_open.write("<b>Introduction</b>\n\n")
file_open.write(f'{openai_completed_introduction}\n\n')
file_open.write("\n\n")

# completes people-also-ask queries
for keyword in chosen_keywords: 
    completed_text = grab_completed_text(keyword)
    file_open = open("openai-completed-description.txt", 'a')
    file_open.write(f'<b>{keyword}</b>\n')
    file_open.write(f'{completed_text}\n\n')
    file_open.write("\n\n")

# completes the conclusion query
conclusion_query = "Write an article conclusion about "  + original_keyword
processed_keyword =  conclusion_query + original_keyword
openai_completed_introduction =  grab_completed_text(processed_keyword)
file_open = open("openai-completed-description.txt", 'a')
file_open.write("<b>Conclusion</b>\n\n")
file_open.write(f'{openai_completed_introduction}\n\n')
file_open.write("\n\n")