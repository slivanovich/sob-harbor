{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSeema Tarana: Seema Tarana (also spelled as Sima Tarana; Persian: سیما ترانه) is an Afghan singer originally from Parwan.  She is popular in Afghanistan and Tajikistan.  She currently resides in Canada from where she continues her music career.  She has two new music videos and they are: Bewafa and Bache Zargar\n\nParasto: Parasto Persian: پرستو‎ ‎ , born Nooria is an Afghan singer.  She has been a singer since the 1970s and rose to fame with her former husband Rahim Mehryar.\n\nJawad Ghaziyar: Jawad Ghaziyar (Persian: جواد غازيار‎ ‎ ) is a popular Afghan singer.  He is one of the 1980s era singers who took refuge in United States after the fall of Afghanistan government in 1992.  Jawad was also a special judge in Season 8 of Afghan Star.\n\nSeeta Qasemi: Seeta Qasemi (Persian: سيتا قاسمى‎ ‎ ; born 6 April 1983 in Kabul, Afghanistan) also known as Seeta Qaseme, is an Afghan singer/songwriter.  She entered the Afghan music scene in 2008.  She sings both in Pashto and Dari and lives in Germany.\n\nBeltoon: Momin Khan Beltoon (Pashto: مومن خان بیلتون‎ ; Persian: مومن خان بيلتون‎ ‎ ) was an Afghan singer from Kabul Province, Afghanistan.  He was born in Chakari village of Khaki Jabbar District, Kabul.  However, he spent most of his life in Logar Province of Afghanistan.  Beltoon sang in both Persian and Pashto languages.  His style of music reflects the Kharabat style of Kabul.  Beltoon's father died before he was born, and his mother did so when he was young.  He was raised by his sister in Logar Province of Afghanistan.  Beltoon learned the rubab and tanbur at a young age.  He started singing at the age of 15.  His first song was in both Persian and Pashto.\n\nMangal (singer): Mangal (Pashto: منگل‎ ), born in Laghman is a prominent Afghan singer who started in the early 1970s.  He and his ex-wife, Naghma, were a popular musical duo who dominated Afghan music scene during the 1970s and early 1990s.  Mangal sings in Pashto and Dari.  His music is popular in Afghanistan, and Pakistan.\n\nZheela: Zheela (also spelled as Zhila and Zhilla, Persian: ‎ ‎ ژیلا, July 15, 1943 – June 28, 2009) was an Afghan singer and actress.  Along with her contemporaries Rukhshana, Qamar Gula and Afsana, she is often cited as one of the first female singers who entered the Afghan music scene professionally.\n\nNaghma: Naghma (Pashto: نغمه, born 1 January 1964 ) is a prominent Afghan singer who started her career in the early 1980s.  She and her ex-husband, Mangal, were a popular musical duo who dominated the Afghan music scene during the 1980s and early 1990s.  Naghma sings in Pashto and Dari (Persian).  Her music is popular in Afghanistan, Tajikistan and among Pashtuns in Pakistan.  She is one of the most popular female artists in Afghanistan and continues to be the voice and face of Pashtun traditional music.\n\nGhulam Dastagir Shaida: Ghulam Dastagir Shaida ( Dari استاد غلام دستگیر شیدا ) Ustad Ghulam Dastagir (1916–1970) was an Afghan singer and musician.  Ustad Shaida was born in the Kharabat neighborhood of Kabul, home of Kabul musicians who sung in classical Indian tradition.  Ustad Shaida is considered as one of the great Ustads of Afghan classical music along with Ustad Sarahang and Ustad Rahim Bakhsh.  His unique voice and style of singing resulted in fellow Kharabat musicians bestowing upon him the title of Shaida, which in Sufi tradition means one who has sacrificed himself for divine love.\n\nRukhshana: Rukhshana (Pashto: رخشانه‎ ) is an Afghan singer.  In the 1960s and 1970s, she, along with Zheela, are recognized as the top two female singers of the country.  She currently resides in Los Angeles and has not participated in any musical acts since her immigration to the United States.\n\nQuestion: Mangal, born in Laghman is a prominent Afghan singer who started in the early 1970s, he and his ex-wife, which prominent Afghan singer who started her career in the early 1980s, were a popular musical duo who dominated Afghan music scene during the 1970s and early 1990s? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"singer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the prominent Afghan singer.\"\n    },\n    \"relationship_to_mangal\": {\n      \"type\": \"string\",\n      \"description\": \"The relationship of the singer to Mangal.\"\n    },\n    \"career_start_decade\": {\n      \"type\": \"string\",\n      \"description\": \"The decade when the singer started her career.\"\n    },\n    \"duo_dominance_period\": {\n      \"type\": \"string\",\n      \"description\": \"The period during which the musical duo dominated the Afghan music scene.\"\n    },\n    \"is_prominent_singer\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the singer is described as prominent.\"\n    }\n  },\n  \"required\": [\n    \"singer_name\",\n    \"relationship_to_mangal\",\n    \"career_start_decade\",\n    \"duo_dominance_period\",\n    \"is_prominent_singer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "singer_name": {
        "type": "string",
        "description": "The name of the prominent Afghan singer."
      },
      "relationship_to_mangal": {
        "type": "string",
        "description": "The relationship of the singer to Mangal."
      },
      "career_start_decade": {
        "type": "string",
        "description": "The decade when the singer started her career."
      },
      "duo_dominance_period": {
        "type": "string",
        "description": "The period during which the musical duo dominated the Afghan music scene."
      },
      "is_prominent_singer": {
        "type": "boolean",
        "description": "Indicates if the singer is described as prominent."
      }
    },
    "required": [
      "singer_name",
      "relationship_to_mangal",
      "career_start_decade",
      "duo_dominance_period",
      "is_prominent_singer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
