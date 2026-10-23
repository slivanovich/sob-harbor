{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRamon Pereira P.: Ramon \"Monchi\" Virgilio Fernando Pereira Perez (December 15, 1918 – August 12, 2013) was a well-known pioneer in radio broadcasting in Panama, best known as the founder of Radio Mia.\n\nWallace Fernando Pereira: Wallace Fernando Pereira (born 29 October 1986 in Cerquilho) is a Brazilian footballer who plays for Greek Super League club AEL.\n\nFernandinho (footballer, born 1985): Luiz Fernando Pereira da Silva (born 25 November 1985), commonly known as Fernandinho, is a Brazilian professional footballer who plays as a winger for Grêmio.\n\nFernando Pereira (disambiguation): Fernando Pereira (1950–1985) was a Dutch photographer.\n\nFernando Pereira: Fernando Pereira (10 May 1950 – 10 July 1985) was a freelance Dutch photographer, of Portuguese origin, who drowned when French intelligence (DGSE) detonated a bomb and sank the \"Rainbow Warrior\", owned by the environmental organisation Greenpeace on 10 July 1985.\n\nRainbow Warrior (1955): Rainbow Warrior was a former UK Ministry of Agriculture, Fisheries and Food (MAFF) trawler called the \"Sir William Hardy\".  She was purchased by the environmental organisation Greenpeace UK – an office established in May 1977 with Susi Newborn, Denise Bell, David McTaggart, Charlie Hutchison and Allan Thornton as directors.  The ship was active in supporting a number of Greenpeace anti-whaling, -seal hunting, -nuclear testing and -nuclear waste dumping campaigns during the late 1970s and early 1980s.  She was sunk whilst in Auckland harbour in New Zealand by operatives of the French intelligence service (DGSE) on 10 July 1985, killing photographer Fernando Pereira.\n\nSinking of the Rainbow Warrior: The sinking of the \"Rainbow Warrior\", codenamed Opération Satanic, was a bombing operation by the \"action\" branch of the French foreign intelligence services, the \"Direction générale de la sécurité extérieure\" (DGSE), carried out on 10 July 1985.  During the operation, two operatives sank the flagship of the Greenpeace fleet, the \"Rainbow Warrior\" in the port of Auckland, New Zealand on its way to a protest against a planned French nuclear test in Moruroa.  Fernando Pereira, a photographer, drowned on the sinking ship.\n\nMiguel Fernando Pereira Rodrigues: Miguel Fernando Pereira Rodrigues (born 16 March 1993 in Fátima) is a Portuguese footballer who plays for Greek club Panetolikos F.C. as a central defender.\n\nGreenpeace: Greenpeace is a non-governmental environmental organization with offices in over 40 countries and with an international coordinating body in Amsterdam, the Netherlands.  Greenpeace was founded by Irving Stowe and Dorothy Stowe, Canadian and US ex-pat environmental activists in 1971, Greenpeace states its goal is to \"ensure the ability of the Earth to nurture life in all its diversity\" and focuses its campaigning on worldwide issues such as climate change, deforestation, overfishing, commercial whaling, genetic engineering, and anti-nuclear issues.  It uses direct action, lobbying, research, and ecotage to achieve its goals.  The global organization does not accept funding from governments, corporations, or political parties, relying on 2.9 million individual supporters and foundation grants.  Greenpeace has a general consultative status with the United Nations Economic and Social Council and is a founding member of the INGO Accountability Charter; an international non-governmental organization that intends to foster accountability and transparency of non-governmental organizations.\n\n2003 São Tomé and Príncipe coup d'état: The 2003 São Tomé and Príncipe coup d'état was an attempted coup by rebels on July 16, 2003.  It was led by Major Fernando Pereira of the military.  The coup leaders claimed that they had acted to overthrow the government to help stop poverty in the region.\n\nQuestion: When was the organization whose boat Fernando Pereira drowned on founded?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"organization_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the organization.\"\n    },\n    \"founding_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the organization was founded.\"\n    },\n    \"event_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"event_description\": {\n          \"type\": \"string\",\n          \"description\": \"Description of the event where the individual drowned.\"\n        },\n        \"victim_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person who drowned.\"\n        },\n        \"boat_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the boat involved in the event.\"\n        }\n      },\n      \"required\": [\n        \"event_description\",\n        \"victim_name\",\n        \"boat_name\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"organization_name\",\n    \"founding_year\",\n    \"event_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "organization_name": {
        "type": "string",
        "description": "The name of the organization."
      },
      "founding_year": {
        "type": "integer",
        "description": "The year the organization was founded."
      },
      "event_details": {
        "type": "object",
        "properties": {
          "event_description": {
            "type": "string",
            "description": "Description of the event where the individual drowned."
          },
          "victim_name": {
            "type": "string",
            "description": "The name of the person who drowned."
          },
          "boat_name": {
            "type": "string",
            "description": "The name of the boat involved in the event."
          }
        },
        "required": [
          "event_description",
          "victim_name",
          "boat_name"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "organization_name",
      "founding_year",
      "event_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
