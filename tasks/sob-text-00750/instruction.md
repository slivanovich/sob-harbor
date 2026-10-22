Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Frank Mata: Frank Jesús Mata (born March 11, 1984) is a former Venezuelan professional baseball pitcher.

Rafael Álvarez (baseball): Rafael Ángel Álvarez Flores (born January 22, 1977) is a former Venezuelan professional baseball outfielder and first baseman, who is currently a coach for the Spain national baseball team.  He was born in Valencia, Carabobo State.

Apocalypto: Apocalypto is a 2006 American epic adventure film directed and produced by Mel Gibson and written by Gibson and Farhad Safinia.  The film features a cast of actors consisting of Rudy Youngblood, Raoul Trujillo, Mayra Sérbulo, Dalia Hernández, Ian Uriel, Gerardo Taracena, Rodolfo Palacios, Bernardo Ruiz Juarez, Ammel Rodrigo Mendoza, Ricardo Diaz Mendoza and Israel Contreras.  Similar to Gibson's earlier film "The Passion of the Christ", all dialogue is in a modern approximation of the ancient language of the setting.  Here, the Yucatec Maya language is used, with English and other language subtitles, which sometimes refer to the language as Mayan.

Israel Contreras: Israel Contreras (born 27 December 1960) is a Venezuelan former professional boxer who won the World Boxing Association bantamweight title.  He had a supporting role in the Mel Gibson film "Apocalypto".

David Griman: David Griman (born March 10, 1967 in Los Teques) is a former Venezuelan professional boxer.  He is a former World Boxing Association (WBA) flyweight (112 lb) champion.

Aquiles Guzmán: Aquiles José Guzmán Matute.  (born April 13, 1965 in Anzoátegui, Venezuela) is a former Venezuelan professional boxer.  He is a former World Boxing Association (WBA) flyweight (112 lb) champion.

Manuel Medina (cyclist): Manuel Eduardo Medina Mariño (born July 14, 1976 in Aragua de Barcelona, Anzoátegui) is a Venezuelan professional bicycle road racing cyclist and former Venezuelan national cycling champion.  He was nicknamed "El Gato" during his career.

Miguel Pérez (baseball): Miguel Ángel Pérez (born September 25, 1983) is a former Venezuelan professional baseball catcher.  He played in Major League Baseball for the Cincinnati Reds in 2005.  He bats and throws right-handed.

Bobby Abreu: Bob Kelly Abreu ( ; ] ; born March 11, 1974), nicknamed "El Comedulce" and also "La Leche", is a former Venezuelan professional baseball outfielder.  He played in Major League Baseball (MLB) for the Houston Astros, Philadelphia Phillies, New York Yankees, Los Angeles Angels of Anaheim, Los Angeles Dodgers, and New York Mets.

Luis Raven: Luis Alberto Raven Enríquez (born November 19, 1968) is a former Venezuelan professional baseball outfielder.  Listed at 6'0" ( ), 185 lb.  ( ), Raven batted and threw right handed.  He was born in La Guaira, Vargas.

Question: Who was the director/producer of the 2006 American epic adventure film, Apocalypto, that cast a former Venezuelan professional boxer as a supporting actor?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "director_producer_name": {
      "type": "string",
      "description": "The name of the director and producer of the film."
    },
    "supporting_actor": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the supporting actor."
        },
        "profession": {
          "type": "string",
          "description": "The profession of the supporting actor."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the supporting actor."
        }
      },
      "required": [
        "name",
        "profession",
        "nationality"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "release_year",
    "director_producer_name",
    "supporting_actor"
  ],
  "additionalProperties": false
}
