{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDemocratic Youth Front (Nicaragua): Democratic Youth Front (in Spanish: \"Frente Juvenil Democratico\") was the youth organization of the Independent Liberal Party in Nicaragua.  In the 1950s the FJD played an important political role northern Nicaragua.  FJD published \"Vanguardia Juvenil\".  Radical sections of FJD later joined the FSLN.\n\nSexenio (Mexico): Sexenio is the popular term for the term limit on the President of Mexico.  The president is limited to a single six-year term, and no one who holds the office even on a caretaker basis is permitted to run for or hold the office again.  It is one of the country's most important political institutions because it is one of the few significant limitations on executive power in Mexico, which is strong at local, state, and national levels.  The sexenio is seen as a reaction to the failed experiment of re-election in Mexico during part of the Porfiriato era (1876–1911).  In addition to restricting the presidency, state governors also face this restriction; no one elected as a governor may ever hold the post again even on an interim basis.\n\nEdøya: Edøya is an island in Smøla Municipality in Møre og Romsdal county, Norway.  The 7.5 km2 island lies in the Edøyfjorden between the larger islands of Smøla (to the north) and Ertvågsøya and Tustna (to the south).  The island played an important political role during the Viking Age.  More recently, it was the center of the old municipality of Edøy and the historic Old Edøy Church is located on the island.\n\nZeyn al-Abedin Maraghei: Zeyn al-Abedin Maraghei (1840 in Maragheh – 1910 in Istanbul) was a pioneer Iranian novelist and a social reformer.  He is most known for the story of \"Travel Diary of Ebrahim Beg\" (\"sīyāhat nāmeh-ī Ebrāhīm-ī Beg\").  This work was critical in the development of novel writing in twentieth-century Iran, and played an important political role as well.  The story was a criticism on Iran's political and social affairs.  It was widely read in Iran and gained the interest of revolutionaries and reformers who made the Constitutional Revolution of 1906.\n\nNancy Reagan: Nancy Davis Reagan (born Anne Frances Robbins; July 6, 1921 – March 6, 2016) was an American film actress and the wife of Ronald Reagan, the 40th President of the United States.  She served as the First Lady of the United States from 1981 to 1989.\n\nTalk About a Stranger: Talk About a Stranger is a 1952 American film noir released in and directed by David Bradley.  The drama features George Murphy, Nancy Davis and Billy Gray.\n\nP. Chinnamma Reddy: P. Chinnamma Reddy was a prominent politician in the Chittoor district, Andhra Pradesh, India until the 1960s.  He played an important political role as a follower of the future President of India, Neelam Sanjeeva Reddy.  He was known for building P.C.R. Junior College and Krishnavani Junior College, and for establishing the Chittoor cooperative sugar factory.  He was a Member of the Legislative Assembly for 15 years, representing the Indian National Congress Party.  He also had a main role in developing the K M Reddy junior college which was established by Konda Muni Reddy.\n\nDualism (politics): In Dutch politics the term dualism is used to refer to the separation of powers between the cabinet and parliament.  In this respect, the way the Dutch cabinets function is somewhat semi-presidential in its system of government, not parliamentary.  Unlike the presidential system, the legislative branch consists of the cabinet together with the parliament and cabinets are formed on basis of a majority in parliament.  Unlike the Westminster parliamentary system, cabinet ministers cannot be members of parliament.  An important political issue is whether ministers and leaders of governing parliamentary parties should prepare important political decisions.  According to the dualistic position, members of parliament of governing parties should function independently of their cabinet.  The term monism is used to refer to a stance that important decisions should be prepared by the members of the governing coalition in order to promote political stability.\n\nNew Order (Indonesia): Immediately following the attempted coup in 1965, the political situation was uncertain, but the Suharto's New Order found much popular support from groups wanting a separation from Indonesia's problems since its independence.  The 'generation of 66' (\"Angkatan 66\") epitomised talk of a new group of young leaders and new intellectual thought.  Following Indonesia's communal and political conflicts, and its economic collapse and social breakdown of the late 1950s through to the mid-1960s, the \"New Order\" was committed to achieving and maintaining political order, economic development, and the removal of mass participation in the political process.  The features of the \"New Order\" established from the late 1960s were thus a strong political role for the military, the bureaucratisation and corporatisation of political and societal organisations, and selective but effective repression of opponents.  Strident anti-communism remained a hallmark of the regime for its subsequent 32 years.\n\nChen Shiju: Chen Shiju (Chinese: 陈世炬）was an important political aide for China's former leader Hu Jintao.  Chen served as Hu's secretary beginning in Guizhou 1986.  Chen was the director of Hu Jintao's Office (Party General Secretary Office) in 2002–2012.  Chen currently serves as deputy director of the General Office of the Communist Party of China.  In 2015 he hold a concurrent post on Deputy Director of the CPC Central Guidance Committee on Ethical and Cultural Construction.\n\nQuestion: What important political role did the female star of the film Talk About a Stranger hold ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film mentioned in the question.\"\n    },\n    \"female_star_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the female star of the film.\"\n    },\n    \"political_role\": {\n      \"type\": \"string\",\n      \"description\": \"The important political role held by the female star.\"\n    },\n    \"role_start_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the political role started.\"\n    },\n    \"role_end_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the political role ended.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"female_star_name\",\n    \"political_role\",\n    \"role_start_year\",\n    \"role_end_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film mentioned in the question."
      },
      "female_star_name": {
        "type": "string",
        "description": "The name of the female star of the film."
      },
      "political_role": {
        "type": "string",
        "description": "The important political role held by the female star."
      },
      "role_start_year": {
        "type": "integer",
        "description": "The year the political role started."
      },
      "role_end_year": {
        "type": "integer",
        "description": "The year the political role ended."
      }
    },
    "required": [
      "film_title",
      "female_star_name",
      "political_role",
      "role_start_year",
      "role_end_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
