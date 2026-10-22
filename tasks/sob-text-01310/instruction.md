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
Moon of Avellaneda: Moon of Avellaneda (Spanish: "Luna de Avellaneda" , also known as "Avellaneda's Moon" in English) is a 2004 Argentine film directed by Juan José Campanella, and written by Campanella, Fernando Castets and Juan Pablo Domenech.  The film stars Ricardo Darín in his third collaboration with Campanella and Eduardo Blanco in his fourth collaboration, as well as Mercedes Morán and Valeria Bertuccelli.

Son of the Bride: Son of the Bride (Spanish: El hijo de la novia ) is a 2001 Argentine comedy drama film directed by Juan José Campanella and written by Campanella and Fernando Castets.  The executive producers were Juan Vera and Juan Pablo Galli, and it was produced by Adrián Suar.  It stars Ricardo Darín, Héctor Alterio, Norma Aleandro, Eduardo Blanco and Natalia Verbeke.

Eduardo Blanco (actor): Eduardo Blanco is an Argentine actor best known for his roles in the trilogy of films directed by Juan José Campanella, his friend and frequent collaborator: "El Mismo Amor, la Misma Lluvia" (1999), "El Hijo de la Novia" (2001) and "Luna de Avellaneda" (2004).

The Secret in Their Eyes: The Secret in Their Eyes (Spanish: "El secreto de sus ojos" ) is a 2009 Argentine-Spanish crime drama film directed, co-written, produced and edited by Juan José Campanella, based on the novel "La pregunta de sus ojos" (""The Question in Their Eyes"") by Eduardo Sacheri, who also co-wrote the screenplay.  The film is a joint production of Argentine and Spanish companies.

Love Walked In (1997 film): Love Walked In is a 1997 Argentine-American neo-noir drama/thriller film co-written and directed by Juan José Campanella and starring Denis Leary, Terence Stamp and Aitana Sánchez-Gijón.  It was based on the novel "Ni el tiro del final" ("Not Even The Final Shot") by Argentine writer José Pablo Feinmann.  The film takes its title from George Gershwin's song "Love Walked In".

Juan José Campanella: Juan José Campanella (born July 19, 1959) is an Argentine television and film director, writer and producer.  He is a prominent figure of cinema in his country, and achieved worldwide fame with the release of "The Secret in Their Eyes" (2009).

The Summit (2017 film): The Summit (Spanish: La cordillera ) is a 2017 Argentine political drama film directed by Santiago Mitre and written by Mitre and .  The film stars Ricardo Darín, Dolores Fonzi, Érica Rivas, Elena Anaya, Daniel Giménez Cacho, Alfredo Castro, Gerardo Romano, Leonardo Franco, Paulina García, and Christian Slater.  It was screened in the Un Certain Regard section at the 2017 Cannes Film Festival.  It was released on 17 August 2017 in Argentina.

Truman (2015 film): Truman is a 2015 Spanish-Argentine comedy-drama film directed by Cesc Gay and co-written by Gay and Tomàs Aragay.  The film stars Ricardo Darín, Javier Cámara, and Dolores Fonzi.

Ricardo Darín: Ricardo Darín (] ; born January 16, 1957) is an Argentine actor, screenwriter and film director.  Widely considered as one of the best and most prolific actors of Argentine cinema.

Same Love, Same Rain: Same Love, Same Rain (Spanish: El mismo amor, la misma lluvia ) is a 1999 Argentine-American romantic comedy film directed by Juan José Campanella and written by Campanella and Fernando Castets.  It stars Ricardo Darín, Soledad Villamil, Ulises Dumont and Eduardo Blanco.

Question: Same Love, Same Rain, is an Argentine-American romantic comedy film, released in what year, and directed by Juan José Campanella, it stars Ricardo Darín, an Argentine actor, screenwriter and film director?

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
      "description": "The year the film was released."
    },
    "director": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the film's director."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "starring_actors": {
      "type": "array",
      "description": "A list of actors starring in the film, with their professions.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actor."
          },
          "professions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of professions for the actor."
          }
        },
        "required": [
          "name",
          "professions"
        ],
        "additionalProperties": false
      }
    },
    "film_genre": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The genres of the film."
    },
    "film_origin": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The countries of origin for the film."
    }
  },
  "required": [
    "film_title",
    "release_year",
    "director",
    "starring_actors",
    "film_genre",
    "film_origin"
  ],
  "additionalProperties": false
}
