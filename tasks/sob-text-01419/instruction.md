{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAokigahara: Aokigahara (青木ヶ原 ) , also known as the Suicide Forest or Sea of Trees (樹海 , Jukai ) , is a forest on the northwestern flank of Japan's Mount Fuji thriving on 30 square kilometers (12 square miles) of hardened lava laid down by the last major eruption of Mount Fuji in 864 CE.  The western edge of Aokigahara, where there are several caves filled with ice, is a popular destination for tourists and school trips.  Parts of Aokigahara are very dense, and the porous lava absorbs sound, helping to provide visitors with a sense of solitude.\n\nMount Fuji Radar System: The Mount Fuji Radar System is a historic weather radar system located on the summit of Mount Fuji, Japan.  It was completed on August 15, 1964 , and is now recorded on the list of IEEE Milestones in electrical engineering.  When first built, the Mount Fuji Radar System was the world's highest weather radar (elevation 3776 meters), and could observe major weather phenomena, such as destructive typhoons, at a range of more than 800 kilometers.  It was designed by the Japan Meteorological Agency and built by Mitsubishi Electric Corporation.\n\nTenjō-Yama Park Mt. Kachi Kachi Ropeway: The Tenjō-Yama Park Mt. Kachi Kachi Ropeway (天上山公園カチカチ山ロープウェイ , Tenjōyama Kōen Kachikachiyama Rōpuwei ) , officially the Lake Kawaguchi Mt. Tenjō Ropeway (河口湖天上山ロープウェイ , Kawaguchiko Tenjōyama Rōpuwei ) , is a Japanese aerial lift line in Fujikawaguchiko, Yamanashi, operated by Fuji Kyuko.  Opened in 1959, the line climbs Mount Tenjō from the shores of Lake Kawaguchi, one of the Fuji Five Lakes.  The line name comes from \"Kachi-kachi Yama\" (lit.  \"Mt. Kachikachi\"), a folktale which took place on the mountain.  The observatory has a view of the lake, as well as Aokigahara forest, and Mount Fuji.\n\nLake Shōji: Lake Shōji (精進湖 , Shōji-ko ) is the one of the Fuji Five Lakes and located in southern Yamanashi Prefecture near Mount Fuji, Japan.\n\nMount Fuji: Mount Fuji (富士山 , Fujisan , ] ) , located on Honshu Island, is the highest mountain in Japan at 3776.24 m .  An active stratovolcano that last erupted in 1707–08, Mount Fuji lies about 100 km south-west of Tokyo, and can be seen from there on a clear day.  Mount Fuji's exceptionally symmetrical cone, which is snow-capped for about 5 months a year, is a well-known symbol of Japan and it is frequently depicted in art and photographs, as well as visited by sightseers and climbers.\n\nSaiko Lake: Lake Saiko (西湖 , Saiko ) is the one of the Fuji Five Lakes and located in southern Yamanashi Prefecture near Mount Fuji, Japan.\n\nFujisan Station: Fujisan Station (富士山駅 , Fujisan-eki ) is a railway station on the Fujikyuko Line in Fujiyoshida, Yamanashi, Japan, operated by the private railway operator Fuji Kyuko (Fujikyu).  The station is located at an altitude of 809 m .  This is one of the gateway stations to Mount Fuji and Fuji Five Lakes, including Lake Kawaguchi and Lake Yamanaka.\n\nLake Kawaguchi: Lake Kawaguchi (河口湖 , Kawaguchi-ko ) is located in the border Fujikawaguchiko and Minobu, southern Yamanashi Prefecture near Mount Fuji, Japan.  It is the second largest of the Fuji Five Lakes in terms of surface area, and is located at the lowest elevation.  It is situated at an altitude of approximately 800 metres, which accounts for its relatively cool summers and frequently icy winters.  It also has the longest shoreline of any of the Fuji Five Lakes.\n\nLake Motosu: Lake Motosu (本栖湖 , Motosu-ko ) is the westernmost of the Fuji Five Lakes and located in southern Yamanashi Prefecture near Mount Fuji, Japan.\n\nFuji Five Lakes: Fuji Five Lakes (富士五湖 , Fuji-goko ) is the name of the area located at the base of Mount Fuji in the Yamanashi Prefecture of Japan.  It has a population of about 100,000.  and sits approximately 1,000 meters above sea level.  The name Fuji Five Lakes comes from the fact that there are five lakes formed by previous eruptions of Mount Fuji.  The principal city in the region, Fujiyoshida, has a population of roughly 54,000 and is particularly famous for its udon noodles.  Another point of interest is Aokigahara Jukai Forest.  The Fuji Five Lakes was selected by the \"Tokyo Nichi Nichi Shimbun\" and \"Osaka Mainichi Shimbun\" as one of the Twenty-Five Winning Sites of Japan in 1927.\n\nQuestion: Fuji Five Lakes (富士五湖 , Fuji-goko ) is the name of the area located at the base of Mount Fuji in the Yamanashi Prefecture of Japan, a point of interest is Aokigahara Jukai Forest, Aokigahara (青木ヶ原 ) , also known as the Suicide Forest or Sea of Tree, is a forest on the northwestern flank ,of Japan's Mount Fuji thriving on 30 square kilometers (12 square miles) of hardened lava laid down by the last major eruption of Mount Fuji in what year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"forest_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the forest.\"\n    },\n    \"forest_location_description\": {\n      \"type\": \"string\",\n      \"description\": \"A description of the forest's location relative to Mount Fuji.\"\n    },\n    \"lava_source_mountain\": {\n      \"type\": \"string\",\n      \"description\": \"The mountain from which the lava originated.\"\n    },\n    \"lava_formation_event\": {\n      \"type\": \"string\",\n      \"description\": \"The event that laid down the hardened lava.\"\n    },\n    \"eruption_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year of the last major eruption that laid down the lava.\"\n    }\n  },\n  \"required\": [\n    \"forest_name\",\n    \"forest_location_description\",\n    \"lava_source_mountain\",\n    \"lava_formation_event\",\n    \"eruption_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "forest_name": {
        "type": "string",
        "description": "The name of the forest."
      },
      "forest_location_description": {
        "type": "string",
        "description": "A description of the forest's location relative to Mount Fuji."
      },
      "lava_source_mountain": {
        "type": "string",
        "description": "The mountain from which the lava originated."
      },
      "lava_formation_event": {
        "type": "string",
        "description": "The event that laid down the hardened lava."
      },
      "eruption_year": {
        "type": "integer",
        "description": "The year of the last major eruption that laid down the lava."
      }
    },
    "required": [
      "forest_name",
      "forest_location_description",
      "lava_source_mountain",
      "lava_formation_event",
      "eruption_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
