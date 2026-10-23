{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPatricia Moody: Patricia Moody (born 13 November 1934) is a British sprint canoer who competed in the late 1950s.  She finished seventh in the K-1 500 m event at the 1956 Summer Olympics in Melbourne.\n\nParrot Carrot: Parrot Carrot is a children's book written by Kate Temple and Jolyon Temple.  It is illustrated by Jon Foye.  The book is published by Australia's largest independent publisher, Allen and Unwin.  The book has also been produced as an app.  It is the world's first augmented reality children's book.  The interactive ebook is voiced by noted Australian singer Kamahl.\n\nRené Libeer: René Jules Libeer (28 November 1934 – 13 November 2006) was a French flyweight boxer.  Competing as an amateur he won bronze medals at the 1956 Summer Olympics and 1957 European Championships.  Next year he turned professional and in 1965 won the vacant European title against Paul Chervet.  After defending it three times he lost it in 1967 to Fernando Atzori.  Their rematch the same year ended in a draw, after which Libeer retired from boxing.\n\nKamahl: Kamahl is the stage name of Kandiah Kamalesvaran {'1': \", '2': \", '3': \", '4': \"} (Tamil: கந்தையா கமலேஸ்வரன் ; born 13 November 1934), a singer and recording artist active in Australia, perhaps best known for \"The Elephant Song\", and his repertoire of popular music.\n\nLaw Lan: Law Lan MH (born 13 November 1934) is a Hong Kong actress.\n\nBenny Shalita: Benny Shalita (Hebrew: בני שליטא‎ ‎ , born 13 November 1934) is an Israeli former politician, who served as a member of the Knesset for Likud between 1981 and 1988, and as mayor of Menahemia from 1956 until 1992.\n\nAlberto Jover Piamonte: Alberto Jover Piamonte, D.D., JCD., (21 November 1934 – 17 December 1998) was the fourth Roman Catholic Archbishop of Jaro in the Philippines.  He was born in Iloilo City on 21 November 1934 and was a native of the District of Jaro, Iloilo City.  After studying Philosophy and Theology at St. Vincent Ferrer Seminary, he was ordained a priest of the Archdiocese of Jaro on 22 March 1958.\n\nWalter Moraes: Walter Moraes (13 November 1934 in Catanduva, São Paulo, Brazil – 17 November 1997 in Diadema, São Paulo), was a Brazilian jurist, Catholic thinker, professor of the University of São Paulo Faculty of Law, judge at the High Court of São Paulo.  Studied in the minor seminary of the Divine Word Missionaries.  He married Sonia dos Santos Moraes in 1959, with whom he had two children.  Graduated in Law and Philosophy by the University of São Paulo.  He began his career as Judge in municipalities of Casa Branca, Quatá and Campos do Jordão.  Pioneered many fields of juridical science in Brazil including copyright, inheritance and family law.  Reformer of the Brazilian Children's code together with Prof. Antonio Chaves.  Important supporter and theorist of the Brazilian pro-life movement.  Spoke against legal abortion in his famous conference \"The Farce of Legal Abortion\", given in the Chamber of Deputies of Brazil on 24 September 1997, less than two months before his death. \n\nPeter Arnett: Peter Gregg Arnett, ONZM (born 13 November 1934) is a New Zealand-born journalist holding both New Zealand and US citizenship.\n\nJimmy Fontana: Jimmy Fontana (13 November 1934 – 11 September 2013) was an Italian actor, composer and singer-songwriter.  Two of his most famous songs are \"Che sarà\", performed also by José Feliciano with Ricchi e Poveri and \"Il Mondo\".\n\nQuestion: Who, born 13 November 1934, voiced the interactive ebook Parrot Carrot ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who voiced the ebook.\"\n    },\n    \"date_of_birth\": {\n      \"type\": \"string\",\n      \"format\": \"date\",\n      \"description\": \"The birth date of the person.\"\n    },\n    \"ebook_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the ebook.\"\n    },\n    \"role_in_ebook\": {\n      \"type\": \"string\",\n      \"description\": \"The role the person played in the ebook production.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"date_of_birth\",\n    \"ebook_title\",\n    \"role_in_ebook\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person who voiced the ebook."
      },
      "date_of_birth": {
        "type": "string",
        "format": "date",
        "description": "The birth date of the person."
      },
      "ebook_title": {
        "type": "string",
        "description": "The title of the ebook."
      },
      "role_in_ebook": {
        "type": "string",
        "description": "The role the person played in the ebook production."
      }
    },
    "required": [
      "person_name",
      "date_of_birth",
      "ebook_title",
      "role_in_ebook"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
