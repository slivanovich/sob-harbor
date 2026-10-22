Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Rohinton Mistry: Rohinton Mistry {'1': ", '2': ", '3': ", '4': "} (born 3 July 1952) is an Indian-born Canadian writer.  He was awarded the Neustadt International Prize for Literature in 2012.

Tales from Firozsha Baag: Tales From Firozsha Baag is a collection of 11 short stories by Rohinton Mistry about the residents of Firozsha Baag, a Parsi-dominated apartment complex in Mumbai (formerly Bombay).  Mistry's first book, it was published by Penguin Canada in 1987.  Although all the stories deal with the same location, many were written without the aim of being collected in the same volume.

Such a Long Journey (film): Such a Long Journey is a 1998 Indo-Canadian english language film based on the novel of the same name written by Rohinton Mistry.  The film is directed by Sturla Gunnarsson with a screenplay by Sooni Taraporevala.  The film received twelve Genie Awards nominations including the Best Picture, Best Director, and Best Actor.  The film was screened at the Toronto International Film Festival.

A Fine Balance: A Fine Balance is the second novel by Rohinton Mistry.  Set in "an unidentified city" in India, initially in 1975 and later in 1984 during the turmoil of The Emergency.  The book concerns four characters from varied backgrounds – Dina Dalal, Ishvar Darji, his nephew Omprakash Darji and the young student Maneck Kohlah – who come together and develop a bond.

Gillian Bradshaw: Gillian Marucha Bradshaw (born May 14, 1956) is an American writer of historical fiction, historical fantasy, children's literature, science fiction, and contemporary science-based novels, who currently lives in Britain.  Her serious historical novels are often set in classical antiquity — Ancient Egypt, Ancient Greece, the Byzantine Empire, Saka and the Greco-Bactrian Kingdom, Imperial Rome, Sub-Roman Britain and Roman Britain.  She has also written two novels set in the English Civil War.

Indian English literature: Indian English Literature (IEL) refers to the body of work by writers in India who write in the English language and whose native or co-native language could be one of the numerous languages of India.  Its early history began with the works of Michael Madhusudan Dutt followed by R. K. Narayan, Mulk Raj Anand and Raja Rao who contributed to Indian fiction in the 1930s.  It is also associated with the works of members of the Indian diaspora, such as V. S. Naipaul, Kiran Desai, Jhumpa Lahiri, Kovid Gupta, Agha Shahid Ali, Rohinton Mistry and Salman Rushdie, who are of Indian descent.

Family Matters (novel): Family Matters is the third novel by Indian-born author Rohinton Mistry.  It was first published by McClelland and Stewart in 2002.

Cyrus Mistry (writer): Cyrus Mistry was born in march 11,1956 is an Indian author and playwright.  He won the 2014 DSC Prize for South Asian Literature for "Chronicle of a Corpse Bearer".  He is the brother of author Rohinton Mistry.

Chor Bazaar: Chor Bazaar, located near Bhendi Bazaar in South Mumbai, is one of the largest flea markets in India.  The area is one of the tourist attractions of Mumbai.  The word "chor" means "thief" in Marathi and Hindi.  The market is thought to have originally been called "Shor Bazaar", meaning "noisy market".  The current name is said to have come from a British mispronunciation.  Eventually however, stolen goods started finding their way into the market, resulting in it living up to its new name.  According to popular legend, if you lose anything in Mumbai you can buy it back from the "Chor Bazaar".  The market has been mentioned in popular novels, including Rohinton Mistry's Such a Long Journey, where it is described as "not a nice place".

Such a Long Journey (novel): Such a Long Journey is a 1991 novel by Rohinton Mistry.  It was shortlisted for the Booker Prize and won several other awards.  In 2010 the book made headlines when it was withdrawn from the University of Mumbai's English syllabus after complaints from the family of the Hindu nationalist politician Bal Thackeray.

Question: Who was born first, Gillian Bradshaw or Rohinton Mistry?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_one": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first person being compared."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the first person."
        },
        "birth_month": {
          "type": "string",
          "description": "The birth month of the first person."
        },
        "birth_day": {
          "type": "integer",
          "description": "The birth day of the first person."
        }
      },
      "required": [
        "name",
        "birth_year",
        "birth_month",
        "birth_day"
      ],
      "additionalProperties": false
    },
    "person_two": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second person being compared."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the second person."
        },
        "birth_month": {
          "type": "string",
          "description": "The birth month of the second person."
        },
        "birth_day": {
          "type": "integer",
          "description": "The birth day of the second person."
        }
      },
      "required": [
        "name",
        "birth_year",
        "birth_month",
        "birth_day"
      ],
      "additionalProperties": false
    },
    "comparison_result": {
      "type": "object",
      "properties": {
        "earlier_birth_person_name": {
          "type": "string",
          "description": "The name of the person who was born first."
        },
        "earlier_birth_year": {
          "type": "integer",
          "description": "The birth year of the person who was born first."
        }
      },
      "required": [
        "earlier_birth_person_name",
        "earlier_birth_year"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The name of the person who was born first."
    }
  },
  "required": [
    "person_one",
    "person_two",
    "comparison_result",
    "final_answer"
  ],
  "additionalProperties": false
}
