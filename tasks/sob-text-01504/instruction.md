{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nWorms Ultimate Mayhem: Worms Ultimate Mayhem is a 3D artillery turn-based tactics video game developed by Team17.  The game is a re-release of \"\" with improved graphics.  It includes the campaign from \"Worms 3D\", adding customized looks to enemies in said campaign.  It features extra maps, new voice acting by Guy Harris and other gameplay fixes such as reworked camera controls.  The game features turn-based gameplay, a single-player campaign, and both local and online multiplayer.\n\nPentax D FA 150-450mm lens: The HD PENTAX-D FA 150-450mm F4.5-5.6 ED DC AW is a super-telezoom lens for Pentax K-mount.  Optically, it features extra low dispersion (ED) elements as well as HD, SP (Super Protect) and Bright Aero coatings.  It is weather sealed and supports quick shift.\n\nShane Hart: Shane Hart is an English extra.  He appeared in \"World War Z\" (2013), \"\" (2014) and \"Hummingbird\" (2014).\n\nThe Forever Changes Concert: The Forever Changes Concert (2003) is the last album released by Love with Arthur Lee.  There was a two-CD re-release in 2007 under the name of The Forever Changes Concert & More, which features extra songs, a live video of \"Alone Again Or\", band images and a screensaver.\n\nMy Wife's Family (1956 film): My Wife's Family is a 1956 British comedy film directed by Gilbert Gunn and starring Ronald Shiner as Doc Knott, Ted Ray, Greta Gynt, Diane Hart and Robertson Hare.  It was a remake of the 1941 British film \"My Wife's Family\", and is the third British film of the stage farce of the same name by actor Fred Duprez.\n\nNational Geographic Society: The National Geographic Society (NGS), headquartered in Washington, D.C., United States, is one of the largest non-profit scientific and educational institutions in the world.  Founded in 1888, its interests include geography, archaeology and natural science, the promotion of environmental and historical conservation, and the study of world culture and history.  The National Geographic Society’s logo is a yellow portrait frame – rectangular in shape – which appears on the margins surrounding the front covers of its magazines and as its television channel logo.  In partnership with 21st Century Fox, the Society operates the magazine, TV channels, a website that features extra content and worldwide events, and other media operations.\n\nMcConkey (film): McConkey is a 2013 documentary film about extreme skier Shane McConkey.  The film follows Shane from growing up as the son of skier Jim McConkey to his days as a professional freeskier.  The film also focuses on Shane's 2009 death during a ski base jump and his continued influence over the sport of skiing.  The film features interviews from notable athletes and friends of Shane such as JT Holmes, Tony Hawk and Travis Pastrana.\n\nCan't Relate: Can't Relate is the first full-length LP release by Caustic Christ October 14, 2003.  The CD version features extra tracks from their self-titled EP and a number of their splits and compilation appearances. \n\nHummingbird (film): Hummingbird (released as Redemption in the United States) is a 2013 British action drama film written and directed by Steven Knight and starring Jason Statham.\n\n1st British Academy Film Awards: The 1st British Film Academy Awards (retroactively known as the British Academy Film Awards), were handed out on 29 May 1949 at the Odeon Cinema, Leicester Square, in London, for films shown in the United Kingdom in 1947 and 1948.  They were presented by the British Film Academy (currently, British Academy of Film and Television Arts (BAFTA)), an organisation established in 1947 by filmmakers from Great Britain, for the \"advancement of the art and technique of the film\".  The Academy bestowed accolades in three categories: Best British Film, Best Picture from any source - British or Foreign and a Special Award.  British film producer Michael Balcon chaired the ceremony.\n\nQuestion: Which British film features extra Shane Hart?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"film_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"film_country_of_origin\": {\n      \"type\": \"string\",\n      \"description\": \"The country of origin of the film.\"\n    },\n    \"featured_actor\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"actor_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actor featured in the film.\"\n        },\n        \"role_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of role the actor played in the film.\"\n        }\n      },\n      \"required\": [\n        \"actor_name\",\n        \"role_type\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_release_year\",\n    \"film_country_of_origin\",\n    \"featured_actor\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "film_release_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "film_country_of_origin": {
        "type": "string",
        "description": "The country of origin of the film."
      },
      "featured_actor": {
        "type": "object",
        "properties": {
          "actor_name": {
            "type": "string",
            "description": "The name of the actor featured in the film."
          },
          "role_type": {
            "type": "string",
            "description": "The type of role the actor played in the film."
          }
        },
        "required": [
          "actor_name",
          "role_type"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "film_release_year",
      "film_country_of_origin",
      "featured_actor"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
