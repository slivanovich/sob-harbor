{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nKocher Viaduct: On the Kocher Viaduct (German: \"Kochertalbrücke\" ) near Schwäbisch Hall in Germany the Autobahn 6 crosses the Kocher valley between Heilbronn and Nuremberg.  With its maximum height of 185m above the valley bottom, it is the highest viaduct in Germany, and was also the bridge with the tallest pillars in the world before the Millau Viaduct, France was completed in 2004.\n\nMillau Viaduct: The Millau Viaduct (French: \"le Viaduc de Millau\" , ] ) is a cable-stayed bridge that spans the gorge valley of the River Tarn near Millau in southern France.  It is the tallest bridge in the world, with one mast's summit at 343.0 m above the base of the structure.  In a Franco-British partnership, it was designed by the English architect Sir Norman Foster and French structural engineer Dr Michel Virlogeux, and as of 2017 it is the twenty-second highest bridge deck in the world, being 270 m between the road deck and the ground below.\n\nRio Grande Gorge Bridge: The Rio Grande Gorge Bridge, locally known as the \"Gorge Bridge\" and the \"High Bridge\", is a steel deck arch bridge across the Rio Grande Gorge 10 mi northwest of Taos, New Mexico, United States.  At 565 ft above the Rio Grande, it is the seventh highest bridge in the United States and 82nd highest bridge in the world.\n\nTable bridge: A table bridge is a moveable bridge in which the deck moves along the vertical axis.  Hydraulic pillars under the bridge raise the bridge deck to allow barge traffic to pass beneath it.  In contrast to a lift bridge, where the deck is pulled upwards along towers, the deck of a table bridge is pushed upwards by otherwise hidden pillars.  The name originates from the fact that when open it resembles a table.\n\nSfalassà Viaduct: Sfalassà Viaduct is a 254 metre high viaduct near Bagnara Calabra, Calabria, Italy.  The bridge is located on Autostrada A2 Salerno-Reggio Calabria Motorway and has a main span of 376 metres.  It is the highest and longest span frame bridge in the world and as of 2012 it is among the 30 highest bridges of any type.  It is the second highest bridge in Italy after the Italia Viaduct.  The Sfalassà Viaduct won the CECM European award in the 1970s.\n\nRoyal Gorge Bridge: The Royal Gorge Bridge is a tourist attraction near Cañon City, Colorado within \"Royal Gorge Bridge & Park\", a 360 acre amusement park located along the edge of the Royal Gorge around both ends of the bridge.  The bridge crosses the gorge 955 ft above the Arkansas River and held the record of highest bridge in the world from 1929 until 2001 when it was surpassed by the Liuguanghe Bridge in China.  The Royal Gorge Bridge maintained the title of the world's highest \"suspension\" bridge until the Beipan River Guanxing Highway Bridge was completed in 2003, also in China.  The bridge remains the highest bridge in the United States and was among the ten highest bridges in the world until 2012.\n\nList of tallest bridges: The list of the world's tallest bridges ranks bridges by the height of their structure.  The structural height of a bridge is the maximum vertical distance from the uppermost point of a bridge, such as the top of a bridge tower in a suspension bridge, down to the lowest visible point of a bridge, where its piers emerge from the surface of the ground or water.  Structural height should not be confused with deck height, which measures the maximum vertical drop distance from the bridge deck (the road bed of a bridge) down to the ground or water surface beneath the bridge span.  A separate list of the world's highest bridges ranks bridges by deck height.\n\nList of highest bridges: This list of the world's highest bridges ranks bridges by deck height.  The deck height of a bridge is the maximum vertical drop distance from the bridge deck (the road, rail or other transport bed of a bridge) down to the ground or water surface beneath the bridge span.  Deck height should not be confused with structural height, which measures the maximum vertical distance from the uppermost point of a bridge (\"e.g. top of the bridge tower\") down to the lowest visible point of a bridge, where its piers emerge from the surface of the ground, foundation or water.  A separate list of the world's tallest bridges ranks bridges by structural height.\n\nSimple suspension bridge: A simple suspension bridge (also rope bridge, swing bridge (in New Zealand), suspended bridge, hanging bridge and catenary bridge) is a primitive type of bridge that is supported entirely from anchors at either end and has no towers or piers.  However, it may have saddles.  In such bridges, the deck of the bridge follows the downward and upward arc of the load-bearing cables, with additional light ropes at a higher level used to form a handrail.  Alternatively, stout handrail cables supported on short piers at each end may be the primary load-bearing element, with the deck suspended below.  Suspended well from two high locations over a river or canyon, simple suspension bridges follow a shallow downward catenary arc and are not suited for modern roads and railroads.  Owing to practical limitation in the grade (i.e. the deck being an arc, not flat) and the response to dynamic loads of the bridge deck, this type is quite restricted in its load-carrying capacity relative to its span.  This type of bridge is considered the most efficient and sustainable design in developing countries, however, especially for river crossings that lie in non-floodplain topography such as gorges.\n\nItalia Viaduct: Italia Viaduct is a 260 m viaduct near Laino Borgo, Calabria, Italy.  It is the highest bridge in Italy, and was the second highest bridge in the world when it opened in 1974.  s of 2017 , it is among the thirty highest bridges in the world.  The bridge is located on Autostrada A2 Salerno-Reggio Calabria Motorway between Laino Borgo and Mormanno and crosses the Lao River Gorge.\n\nQuestion: What is as of 2017 the twenty-second highest bridge deck in the world, and beat the Kocher Viaduct for having the tallest pillars in the world?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"bridge_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the bridge that meets the criteria.\"\n    },\n    \"deck_height_information\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"rank_as_of_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The bridge's rank by deck height in the specified year.\"\n        },\n        \"year_of_ranking\": {\n          \"type\": \"integer\",\n          \"description\": \"The year for which the deck height ranking is valid.\"\n        },\n        \"deck_height_meters\": {\n          \"type\": \"integer\",\n          \"description\": \"The height of the bridge deck above the ground in meters.\"\n        }\n      },\n      \"required\": [\n        \"rank_as_of_year\",\n        \"year_of_ranking\",\n        \"deck_height_meters\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"pillar_height_record_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"record_achieved\": {\n          \"type\": \"string\",\n          \"description\": \"The specific record achieved by the bridge regarding its pillars.\"\n        },\n        \"previous_record_holder\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the bridge that previously held the pillar height record.\"\n        },\n        \"year_record_achieved\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the bridge achieved the pillar height record.\"\n        }\n      },\n      \"required\": [\n        \"record_achieved\",\n        \"previous_record_holder\",\n        \"year_record_achieved\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"bridge_name\",\n    \"deck_height_information\",\n    \"pillar_height_record_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "bridge_name": {
        "type": "string",
        "description": "The name of the bridge that meets the criteria."
      },
      "deck_height_information": {
        "type": "object",
        "properties": {
          "rank_as_of_year": {
            "type": "integer",
            "description": "The bridge's rank by deck height in the specified year."
          },
          "year_of_ranking": {
            "type": "integer",
            "description": "The year for which the deck height ranking is valid."
          },
          "deck_height_meters": {
            "type": "integer",
            "description": "The height of the bridge deck above the ground in meters."
          }
        },
        "required": [
          "rank_as_of_year",
          "year_of_ranking",
          "deck_height_meters"
        ],
        "additionalProperties": false
      },
      "pillar_height_record_details": {
        "type": "object",
        "properties": {
          "record_achieved": {
            "type": "string",
            "description": "The specific record achieved by the bridge regarding its pillars."
          },
          "previous_record_holder": {
            "type": "string",
            "description": "The name of the bridge that previously held the pillar height record."
          },
          "year_record_achieved": {
            "type": "integer",
            "description": "The year the bridge achieved the pillar height record."
          }
        },
        "required": [
          "record_achieved",
          "previous_record_holder",
          "year_record_achieved"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "bridge_name",
      "deck_height_information",
      "pillar_height_record_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
