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
Gaetana: Gaetana is the debut album by Italian pop singer Giusy Ferreri,

Silvia Olari (album): Silvia Olari is the debut album by Italian pop singer Silvia Olari.  The album was released on March 27, 2009, by Warner Bros.  Records.  Luca Jurman collaborated as musician and arranger for all the cd.  Nek wrote the first single "Fino all'Anima".

Stai Fermo Lì: "Stai fermo lì" is a song by Italian pop singer Giusy Ferreri, released as third single from her debut album "Gaetana", the song was written and produced by Italian Pop-R&B singer Tiziano Ferro.

Novembre (song): "Novembre" is a song by Italian pop singer Giusy Ferreri, released as second single from her debut album "Gaetana".  It was written by Roberto Casalino and produced by Tiziano Ferro.

Michele Bravi: Michele Bravi (born 19 December 1994) is an Italian pop singer .  He rose to fame after winning the seventh series of the Italian "X Factor".  His coronation song, "La vita e la felicità", was penned by Tiziano Ferro and, after being released as his debut single, it reached the top spot of the Italian Singles Chart.  Bravi's debut album, "A passi piccoli", was released in June 2014.

Sexy Girl (Sabrina song): "Sexy Girl" is a song by Italian pop singer Sabrina.  It was released in August 1986 by Baby Records as the first single from her debut album "Sabrina".  Produced by Claudio Cecchetto, the song became a top 20 hit in her native Italy and was also successful two years later as a remixed version in Finland.

Tutt'al più: Tutt'al più (English:"At most") is a song by Italian pop singer Laura Pausini.  The song was composed by Angelo Valsiglio and Pietro Cremonesi and written by Roberto Casini.  The song is translated into Spanish under the title ¿Por qué no? .  The song was released as a promotional single from her debut album "Laura Pausini".

Gala (singer): Gala (born Gala Rizzatto, 6 September 1975) is an Italian pop singer and songwriter that lives in Brooklyn, New York.  Gala has sold over six million records worldwide.  Her debut album "Come Into My Life" included the multiplatinum singles "Freed from Desire", "Let a Boy Cry" and "Come Into My Life" which reached the Top 3 in music charts across Europe, South America, Russia and the Middle East.

Come into My Life (Gala song): "Come into My Life" is a song written and recorded by the Brooklyn-based Italian singer-songwriter Gala.  It was released in November 1997 as the third single from her first album, "Come into My life".  The song achieved success in Europe, South America, Russia and Middle East.

La differenza tra me e te: "La differenza tra me e te" is a pop song written by Italian pop singer Tiziano Ferro.  It was released as the first single from his fifth album "L'amore è una cosa semplice" (2011) and achieved success in Italy, where it was certified double platinum by the Federation of the Italian Music Industry, and in Belgium.  A Spanish-language version of the song was also released.  Titled "La diferencia entre tú y yo", it served as the first single from "El amor es una cosa simple", the Spanish edition of Ferro's fifth studio album.

Question: What is the debut album of this Italian pop singer and songwriter who wrote and recorded the song "Come into My Life?"

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "singer_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "nationality": {
          "type": "string"
        },
        "role": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "name",
        "nationality",
        "role"
      ],
      "additionalProperties": false
    },
    "debut_album": {
      "type": "string"
    },
    "associated_song": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "release_year": {
          "type": "integer"
        },
        "is_debut_album_single": {
          "type": "boolean"
        }
      },
      "required": [
        "title",
        "release_year",
        "is_debut_album_single"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "singer_details",
    "debut_album",
    "associated_song"
  ],
  "additionalProperties": false
}
