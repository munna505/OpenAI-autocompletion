import openai

#use your own OpenAI API key
openai.api_key = 'YOU_API_KEY'



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




# stores queries here
chosen_keywords = []


# opens the people-also-ask.txt file to read the quesitons
file_open_paan = open('people-also-ask.txt', 'r')
chosen_keywords = file_open_paan.read().splitlines()
original_keyword_untrimmed = chosen_keywords[0].split(' ')
original_keyword =  original_keyword_untrimmed[1]
introduction = 'Introduction about ' + original_keyword
conclusion = 'Conclusion about ' + original_keyword
chosen_keywords.pop(0)

# completes the introduction query
introduction_query = input("Input your query for the introduction. For example, write an article introduction about bicycles.\n::- ")
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
conclusion_query = input("Input your query for the introduction. For example, write a conclusion  about bicycles.\n::- ")
processed_keyword =  conclusion_query + original_keyword
openai_completed_introduction =  grab_completed_text(processed_keyword)
file_open = open("openai-completed-description.txt", 'a')
file_open.write("<b>Conclusion</b>\n\n")
file_open.write(f'{openai_completed_introduction}\n\n')
file_open.write("\n\n")