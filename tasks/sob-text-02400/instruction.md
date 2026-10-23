{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBritain's Great War: Britain's Great War is a British documentary television series that broadcast on BBC One 27 January 2014.  The documentary series is presented by Jeremy Paxman and was produced by the Open University and BBC Productions.  The series shows how World War I affected Britain and its people.  The series leads the BBC World War I centenary season.\n\nMexico in World War I: Mexico was a neutral country in the Great War (World War I) that lasted from 1914 to 1918.  The Great War broke out in Europe in August 1914 as the Mexican Revolution was in the midst of full-scale civil war between factions that had helped oust General Victoriano Huerta from the presidency earlier that year.  The Constitutionalist Army of Venustiano Carranza under the generalship of Alvaro Obregón defeated the army of Pancho Villa in the Battle of Celaya in April 1915.\n\nCenotaph War Memorial, Colombo: The Cenotaph War Memorial in Viharamahadevi Park, Colombo, Sri Lanka is dedicated to the military personal from Ceylon killed in action during the two world wars.  It comprises a towering Cenotaph and Memorial Walls.  The foundation stone was laid by Brigadier General Sir William Henry Manning, Governor of Ceylon on December 7, 1921 and was unveiled by him October 27, 1923 at the Galle Face Green and was known as the Victory tower.  It was dismantled and re-erected at Victoria Park, during World War II after fears that the Japanese might use it as a marker to direct their artillery.  The Cenotaph contains the names of those killed in the Great War, while the Memorial Wall behind it maintains the names of those killed in the Second World War.  A single woman, Miss L. Midwood is listed among the dead of the Great war.\n\nJeremy Paxman: Jeremy Dickson Paxman (born 11 May 1950) is an English broadcaster, journalist, and author.  He is the question master of \"University Challenge\", having succeeded Bamber Gascoigne when the programme was revived in 1994.\n\nMuseum of the Great War: The Museum of the Great War (French: Historial de la Grande Guerre ) located near the heart of the World War I Somme battlefields, is housed within the Château de Péronne, a castle in the town of Péronne, France.  The museum looks mostly at the Great War, and the years just before and just after.  It strives to place war in a social context, stressing \"the common suffering of the combatants\" and \"the civilians, who were equally mobilised by the war effort\".\n\nFirst Eagles: The Great War 1918: First Eagles: The Great War 1918 (Also called First Eagles: The Great Air War 1918) is a PC game (Combat / Flight Simulator) that focuses on World War I (\"the Great War\") between 1917 and 1918.\n\nThe Great War for Civilisation: The Great War for Civilisation: The Conquest of the Middle East is a book published in 2005 by the award-winning English journalist Robert Fisk.  The book is a compilation of many of the articles Fisk wrote when he was serving as a correspondent in the Middle East for \"The Times\" and \"The Independent\".  The book revolves around several key themes regarding the history of the modern Middle East: the Arab-Israeli conflict, the Soviet invasion of Afghanistan, the Persian Gulf War as well as the 2003 Iraq War (United States invasion of Iraq) as well as other regional conflicts such as the Armenian Genocide and the Algerian Civil War.  The \"Great War for Civilisation\" is the second book Fisk has written about the Middle East with the first one, \"Pity the Nation\", (Nation Books, 2002) being about the Lebanese Civil War.\n\nCastles of Steel: Castles of Steel: Britain, Germany, and the Winning of the Great War at Sea is a work of non-fiction by Pulitzer Prize-winner Robert K. Massie.  It details the naval actions of the First World War with an emphasis on those of the United Kingdom and Imperial Germany.  This book continues the examination of the naval arms race between these two powers in Massie's tome \"Dreadnought: Britain, Germany, and the coming of the Great War\".  The term \"castles of steel\" was coined by the British First Lord of the Admiralty Winston Churchill in reference to the large number of the Royal Navy's battleships he saw in review at Spithead in 1914.\n\nDescent: FreeSpace – The Great War: Descent: FreeSpace – The Great War, also known as Conflict: FreeSpace – The Great War in Europe, is a 1998 space combat simulation IBM PC compatible computer game developed by Volition, when it was split off from Parallax Software, and published by Interplay Productions.  In 2001, it was ported to the Amiga platform as FreeSpace: The Great War by Hyperion Entertainment.  The game places players in the role of a human pilot, who operates in several classes of starfighter and combats against opposing forces, either human or alien, in various space-faring environments, such as in orbit above a planet or within an asteroid belt.  The story of the game's single player campaign focuses on a war in the 24th century between two factions, one human and the other alien, that is interrupted in its fourteenth year by the arrival of an enigmatic and militant alien race, whose genocidal advance forces the two sides into a ceasefire in order to work together to halt the threat.\n\nWestern Front Association: The Western Front Association (WFA) was inaugurated on 11 November 1980, in order to further interest in The Great War of 1914-1918.  The WFA aims to perpetuate the memory, courage and comradeship of all those who fought on all sides and who served their countries during The Great War.  The Western Front Association does not seek to justify or glorify war.  It is not a re-enactment society, nor is it commercially motivated.  It is entirely non-political.  The object of the Association is to educate the public in the history of The Great War with particular reference to the Western Front.\n\nQuestion: In what year was the presenter of \"Britain's Great War\" born?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"documentary_series_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the documentary series.\"\n    },\n    \"presenter_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the presenter of the documentary series.\"\n    },\n    \"presenter_birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the presenter.\"\n    },\n    \"presenter_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the presenter.\"\n    },\n    \"presenter_occupations\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of occupations held by the presenter.\"\n    }\n  },\n  \"required\": [\n    \"documentary_series_title\",\n    \"presenter_name\",\n    \"presenter_birth_year\",\n    \"presenter_nationality\",\n    \"presenter_occupations\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "documentary_series_title": {
        "type": "string",
        "description": "The title of the documentary series."
      },
      "presenter_name": {
        "type": "string",
        "description": "The name of the presenter of the documentary series."
      },
      "presenter_birth_year": {
        "type": "integer",
        "description": "The birth year of the presenter."
      },
      "presenter_nationality": {
        "type": "string",
        "description": "The nationality of the presenter."
      },
      "presenter_occupations": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of occupations held by the presenter."
      }
    },
    "required": [
      "documentary_series_title",
      "presenter_name",
      "presenter_birth_year",
      "presenter_nationality",
      "presenter_occupations"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
