{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTom Clancy's Splinter Cell: Double Agent: Tom Clancy's Splinter Cell: Double Agent is an action-adventure stealth video game, developed and published by Ubisoft.  The series, endorsed by American author Tom Clancy, follows the character Sam Fisher, an agent employed by a black-ops division of the National Security Agency, dubbed Third Echelon.  \"Double Agent\" was released for the GameCube, PlayStation 2, Xbox and Xbox 360 in October 2006.  The Wii and Microsoft Windows versions were released in November 2006.  A PlayStation 3 version was released in March 2007.  Originally the game was set for a March 2006 release, but Ubisoft moved the release date to October 2006 in order to have more development time.  Ubisoft then released their fiscal quarter results for Q1 2006 and announced that \"Double Agent\" would be put back at least one month in order to boost Q3 2006 income.\n\nGerman weather ship Lauenburg: Lauenburg was a German weather ship used in the early years of the Second World War to provide weather reports for German shipping, particularly German U-boats.  Her capture and subsequent sinking on 28 June 1941 allowed the Royal Navy to acquire important German code books and parts of an Enigma machine, and came after the German use of such vessels had been identified as a weakness that could be exploited to break the Enigma code.\n\nCode Name: Diamond Head: Code Name: Diamond Head is a 1977 American spy film starring Roy Thinnes as an undercover counterintelligence officer known as Diamond Head whose mission is to stop a rogue double agent from stealing the formula for a new chemical weapon.  Originally filmed as a pilot for a new television drama (which was never picked up by the networks), it was eventually used for \"The NBC Monday Movie\" on U.S. broadcast network NBC.\n\nAnthony Faramus: Anthony Charles Faramus (27 July 1920 – August 1990) was an actor, author and hairdresser.  He was born in Saint Peter, Jersey and died in Surrey.  The autobiographical accounts of his survival of Fort de Romainville, Buchenwald and the Mauthausen-Gusen concentration camp complex were published as \"The Faramus Story\" in 1954 and \"Journey Into Darkness\" in 1990.  Two books about Agent Zigzag, the double agent Eddie Chapman, also document aspects of Faramus’s 'ruse' to join the Nazis as a collaborator and a spy, his imprisonment in Jersey, Paris and the concentration camps.\n\nHosteen Klah: Hosteen Klah (Navajo: , 1867–1937) was a Navajo artist and medicine man.  He documented aspects of Navajo religion and related ceremonial practices.  He was also a master weaver.\n\nEddie Chapman: Edward Arnold Chapman (16 November 1914 – 11 December 1997) was an English wartime spy.  During the Second World War he offered his services to Nazi Germany as a spy and subsequently became a British double agent.  His British Secret Service handlers codenamed him Zigzag in acknowledgement of his rather erratic personal history.  He had a number of criminal aliases known by the British police, amongst them Edward Edwards, Arnold Thompson and Edward Simpson.  His German codename was Fritz or, later, after endearing himself to his German contacts, its diminutive form of Fritzchen.\n\nOperation Willi: Operation Willi was the German code name for the unsuccessful attempt by the SS to kidnap Edward, Duke of Windsor in July 1940 and induce him to work with German dictator Adolf Hitler for either a peace settlement with Britain, or a restoration to the throne after the German conquest of Great Britain.\n\nRoger Grosjean: Roger Grosjean (25 July 1920 – 7 June 1975) started his career as a French Air Force fighter pilot in France, England and North Africa.  This involved a short stint as a Security Service (MI5) double agent during World War II (code name FIDO).  He then became a successful archeologist in Corsica.\n\nJohnny Jebsen: Johann-Nielsen Jebsen, Nickname \"Johnny\", was an anti-Nazi German intelligence officer and British double agent (code name Artist) during the Second World War.  Jebsen recruited Dušan Popov (who became the British agent Tricycle) to the Abwehr and through him later joined the Allied cause.  Kidnapped from Lisbon by the Germans shortly before D-Day, Jebsen was tortured in prison and spent time in a concentration camp before disappearing, presumed killed, at the end of the war.\n\nOperation Christ Rose: Operation Christ Rose was the German code name (translated into English) for the counterattack by the Nazis that led to the Battle of the Bulge.\n\nQuestion: What was the German code name for the double agent that documented aspects of Faramus's ruse to join the Nazis?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"double_agent_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the double agent.\"\n    },\n    \"double_agent_british_codename\": {\n      \"type\": \"string\",\n      \"description\": \"The British codename assigned to the double agent.\"\n    },\n    \"double_agent_german_codenames\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of German codenames used for the double agent.\"\n    },\n    \"person_whose_ruse_was_documented\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person whose ruse to join the Nazis was documented by the double agent's actions.\"\n    },\n    \"german_codename_for_double_agent\": {\n      \"type\": \"string\",\n      \"description\": \"The primary German codename for the double agent in question.\"\n    }\n  },\n  \"required\": [\n    \"double_agent_name\",\n    \"double_agent_british_codename\",\n    \"double_agent_german_codenames\",\n    \"person_whose_ruse_was_documented\",\n    \"german_codename_for_double_agent\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "double_agent_name": {
        "type": "string",
        "description": "The full name of the double agent."
      },
      "double_agent_british_codename": {
        "type": "string",
        "description": "The British codename assigned to the double agent."
      },
      "double_agent_german_codenames": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of German codenames used for the double agent."
      },
      "person_whose_ruse_was_documented": {
        "type": "string",
        "description": "The name of the person whose ruse to join the Nazis was documented by the double agent's actions."
      },
      "german_codename_for_double_agent": {
        "type": "string",
        "description": "The primary German codename for the double agent in question."
      }
    },
    "required": [
      "double_agent_name",
      "double_agent_british_codename",
      "double_agent_german_codenames",
      "person_whose_ruse_was_documented",
      "german_codename_for_double_agent"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
