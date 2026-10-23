{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBangaaru Kalalu: Bangaru Kalalu (English:Golden Dreams) is a 1974 Telugu drama film, produced by D. Madhusudhana Rao under Annapurna Pictures banner and directed by Adurthi Subba Rao.  Starring Akkineni Nageswara Rao, Waheeda Rehman, Lakshmi in the lead roles and music composed by Saluri Rajeswara Rao.  The film was based on the \"Yaddanapudi Sulochana Rani\" novel of the same name.\n\nMangalya Balam: Mangalya Balam (English: Power of Wedding Chain) is a 1959 Telugu drama film produced by D. Madhusudhana Rao under Annapurna Pictures and directed by Adurthi Subba Rao.  Starring Akkineni Nageswara Rao, Savitri in the lead roles and music composed by Master Venu.  The film is based on Aasapoorna Devi's Bengali novel \"Agni Pariksha\" which was simultaneously remade as Tamil Movie \"Manjal Mahimai\" (1959); both the movies are made simultaneously by same banner & director and some of the scenes & artists are same in both versions.  Later remade as Hindi movie \"Chhoti Si Mulaqat\" (1967) with slight changes, starring Uttam Kumar, Vyjayanthimala in pivotal roles.\n\nAnnapurna Pictures: Annapurna Pictures is an American motion picture company founded by Megan Ellison in 2011.  It specializes in film production, television production, video game development, distribution, marketing, and finance.\n\nChaduvukunna Ammayilu: Chaduvukunna Ammayilu (English: \"Educated Girls\") is a 1963 Indian Telugu drama film, produced by D. Madhusudhana Rao on Annapurna Pictures banner and directed by Adurthi Subba Rao.  Starring Akkineni Nageswara Rao, Savitri, Krishna Kumari in the lead roles and music composed by Saluri Rajeswara Rao.  The film is based on the Telugu novel \"Kaalaatheetha Vyakthulu\" written by \"Dr. Sridevi\". The film recorded as \"Super Hit\" at the box office.\n\nVelugu Needalu: Velugu Needalu (\"Light & Shadows\") is a 1961 Telugu language film produced by D. Madhusudhana Rao under Annapurna Pictures banner and directed by Adurthi Subba Rao.  Starring Akkineni Nageswara Rao, Savitri in the lead roles and music composed by Pendyala Nageswara Rao.  The film was simultaneously filmed in Tamil as Thooya Ullam (\"Pure Heart\").  The film has received the Filmfare Award for Best Film - Telugu.\n\nAatma Gowravam: Aatma Gowravam (English: Self-Esteem; Telugu: ఆత్మ గౌరవం ) is a 1965 Telugu drama film, produced by D. Madhusudhana Rao on Annapurna Pictures banner and directed by K. Viswanath.  Starring Akkineni Nageswara Rao, Kanchana, Rajasree in the lead roles and music composed by Saluri Rajeswara Rao.\n\nDoctor Chakravarty: Doctor Chakravarthy is 1964 Telugu drama film produced by D. Madhusudhana Rao on Annapurna Pictures banner and directed by Adurthi Subba Rao.  Starring Akkineni Nageswara Rao, Savitri, Jaggaiah in the lead roles and music composed by Saluri Rajeswara Rao.  The film is based on Koduri Kousalya Devi's \"Chakrabhramanam\" (Novel).  The film recorded as \"Blockbuster\" at the box office.  It is the first film to win the Nandi Award instituted by Government of Andhra Pradesh in 1964.  It inspired many people in India to become doctors.\n\nThodi Kodallu: Thodi Kodallu (English: \"Co-Sisters\") is a 1957 Telugu drama film produced by D. Madhusudhana Rao under Annapurna Pictures and directed by Adurthi Subba Rao.  Starring Akkineni Nageswara Rao, Savitri in the lead roles and music composed by Master Venu.  The film is based on Sharat Chandra Chatterjee's Bengali novel \"Nishkruti\" which was simultaneously remade as Tamil Movie \"Engal Veettu Mahalakshmi\" (1957); both the movies are made simultaneously by same banner & director and some of the scenes & artists are same in both versions.  The film won the Certificate of merit for Best Feature Film in Telugu.\n\nDonga Ramudu: Donga Ramudu (Telugu: దొంగ రాముడు) is a 1955 Telugu drama film, produced by D. Madhusudhana Rao on Annapurna Pictures banner and directed by K. V. Reddy.  Starring Akkineni Nageswara Rao, Savitri, Jamuna in the lead roles and music composed by Pendyala Nageswara Rao.  The film was archived in the curriculum of the Film and Television Institute of India The film is debut venture to the \"Annapurna Pictures\" into film industry who gave memorable hits with Akkineni Nageswara Rao.\n\nIddaru Mitrulu (1961 film): Iddaru Mitrulu (English: Two Friends) is a 1961 Telugu drama film, produced by D. Madhusudhana Rao under Annapurna Pictures and directed by Adurthi Subba Rao.  Starring Akkineni Nageswara Rao, Raja Sulochana, E. V. Saroja in the lead roles and music composed by Saluri Rajeswara Rao.  The film is a remake of 1957 Bengali film \"Tasher Ghar\" (1957).\n\nQuestion: Iddaru Mitrulu, is a 1961 Telugu drama film, produced by D. Madhusudhana Rao under Annapurna Pictures, an American motion picture company founded by who in 2011?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"company_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the company.\"\n        },\n        \"origin_country\": {\n          \"type\": \"string\",\n          \"description\": \"The country of origin for the company.\"\n        },\n        \"founding_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the company was founded.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"origin_country\",\n        \"founding_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"founder_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the founder of the company.\"\n        }\n      },\n      \"required\": [\n        \"name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"action\": {\n      \"type\": \"string\",\n      \"description\": \"The action performed by the founder related to the company.\"\n    }\n  },\n  \"required\": [\n    \"company_details\",\n    \"founder_details\",\n    \"action\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "company_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the company."
          },
          "origin_country": {
            "type": "string",
            "description": "The country of origin for the company."
          },
          "founding_year": {
            "type": "integer",
            "description": "The year the company was founded."
          }
        },
        "required": [
          "name",
          "origin_country",
          "founding_year"
        ],
        "additionalProperties": false
      },
      "founder_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the founder of the company."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      },
      "action": {
        "type": "string",
        "description": "The action performed by the founder related to the company."
      }
    },
    "required": [
      "company_details",
      "founder_details",
      "action"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
