{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRisley Park Lanx: The Risley Park Lanx is a large Roman silver dish (or lanx) that was discovered in 1729 in Risley Park, Derbyshire.  In Roman times, a lanx was generally a large serving platter, about 15 by 20 inches in size.  Particularly ornamented ones were used to make offerings or sacrifices.  The inscription on the Risley Park Lanx suggests it was used as a \"church plate\".\n\nHildesheim Treasure: The Hildesheim Treasure, unearthed on October 17, 1868 in Hildesheim, Germany, is the largest collection of Roman silver found outside imperial frontiers.  Most of it can be dated to the 1st century AD.  The trove consists of about seventy exquisitely crafted solid silver vessels for eating and drinking and is now kept in the Antikensammlung Berlin (Altes Museum).  It is generally believed that the treasure was the table service of a Roman commander, perhaps Publius Quinctilius Varus, who was militarily active in Germania.  However, others also suggest that the treasure may have been war spoils rather than a table service.\n\nMildenhall Treasure: The Mildenhall Treasure is a large hoard of masterpieces of Roman silver tableware from the 4th century AD, and by far the most valuable Roman objects artistically and by weight of bullion in Britain.  It was found at West Row, near Mildenhall, Suffolk.  It consists of over thirty items and includes the Great Dish weighing over 8kg alone.\n\nCanadian Museum of History: The Canadian Museum of History (French: \"Musée canadien de l’histoire\" , formerly the Canadian Museum of Civilization) is Canada's national museum of human history.  It is located in the Hull area of Gatineau, Quebec, directly across the Ottawa River from Parliament Hill in Ottawa, Ontario.  The museum's primary purpose is to collect, study, preserve, and present material objects that illuminate the human history of Canada and the cultural diversity of its people.  In October 2012, it was announced that the museum would be renamed from the Canadian Museum of Civilization to the Canadian Museum of History, with an increased focus on Canadian history and people.  The name change became official when the \"Canadian Museum of History Act\" received Royal Assent on December 12, 2013.  Changes to the museum's visual identity were implemented gradually over the course of the following months.\n\nLiberty Osaka: Liberty Osaka (Osaka Human Rights Museum) is situated in Naniwa-ku, a ward in south Osaka City.  As the first general museum dedicated to human rights in Japan, the focus of its permanent exhibits is the history of the struggle against discrimination experienced by the nation's minority ethnic groups; the Burakumin, the Ainu of Hokkaidō, the Ryukyuans of Okinawa and Japan's communities of Korean and Chinese descent.  There are also exhibits dedicated to discrimination issues affecting women, lesbians, gays, bisexuals and transgender people, the physically challenged and the survivors of the atomic bombing of Hiroshima and Nagasaki (the Hibakusha).  Founded in December 1985 to document the history of the Osaka human rights movement, it was relaunched in December 1995 as the Osaka Jinken Hakubutsu-kan (Human Rights Museum).\n\nCorbridge Lanx: The Corbridge Lanx is the name of a Roman silver dish found near Corbridge, northern England in 1735.  Once part of a large Roman treasure, only the silver lanx remains from the original find.  The British Museum eventually purchased it in 1993.\n\nHoxne Hoard: The Hoxne Hoard ( ) is the largest hoard of late Roman silver and gold discovered in Britain, and the largest collection of gold and silver coins of the fourth and fifth century found anywhere within the Roman Empire.  Found by Eric Lawes, a metal detectorist in the village of Hoxne in Suffolk, England, on 16 November 1992, the hoard consists of 14,865 Roman gold, silver and bronze coins from the late fourth and early fifth centuries, and approximately 200 items of silver tableware and gold jewellery.  The objects are now in the British Museum in London, where the most important pieces and a selection of the rest are on permanent display.  In 1993, the Treasure Valuation Committee valued the hoard at £1.75 million (today £).\n\nCanterbury Roman Museum: The Canterbury Roman Museum in Canterbury, Kent, houses a Roman pavement which is a scheduled monument, in the remains of a Roman courtyard house which itself is a grade I listed building.  The pavement was discovered after World War II bombing, and has been open to the public since 1946.  The museum was established in 1961, but it has been under threat of closure as of 2009.  It houses many excavated artifacts from Roman Canterbury, including the important late Roman silver hoard known as the Canterbury Treasure, together with reconstructions of the Roman town.\n\nBritish Museum: The British Museum, located in the Bloomsbury area of London, United Kingdom, is a public institution dedicated to human history, art and culture.  Its permanent collection, numbering some 8 million works, is among the largest and most comprehensive in existence and originates from all continents, illustrating and documenting the story of human culture from its beginnings to the present.\n\nWater Newton Treasure: The Water Newton Treasure is a hoard of fourth-century Roman silver, discovered near the Roman town of \"Durobrivae\" at Water Newton in the English county of Cambridgeshire.  The hoard consisted of 27 silver items and one small gold plaque.  Because of inscriptions found on some of the pieces in the collection it has been suggested that they may have been used in a local church, and they therefore comprise the earliest probable group of Christian liturgical silver yet found in the Roman Empire.\n\nQuestion: What Bloomsbury museum dedicated to human history has a Roman silver dish found in 1735?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"museum_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the museum.\"\n    },\n    \"location\": {\n      \"type\": \"string\",\n      \"description\": \"The specific area or city where the museum is located.\"\n    },\n    \"dedication\": {\n      \"type\": \"string\",\n      \"description\": \"The primary focus or dedication of the museum.\"\n    },\n    \"roman_silver_dish\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"dish_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the Roman silver dish.\"\n        },\n        \"discovery_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the Roman silver dish was discovered.\"\n        }\n      },\n      \"required\": [\n        \"dish_name\",\n        \"discovery_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"museum_name\",\n    \"location\",\n    \"dedication\",\n    \"roman_silver_dish\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "museum_name": {
        "type": "string",
        "description": "The name of the museum."
      },
      "location": {
        "type": "string",
        "description": "The specific area or city where the museum is located."
      },
      "dedication": {
        "type": "string",
        "description": "The primary focus or dedication of the museum."
      },
      "roman_silver_dish": {
        "type": "object",
        "properties": {
          "dish_name": {
            "type": "string",
            "description": "The name of the Roman silver dish."
          },
          "discovery_year": {
            "type": "integer",
            "description": "The year the Roman silver dish was discovered."
          }
        },
        "required": [
          "dish_name",
          "discovery_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "museum_name",
      "location",
      "dedication",
      "roman_silver_dish"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
