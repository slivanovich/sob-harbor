{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nType 92 heavy machine gun: The Type 92 Heavy Machine Gun (九二式重機関銃 , Kyūni-shiki jū-kikanjū ) entered service in 1932 and was the standard Japanese heavy machine gun used during World War II.  It was used extensively by the Imperial Japanese Army and Collaborationist Chinese forces.  Captured weapons were also used extensively by Chinese National Revolutionary Army troops against the Japanese during World War II, and the Korean People's Army against the United Nations forces during the Korean War.  The Type 92 refers to the Japanese Imperial year 2592 – 1932 in the Gregorian calendar – in which the gun entered service.  Designed by Kijiro Nambu and built by Hino Motors and Hitachi, total production was about 45,000 guns.\n\nM1917 Browning machine gun: The M1917 Browning machine gun is a heavy machine gun used by the United States armed forces in World War I, World War II, Korea, and to a limited extent in Vietnam; it has also been used by other nations.  It was a crew served, belt-fed, water-cooled machine gun that served alongside the much lighter air-cooled Browning M1919.  It was used at the battalion level, and often mounted on vehicles (such as a jeep).  There were two main iterations of it: the M1917, which was used in World War I; and the M1917A1; which was used thereafter.  The M1917, which was used on some aircraft as well as in a ground role, had a cyclic rate of 450 rounds per minute; the M1917A1 had a cyclic rate of 450 to 600 rounds per minute.\n\nBreda Model 1931 machine gun: The Breda Model 31 was a widely used Italian heavy machine gun produced by Società Italiana Ernesto Breda and used by the Italian Navy and Italian Army during World War II.  At sea it was employed as a light anti-aircraft gun, while on land it was mounted on armored command vehicles where it was used as a heavy machine gun.  After World War II it remained in use aboard the patrol boats of the Guardia di Finanza.\n\n1939 Infantry Regiment (Poland): The Polish Infantry Regiment during World War 2 (in Polish Pulk Piechoty) comprised on average some 2,900 men and 60 officers organised around 3 rifle battalions armed with the Mauser 98k 7.92mm bolt-action rifle.  Each 19-man squad was also issued the RKM wz.28 light machine gun.  Other regimental weapons included the Polish version of the French Model 1897 75-mm field gun, the Wz.  35 anti-tank rifle, the Ckm wz.30 heavy machine gun, the wz.31 81 mm mortar, and the wz.36 46mm light mortar/grenade launcher.\n\nType 97 heavy tank machine gun: The Type 97 heavy tank machine gun (九七式車載重機関銃 , Kyū-nana-shiki shasai jū-kikanjū ) was the standard machine gun used in tanks and armored vehicles of the Imperial Japanese Army during World War II, a heavy machine gun by infantry forces, This weapon was not related to the Type 97 aircraft machine gun used in several Japanese Navy aircraft including the A6M Zero.\n\nM2 Browning: The M2 Machine Gun or Browning .50 Caliber Machine Gun is a heavy machine gun designed toward the end of World War I by John Browning.  Its design is similar to Browning's earlier M1919 Browning machine gun, which was chambered for the .30-06 cartridge.  The M2 uses the much larger and much more powerful .50 BMG cartridge, which was developed alongside and takes its name from the gun itself (BMG standing for \"Browning Machine Gun\").  It has been referred to as \"Ma Deuce\", in reference to its M2 nomenclature.  The design has had many specific designations; the official designation for the current infantry type is Browning Machine Gun, Cal.  .50, M2, HB, Flexible.  It is effective against infantry, unarmored or lightly armored vehicles and boats, light fortifications and low-flying aircraft.  The M2 has been produced longer than any other machine gun.\n\nPM M1910: The PM M1910 (Russian: Пулемёт Максима образца 1910 года, \"Pulemyot Maxima obraztsa 1910 goda\" or \"Maxim's machine gun model 1910\") was a heavy machine gun used by the Imperial Russian Army during World War I and the Red Army during Russian Civil War and World War II.  Later, the gun saw service in the Korean War and the Vietnam War, and some have been spotted in the War in Donbass.\n\nKarabin maszynowy obserwatora wz.37: The karabin maszynowy obserwatora wz.37 (Polish for \"observers machine gun\") is a Polish version of the Browning wz.1928.  It was a flexible machine gun used in the some Polish airplanes in the beginning of World War II.\n\nType 1 heavy machine gun: The Type 1 Heavy Machine Gun (一式重機関銃 , Iti-shiki juu-kikanjuu ) was a heavy machine gun used by the Imperial Japanese Army during the Second World War starting from 1941.\n\nCkm wz. 30: Ckm wz.  30 (short for \"ciężki karabin maszynowy wz.  30\"; \"heavy machine gun 1930 Pattern\") is a Polish-made clone of the American Browning M1917 heavy machine gun.  Produced with various modifications such as greater caliber, longer barrel and adjustable sighting device, it was an improved although unlicensed copy of its predecessor, and was the standard machine gun of the Polish Army since 1931.\n\nQuestion: The Ckm wz. 30 was a Polish-made clone of what American heavy machine gun used by the United States in World War I, World War II, Korea and to a limited extent in Vietnam?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"cloned_machine_gun_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the American heavy machine gun that was cloned.\"\n    },\n    \"cloned_machine_gun_conflicts_used_in\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"List of conflicts in which the cloned American machine gun was used by the United States.\"\n    },\n    \"cloning_machine_gun_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the machine gun that was a clone.\"\n        },\n        \"country_of_origin\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the cloning machine gun was made.\"\n        },\n        \"relationship_type\": {\n          \"type\": \"string\",\n          \"description\": \"Describes the relationship to the original machine gun (e.g., clone, copy).\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"country_of_origin\",\n        \"relationship_type\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"cloned_machine_gun_name\",\n    \"cloned_machine_gun_conflicts_used_in\",\n    \"cloning_machine_gun_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "cloned_machine_gun_name": {
        "type": "string",
        "description": "The name of the American heavy machine gun that was cloned."
      },
      "cloned_machine_gun_conflicts_used_in": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "List of conflicts in which the cloned American machine gun was used by the United States."
      },
      "cloning_machine_gun_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the machine gun that was a clone."
          },
          "country_of_origin": {
            "type": "string",
            "description": "The country where the cloning machine gun was made."
          },
          "relationship_type": {
            "type": "string",
            "description": "Describes the relationship to the original machine gun (e.g., clone, copy)."
          }
        },
        "required": [
          "name",
          "country_of_origin",
          "relationship_type"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "cloned_machine_gun_name",
      "cloned_machine_gun_conflicts_used_in",
      "cloning_machine_gun_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
