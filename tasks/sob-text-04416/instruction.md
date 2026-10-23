{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMiss International 2009: Miss International 2009, the 49th Miss International pageant, was held on November 28, 2009 at the Sichuan International Tennis Center in Chengdu, Sichuan, China.  The pageant was originally scheduled to be held on November 7, 2009 at The Venetian Macao in Macau, but the host committee backed out.  66 contestants competed for the coveted title.  Alejandra Andreu of Spain crowned Anagabriela Espinoza of Mexico as the new titleholder.\n\nMiss International 2004: Miss International 2004, the 44th Miss International pageant, was held on October 16, 2004 at the Workers Indoor Arena in Beijing, China.  58 contestants from all over the world competed for the crown.  Miss International 2003, Goizeder Azua of Venezuela, crowned her successor Jeymmy Vargas of Colombia as the new Miss International.\n\nMiss International 1964: Miss International 1964, the 5th Miss International pageant, was held on August 14, 1964 in Long Beach, California, USA.  40 contestants competed in this pageant.  Gemma Cruz from the Philippines was crowned the winner of the pageant by outgoing titleholder, Gudrun Bjarnadottir from Iceland.  Cruz made history receiving the first Miss International title for the country (the first major title) and in Asia.\n\nMiss International 2007: Miss International 2007, the 47th Miss International pageant, was held on October 15, 2007 at The Prince Park Tower in Tokyo, Japan.  61 contestants from all over the world competed for the crown.  Miss International 2006, Daniela Di Giacomo of Venezuela, crowned her successor Priscila Perales of Mexico as the new Miss International.\n\nAlejandra Andreu: Alejandra Andreu Santamarta (born February 25, 1990 in Zaragoza) is a Spanish beauty pageant titleholder who won the Miss International 2008 title at The Venetian Macao in Macau on November 8, 2008.  She also won the special award of \"Miss Photogenic\" at this pageant.  Andreu's victory marks the third Miss International crown for Spain.  Other winners were Pilar Medina (1977) and Silvia de Esteban (1990).  It is also the first \"Grand Slam\" beauty title for Spain since 1990.  Andreu also became one of the youngest winners in Miss International history when she was 18 at the coronation moment.\n\nMacau: Macau ( ), also spelled Macao and officially the Macao Special Administrative Region of the People's Republic of China, is an autonomous region on the western side of the Pearl River estuary in East Asia.  Macau is bordered by the city of Zhuhai in Mainland China to the north and the Pearl River Delta to the east and south.  Hong Kong lies about 64 km to its east across the Delta.  With a population of 650,900 living in an area of 30.5 km2 , it is the most densely populated region in the world.  A former Portuguese colony, it was returned to Chinese sovereignty on 20 December 1999.\n\nMiss International 1975: Miss International 1975, the 15th Miss International pageant, was held on November 3, 1975 at the Okinawa's Expo Portside Theater in Motobu, Japan.  48 contestants competed for the pageant.  Finally, Lidija Manić from Yugoslavia crown as Miss International 1975 by outgoing titleholder, Brucene Smith from USA.\n\nMiss International 2008: Miss International 2008, the 48th Miss International pageant, was held on November 8, 2008 at The Venetian Macao in Macau，the presenters are Dodo Cheng, Eric Tsang, Astrid Chan.  63 contestants from all over the world competed for the crown, marking the biggest turnout in the 48 years of the pageant, surpassing the previous of 61 during last year pageant.  The contestants also paid a visit to Hong Kong, Tokyo.  Miss International 2007, Priscila Perales of Mexico, crowned her successor Alejandra Andreu of Spain as the new Miss International.\n\nMiss International 1971: Miss International 1971, the 11th Miss International pageant, was held on May 26, 1971 in Long Beach, California, USA once more (it staged the first 6 Miss International pageants, from 1960-1967; with the 1966 pageant being cancelled).  50 contestants competed for the pageant.  Finally, Jane Hansen from New Zealand crown as Miss International 1971 by outgoing titleholder, Aurora Pijuan from the Philippines.\n\nMiss International 1968: Miss International 1968, the 8th Miss International pageant, was held on October 9, 1968 at the Nippon Budokan Hall in Tokyo, Japan, marking the first overseas hosting of the Miss International pageant after staging in Long Beach, California since its inception in 1960.  Maria da Glória Carvalho from Brazil was crowned the winner by outgoing titleholder, Mirta Massa from Argentina.\n\nQuestion: Miss International 2008, the 48th Miss International pageant, was held on November 8, 2008 at The Venetian Macao in which autonomous region on the western side of the Pearl River estuary in East Asia?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"pageant_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the pageant was held.\"\n        },\n        \"edition\": {\n          \"type\": \"integer\",\n          \"description\": \"The edition number of the Miss International pageant.\"\n        }\n      },\n      \"required\": [\n        \"year\",\n        \"edition\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"event_location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"venue_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the venue where the pageant was held.\"\n        },\n        \"autonomous_region_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the autonomous region where the pageant was held.\"\n        },\n        \"region_description\": {\n          \"type\": \"string\",\n          \"description\": \"A description of the autonomous region's geographical location.\"\n        }\n      },\n      \"required\": [\n        \"venue_name\",\n        \"autonomous_region_name\",\n        \"region_description\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"final_answer\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the autonomous region that is the answer to the question.\"\n    }\n  },\n  \"required\": [\n    \"pageant_details\",\n    \"event_location\",\n    \"final_answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "pageant_details": {
        "type": "object",
        "properties": {
          "year": {
            "type": "integer",
            "description": "The year the pageant was held."
          },
          "edition": {
            "type": "integer",
            "description": "The edition number of the Miss International pageant."
          }
        },
        "required": [
          "year",
          "edition"
        ],
        "additionalProperties": false
      },
      "event_location": {
        "type": "object",
        "properties": {
          "venue_name": {
            "type": "string",
            "description": "The name of the venue where the pageant was held."
          },
          "autonomous_region_name": {
            "type": "string",
            "description": "The name of the autonomous region where the pageant was held."
          },
          "region_description": {
            "type": "string",
            "description": "A description of the autonomous region's geographical location."
          }
        },
        "required": [
          "venue_name",
          "autonomous_region_name",
          "region_description"
        ],
        "additionalProperties": false
      },
      "final_answer": {
        "type": "string",
        "description": "The name of the autonomous region that is the answer to the question."
      }
    },
    "required": [
      "pageant_details",
      "event_location",
      "final_answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
