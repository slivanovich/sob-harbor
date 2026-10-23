{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPrimer amor, a mil por hora: Primer amor, a mil por hora (English title: \"First love, a thousand per hour\") is a Mexican telenovela produced by Pedro Damián for Televisa in 2000.  It is a remake of another Televisa telenovela titled \"Quinceañera\".  This teen-oriented soap was one of the highest-rated in its time-slot.\n\nTequila, Jalisco: Santiago de Tequila (    ; Nahuatl: \"Tequillan, Tecuila\" \"place of tribute\") is a Mexican town and municipality located in the state of Jalisco about 60 km from the city of Guadalajara.  Tequila is best known as being the birthplace of the drink that bears its name, “tequila,” which is made from the blue agave plant, native to this area.  The heart of the plant contains sugars and had been used by native peoples here to make a fermented drink.  After the Spanish arrived, they took this fermented beverage and distilled it, producing the tequila known today.  The popularity of the drink and the history behind it has made the town and the area surrounding it a World Heritage Site.  It was also named a \"Pueblo Mágico\" (Magical Town) in 2003 by the Mexican federal government.  Tequila has also been famous for being the prime setting in the successful Televisa telenovela \"Destilando Amor\", starring Angélica Rivera and Eduardo Yáñez.\n\nCynthia Klitbo: Cynthia Klitbo (] ; born Diana Cynthia Klitbo on March 11, 1967 in Zacatecas, Mexico) is a Mexican actress of telenovelas, theater and Mexican cinema.  She is best known for her roles as Laura in Televisa's telenovela La Dueña (Mexico) (1995), as Tamara de Duval in Televisa's telenovela El privilegio de amar (1998) and as Juana Godoy de González in Televisa's telenovela Teresa (2010 telenovela).\n\nCaer en tentación: Caer en tentación is a Mexican telenovela produced by Giselle González for Televisa, and it started airing on Mexican broadcast channel Las Estrellas on September 18, 2017.  Based on the Argentine drama by Erika Halvorsen and Gonzalo Demaría, titled \"Amar después de amar\".  The series stars Silvia Navarro, Gabriel Soto, Adriana Louvier, and Carlos Ferro.\n\nAnabel Ferreira: Anabel Ferreira (born Anabel Ferreira Batiz; 1960 in Aguascalientes) is a Mexican actress and comedian.  Ferreira has been with Televisa from 1981 until 1996 and again since 2008.  In between, she spent a decade at TV Azteca.  Most recently appearing on the Televisa telenovela \"Soy tu dueña\", she is best known as the star of her own comedy/variety series, \"Anabel\" (Both programs, as with most of Ferreira's work with Televisa, have aired on Univision in the United States, among other networks in other countries).  Ferreira still works in Mexico but now lives in Los Angeles, California.\n\nMarjorie de Sousa: Marjorie de Sousa (born Marjorie Lissette de Sousa Rivas on April 23, 1980 in Las Acacias, Parroquia San Pedro, Caracas, Venezuela) is a Venezuelan actress and model of Portuguese descent.  She is worldwide known for her villain roles as Camelia Valente in Venevisión's telenovela Gata Salvaje (2002), as Carol in the Televisa telenovela Mariana de la Noche (2003), as Kendra Ferreti in the Televisa telenovela Amores Verdaderos (2012), as Sofía Ripoll / Sofía Fernández in the Televisa telenovela Hasta el fin del mundo (2014) and recently as Cristina Vélez, the co-protagonist of Televisa's telenovela, Sueño de amor (2016).\n\nAmor real: Amor Real (\"Real Love\") is a Mexican telenovela, which was produced and broadcast by Televisa in 2003.  \"Amor Real\" is a historical telenovela set in the Mexican post-independence period of the mid-19th century.  The telenovela aired on Univision in the United States, REN TV in Russia, and La 1 in Spain, among others.  It was successfully distributed to many countries worldwide.  Also, in 2005, \"Amor real\" was released on DVD and it became the first telenovela to be released with English subtitles.  Televisa has released an abridged DVD version of the novela in several countries.\n\nList of A que no me dejas episodes: This is a list of episodes for the Televisa telenovela \"A que no me dejas\".\n\nTres mujeres: Tres mujeres (English title: \"Three women\") is a Mexican telenovela produced by Roberto Hernández Vázquez for Televisa in 1999-2000.  When it came out it was such a success that they added 3x the normal amount of chapters.  There are 280 Chapters when there are normally about 100 chapters.  The Telenovela ended in 2000, which made it the longest Telenovela produced my Televisa until Clase 406.\n\nSaturno (song): \"Saturno\" is a song recorded by Spanish singer-songwriter Pablo Alborán, serving as the lead single for his forthcoming third studio album.  The song was released worldwide on 8 September 2017.  The song is the main theme of the Mexican telenovela \"Caer en tentación\".\n\nQuestion: Saturno is the theme of which Televisa telenovela?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song.\"\n    },\n    \"telenovela_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the telenovela.\"\n        },\n        \"producer\": {\n          \"type\": \"string\",\n          \"description\": \"The company that produced the telenovela.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"producer\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"song_role\": {\n      \"type\": \"string\",\n      \"description\": \"The role of the song in the telenovela (e.g., 'main theme').\"\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"telenovela_details\",\n    \"song_role\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song."
      },
      "telenovela_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the telenovela."
          },
          "producer": {
            "type": "string",
            "description": "The company that produced the telenovela."
          }
        },
        "required": [
          "title",
          "producer"
        ],
        "additionalProperties": false
      },
      "song_role": {
        "type": "string",
        "description": "The role of the song in the telenovela (e.g., 'main theme')."
      }
    },
    "required": [
      "song_title",
      "telenovela_details",
      "song_role"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
