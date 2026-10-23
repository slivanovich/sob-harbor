{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJohn Coates (businessman): John Fitzgerald Coates (born January 1970), is an English businessman and joint chief executive (CEO) of online gambling company Bet365.  He has been listed in the \"Forbes\" magazine’s 29th annual rich list, with an estimated personal fortune of $1.3 billion (roughly £850 million).\n\nLadbrokes Coral: Ladbrokes Coral Group plc is a British based betting and gambling company.  It is based in London.  From 14 May 1999 to 23 February 2006, when it owned the Hilton hotel brand outside the United States, it was known as \"Hilton Group plc\".  It is listed on the London Stock Exchange and is a member of the FTSE 250 Index, having been relegated from the FTSE 100 Index in June 2006.\n\nDafabet: Dafabet is a privately owned online gambling company based in Makati, Philippines.  It is the flagship brand and subsidiary of AsianBGE, and is licensed and regulated by Cagayan Economic Zone Authority (CEZA) and First Cagayan Leisure and Resorts Corporation (FCLRC).  Dafabet operates a website that provides a secure service for customers to wager online.\n\nPraesepe (company): Paresepe is a British bingo, arcade gaming and gambling company formed in 2007 based in Milton Keynes.  It owns the high street gambling arcade chain Cashino.\n\nBet365: Bet365 Group Ltd (styled as \"bet365\") is a gambling company based in the United Kingdom.  Bet365 is one of the world's leading online gambling groups with over 19 million customers in almost two hundred countries.  The Group employs over 3,000 people and is the largest private employer in the city of Stoke-on-Trent.\n\nTlcbet: TLCBET [tóng.lè.chéng] (formerly known as TLC88 and TLC188) is a Philippines based online gambling company founded in 2010.  TLCBET offers up to 4,000 in-running games every month.\n\nEndorphina: Endorphina Inc. is a Czech online gambling company based in Prague, established in 2012.  The company produces virtual slot machines which can be played using virtual currency such as Bitcoins, as well as real currency.\n\nDenise Coates: Denise Coates CBE (born 26 September 1967) is an English businesswoman, founder and joint chief executive of online gambling company Bet365.  She has been listed in the \"Forbes\" magazine’s rich list, with an estimated personal fortune of $4.1 billion (approximately £3.17 billion).\n\nJohann Graf: Johann Graf (born 1946) is an Austrian businessman, the founder and owner of Novomatic, an Austrian gambling company.\n\nThe Rank Group: The Rank Group is a British gambling company based in the United Kingdom.  Rank was formerly involved in the cinema and motion picture industry until 2006, and continues to use the Gongman logo originally used by the Rank Organisation's film distribution subsidiary General Film Distributors.  Its brands now include Mecca Bingo, and Grosvenor Casinos, the UK's largest casino operator.\n\nQuestion: Denise Coates was the founder of the gambling company based in what country?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"founder_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the founder.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the person in founding the company.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"company_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the company founded.\"\n        },\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of business the company operates in.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"type\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"company_base_country\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the company is based.\"\n    }\n  },\n  \"required\": [\n    \"founder_details\",\n    \"company_details\",\n    \"company_base_country\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "founder_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the founder."
          },
          "role": {
            "type": "string",
            "description": "The role of the person in founding the company."
          }
        },
        "required": [
          "name",
          "role"
        ],
        "additionalProperties": false
      },
      "company_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the company founded."
          },
          "type": {
            "type": "string",
            "description": "The type of business the company operates in."
          }
        },
        "required": [
          "name",
          "type"
        ],
        "additionalProperties": false
      },
      "company_base_country": {
        "type": "string",
        "description": "The country where the company is based."
      }
    },
    "required": [
      "founder_details",
      "company_details",
      "company_base_country"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
