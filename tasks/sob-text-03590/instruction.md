{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBoğaziçi University: Boğaziçi University (also known as Bosphorus University, Turkish: \"Boğaziçi Üniversitesi\" , \"Boğaziçi\" literally meaning Bosphorus in Turkish) is a major research university located on the European side of the Bosphorus strait in Istanbul, Turkey.  It has four faculties and two schools offering undergraduate degrees, and six institutes offering graduate degrees.  The language of instruction is English.\n\nŚwięty Krzyż TV Tower: Święty Krzyż TV Tower ( Polish: RTCN Święty Krzyż ) is the tallest free-standing TV tower in Poland.  (Taller architectural structures in Poland are guyed masts or highrise buildings and chimneys equipped with antennas).  Święty Krzyż TV Tower, which was built in 1966, is a 157 metre tall concrete TV tower situated near the monastery on Łysa Góra.  Święty Krzyż TV Tower is not accessible by tourists.  The hyperbolic-shaped basement floors resemble those of the Ochsenkopf TV Tower in Germany.\n\nBorisova Gradina TV Tower: The Borisova Gradina TV Tower or the Old TV Tower is a 106-metre tall (including the aerial) TV tower in the garden Borisova Gradina in Sofia, the capital of Bulgaria.  It is known as the tower used for the first Bulgarian National Television broadcasts in 1959.\n\nEndem TV Tower: Endem TV Tower is a TV tower in Beylikdüzü, Istanbul, Turkey.  It was built between 1998 and 2002, and has a now closed revolving restaurant 154 m above ground, as well as an observation deck at 160 m .  The total height of the tower si 257 m including the antenna.\n\nMiskolc-Avas TV Tower: Miskolc-Avas TV Tower (in colloquial speech \"Avasi kilátó,\" Avas Lookout Tower) is a 72 metre tall TV tower with an observation deck on the Avas hill in Miskolc, Hungary.  The Avas TV Tower was designed by Miklós Hófer and György Vörös, and was built in 1966 in place of a wooden lookout tower.  It is commonly regarded as the symbol of the city, even though in the 1990s the bell tower of the Avas church was declared the city's symbol in its place.\n\nKherson TV Tower: Kherson TV Tower (Ukrainian: Херсонська телевежа \"Kherson TV Tower\") is a 200 m tall space framed Ukrainian truss communications tower that is made of steel.  The building is uniquely built, having been built by using the cross bracing system.  The tower is a truss TV tower, specifically, a Vierendeel truss tower, wherein a structure's members are not triangulated but form rectangular openings instead (see Vierendeel Truss).  The tower has an antenna that measures 199.95 m and a roof that measures 189.89 m .  The tower, possessing a total height of 200 m , is also considered the tallest structure in the whole oblast (province) of Kherson'ka.\n\nPitampura TV Tower: Pitampura TV Tower is a 235 m -tall television tower, built in 1988, with an observation deck that is located in the northwest of New Delhi, India.  It is the 15th tallest structure in India, and the tallest structure in Delhi.  Dilli Haat Pitampura is also situated near the TV tower.  The Tower was dedicated to the Nation as Dr. B. R. Ambedkar TV Tower 10 April 1992 by the Hon’ble Sh.  Ajeet Kumar Panja Minister for The State of Information & Broadcasting.\n\nFeza Gürsey Institute: Feza Gürsey Institute (Turkish: \"Feza Gürsey Enstitüsü\" ) is a joint institute of Boğaziçi University and TÜBİTAK (Scientific and Technological Research Council of Turkey) on physics research, founded in 1983 by Erdal İnönü with the name \"Research Institute for Basic Sciences\".  It now continues as the \"Feza Gürsey Institute\", having been renamed in honor of Feza Gürsey, a distinguished Turkish physicist.  The institute is located within the Kandilli Campus of the Boğaziçi University in Istanbul, Turkey.  Currently it hosts researchers in mathematics and theoretical physics.\n\nTortoise Mountain TV Tower: Tortoise Mountain TV Tower () is a 311.4 m high TV Tower at Wuhan, People's Republic of China.  It is a concrete tower equipped with an observation deck in a height of 210 m .  It does not stand directly upon the hill, which is occupied by an ancient temple complex (Qing Chuan Ge (晴川閣) from the Three Kingdoms, Song, and Ming Dynasties).  Guishan TV Tower is China's first self-developed TV tower, opened in 1986.\n\nBoğaziçi Sultans: Boğaziçi Sultans is Turkey's first American football team, founded in 1987 at the Boğaziçi University in Istanbul.  Formerly named as \"Bogaziçi Elephants\", the team improved their game by practicing with American soldiers, and played their first game against another Turkish team with \"Istanbul Pistoflar\" winning 28-0.  The team's head coach is Erdem Özsalih.  The team plays in the American Football First League of Turkey and American Football University League of Turkey.\n\nQuestion: Where should I visit in Turkey, Endem TV Tower or Boğaziçi University?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"recommended_destination\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the recommended place to visit.\"\n        },\n        \"location\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"city\": {\n              \"type\": \"string\",\n              \"description\": \"The city where the recommended destination is located.\"\n            },\n            \"country\": {\n              \"type\": \"string\",\n              \"description\": \"The country where the recommended destination is located.\"\n            }\n          },\n          \"required\": [\n            \"city\",\n            \"country\"\n          ],\n          \"additionalProperties\": false\n        },\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of the recommended destination (e.g., university, TV tower).\"\n        },\n        \"description_points\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"Key descriptive points about the recommended destination from the context, relevant for a visit.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"location\",\n        \"type\",\n        \"description_points\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"alternative_destination\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the alternative place considered for a visit.\"\n        },\n        \"location\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"city\": {\n              \"type\": \"string\",\n              \"description\": \"The city where the alternative destination is located.\"\n            },\n            \"country\": {\n              \"type\": \"string\",\n              \"description\": \"The country where the alternative destination is located.\"\n            }\n          },\n          \"required\": [\n            \"city\",\n            \"country\"\n          ],\n          \"additionalProperties\": false\n        },\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of the alternative destination (e.g., university, TV tower).\"\n        },\n        \"description_points\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"Key descriptive points about the alternative destination from the context, relevant for a visit.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"location\",\n        \"type\",\n        \"description_points\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"recommendation_summary\": {\n      \"type\": \"string\",\n      \"description\": \"A brief summary explaining the recommendation based on the provided context.\"\n    }\n  },\n  \"required\": [\n    \"recommended_destination\",\n    \"alternative_destination\",\n    \"recommendation_summary\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "recommended_destination": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the recommended place to visit."
          },
          "location": {
            "type": "object",
            "properties": {
              "city": {
                "type": "string",
                "description": "The city where the recommended destination is located."
              },
              "country": {
                "type": "string",
                "description": "The country where the recommended destination is located."
              }
            },
            "required": [
              "city",
              "country"
            ],
            "additionalProperties": false
          },
          "type": {
            "type": "string",
            "description": "The type of the recommended destination (e.g., university, TV tower)."
          },
          "description_points": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Key descriptive points about the recommended destination from the context, relevant for a visit."
          }
        },
        "required": [
          "name",
          "location",
          "type",
          "description_points"
        ],
        "additionalProperties": false
      },
      "alternative_destination": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the alternative place considered for a visit."
          },
          "location": {
            "type": "object",
            "properties": {
              "city": {
                "type": "string",
                "description": "The city where the alternative destination is located."
              },
              "country": {
                "type": "string",
                "description": "The country where the alternative destination is located."
              }
            },
            "required": [
              "city",
              "country"
            ],
            "additionalProperties": false
          },
          "type": {
            "type": "string",
            "description": "The type of the alternative destination (e.g., university, TV tower)."
          },
          "description_points": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Key descriptive points about the alternative destination from the context, relevant for a visit."
          }
        },
        "required": [
          "name",
          "location",
          "type",
          "description_points"
        ],
        "additionalProperties": false
      },
      "recommendation_summary": {
        "type": "string",
        "description": "A brief summary explaining the recommendation based on the provided context."
      }
    },
    "required": [
      "recommended_destination",
      "alternative_destination",
      "recommendation_summary"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
