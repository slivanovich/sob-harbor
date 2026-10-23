{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGURPS Magic: GURPS Magic is a source book for the GURPS Role-playing game from Steve Jackson Games that provides in depth coverage of magic in the context of GURPS.  The book expands on the material outlined in the Basic Set, provides alternative forms of magic for GMs to use, and contains much more material.  The first edition was published in 1989.\n\nGURPS Fantasy: GURPS Fantasy is a \"Genre Toolkit\" source book for the GURPS Role-playing game.  The fourth edition of GURPS separates the fantasy parts into fantasy and a setting book called GURPS Banestorm\n\nGURPS Banestorm: GURPS Banestorm, written by Phil Masters and Jonathan Woodward, was released in October 2005.  It is a setting sourcebook for the fourth edition of the GURPS Role-playing game.  It details a fantasy setting called \"Yrth\" that has been updated from the older GURPS Fantasy source books Orcslayer and GURPS Magic (first edition).  The standard fantasy elements such as Wizards, Orcs, Elves, and Dwarves are present, along with connections to Infinite Worlds.  There are also some more unusual fantastic races like the Reptile Men, and several others which can be added in as desired by the game master.\n\nGURPS Blood Types: GURPS Blood Types (ISBN  ) is a 128-page soft-bound book compiled by Lane Grate and published in 1995 by Steve Jackson Games as a supplement for the third edition GURPS role-playing game system.  It contains biographies and gaming statistics for 23 vampiress, vampire-like beings, and guidelines on creating more for various campaign settings.\n\nGURPS Traveller: Interstellar Wars: GURPS Traveller: Interstellar Wars is the first fourth edition book in the GURPS Traveller role-playing game series, by Steve Jackson Games, set early in the history of the Traveller universe.\n\nGURPS Infinite Worlds: GURPS Infinite Worlds is a supplement for the Fourth Edition of the \"GURPS\" role-playing game, published by Steve Jackson Games in 2005 and written by Kenneth Hite, Steve Jackson, and John M. Ford.  It expands upon the campaign setting of conflict between the \"Infinity Patrol\", which is the time-travel agency on \"our\" Earth, referred to as Homeline, and \"Centrum\" across a multiplicity of alternate history Earths.  This was presented in the \"Fourth Edition GURPS Basic Set\" (and originated in the Third Edition supplements \"GURPS Time Travel\", \"GURPS Alternate Earths\", and \"GURPS Alternate Earths II\").\n\nGURPS Japan: GURPS Japan, full title GURPS Japan: Roleplaying in the World of the Shogunate (1st edition) or GURPS Japan: Beauty, Terror, and Adventure (2nd edition), is a sourcebook for \"GURPS\", a role-playing game by Steve Jackson Games.  The first edition was published in 1988.\n\nGURPS Illuminati: GURPS Illuminati is a supplement for the GURPS tabletop role-playing game about secret societies, conspiracies, and conspiracy theories.  It was published in 1992, the year before Steve Jackson Games sued the Secret Service, and it won the Origins award for best role-playing game supplement in 1993, as the Origins Awards were not awarded in 1992.\n\nWizard (board game): \"Wizard\" was designed by Steve Jackson, later of Steve Jackson Games, and released by Metagaming in 1978 as Microgame #6 as a magic-based pocket board game of individual combat.  It was based on Metagaming's earlier Melee (game) release, with the difference being that it added magic to the game system.  \"Melee\", \"Wizard\" and gamemaster supplement \"In the Labyrinth\" eventually formed Metagaming's \"The Fantasy Trip\" fantasy role-playing system.  Both \"Melee\" and \"Wizard\" were expanded and re-released as \"Advanced Wizard\" and \"Advanced Melee\", with many role-playing elements added to the basic fantasy combat system.  When Steve Jackson released GURPS years later, the magic system in its fantasy supplements took some ideas from Wizard.\n\nGURPS Martial Arts: GURPS Martial Arts is a source book for the GURPS role-playing game, published by Steve Jackson Games; the most recent edition was scheduled to be released in 2007.  \"GURPS Martial Arts\" includes new perks, skills, techniques, styles, weapons, and combat rules for GURPS, as well as history on the martial arts, pregenerated NPCs, and ideas for martial-arts campaigns.  The book is an essential for any game that features large amounts of melee combat, in any genre or setting.\n\nQuestion: What is the time-travel agency called in the expanded fourth edition of the \"GURPS\" role-playing game published by Steve Jackson Games in 2005 that connects to GURPS Banestorm?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"agency_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the time-travel agency.\"\n    },\n    \"detailing_book\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the GURPS supplement where the agency is detailed.\"\n        },\n        \"publisher\": {\n          \"type\": \"string\",\n          \"description\": \"The publisher of the supplement.\"\n        },\n        \"publication_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the supplement was published.\"\n        },\n        \"gurps_edition\": {\n          \"type\": \"string\",\n          \"description\": \"The GURPS edition the supplement is for.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"publisher\",\n        \"publication_year\",\n        \"gurps_edition\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"related_settings\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Other GURPS settings or books connected to this agency's campaign setting.\"\n    }\n  },\n  \"required\": [\n    \"agency_name\",\n    \"detailing_book\",\n    \"related_settings\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "agency_name": {
        "type": "string",
        "description": "The name of the time-travel agency."
      },
      "detailing_book": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the GURPS supplement where the agency is detailed."
          },
          "publisher": {
            "type": "string",
            "description": "The publisher of the supplement."
          },
          "publication_year": {
            "type": "integer",
            "description": "The year the supplement was published."
          },
          "gurps_edition": {
            "type": "string",
            "description": "The GURPS edition the supplement is for."
          }
        },
        "required": [
          "title",
          "publisher",
          "publication_year",
          "gurps_edition"
        ],
        "additionalProperties": false
      },
      "related_settings": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Other GURPS settings or books connected to this agency's campaign setting."
      }
    },
    "required": [
      "agency_name",
      "detailing_book",
      "related_settings"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
