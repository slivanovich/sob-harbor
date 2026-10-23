{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPrincess Sara bint Faisal: Princess Sara bint Faisal of Jordan (born 27 March 1997) is the daughter Prince Faisal bin Hussein and Princess Alia, and a niece of King Abdullah II of Jordan.  She is the younger sister of Princess Ayah and Prince Omar, and is also twin to Princess Aisha.  Princess Sara currently attends Amman Baccalaureate School and is a senior.\n\nPrincess Iman bint Hussein: Princess Iman bint Hussein (born 24 April 1983) is the daughter of King Hussein and Queen Noor of Jordan.  She has two full brothers, Hamzah and Hashim, and a younger sister, Princess Raiyah.  She is a half-sister to King Abdullah II of Jordan.\n\nPrincess Aisha bint Faisal: Princess Aisha bint Faisal of Jordan (born 27 March 1997) is the daughter of Prince Faisal bin Hussein and Princess Alia, and a niece of King Abdullah II of Jordan.  She is the younger sister of Princess Ayah and Prince Omar, and is also twin to Princess Sara.  She attends Amman Baccalaureate School, a private school in Amman, Jordan.\n\nAbdullah II of Jordan: Abdullah II bin Al-Hussein (Arabic: عبد الله الثاني بن الحسين‎ ‎ , \"ʿAbdullāh aṯ-ṯānī ibn Al-Ḥusayn\", born 30 January 1962) has been King of Jordan since the 1999 death of his father, King Hussein.  According to Abdullah, he is a 41st-generation direct descendant of Muhammad as he belongs to the Hashemite family—who have ruled Jordan since 1921.\n\nPrincess Aisha bint Hussein: Princess Aisha bint Hussein (born 23 April 1968) is the sister of King Abdullah II of Jordan and is the twin sister of Princess Zein.  Her parents are Princess Muna al-Hussein and King Hussein.\n\nPrincess Zein bint Hussein: Princess Zein bint Hussein (born 23 April 1968) is the sister of King Abdullah II of Jordan and the twin sister of Princess Aisha bint Hussein.\n\nPrincess Raiyah bint Hussein: Princess Raiyah bint Hussein (born 9 February 1986) is the youngest daughter of King Hussein of Jordan and Queen Noor.  She has two brothers Hamzah and Hashem and an elder sister Princess Iman.  She is a half-sister to King Abdullah II of Jordan.\n\nPrincess Alia bint Hussein: Princess Alia bint Hussein (born 13 February 1956) is the eldest child of King Hussein of Jordan from his first wife, Sharifa Dina bint Abdul-Hamid.\n\nHaya bint Hussein: Princess Haya bint Hussein (Arabic: الأميرة هيا بنت الحسين‎ ‎ ; born 3 May 1974) is the daughter of King Hussein of Jordan and his third wife, Queen Alia, and the half-sister of King Abdullah II.  Princess Haya is the fourth and junior wife of the United Arab Emirates' prime minister, Sheikh Mohammed bin Rashid Al Maktoum, being known internationally as Princess Haya of Jordan.  She is a 41st-generation direct descendant of Muhammad since she was born to the Hashemite family (who have ruled Jordan since 1921).\n\nPrince Omar bin Faisal: Prince Omar bin Faisal of Jordan (born 22 October 1993) is the second child and elder son of Prince Faisal bin Hussein and Princess Alia and is a nephew of King Abdullah II of Jordan.  He is the younger brother of Princess Ayah, and older brother to the twins Princess Aisha and Princess Sara.\n\nQuestion: Princess Aisha bint Hussein is the sister of the King who has ruled since what year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"princess_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the princess.\"\n    },\n    \"princess_birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the princess.\"\n    },\n    \"king_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the king.\"\n    },\n    \"relationship_to_king\": {\n      \"type\": \"string\",\n      \"description\": \"The relationship of the princess to the king.\"\n    },\n    \"king_reign_start_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the king began his reign.\"\n    }\n  },\n  \"required\": [\n    \"princess_name\",\n    \"princess_birth_year\",\n    \"king_name\",\n    \"relationship_to_king\",\n    \"king_reign_start_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "princess_name": {
        "type": "string",
        "description": "The full name of the princess."
      },
      "princess_birth_year": {
        "type": "integer",
        "description": "The birth year of the princess."
      },
      "king_name": {
        "type": "string",
        "description": "The full name of the king."
      },
      "relationship_to_king": {
        "type": "string",
        "description": "The relationship of the princess to the king."
      },
      "king_reign_start_year": {
        "type": "integer",
        "description": "The year the king began his reign."
      }
    },
    "required": [
      "princess_name",
      "princess_birth_year",
      "king_name",
      "relationship_to_king",
      "king_reign_start_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
