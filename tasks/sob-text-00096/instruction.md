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
Frontier of the Dawn: Frontier of the Dawn (French: La Frontiere de l'Aube ) is a 2008 French drama film directed by Philippe Garrel.  The film stars Louis Garrel, Laura Smet, and Clémentine Poidatz and was photographed by cinematographer William Lubtchansky in black and white.  It premiered at the 2008 Cannes Film Festival in competition.

Stephan Elliott: Stephan Elliott (born 27 August 1964) is an Australian film director and screenwriter.  His best-known film internationally is "The Adventures of Priscilla, Queen of the Desert" (1994).

Clotilde Hesme: Clotilde Hesme (born 30 July 1979) is a French actress, best known for playing Lilie in Philippe Garrel's "Regular Lovers" and Alice in Christophe Honoré's "Love Songs".  She is also known for the role of Adèle from the TV series "Les Revenants".

Philippe Garrel: Philippe Garrel (] ; born 6 April 1948) is a French director, cinematographer, screenwriter, film editor and producer, associated with New Wave movement.  His films have won him awards at the prestigious Cannes Film Festival and Venice Film Festival.

Le vent de la nuit: Le Vent de la nuit ("Night Wind" in English) is a French drama film that came out in 1999, starring Catherine Deneuve and directed by Philippe Garrel, with a score by John Cale.  It tells a story of transient loves and willed deaths, in which a callow young man abandons an older woman and loses a wiser friend.

Anémone: Anémone (Anne Bourguignon ), born 9 August 1950, is a French actress, filmmaker and political activist.  She took her stage name in 1968 from the title of her film debut in Philippe Garrel's "Anémone".

Arlette Langmann: Arlette Langmann (born on April 3, 1946) is a French screenwriter, film editor and production designer.  Born in Paris to Jewish immigrant parents from Romania and Poland, Langmann is best known for her long-running collaborations with her brother Claude Berri, Maurice Pialat, and Philippe Garrel.

Regular Lovers: Regular Lovers (French: Les Amants réguliers ) is a 2005 French independent coming-of-age romantic drama film directed by Philippe Garrel and starring his son, actor Louis Garrel.  The director's father, actor Maurice Garrel, has a supporting role.

La Naissance de l'amour: La Naissance de l'amour is a 1993 drama film directed by Philippe Garrel.  Garrel also wrote the screenplay together with his long-time collaborators Muriel Cerf and Marc Cholodenko.

A Burning Hot Summer: A Burning Hot Summer (pre-release title: That Summer) is a 2011 drama film directed by Philippe Garrel, starring Monica Bellucci, Louis Garrel, Céline Sallette, and Jérôme Robart.  Its original French title is Un été brûlant, which means "A burning summer".  The film portrays a tempestuous relationship between an actress and a painter.

Question: Between Stephan Elliott and Philippe Garrel who was born earlier?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_a_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_year": {
          "type": "integer"
        },
        "birth_month": {
          "type": "string"
        },
        "birth_day": {
          "type": "integer"
        }
      },
      "required": [
        "name",
        "birth_year",
        "birth_month",
        "birth_day"
      ],
      "additionalProperties": false
    },
    "person_b_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_year": {
          "type": "integer"
        },
        "birth_month": {
          "type": "string"
        },
        "birth_day": {
          "type": "integer"
        }
      },
      "required": [
        "name",
        "birth_year",
        "birth_month",
        "birth_day"
      ],
      "additionalProperties": false
    },
    "earlier_born_person_name": {
      "type": "string",
      "description": "The name of the person who was born earlier."
    },
    "earlier_born_person_birth_year": {
      "type": "integer",
      "description": "The birth year of the person who was born earlier."
    },
    "comparison_summary": {
      "type": "string",
      "description": "A summary statement comparing the birth dates of the two individuals."
    }
  },
  "required": [
    "person_a_details",
    "person_b_details",
    "earlier_born_person_name",
    "earlier_born_person_birth_year",
    "comparison_summary"
  ],
  "additionalProperties": false
}
