{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGilles Schnepp: Gilles Schnepp, (born in Lyon, France, on 16 October 1958) is a French corporate senior executive.  He is married to Ms Blandine Favre-Gilly (attorney at law) and has three children: Paul, Adrien and Marie.\n\nCorinne Maier: Corinne Maier (born December 7, 1963) is a Swiss-born, French psychoanalyst, economist, and best-selling writer.  She is best known for being the author of \"Bonjour paresse\", a cynical critique of French corporate culture.  In 2016, Maier was named as one of the BBC 100 Women.\n\nDominique Lafont: Dominique Lafont (born March 29, 1961), is a French corporate leader.  In 2006, he became Managing Director for Africa in the Bolloré Group.  On January 1, 2012, he was named President of Bolloré Africa Logistics, the Group subsidiary combining all of the Group's infrastructure and logistic activities both within Africa and outside the continent, across the major emerging countries trading with Africa.\n\nMuhammad Naeem (physicist): Muhammad Naeem, is a Pakistani nuclear scientist who is the current chairman of the Pakistan Atomic Energy Commission (PAEC).  He is also the current chairman of the Board of Governors of Pakistan Institute of Engineering and Applied Sciences (PIEAS).\n\nBonjour paresse: Bonjour paresse (\"Hello Laziness\") is the title of an international bestseller by Corinne Maier, a French writer, psychoanalyst, and economist.  The book is a highly cynical and humorous critique of contemporary French corporate culture (epitomized for Maier by the middle manager) that advocates various ways of undermining the system.  The title is a reference to Françoise Sagan's novel \"Bonjour Tristesse\".  It is variously subtitled \"Jumping Off the Corporate Ladder\", or \"Why Hard Work Doesn’t Pay\" depending on the edition.  Because of their similar attitudes towards the workplace, Maier has been frequently compared to Dilbert creator Scott Adams.\n\nFrançois Pérol: François Pérol (born on the 6 November 1963) is a French banker and high-ranking official and is the current chairman of Natixis.\n\nHemaka Amarasuriya: Hemaka Amarasuriya is a Sri Lankan corporate leader and executive, who holds and has held many corporate positions in Sri Lanka and the region.  He was the former CEO and current chairman of Singer Sri Lanka.  He is also the chairman of Sri Lanka Insurance, Nations Trust Bank and NDB Group.\n\nFrench company law: French company law is the law governing corporations incorporated in France or under French corporate law.\n\nSanghiya Sadbhawna Party: The Nepal Sadbhavana Party is a regional political party in Nepal that works for Madhesi rights.  It was founded in 2011 as the Sanghiya Sadbhavana Council after splitting from the Nepal Sadbhavana Party and in 2015 Nepal sadhbhawana party led by sarita giri and sanghiya sadbhawana led by Anil kumar jha both joined and become a single party named Nepal sadbhawna party.Anil kumar jha is the current chairman of this party, Anil Kumar Jha who is the current chairman.\n\nNatixis: Natixis is a French corporate and investment bank created in November 2006 from the merger of the asset management and investment banking operations of \"Natexis Banque Populaire\" (Banque Populaire group) and \"IXIS\" (Groupe Caisse d'Epargne).\n\nQuestion: Who is the current chairman of French corporate?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who is the chairman.\"\n    },\n    \"role\": {\n      \"type\": \"string\",\n      \"description\": \"The specific role held by the person in the organization.\"\n    },\n    \"organization_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the organization the person chairs.\"\n    },\n    \"organization_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of the organization.\"\n    },\n    \"person_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the person.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"role\",\n    \"organization_name\",\n    \"organization_type\",\n    \"person_nationality\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person who is the chairman."
      },
      "role": {
        "type": "string",
        "description": "The specific role held by the person in the organization."
      },
      "organization_name": {
        "type": "string",
        "description": "The name of the organization the person chairs."
      },
      "organization_type": {
        "type": "string",
        "description": "The type of the organization."
      },
      "person_nationality": {
        "type": "string",
        "description": "The nationality of the person."
      }
    },
    "required": [
      "person_name",
      "role",
      "organization_name",
      "organization_type",
      "person_nationality"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
