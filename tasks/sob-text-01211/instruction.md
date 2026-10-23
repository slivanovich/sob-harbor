{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nVog: Vog is a form of air pollution that results when sulfur dioxide and other gases and particles emitted by an erupting volcano react with oxygen and moisture in the presence of sunlight.  The word is a portmanteau of the words \"volcanic\", \"smog\", and \"fog\".  The term is in common use in the Hawaiian islands, where the Kīlauea volcano, on the Island of Hawaiʻ i (aka \"The Big Island\"), has been erupting continuously since January 3, 1983.  Based on June 2008 measurements, Kīlauea emits 2,000–4,000 tons of sulfur dioxide (SO) every day.\n\nMontserrat Volcano Observatory: The Montserrat Volcano Observatory (MVO) is a volcano observatory which is located on the Caribbean island of Montserrat, where the Soufrière Hills volcano (SHV) has been actively erupting since 1995.\n\nParícutin: Parícutin (or Volcán de Parícutin, also accented Paricutín) is a cinder cone volcano located in the Mexican state of Michoacán, near the city of Uruapan and about 322 km west of Mexico City.  The volcano surged suddenly from the cornfield of local farmer Dionisio Pulido in 1943, attracting both popular and scientific attention.\n\nPoás Volcano: The Poás Volcano, (Spanish: \"Volcán Poás\"), is an active 2708 m stratovolcano in central Costa Rica and is located within Poas Volcano National Park.  It has erupted 40 times since 1828, including April, 2017 when visitors and residents were evacuated.  The volcano and surrounding park are currently closed indefinitely, with a 2.5 kilometer safety perimeter established around the erupting crater.\n\nPlymouth, Montserrat: Plymouth was the capital of the island of Montserrat, an overseas territory of the United Kingdom located in the Leeward Island chain of the Lesser Antilles, West Indies.  Constructed on historical lava deposits near the then-inactive Soufriere Hills volcano, the town was evacuated when the volcano resumed erupting in 1995.  Plymouth was abandoned permanently in 1997 after it was burnt and mostly buried by a series of pyroclastic flows and lahars. For centuries it had been the only port of entry to the island.\n\nNe Ch'e Ddhawa: Ne Ch'e Ddhawa (also known as Wootten's Cone) is a volcano located 7 km upstream from Fort Selkirk in the Fort Selkirk Volcanic Field of central Yukon, Canada.  It has been described as a cinder cone or a subglacial mound.  The volcano erupted subglacially during the late Pleistocene, erupting hyaloclastite tuffs, breccias, and pillow breccias.\n\nVolcano School: The Volcano School refers to a group of non-native Hawaiian artists who painted dramatic nocturnal scenes of Hawaii's erupting volcanoes.  Some of the artists also produced watercolors, which, by the nature of the medium, tended to be diurnal.  At their best, these paintings exemplify a fusion of the European Sublime aesthetic, Romantic landscapes, and the American landscape traditions.  Two volcanoes on the Island of Hawaii, Kilauea and Mauna Loa, were intermittently active during the 1880s and 1890s, when interest in Volcano School paintings peaked.  Getting to Kilauea, the more frequently painted volcano required an arduous two- or three-day roundtrip journey on horseback.\n\nCaptain from Castile: Captain from Castile is a historical adventure film released by 20th Century Fox in 1947.  Directed by Henry King, the Technicolor film starred Tyrone Power, Jean Peters, and Cesar Romero.  Shot on location in Michoacán, Mexico, the film includes scenes of the Parícutin volcano, which was then erupting.  \"Captain from Castile\" was the feature film debut of actress Jean Peters, who later married industrialist Howard Hughes, and of Mohawk actor Jay Silverheels, who later portrayed Tonto on the television series \"The Lone Ranger\".\n\nVolcanic bomb: A volcanic bomb is a mass of molten rock (tephra) larger than 64 mm (2.5 inches) in diameter, formed when a volcano ejects viscous fragments of lava during an eruption.  They cool into solid fragments before they reach the ground.  Because volcanic bombs cool after they leave the volcano, they are extrusive igneous rocks.  Volcanic bombs can be thrown many kilometres from an erupting vent, and often acquire aerodynamic shapes during their flight.  Bombs can be extremely large; the 1935 eruption of Mount Asama in Japan expelled bombs measuring 5–6 m in diameter up to 600 m from the vent.  Volcanic bombs are a significant volcanic hazard, and can cause severe injuries and death to people in an eruption zone.  One such incident occurred at Galeras volcano in Colombia in 1993; six people near the summit were killed and several seriously injured by lava bombs when the volcano erupted unexpectedly.\n\nEduardo Lefebvre Scovell: Eduardo Lefebvre Scovell (1864–1918) was a British artist.  He is one of the Volcano School, a group of non-native artists who painted dramatic nocturnal scenes of Hawaii's erupting volcanoes.\n\nQuestion: What volcano surged suddenly from a cornfield and was filmed erupting during the filming of scenes in the movie Captain from Castile?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"volcano_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the volcano.\"\n    },\n    \"location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the volcano is located.\"\n        },\n        \"state_or_region\": {\n          \"type\": \"string\",\n          \"description\": \"The state or region within the country.\"\n        }\n      },\n      \"required\": [\n        \"country\",\n        \"state_or_region\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"origin_event_description\": {\n      \"type\": \"string\",\n      \"description\": \"A description of how the volcano originated or appeared.\"\n    },\n    \"featured_in_movie\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"movie_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the movie in which the volcano was featured.\"\n        },\n        \"movie_release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the movie.\"\n        },\n        \"was_erupting_during_filming\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the volcano was erupting when filmed for the movie.\"\n        }\n      },\n      \"required\": [\n        \"movie_title\",\n        \"movie_release_year\",\n        \"was_erupting_during_filming\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"volcano_name\",\n    \"location\",\n    \"origin_event_description\",\n    \"featured_in_movie\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "volcano_name": {
        "type": "string",
        "description": "The name of the volcano."
      },
      "location": {
        "type": "object",
        "properties": {
          "country": {
            "type": "string",
            "description": "The country where the volcano is located."
          },
          "state_or_region": {
            "type": "string",
            "description": "The state or region within the country."
          }
        },
        "required": [
          "country",
          "state_or_region"
        ],
        "additionalProperties": false
      },
      "origin_event_description": {
        "type": "string",
        "description": "A description of how the volcano originated or appeared."
      },
      "featured_in_movie": {
        "type": "object",
        "properties": {
          "movie_title": {
            "type": "string",
            "description": "The title of the movie in which the volcano was featured."
          },
          "movie_release_year": {
            "type": "integer",
            "description": "The release year of the movie."
          },
          "was_erupting_during_filming": {
            "type": "boolean",
            "description": "Indicates if the volcano was erupting when filmed for the movie."
          }
        },
        "required": [
          "movie_title",
          "movie_release_year",
          "was_erupting_during_filming"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "volcano_name",
      "location",
      "origin_event_description",
      "featured_in_movie"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
