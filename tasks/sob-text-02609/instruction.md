{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n2007 All-Africa Games: The 9th All-Africa Games took place between 11 and 23 July 2007 in Algiers, the capital city of Algeria.  Algiers is the first city to hold All-Africa Games for a second time.  The 1978 All-Africa Games were held there.  Besides Algeria, only Nigeria has hosted the event twice, but with different host cities.  4793 athletes took part to these games.\n\nCecilia Offiong: Cecilia Otu Offiong (born June 13, 1986 in Calabar, Cross River) is a Nigerian table tennis player.  She won two gold medals, along with her partner Offiong Edem, in the women's doubles at the 2007 All-Africa Games in Algiers, Algeria, and at the 2011 All-Africa Games in Maputo, Mozambique.  As of February 2013, Offiong is ranked no. 452 in the world by the International Table Tennis Federation (ITTF).  She is a member of the table tennis team for Calabar Sports Club, and is coached and trained by Obisanya Babatunde.  Offiong is also right-handed, and uses the shakehand grip.\n\nKahina Saidi: Kahina Saidi (Arabic: كهينة سعيدي‎ ‎ ; born March 17, 1984) is an Algerian judoka, who played for the half-middleweight category.  She is a four-time medalist at the African Judo Championships, and a bronze medalist at the 2009 Mediterranean Games in Pescara, Italy.  She also won two medals in the same division at the 2007 All-Africa Games in Algiers, and at the 2011 All-Africa Games in Maputo, Mozambique.\n\nZimbabwe at the 2011 All-Africa Games: In mid-August 2011, Zimbabwe's Chef de Mission for the 2011 All-Africa Games, Custom Kachambwa, announced that the country would send 170 athletes in 17 disciplines to the 10th All-Africa Games in Maputo, Mozambique, September 3–18, 2011.\n\nNesria Jelassi: Nesria Al-Jelassi (also Nesria Jelassi, Arabic: نسرية الجلاصي‎ ‎ ; born 19 August 1989) is a Tunisian judoka, who played for the lightweight category.  She is a two-time Tunisian judo champion, and a four-time medalist for the 57 and 63 kg classes at the African Judo Championships.  She also won a gold medal at the 2011 All-Africa Games in Maputo, Mozambique, and silver at the 2007 All-Africa Games in Algiers, Algeria.\n\nSandrine Ilendou: Sandrine Ilendou (born November 19, 1983) is a Gabonese judoka, who played for the extra-lightweight category.  She won the bronze medal for her category at the 2007 All-Africa Games in Algiers, Algeria, and silver at the 2011 All-Africa Games in Maputo, Mozambique, losing out to Tunisia's Amani Khalfaoui.\n\n2011 All-Africa Games: The 10th All-Africa Games took place between September 3–18, 2011 in Maputo, Mozambique.  Maputo's hosting marked the third time the Games was held in the southern part of the continent.\n\nChouaib Bouloudinat: Chouaib Bouloudinat or \"Bouloudinats\" (born January 8, 1987 in Constantine) is an Algerian boxer who won the 2011 All-Africa Games and fought at the 2012 Olympics.\n\nMaria Muchavo: Maria Elisa Muchavo (born 26 July 1992 in Maputo) is a disabled track and field athlete from Mozambique who won a silver medal at the 2014 Commonwealth Games in the T12 100 metres event.  She was her country's first woman to compete at the Summer Paralympics, doing so in 2012.  She was a 200 metres bronze medallist at the 2011 All-Africa Games.\n\nSamir Brahimi: Samir Brahimi is an Algerian boxer born on 17 May 1990.  His amateur career was marked by a bronze medal at the African Championships of Vacoas in 2009 and another in Yaounde in 2011, and a silver medal at the All Africa Games in Maputo in 2011, flyweight category.\n\nQuestion: Samir Brahimi is an Algerian boxer born on 17 May 1990, he won a silver medal at the 2011 All-Africa Games, the 10th All-Africa Games took place between September 3–18, 2011 in Maputo, in which country?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"athlete\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"nationality\": {\n          \"type\": \"string\"\n        },\n        \"birth_date\": {\n          \"type\": \"string\",\n          \"format\": \"date\"\n        },\n        \"sport\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\",\n        \"birth_date\",\n        \"sport\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"event\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"year\": {\n          \"type\": \"integer\"\n        },\n        \"edition\": {\n          \"type\": \"string\"\n        },\n        \"host_city\": {\n          \"type\": \"string\"\n        },\n        \"host_country\": {\n          \"type\": \"string\"\n        },\n        \"start_date\": {\n          \"type\": \"string\",\n          \"format\": \"date\"\n        },\n        \"end_date\": {\n          \"type\": \"string\",\n          \"format\": \"date\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"year\",\n        \"edition\",\n        \"host_city\",\n        \"host_country\",\n        \"start_date\",\n        \"end_date\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"athlete_achievement\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"medal_type\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"medal_type\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"answer\": {\n      \"type\": \"string\"\n    }\n  },\n  \"required\": [\n    \"athlete\",\n    \"event\",\n    \"athlete_achievement\",\n    \"answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "athlete": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "nationality": {
            "type": "string"
          },
          "birth_date": {
            "type": "string",
            "format": "date"
          },
          "sport": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "nationality",
          "birth_date",
          "sport"
        ],
        "additionalProperties": false
      },
      "event": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "year": {
            "type": "integer"
          },
          "edition": {
            "type": "string"
          },
          "host_city": {
            "type": "string"
          },
          "host_country": {
            "type": "string"
          },
          "start_date": {
            "type": "string",
            "format": "date"
          },
          "end_date": {
            "type": "string",
            "format": "date"
          }
        },
        "required": [
          "name",
          "year",
          "edition",
          "host_city",
          "host_country",
          "start_date",
          "end_date"
        ],
        "additionalProperties": false
      },
      "athlete_achievement": {
        "type": "object",
        "properties": {
          "medal_type": {
            "type": "string"
          }
        },
        "required": [
          "medal_type"
        ],
        "additionalProperties": false
      },
      "answer": {
        "type": "string"
      }
    },
    "required": [
      "athlete",
      "event",
      "athlete_achievement",
      "answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
