{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPyeongchang County: Pyeongchang (] ; in full, \"Pyeongchang-gun\" ] ; ) is a county in Gangwon province of South Korea located in the Taebaek Mountains region.  It is home to several Buddhist temples, including Woljeongsa.  It is approximately 180 km east of Seoul, the capital of South Korea.  Pyeongchang will host the 2018 Winter Olympics and the 2018 Winter Paralympics.\n\n2006–07 Biathlon World Cup statistics: The 2006–07 Biathlon World Cup statistics gives a detailed tabular account of the accumulating Biathlon World Cup scores and related rankings of the top 30 biathletes in the Total (Overall) World Cup, and the top 15 in each of the Individual, Sprint, Pursuit, and Mass start Cups, as well as the top 10 nations in the Relay Cup and top 15 in the Nation Cup, for the duration of the 2006-07 World Cup season, including the 2007 Biathlon World Championships, which counted as usual in the World Cup scores.\n\n2004–05 Biathlon World Cup: The 2004−05 Biathlon World Cup was a multi-race tournament over a season of biathlon, organised by the International Biathlon Union.  The Biathlon World Championships 2005 were part of the Biathlon World Cup.\n\nBiathlon World Championships 1987: The 23rd Biathlon World Championships for men were held in 1987 for the second time in Lake Placid, New York, United States.  The 4th women's world championships were held in Lahti, Finland.\n\nDorothea Wierer: Dorothea Wierer Corradini (born 3 April 1990) is an italian biathlete.  She competes in the Biathlon World Cup.  Wierer has won a bronze medal at the Biathlon World Championships 2013 (4x6 km relay).  Together with Karin Oberhofer, Dominik Windisch and Lukas Hofer she won a bronze medal in the Mixed relay at the 2014 Winter Olympics, in Sochi, Russia.  As of February 2015, Wierer has finished on the podium five times in the Biathlon World Cup.  Her best overall finish in the Biathlon World Cup is 3rd, in the 2015–16 season.\n\nBiathlon World Championships 2008: The 42nd Biathlon World Championships were held in Östersund in Jämtland in central Sweden from February 8 to February 17, 2008.  It was the second time Östersund was hosting the Biathlon World Championships, the first being in 1970.  It was also 50 years after the first Biathlon World Championships, which were held 1958 in Saalfelden, Austria.\n\nBiathlon World Championships 2009: The 43rd Biathlon World Championships were held in Pyeongchang, South Korea from February 13 to February 22, 2009.  It was the first time that the Biathlon World Championships were held in Asia (outside of Asian Russia).\n\nMateusz Janik: Mateusz Janik (born 20 November 1995) is a Polish biathlete.  He has competed in the Biathlon World Cup, and represented Poland at the Biathlon World Championships 2015 and Biathlon World Championships 2016.\n\nSimon Schempp: Simon Schempp (born 14 November 1988) is a German biathlete.  In 2009, he made his World Cup debut.  He became world champion by winning gold in the 15km mass start race at the Biathlon World Championships 2017 in Hochfilzen.  He also won three more gold medals, two for being part of the German Biathlon World Championships 2010 mixed relay team in Khanty-Mansiysk and the German Biathlon World Championships 2017 mixed relay team in Hochfilzen, and one gold medal as part of the German Biathlon World Championships 2015 men's relay team in Kontiolahti.\n\n2003–04 Biathlon World Cup: The 2003−04 Biathlon World Cup was a multi-race tournament over a season of biathlon, organised by the International Biathlon Union.  The Biathlon World Championships 2004 were part of the Biathlon World Cup.\n\nQuestion: In which province is the county where The 43rd Biathlon World Championships were held ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"event_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the biathlon championship event.\"\n    },\n    \"championship_edition\": {\n      \"type\": \"integer\",\n      \"description\": \"The edition number of the Biathlon World Championships.\"\n    },\n    \"host_county\": {\n      \"type\": \"string\",\n      \"description\": \"The county that hosted the championships.\"\n    },\n    \"host_province\": {\n      \"type\": \"string\",\n      \"description\": \"The province in which the host county is located.\"\n    }\n  },\n  \"required\": [\n    \"event_name\",\n    \"championship_edition\",\n    \"host_county\",\n    \"host_province\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "event_name": {
        "type": "string",
        "description": "The name of the biathlon championship event."
      },
      "championship_edition": {
        "type": "integer",
        "description": "The edition number of the Biathlon World Championships."
      },
      "host_county": {
        "type": "string",
        "description": "The county that hosted the championships."
      },
      "host_province": {
        "type": "string",
        "description": "The province in which the host county is located."
      }
    },
    "required": [
      "event_name",
      "championship_edition",
      "host_county",
      "host_province"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
