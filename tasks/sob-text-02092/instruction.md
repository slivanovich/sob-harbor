{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRosa salvaje: Rosa salvaje (English title: \"Wild Rose\") (] ; is a Mexican telenovela produced by Valentín Pimstein for Televisa.  The telenovela premiered on Canal de las Estrellas on July 6, 1987 and ran for 199 episodes until April 8, 1988.  This telenovela was a huge success in Mexico, Latin America, Bulgaria, Croatia, Serbia, Bosnia and Herzegovina, Russia, Estonia, China the United States, Indonesia and provided the template for numerous other Latin American soap operas in terms of story, plot twists and characters for years to come.\n\nLo que la vida me robó: Lo que la vida me robó (English title: \"What Life Took From Me\"), is a Mexican telenovela produced by Angelli Nesma Medina for Televisa, broadcast by Canal de las Estrellas now known as Las Estrellas.  The series originally aired from October 28, 2013 to July 27, 2014.  It is an adaptation of the telenovela of 1983 \"Bodas de odio\" produced by Ernesto Alonso, which also inspired \"Amor real\", produced by Carla Estrada in 2003.\n\nLas Estrellas: Las Estrellas (The Stars; previously El Canal de las Estrellas) is one of the cornerstone networks of Televisa, with affiliate stations all over Mexico, flagshipped at XEW-TV in Mexico City.  Many of the programs of \"Las Estrellas\" are seen in the United States on Univision, UniMás, and Galavisión.  Las Estrellas has been criticized for its practice of airing a significant amount of 4:3 standard definition content stretched to 16:9 high definition that some TV viewers have nicknamed Stretch-o-Vision, until 14 March 2012, when Las Estrellas, FOROtv, Canal 5 and Galavisión started to broadcast a significant amount of 4:3 standard definition content in their original resolution.\n\nLas Estrellas (telenovela): Las Estrellas is an Argentine telenovela produced by Pol-Ka Producciones for El Trece.  It stars Celeste Cid, Marcela Kloosterboer, Natalie Pérez, Violeta Urtizberea, Justina Bustos, Esteban Lamothe, Gonzalo Valenzuela, and Rafael Ferro.  It premiered on May 29, 2017.\n\nMi corazón es tuyo: Mi corazón es tuyo (English: \"My heart is yours\") is a Mexican telenovela produced by Juan Osorio for Televisa and airs weeknights on El Canal de las Estrellas.  The telenovela is an adaptation of the Spanish telenovela \"Ana y los 7\".  It was adapted in Mexico by Alejandro Pohlenz, Marcia del Río, and Pablo Ferrer.\n\nMaritza Rodríguez: Maritza Rodríguez Gómez (born 1 September 1975 in Barranquilla, Colombia) is a Colombian telenovela actress and model.  She is best known for her roles as Cristal Covarrubias in Venevisión's telenovela Ángel Rebelde (2003), as Marfil Mondragon de Irázabal and Deborah Mondragón de Dávila in Venevisión's telenovela Acorralada (2007), as Sara Andrade in Telemundo's telenovela El Rostro de Analia (2008), as Pilar and Raquel Arismendi in Telemundo's telenovela La Casa de al Lado (2011), as Antonia Villarroel in Telemundo's telenovela El Rostro de la Venganza (2012) and now as Teresa Cristina Palmer in Telemundo's telenovela Marido En Alquiler (2013).\n\nLa usurpadora: La Usurpadora (International Title: \"Deceptions\") is a Mexican romantic drama telenovela produced by Salvador Mejia Alejandre and originally broadcast on Canal de las Estrellas from February 9 to July 24, 1998.  It starred Gabriela Spanic and Fernando Colunga, and was based on \"La Intrusa\", a novela originally broadcast in Venezuela which was itself a remake of Radio Caracas Television's 1971 telenovela \"La Usurpadora\", which was starred by Marina Baura and Raúl Amundaray.  This was one of the last telenovelas to feature Libertad Lamarque, who here portrayed the character of Abuela Piedad Bracho.  The show's premise revolves around a pair of twin sisters who were separated when they were young, and as adults the younger sister is forced to act as a \"replacement\" for her wealthy twin who wants to temporarily leave her husband and his family to enjoy a life of luxury with multiple lovers.  The telenovela had huge success in Mexico with ratings of 38.4 and has been exported and ported to various languages across the world.\n\nVioleta Urtizberea: Violeta Urtizberea is an Argentine actress.  She began working on Magazine for fai in the channel Telefe, along her father Mex Urtizberea.  She made other works with him, and then began her own career.  She worked once again with her father in the 2012 telenovela Graduados.\n\nGabriela Goddzer: Gabriela Goddzer is a fictional character in the 2012 Argentine telenovela \"Graduados\".  She is played by Violeta Urtizberea.\n\nList of Mi corazón es tuyo episodes: Mi corazón es tuyo (English: \"My Heart Is Yours\") is a Mexican telenovela produced by Juan Osorio for Televisa, which is transmitted by El Canal de las Estrellas.  The telenovela is an adaptation of the Spanish telenovela \"Ana y los 7\".  It is adapted in Mexico by Alejandro Pohlenz, Marcia del Río and Pablo Ferrer.\n\nQuestion:  Las Estrellas telenovela actress Violeta Urtizberea and her father worked for which telenovela in 2012?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actress_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actress mentioned in the question.\"\n    },\n    \"father_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actress's father.\"\n    },\n    \"telenovela_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the telenovela they worked on together.\"\n    },\n    \"year_of_production\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the telenovela was produced or aired.\"\n    },\n    \"country_of_origin\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the telenovela was produced.\"\n    }\n  },\n  \"required\": [\n    \"actress_name\",\n    \"father_name\",\n    \"telenovela_name\",\n    \"year_of_production\",\n    \"country_of_origin\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actress_name": {
        "type": "string",
        "description": "The name of the actress mentioned in the question."
      },
      "father_name": {
        "type": "string",
        "description": "The name of the actress's father."
      },
      "telenovela_name": {
        "type": "string",
        "description": "The name of the telenovela they worked on together."
      },
      "year_of_production": {
        "type": "integer",
        "description": "The year the telenovela was produced or aired."
      },
      "country_of_origin": {
        "type": "string",
        "description": "The country where the telenovela was produced."
      }
    },
    "required": [
      "actress_name",
      "father_name",
      "telenovela_name",
      "year_of_production",
      "country_of_origin"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
