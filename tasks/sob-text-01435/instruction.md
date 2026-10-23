{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nNasr ad-Din (Lamtuna): Imam Nasr ad-Din was a Lamtuna Berber religious and military leader, who from 1644 to 1674 led an alliance of Sanhadja Berber tribes in an attempt to repulse the Maqil Arabs then entering their areas of the western Sahara desert (mainly today's Mauritania, southern Morocco and Western Sahara).  The conflict, the Char Bouba war (or 30-years war) was eventually lost by the Berber tribes, and they were reduced to subordinate roles in the elaborate tribal hierarchy that was then developed by the Arabo-Berber Moorish people that resulted from the fusion between indigenous and immigrant peoples.\n\nOuargla: Ouargla (Berber: Wargren or Wargla, Arabic: ورجلان، ورقلة‎ ‎ , old Berber name: Wareglan) is the capital city of Ouargla Province in the Sahara Desert in southern Algeria.  It has a flourishing petroleum industry and hosts one of Algeria's universities, the University of Ouargla.  The commune of Ouargla had a population of 133,024 in the 2008 census, up from 112,339 in 1998, and an annual population growth rate of 1.7%.  However, including the commune of Rouissat, found in Ouargla's urban area, gives a total population of 191,136.\n\nMurzuq Desert: The Murzuq Desert, Idehan Murzuq, Idhan Murzuq, (also Murzaq, Murzuk, Marzuq and Murzak), is an erg in southwestern Libya with a surface of approximately 58,000 km.  It is named after the town of Murzuk in the Fezzan.  Like the Idehan Ubari further north, the Idehan Murzuq is part of the greater Sahara Desert region.  It is separated from the southern Sahara Desert by the Tibesti Mountains and the Tassili n'Ajjer.\n\nFestival au Désert: The Festival au désert (\"Festival in the Desert\") is an annual concert in Mali, showcasing traditional Tuareg music as well as music from around the world.  The first Festival took place in Tin Essako in 2001 and then it moved in 2002 to Tessalit in the Kidal region (North-Eastern Mali).  From 2003 until 2009 the festival was held in Essakane, 65km from Timbuktu, but because of security issues, from 2010 the festival was held on the outskirts of Timbuktu.\n\nTuareg people: The Tuareg people ( ; also spelled Twareg or Touareg; endonym \"Kel Tamasheq\", \"Kel Tagelmust\") are a large Berber ethnic confederation.  They principally inhabit the Sahara desert, in a vast area stretching from far southwestern Libya to southern Algeria, Niger, Mali and Burkina Faso.  Traditionally nomadic pastoralists, small groups of Tuareg are also found in northern Nigeria.\n\nNumidia: Numidia (202 BC – 40 BC, Berber: Inumiden) was an ancient Berber kingdom of the Numidians, located in what is now Algeria and a smaller part of Tunisia and Libya in the Berber world, in North Africa.  The polity was originally divided between Massylii in the east and Masaesyli in the west.  During the Second Punic War (218-201 BC), Massinissa, king of the Massylii, defeated Syphax of the Masaesyli to unify Numidia into one kingdom.  The kingdom began as a sovereign state and later alternated between being a Roman province and a Roman client state.  It was bordered by the kingdom of Mauretania to the west, Africa Proconsularis (modern-day Tunisia) to the east, the Mediterranean Sea to the north, and the Sahara Desert to the south.  It is considered to be one of the first major states in the history of Algeria and the Berber world.\n\nJebil National Park: Jebil is a national park in Tunisia situated within the Sahara desert.  Covering an area of 150,000 hectares, it is the country's largest national park and makes up most of the southern part of the country.  Though large, it is relatively new having been designated a national park in 1994 (unofficially since 1984).  It is the only national park within the Sahara desert proper.\n\nGaramantes: The Garamantes (possibly from the Berber \"igherman\" / \"iɣerman\", meaning: \"cities\" in modern Berber; or possibly from \"igerramen\" meaning \"saints, holy/sacred people\" in modern Berber) were a Berber tribe who developed an advanced civilization in ancient southwestern Libya.  They used an elaborate underground irrigation system, and founded prosperous Berber kingdoms or city-states in the Fezzan area of Libya, in the Sahara desert.  They were a local power between 500 BC and 700 AD.\n\nReggane: Reggane (from Berber \"Argan\"; Arabic: رقان‎ ‎ ) is a town and commune, and the capital of Reggane District, in Adrar Province, central Algeria.  Reggane lies in the Sahara Desert near an oasis.  According to the 2008 census it has a population of 20,402, up from 14,179 in 1998, with an annual growth rate of 3.8%.  Berber tribes and people live in and around Reggane.\n\nAtlas Mountains: The Atlas Mountains (Arabic: جبال الأطلس‎ ‎ , \"jibāl al-ʾaṭlas\"; Berber: , \"idurar n waṭlas\") are a mountain range in the Maghreb.  It stretches around 2,500 km through Morocco, Algeria and Tunisia.  The range's highest peak is Jebel Toubkal, with an elevation of 4167 m in southwestern Morocco.  It separates the Mediterranean and Atlantic coastlines from the Sahara Desert.  The Atlas mountains are primarily inhabited by Berber populations.  The terms for 'mountain' in some Berber languages are \"adrar\" and \"adras\", which are believed to be cognates of the toponym \"Atlas\".\n\nQuestion: What large Berber confederation, principally inhabiting the Sahara desert, also has an annual festival showcasing their traditional music?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"berber_confederation_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the large Berber ethnic confederation.\"\n    },\n    \"primary_habitat\": {\n      \"type\": \"string\",\n      \"description\": \"The principal region inhabited by the confederation.\"\n    },\n    \"has_annual_festival\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the confederation has an annual festival.\"\n    },\n    \"festival_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"festival_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the annual festival.\"\n        },\n        \"music_showcased\": {\n          \"type\": \"string\",\n          \"description\": \"Description of the music showcased at the festival.\"\n        },\n        \"festival_location_history\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of locations where the festival has been held over time.\"\n        }\n      },\n      \"required\": [\n        \"festival_name\",\n        \"music_showcased\",\n        \"festival_location_history\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"berber_confederation_name\",\n    \"primary_habitat\",\n    \"has_annual_festival\",\n    \"festival_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "berber_confederation_name": {
        "type": "string",
        "description": "The name of the large Berber ethnic confederation."
      },
      "primary_habitat": {
        "type": "string",
        "description": "The principal region inhabited by the confederation."
      },
      "has_annual_festival": {
        "type": "boolean",
        "description": "Indicates if the confederation has an annual festival."
      },
      "festival_details": {
        "type": "object",
        "properties": {
          "festival_name": {
            "type": "string",
            "description": "The name of the annual festival."
          },
          "music_showcased": {
            "type": "string",
            "description": "Description of the music showcased at the festival."
          },
          "festival_location_history": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of locations where the festival has been held over time."
          }
        },
        "required": [
          "festival_name",
          "music_showcased",
          "festival_location_history"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "berber_confederation_name",
      "primary_habitat",
      "has_annual_festival",
      "festival_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
