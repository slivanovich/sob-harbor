{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSkrad (castle): Skrad (] is a medieval ruined castle located on the right bank of the Korana river in modern Karlovac County, Croatia.  It overlooks the river gorge from a small hill at the end of a larger hill, whose height above sea level is 430 m.  It is roughly triangular in plan, and once included 6 towers, a church, and a number buildings, though today very little rises above grass-level.  It was one of the larger castles in the region, though not quite as large as Modruše or Cetin.\n\nCaisteal Maol: Caisteal Maol (Gaelic: \"Caisteal\", 'Castle', \"Maol\", 'bare') is a ruined castle located near the harbour of the village of Kyleakin, Isle of Skye, Scotland.  It is also known as Castle Moil, Castle Maol, Dun Akyn, Dunakin Castle Dun Haakon and Castle Dunakin.\n\nSheriff of Lorn: The Sheriff of Lorn/Lorne was historically the royal official responsible for enforcing law and order in Lorne, Scotland and bringing criminals to justice.  The sheriffdom was created in 1293 by King John of Scotland in an effort to maintain peace in the western reaches of his realm.  Dunollie Castle was the seat of the sheriff.\n\nCastlelost Castle: Castlelost Castle (Irish: \"Caisleán Loiste\") is a ruined castle located just north of Rochfortbridge in County Westmeath, Ireland.  The castle itself dates back to the Norman invasion of Ireland.  The only visible features still on the site are the ruined tower house as well as a small mote.\n\nDunollie Castle: Dunollie Castle (Scottish Gaelic: Dùn Ollaigh) is a small ruined castle located on a hill north of the town of Oban, on the west coast of Scotland in Argyll.  The site enjoys views over towards the island of Kerrera and a view of the town, harbour, and outlying isles.  The castle is open to the public as part of the Dunollie Museum, Castle and Grounds.\n\nFalkenstein Castle (Gerstetten): Falkenstein Castle (German: \"Burg Falkenstein\" ) is a ruined castle located near Dettingen am Albuch, a borough of Gerstetten, in Heidenheim district of Baden-Württemberg in Germany.  The castle is one of at least 16 castles known as Falkenstein in Germany, and is therefore called Falkenstein (Gerstetten) to clarify which castle is meant.  The ruins of the castle are open to the public and require a walk of less than an hour to visit.\n\nAchalm Castle: Achalm Castle is a ruined castle located above the towns of Reutlingen and Pfullingen in Baden-Württemberg, Germany.  Situated on the top of a hill at the edge of the Swabian Alb the ruins of the 11th-century castle are topped by a look-out tower from 1838.\n\nAkçakoca: Akçakoca is both a town and district of Düzce Province, in the Black Sea region of Turkey, located about 200 km east of Istanbul.  The town was named after a Turkish chieftain of the 14th century CE who captured the area for the Ottoman Empire, and sports a statue in his honor.  The town features a modern mosque of unusual design.  Tourist attractions include beaches and a small ruined castle.  It is the regional center of hazelnut cultivation.  The mayor is Cüneyt Yemenici (Ak Parti).\n\nDunoon Castle: Dunoon Castle is a ruined castle located at Dunoon on the Cowal peninsula in Argyll and Bute, Scotland.  The castle sat upon a cone-shaped hill of about 80 feet high, a volcanic plug.  Very little remains of the castle's structure today.\n\nBurt Castle: Burt Castle is a ruined castle located close to Newtowncunningham and Burt, County Donegal, Ireland.  Historically it was sometimes spelt as Birt Castle.  It is also known by the name O'Doherty's Castle, and should not be mistaken for O'Doherty's Castle near Buncrana.\n\nQuestion: The seat of the sheriff of Lorn was a small ruined castle located on a hill north of the town of what?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"sheriffdom_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the sheriffdom.\"\n    },\n    \"castle_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the castle that was the seat of the sheriff.\"\n    },\n    \"castle_state\": {\n      \"type\": \"string\",\n      \"description\": \"The current state of the castle (e.g., ruined).\"\n    },\n    \"location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"town_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the town the castle is located north of.\"\n        },\n        \"direction_from_town\": {\n          \"type\": \"string\",\n          \"description\": \"The direction of the castle relative to the town.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the castle is located.\"\n        },\n        \"region\": {\n          \"type\": \"string\",\n          \"description\": \"The region or county where the castle is located.\"\n        }\n      },\n      \"required\": [\n        \"town_name\",\n        \"direction_from_town\",\n        \"country\",\n        \"region\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"sheriffdom_name\",\n    \"castle_name\",\n    \"castle_state\",\n    \"location\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "sheriffdom_name": {
        "type": "string",
        "description": "The name of the sheriffdom."
      },
      "castle_name": {
        "type": "string",
        "description": "The name of the castle that was the seat of the sheriff."
      },
      "castle_state": {
        "type": "string",
        "description": "The current state of the castle (e.g., ruined)."
      },
      "location": {
        "type": "object",
        "properties": {
          "town_name": {
            "type": "string",
            "description": "The name of the town the castle is located north of."
          },
          "direction_from_town": {
            "type": "string",
            "description": "The direction of the castle relative to the town."
          },
          "country": {
            "type": "string",
            "description": "The country where the castle is located."
          },
          "region": {
            "type": "string",
            "description": "The region or county where the castle is located."
          }
        },
        "required": [
          "town_name",
          "direction_from_town",
          "country",
          "region"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "sheriffdom_name",
      "castle_name",
      "castle_state",
      "location"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
