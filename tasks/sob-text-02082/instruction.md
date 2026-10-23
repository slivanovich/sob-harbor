{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJoanne Clifton: Joanne Kirsty Clifton (born 24 October 1983), also known as Jo, is a British professional dancer, presenter, actress, singer.  born in Waltham, Lincolnshire.  She won the World Ballroom Showdance Championship in 2013 and also won the European Professional Ballroom Championship and World Dancesport Games.  She has been a professional dancer on the BBC TV series \"Strictly Come Dancing\" since 2014, winning the Christmas Special in 2015 with Harry Judd who was series 9 champion and the fourteenth series in 2016 with Ore Oduba.  Also appearing as an expert presenter on \"\" in 2015.\n\nCome Dancing: Come Dancing was a British ballroom dancing competition show that ran on and off on the BBC from 1950 to 1998, becoming one of television's longest-running shows.  Unlike its follow up show \"Strictly Come Dancing\" contestants were not celebrities.\n\nAnton du Beke: Anthony Paul Beke (born 20 July 1966), known professionally as Anton du Beke, is a British ballroom dancer and television presenter, best known as a professional dancer on the BBC One celebrity dancing show \"Strictly Come Dancing\" since the show began in 2004.  In 2009, he presented the UK version of \"Hole in the Wall\", for the BBC, replacing Dale Winton after being a team captain in 2008.\n\nStrictly Come Dancing: It Takes Two: Strictly Come Dancing: It Takes Two, also known as Strictly: It Takes Two or simply It Takes Two, is a British television programme, the companion show to the popular BBC One programme \"Strictly Come Dancing\".  It is broadcast on weeknights during the run of the main show on BBC Two at 6:30 pm.  Claudia Winkleman originally presented the show, however she left in 2011 and now presents the main show.  Since 2011, Zoë Ball has presented the show.\n\nBrendan Cole: Brendan Cole (born 23 April 1976) is a New Zealand ballroom dancer, specialising in Latin American dancing.  He is most famous for appearing as a professional dancer on the BBC One show, \"Strictly Come Dancing\".  From 2005 to 2009, he was a judge on the New Zealand version of the show, \"Dancing with the Stars\".\n\nTess Daly: Helen Elizabeth \"Tess\" Daly (born 27 April 1969) is an English model and television presenter, best known for co-presenting the BBC One celebrity dancing show \"Strictly Come Dancing\" since 2004.\n\nStep Up to the Plate: Step Up to the Plate is a United Kingdom-based television program, produced by Endemol, for the BBC.  It was hosted by Anton du Beke and Loyd Grossman\n\nJanette Manrara: Janette Manrara (born November 16, 1983) is an American professional dancer and choreographer from Miami, Florida.  Originally a Salsa dancer, learning from her Cuban family, she formally studied dance from the age of 19.  Manrara is best known for her appearances on the US series \"So You Think You Can Dance\" and British Ballroom Reality Television competition, \"Strictly Come Dancing\".\n\nDianne Buswell: Dianne Buswell (born 1989) is an Australian ballroom dancer.  She has appeared on \"So You Think You Can Dance Australia\" and was a professional dancer on the Australian version of \"Dancing with the Stars\" in 2015.  Buswell became a professional dancer on \"Strictly Come Dancing\" beginning in 2017.\n\nMatthew Cutler: Matthew David Cutler (born 30 October 1973) is an English dancer and former World Amateur Latin-American champion.  He was a professional dancer on the BBC dancing show, Strictly Come Dancing.\n\nQuestion: what show was hosted by a British ballroom dancer and television presenter, best known as a professional dancer on the BBC One celebrity dancing show \"Strictly Come Dancing\" since the show began in 2004\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"show_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the television show.\"\n    },\n    \"host_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"host_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the host.\"\n        },\n        \"host_profession\": {\n          \"type\": \"string\",\n          \"description\": \"The primary profession of the host.\"\n        },\n        \"best_known_for_show\": {\n          \"type\": \"string\",\n          \"description\": \"The show the host is best known for.\"\n        },\n        \"best_known_for_role\": {\n          \"type\": \"string\",\n          \"description\": \"The role the host is best known for in that show.\"\n        }\n      },\n      \"required\": [\n        \"host_name\",\n        \"host_profession\",\n        \"best_known_for_show\",\n        \"best_known_for_role\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"show_network\": {\n      \"type\": \"string\",\n      \"description\": \"The television network the show was produced for.\"\n    }\n  },\n  \"required\": [\n    \"show_name\",\n    \"host_details\",\n    \"show_network\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "show_name": {
        "type": "string",
        "description": "The name of the television show."
      },
      "host_details": {
        "type": "object",
        "properties": {
          "host_name": {
            "type": "string",
            "description": "The name of the host."
          },
          "host_profession": {
            "type": "string",
            "description": "The primary profession of the host."
          },
          "best_known_for_show": {
            "type": "string",
            "description": "The show the host is best known for."
          },
          "best_known_for_role": {
            "type": "string",
            "description": "The role the host is best known for in that show."
          }
        },
        "required": [
          "host_name",
          "host_profession",
          "best_known_for_show",
          "best_known_for_role"
        ],
        "additionalProperties": false
      },
      "show_network": {
        "type": "string",
        "description": "The television network the show was produced for."
      }
    },
    "required": [
      "show_name",
      "host_details",
      "show_network"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
