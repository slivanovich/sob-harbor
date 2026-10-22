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
To Die like a Man: To Die like a Man (Portuguese: Morrer Como Um Homem ) is a 2009 Portuguese drama film directed by João Pedro Rodrigues, produced by the production company Rosa Filmes.

The Ornithologist (film): The Ornithologist (original title: O Ornitólogo) is a 2016 Portuguese film directed by João Pedro Rodrigues.  It was released in 2016.

Two Drifters: Two Drifters (also known as Odete) is a Portuguese feature film directed by João Pedro Rodrigues, produced at the independent production company Rosa Filmes and released in 2005.

João Pedro Mendes Silva: João Pedro Mendes Silva, known as João Pedro (born 27 July 1989) is a Portuguese football player who plays for Vizela.

João Pedro Guerra Cunha: João Pedro Guerra Cunha (born 4 May 1986 in Figueira de Castelo Rodrigo, Guarda), known as João Pedro, is a Portuguese professional footballer who plays for Cypriot club Apollon Limassol as a midfielder.

A Última Vez Que Vi Macau: A Última Vez Que Vi Macau is a 2012 Portuguese film directed by João Pedro Rodrigues and João Rui Guerra da Mata.  It will be in competition for the Golden Leopard at the 2012 Locarno International Film Festival.  It was shot in Macau.

João Pedro (Brazilian footballer): João Pedro Geraldino dos Santos Galvão (born 9 March 1992), commonly known as João Pedro, is a Brazilian professional footballer who plays for Cagliari Calcio as an attacking midfielder.

João Pedro Sousa Silva: João Pedro Sousa Silva (born 13 November 1996 in Ponta Delgada, Azores), known as João Pedro, is a Portuguese professional footballer who plays for Gil Vicente F.C. as a forward.

João Pedro Rodrigues: João Pedro Rodrigues is a Portuguese film director.  He is considered to be part of "The School of Reis" film family.

Maurice Pialat: Maurice Pialat (] ; 31 August 1925 – 11 January 2003) was a French film director, screenwriter and actor noted for the rigorous and unsentimental style of his films.  His work is often described as being "realist", though many film critics acknowledge that it does not fit the traditional definition of realism.

Question: What career did Maurice Pialat and João Pedro Rodrigues share?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "careers": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "name",
        "careers"
      ],
      "additionalProperties": false
    },
    "person_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "careers": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "name",
        "careers"
      ],
      "additionalProperties": false
    },
    "shared_career": {
      "type": "string"
    }
  },
  "required": [
    "person_1",
    "person_2",
    "shared_career"
  ],
  "additionalProperties": false
}
