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
Gene Brewer: Gene Brewer (born Eugene N. Brewer, 4 July 1937) is an American writer, the author of the K-PAX series of novels, about a man who claims to be a visiting extraterrestrial from a planet called K-PAX: "K-PAX" (1995), "On a Beam of Light" (2001), "K-PAX III: The Worlds of Prot" (2002), "" (2007) and "Prot's Report", a brief natural history of the Earth, which appears in "K-PAX: The Trilogy", an omnibus edition of the first three K-PAX books.  The first book in the series was made into a Universal Pictures film in 2001; it stars Kevin Spacey and Jeff Bridges.

L'Inhumaine: L'Inhumaine ("the inhuman woman") is a 1924 French drama-science fiction film directed by Marcel L'Herbier; it has the subtitle histoire féerique ("fairy story", "story of enchantment").  It was notable for its experimental techniques and for the collaboration of many leading practitioners in the decorative arts, architecture and music.  The film gave rise to much controversy on its release.

Man Facing Southeast: Man Facing Southeast (Spanish: Hombre mirando al sudeste ) is a 1986 Argentine drama-science fiction film written and directed by Eliseo Subiela and starring Lorenzo Quinteros and Hugo Soto.

Star Trek: Star Trek is an American science fiction media franchise based on the television series created by Gene Roddenberry.  The first television series, simply called "Star Trek" and now referred to as "", debuted in 1966 and aired for three seasons on the television network NBC.  It followed the interstellar adventures of Captain James T Kirk (William Shatner) and his crew aboard the starship USS "Enterprise", a space exploration vessel, built by the interstellar federal republic United Federation of Planets in the twenty-third century.  The "Star Trek" canon of the franchise includes "The Original Series", an animated series, five spin-off television series, and its film franchise in addition to further adaptations made in several media since the original.

K-PAX (film): K-PAX is a 2001 American science fiction-mystery film based on Gene Brewer's 1995 novel of the same name, directed by Iain Softley, starring Kevin Spacey, Jeff Bridges, Mary McCormack and Alfre Woodard.  Brewer's novel and the subsequent film are uncredited adaptations of the 1986 Argentinian film "Man Facing Southeast" by director, Eliseo Subiela.  The film is about a psychiatric patient who claims to be an alien from the planet K-PAX.  During his treatment, the patient demonstrates an outlook on life that ultimately proves inspirational for his fellow patients and especially for his psychiatrist.

Scarecrow &amp; Other Anomalies: Scarecrow & Other Anomalies, by Oliverio Girondo, is a collection of short prose poems written originally in Spanish.  "Scarecrow" inspired the feature film "The Dark Side of the Heart" (1994), directed by Eliseo Subiela.

The Effect of Love: The Effect of Love (Spanish: El resultado del amor) is a 2007 Argentinian drama film, written and directed by Eliseo Subiela, an Argentinian film director.  The film was shot in Buenos Aires and San Luis in Argentina.

K-PAX: K-PAX is an American science fiction novel by Gene Brewer, the first in the K-PAX series.

The Dark Side of the Heart: The Dark Side of the Heart (Spanish: El lado oscuro del corazón ) is a 1992 Argentine drama film directed by Eliseo Subiela.  The film was selected as the Argentine entry for the Best Foreign Language Film at the 65th Academy Awards, but was not accepted as a nominee.

The Adventures of God: The Adventures of God (Spanish: "Las Aventuras de Dios" ) is a 2000 Argentine fantasy drama film directed and written by Eliseo Subiela.

Question: What is a 1986 Argentine drama-science fiction film written and directed by Eliseo Subiela, that has uncredited adaptations made from it to  a 2001 American science fiction-mystery film based on Gene Brewer's 1995 novel ?

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
    "country_of_origin": {
      "type": "string",
      "description": "The country where the film was produced."
    },
    "genres": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of genres the film belongs to."
    },
    "director": {
      "type": "string",
      "description": "The director of the film."
    },
    "writer": {
      "type": "string",
      "description": "The writer of the film."
    },
    "uncredited_adaptations": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "adaptation_title": {
            "type": "string",
            "description": "The title of the uncredited adaptation."
          },
          "adaptation_type": {
            "type": "string",
            "description": "The type of the adaptation (e.g., 'film', 'novel')."
          },
          "adaptation_year": {
            "type": "integer",
            "description": "The release year of the adaptation."
          },
          "source_material_author": {
            "type": "string",
            "description": "The author of the source material for the adaptation."
          },
          "source_material_year": {
            "type": "integer",
            "description": "The release year of the source material for the adaptation."
          }
        },
        "required": [
          "adaptation_title",
          "adaptation_type",
          "adaptation_year",
          "source_material_author",
          "source_material_year"
        ],
        "additionalProperties": false
      },
      "description": "A list of works that are uncredited adaptations of this film."
    }
  },
  "required": [
    "film_title",
    "release_year",
    "country_of_origin",
    "genres",
    "director",
    "writer",
    "uncredited_adaptations"
  ],
  "additionalProperties": false
}
