{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBattle of Arnemuiden: The Battle of Arnemuiden was a naval battle fought on 23 September 1338 at the start of the Hundred Years' War between England and France.  It was the first naval battle of the Hundred Years' War and the first recorded European naval battle using artillery, as the English ship \"Christopher\" had three cannons and one hand gun.\n\nZuihō-class aircraft carrier: The \"Zuihō\" class (瑞鳳型 ) was a group of two aircraft carriers built for the Imperial Japanese Navy before World War II.  Both ships were originally built as submarine tenders, but were subsequently converted into carriers.  Completed in early 1942, \"Shōhō\" supported the invasion forces in Operation MO, the invasion of Port Moresby, New Guinea, and was sunk by American carrier aircraft on her first combat operation during the Battle of the Coral Sea on 7 May.  \"Shōhō\" was the first Japanese aircraft carrier to be sunk during World War II.  \"Zuihō\" played a secondary role in the Battle of Midway in mid-1942 and did not engage any American aircraft or ships during the battle.  The ship participated in the Guadalcanal Campaign during the rest of 1942.  She was lightly damaged during the Battle of the Santa Cruz Islands during this campaign and covered the evacuation of Japanese forces from the island in early 1943 after repairs.\n\nBattle of Amorgos: The Battle of Amorgos was one of the naval battles of the Lamian War (323–322 BC), fought between the Macedonian navy under Cleitus the White and the Athenian navy under Euetion.  Although few details are known, it was a clear Athenian defeat, although the Athenians seem to have suffered few losses.  Regarded as the decisive naval battle of the war, it signalled the end of Athenian thalassocracy and political independence.\n\nBattle of Jutland: The Battle of Jutland (German: \"Skagerrakschlacht\" , the Battle of Skagerrak) was a naval battle fought by the British Royal Navy's Grand Fleet under Admiral Sir John Jellicoe, against the Imperial German Navy's High Seas Fleet under Vice-Admiral Reinhard Scheer during the First World War.  The battle unfolded in extensive maneuvering and three main engagements (the battlecruiser action, the fleet action and the night action), from 31 May to 1 June 1916, off the North Sea coast of Denmark's Jutland Peninsula.  It was the largest naval battle and the only full-scale clash of battleships in that war.  Jutland was the third fleet action between steel battleships, following the smaller but more decisive battles of the Yellow Sea (1904) and Tsushima (1905) during the Russo-Japanese War.  Jutland was the last major battle in world history fought primarily by battleships.\n\nBattle of Midway: The Battle of Midway was a decisive naval battle in the Pacific Theater of World War II which occurred between 4 and 7 June 1942, only six months after Japan's attack on Pearl Harbor and one month after the Battle of the Coral Sea.  The United States Navy under Admirals Chester Nimitz, Frank Jack Fletcher, and Raymond A. Spruance defeated an attacking fleet of the Imperial Japanese Navy under Admirals Isoroku Yamamoto, Chuichi Nagumo, and Nobutake Kondo near Midway Atoll, inflicting devastating damage on the Japanese fleet that proved irreparable.  Military historian John Keegan called it \"the most stunning and decisive blow in the history of naval warfare.\"\n\nBattle of the Java Sea: The Battle of the Java Sea was a decisive naval battle of the Pacific campaign of World War II.\n\nBattle of Tsushima: The Battle of Tsushima (Russian: Цусимское сражение , \"Tsusimskoye srazheniye\"), also known as the Battle of Tsushima Strait and the Naval Battle of the Sea of Japan (Japanese: 日本海海戦, \"Nihonkai-Kaisen\") in Japan, was a major naval battle fought between Russia and Japan during the Russo-Japanese War.  It was naval history's only decisive sea battle fought by modern steel battleship fleets, and the first naval battle in which wireless telegraphy (radio) played a critically important role.  It has been characterized as the \"dying echo of the old era – for the last time in the history of naval warfare, ships of the line of a beaten fleet surrendered on the high seas\".\n\nPatricio Montojo y Pasarón: Rear Admiral Patricio Montojo y Pasarón (September 7, 1839 – September 30, 1917) was a career Spanish naval officer who commanded the restored Kingdom of Spain's Pacific Squadron based in the Philippines during the Spanish–American War.  Considered to have been a man of high ability and experience, he was given what was regarded as an impossible task of defending the Spanish Philippines with antiquated ships and low supplies against the more formidable U.S. Asiatic Squadron.  Montojo became known for his defeat at the Battle of Manila Bay (1 May 1898) by U.S. Navy Admiral George Dewey, being a decisive naval battle of the war.  After the conflict, the rear admiral was held accountable for the defeat and was court-martialed, but that was later overturned, though Montojo was still discharged from the Spanish Navy.\n\nJapanese aircraft carrier Zuihō: Zuihō (瑞鳳 , \"Auspicious Phoenix\" or \"Fortunate Phoenix\") was a light aircraft carrier of the Imperial Japanese Navy.  Originally laid down as the submarine support ship \"Takasaki\", she was renamed and converted while under construction into an aircraft carrier.  The ship was completed during the first year of World War II and participated in many operations.  \"Zuihō\" played a secondary role in the Battle of Midway in mid-1942 and did not engage any American aircraft or ships during the battle.  The ship participated in the Guadalcanal Campaign during the rest of 1942.  She was lightly damaged during the Battle of the Santa Cruz Islands during this campaign and covered the evacuation of Japanese forces from the island in early 1943 after repairs.\n\nBattle of Buceo: The Battle of Buceo was a decisive naval battle which took place on 14–17 May 1814, during the Argentine War of Independence between an Argentine fleet under William Brown and a Spanish fleet under Admiral Sienna off the coast of Montevideo, in today's Uruguay.\n\nQuestion: What was a decisive naval battle in the Pacifix Theater of WW2 that \"Zuihō\" played a secondary role in?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"battle_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the naval battle.\"\n    },\n    \"is_decisive\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the battle was considered decisive.\"\n    },\n    \"war_theater\": {\n      \"type\": \"string\",\n      \"description\": \"The theater of war where the battle took place.\"\n    },\n    \"ship_involvement\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"ship_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the ship involved.\"\n        },\n        \"role_in_battle\": {\n          \"type\": \"string\",\n          \"description\": \"Description of the ship's role in the battle.\"\n        },\n        \"engaged_enemy\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the ship engaged enemy aircraft or ships during the battle.\"\n        }\n      },\n      \"required\": [\n        \"ship_name\",\n        \"role_in_battle\",\n        \"engaged_enemy\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"battle_name\",\n    \"is_decisive\",\n    \"war_theater\",\n    \"ship_involvement\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "battle_name": {
        "type": "string",
        "description": "The name of the naval battle."
      },
      "is_decisive": {
        "type": "boolean",
        "description": "Indicates if the battle was considered decisive."
      },
      "war_theater": {
        "type": "string",
        "description": "The theater of war where the battle took place."
      },
      "ship_involvement": {
        "type": "object",
        "properties": {
          "ship_name": {
            "type": "string",
            "description": "The name of the ship involved."
          },
          "role_in_battle": {
            "type": "string",
            "description": "Description of the ship's role in the battle."
          },
          "engaged_enemy": {
            "type": "boolean",
            "description": "Indicates if the ship engaged enemy aircraft or ships during the battle."
          }
        },
        "required": [
          "ship_name",
          "role_in_battle",
          "engaged_enemy"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "battle_name",
      "is_decisive",
      "war_theater",
      "ship_involvement"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
