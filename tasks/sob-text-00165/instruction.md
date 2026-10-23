{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nVancouveria: Vancouveria ( ) is a small group of plants belonging to the barberry family described as a genus in 1834.  The three plants in this genus are known generally as inside-out flowers, and they are endemic to the West Coast of the United States.  The genus was named after George Vancouver, English navigator and explorer.\n\nWaragi: Waragi (pronounced ] , also known as enguli) is a generic term in Uganda for domestic distilled beverages. Waragi is also given different names, depending on region of origin, the distillation process, or both.  Waragi is known as a form of homemade Gin.  It is commonly called Waragi in the central area of Uganda but in the West it is sometimes called \"Kasese\".  In northern Uganda it is more commonly called \"Lira Lira.\"  The manufacturing of Waragi does not vary too much in the different parts of Uganda - only the ingredients are slightly different.  A commercial brand called Uganda Waragi is produced and marketed by East African Breweries Limited.\n\nMixe languages: The Mixe languages are languages of the Mixean branch of the Mixe–Zoquean language family indigenous to southern Mexico.  According to a 1995 classification, there are seven of them (including one that is extinct).  The four that are spoken in Oaxaca are commonly called Mixe while their two relatives spoken in Veracruz are commonly called \"Popoluca\", but sometimes also Mixe (these are \"Oluta Popoluca\" or \"Olutec Mixe\" and \"Sayula Popoluca\" or \"Sayultec Mixe\").  This article is about the Oaxaca Mixe languages, which their speakers call \"Ayuujk\", \"Ayüük\" or \"Ayuhk\".\n\n29er (bicycle): 29ers or two-niners are mountain bikes and hybrid bikes that are built to use 700c or 622 mm ISO (inside rim diameter) wheels, commonly called 29\" wheels.  Most mountain bikes use ISO 559 mm wheels, commonly called 26\" wheels.  The ISO 622 mm wheel is typically also used for road-racing, trekking, cyclo-cross, touring and hybrid bicycles.\n\nInterexchange carrier: An Interexchange Carrier (IXC) is a U.S. legal and regulatory term for a telecommunications company, commonly called a long-distance telephone company, such as MCI (before its absorption by Verizon), Sprint and the former AT&T Corporation (before its merger with SBC in 2005).  In the United States, it is defined as any carrier that provides inter-LATA communication, where a LATA is a local access and transport area.  From the telephone user's point of view, the long-distance company does not handle calls that do not have additional tolls.  Calls made across phone circuits within the local geographic area covered by one local network are handled only by that one LATA, commonly called a 'local telephone exchange.'  Local calls are usually defined by connections made without additional charge whether the connected call is in the same LATA or connects to another LATA with no charge.  In the United States intraLATA usually refers to rated or 'Toll' calls between LATA within state boundaries, as opposed to interstate, or calls between LATA in different states.\n\nCandidiasis: Candidiasis is a fungal infection due to any type of \"Candida\" (a type of yeast).  When it affects the mouth, it is commonly called thrush.  Signs and symptoms include white patches on the tongue or other areas of the mouth and throat.  Other symptoms may include soreness and problems swallowing.  When it affects the vagina, it is commonly called a yeast infection.  Signs and symptoms include genital itching, burning, and sometimes a white \"cottage cheese-like\" discharge from the vagina.  Less commonly the penis may be affected, resulting in itchiness.  Very rarely, the infection may become invasive, spreading to other parts of the body.  This may result in fevers along with other symptoms depending on the parts involved.\n\nMagnetic cartridge: A magnetic cartridge, more commonly called a phonograph cartridge or phono cartridge or (colloquially) a pickup, is an electromechanical transducer used in the playback of analog sound recordings called records on a record player, now commonly called a turntable because of its most prominent component but formally known as a phonograph in the US and a gramophone in the UK.\n\nBasselinia: Basselinia is a genus of flowering plant in the Arecaceae family.  The entire genus is endemic to the Island of New Caledonia in the Pacific.  In some (but not all) molecular phylogenetic analyses, \"Hedyscepe\" from Lord Howe Island is nested in \"Basselinia\".\n\nSato (beverage): Sato (Thai: สาโท ,  ] , rtgs: \"satho\" ) is a traditional northeastern Thailand (Isan) beer style that has been made for centuries from starchy glutinous or sticky rice by growers in that region.  Just as other regional varieties made not from grapes but cereal are commonly called wine rather than beer, \"sato\" is commonly called Thai rice wine.  When brewed in little brown jugs called \"hai\" (ไห ), it is called lao hai (เหล้าไห ) or lao u (เหล้าอุ ).\n\nRanks of the Bangladesh Army: The Bangladesh Army (Bengali: বাংলাদেশ সেনাবাহিনী ) is the land forces branch of the Military of Bangladesh.  The rank structure of the Bangladesh Army is divided in two main parts: commissioned officers/officers and soldiers, officers have two categories of ranks one is known simply as officers and the other category is generals or general officers, on the other hand soldiers have three categories of ranks.  Junior Commissioned Officers (JCOs) and NCOs are enlisted personnel, not officers.  From the rank of Second Lieutenant to the highest rank of General all are commissioned officers.  Commissioned Officers are regarded as 1st class Bangladesh-government officer.  Men and women can receive commission from BMA, Bhatiary.  'Sainik' (Bengali: সৈনিক ) is a Bengali word, it means Soldier in English, the rank \"Sainik\" is equivalent to 'Sepoy' or 'Jawan' of Pakistan Army and Indian Army.  From a \"Sainik\" a person is promoted to Lance Corporal, and from this rank he/she gets NCO (Non Commissioned Officer) status.  From the rank of 'Warrant Officer' persons are called JCO.  From Major-General to General, officers of these rank holders are commonly called 'generals' and Brigadier-generals are known as Brigadiers in contraction, the suffix 'general' was added in 2001.  2nd Lieutenant, Lieutenants and Captains are considered junior officers (not junior commissioned officer).  Major and Lieutenant-colonels (commonly called as colonels) are mid-ranking officers.  Colonel and above are considered as senior officers.  The insignias of Major-general and Lieutenant-general and full-general were changed in 2013, previously Major-General insignia was a pip over a crossed sword and baton and Lieutenant-General was 'shapla' (water lily) over a crossed sword and baton and full-general had a 'shapla' over a pip over crossed sword and baton.\n\nQuestion: Basselinia and Vancouveria, are commonly called what?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"entities_examined\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\"\n          },\n          \"type_from_context\": {\n            \"type\": \"string\"\n          },\n          \"specific_common_name\": {\n            \"type\": \"string\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"type_from_context\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"number_of_entities_examined\": {\n      \"type\": \"integer\"\n    },\n    \"general_common_classification\": {\n      \"type\": \"string\"\n    }\n  },\n  \"required\": [\n    \"entities_examined\",\n    \"number_of_entities_examined\",\n    \"general_common_classification\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "entities_examined": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "type_from_context": {
              "type": "string"
            },
            "specific_common_name": {
              "type": "string"
            }
          },
          "required": [
            "name",
            "type_from_context"
          ],
          "additionalProperties": false
        }
      },
      "number_of_entities_examined": {
        "type": "integer"
      },
      "general_common_classification": {
        "type": "string"
      }
    },
    "required": [
      "entities_examined",
      "number_of_entities_examined",
      "general_common_classification"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
