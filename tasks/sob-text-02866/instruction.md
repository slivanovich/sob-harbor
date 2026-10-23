{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBobsleigh at the 1964 Winter Olympics – Four-man: Four-man bobsleigh at the 1964 Winter Olympics took place on 5 and 7 February at Bob und Rodelbahn Igls, Innsbruck, Austria.  This event was last run at the 1956 Winter Olympics as bobsleigh was not part of the 1960 games.\n\nBobsleigh at the 2012 Winter Youth Olympics: Bobsleigh at the 2012 Winter Youth Olympics took place at the Olympic Sliding Centre Innsbruck in Igls, Innsbruck, Austria on January 16.  The competition had a 2 boys' and a 2 girls' events, with the 4 boys' competition being excluded.\n\nFIBT World Championships 2000: The FIBT World Championships 2000 took place in Altenberg, Germany (men's bobsleigh), Winterberg, Germany (women's bobsleigh), and Igls, Austria (men's and women's skeleton).  Altenberg hosted the championship event for the fourth time, doing so previously in 1991 (bobsleigh), 1994 (skeleton), and 1999 (skeleton).  Winterberg hosted the championship event for the second time, doing so previously in 1995 (bobsleigh).  Igls hosted the championship for the fifth time, doing do previously in 1935 (two-man) and 1963, 1991 (skeleton), and 1993 (bobsleigh).  Two-woman bobsleigh and women's skeleton debuted at these championships.\n\nBobsleigh at the 1964 Winter Olympics – Two-man: Two-man bobsleigh at the 1964 Winter Olympics took place on 31 January and 1 February at Bob und Rodelbahn Igls, Innsbruck, Austria.  This event was last run at the 1956 Winter Olympics as bobsleigh was not part of the 1960 games.\n\nBobsleigh at the 1994 Winter Olympics – Two-man: Two-man bobsleigh at the 1994 Winter Olympics took place on 19 and 20 February 1994 at Lillehammer Olympic Bobsleigh and Luge Track.\n\nBobsleigh at the 2010 Winter Olympics – Two-man: The two-man bobsleigh competition at the 2010 Winter Olympics in Vancouver, British Columbia, Canada was held at the Whistler Sliding Centre in Whistler, British Columbia on 20–21 February.  The German team of André Lange and Kevin Kuske were the defending Olympic champions in this event.  Switzerland's team of Ivo Rüegg and Cedric Grand were the defending world champions in this event.  The test event held at the Olympic venue was won by the German duo of Thomas Florschütz and Marc Kühne.  The last World Cup event prior to the 2010 Games took place in Igls, Austria (southeast of Innsbruck) on 23 January 2010 and was won by the Swiss duo of Beat Hefti and Thomas Lamparter while Rüegg won the overall World Cup in the two-man event.\n\nBobsleigh at the 1976 Winter Olympics – Two-man: The Two-man bobsleigh competition at the 1976 Winter Olympics in Innsbruck was held on 6 and 7 February, at Olympic Sliding Centre Innsbruck.\n\n2012 Winter Youth Olympics: The 2012 Winter Youth Olympic Games (German: \"Olympische Jugend-Winterspiele 2012\"), officially known as the I Winter Youth Olympic Games (YOG), were an international multi-sport event for youths that took place in Innsbruck, on 13–22 January 2012.  They were the inaugural Winter Youth Olympics, a major sports and cultural festival celebrated in the tradition of the Olympic Games.  Approximately 1100 athletes from 70 countries competed.  The decision for Innsbruck to host the Games was announced on 12 December 2008 after mail voting by 105 International Olympic Committee (IOC) members.  Innsbruck is the first city to host three winter Olympic events, having previously hosted the 1964 Winter Olympics and the 1976 Winter Olympics.\n\nInnsbruck: Innsbruck (] , ] ) is the capital city of Tyrol in western Austria.  It is in the Inn valley, at its junction with the Wipp valley, which provides access to the Brenner Pass some 30 km to the south.\n\nBobsleigh at the 1964 Winter Olympics: The Bobsleigh 1964 Winter Olympics events took place between 31 January - 7 February 1964 at Bob und Rodelbahn Igls, Innsbruck, Austria.  This marked the return of Bobsleigh to the Winter Olympics as no bob events took place at the 1960 Winter Olympics.\n\nQuestion: Two-man bobsleigh at the 1964 Winter Olympics took place on 31 January and 1 February at Bob und Rodelbahn Igls, Innsbruck, Austria, Innsbruck is the capital city of which city, in western Austria?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"event_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"dates\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          }\n        },\n        \"venue\": {\n          \"type\": \"string\"\n        },\n        \"city\": {\n          \"type\": \"string\"\n        },\n        \"country\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"dates\",\n        \"venue\",\n        \"city\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"innsbruck_geographical_context\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"city_name\": {\n          \"type\": \"string\"\n        },\n        \"capital_of_region\": {\n          \"type\": \"string\"\n        },\n        \"region_location_in_country\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"city_name\",\n        \"capital_of_region\",\n        \"region_location_in_country\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"answer_region\": {\n      \"type\": \"string\"\n    }\n  },\n  \"required\": [\n    \"event_details\",\n    \"innsbruck_geographical_context\",\n    \"answer_region\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "event_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "dates": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "venue": {
            "type": "string"
          },
          "city": {
            "type": "string"
          },
          "country": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "dates",
          "venue",
          "city",
          "country"
        ],
        "additionalProperties": false
      },
      "innsbruck_geographical_context": {
        "type": "object",
        "properties": {
          "city_name": {
            "type": "string"
          },
          "capital_of_region": {
            "type": "string"
          },
          "region_location_in_country": {
            "type": "string"
          }
        },
        "required": [
          "city_name",
          "capital_of_region",
          "region_location_in_country"
        ],
        "additionalProperties": false
      },
      "answer_region": {
        "type": "string"
      }
    },
    "required": [
      "event_details",
      "innsbruck_geographical_context",
      "answer_region"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
