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
We Meet at Tove's: We Meet at Tove's (Danish: Så mødes vi hos Tove ) is a 1946 Danish drama directed by Alice O'Fredericks and Grete Frische.  The film stars an ensemble cast, including Illona Wieselmann, Gull-Maj Norin, Helle Virkner and Inger Stender in a story about eight women who meet ten years after their high school graduation to discuss the reality of their lives.  It has been noted as one of the first Danish films which focused on women and women's rights.

That's Me, Too: Sådan er Jeg Osse or That's Me, Too is a 1980 Danish drama film directed and written by Lise Roos.  It was the last film to star Inger Stender.

Sandra Hüller: Sandra Hüller (born April 30, 1978) is a German actress.  She gained critical praise for her portrait of Anneliese Michel in Hans-Christian Schmid's drama "Requiem," and is best known internationally for her starring role in Maren Ade's comedy "Toni Erdmann."  Hüller is one of the era-defining German actresses of her generation.  Besides Julia Jentsch and Nina Hoss, she is the only German actress to win both the European film award and the Silver Bear for Best Actress, top honors of the European Film Academy and Berlin Film Festival, respectively, in the 21st century.

Hanna Schygulla: Hanna Schygulla (born 25 December 1943) is a German actress and chanson singer.  Long associated with the theater and film director Rainer Werner Fassbinder, for whom she first worked in 1965, she is generally considered the most prominent German actress of the New German Cinema.  She won the 1979 Berlin Silver Bear for Best Actress for Fassbinder's "The Marriage of Maria Braun", and the 1983 Cannes Film Festival Award for Best Actress for the Marco Ferreri film "The Story of Piera".

Glasflügel BS-1: The Glasflügel BS-1, sometimes called the Björn Stender BS-1 or the Stender BS-1, is a West German, high-wing, single seat, T-tailed, FAI Open Class glider that was designed by Björn Stender and produced by Glasflügel.

Marlene Dietrich: Marie Magdalene "Marlene" Dietrich ( , ] ; 27 December 1901 – 6 May 1992) was a German actress and singer who held both German and American citizenship.  Throughout her unusually long career, which spanned from the 1910s to the 1980s, she maintained popularity by continually reinventing herself.

Odds 777: Odds 777 is a 1932 Danish family film directed by George Schnéevoigt.  The film stars Liva Weel and Inger Stender.

Inger Stender: Inger Stender (1912–1989) was a Danish actress of stage, film and television whose sophisticated elegance and classic beauty earned her the description of Denmark's version of Marlene Dietrich.

Hotel Paradis: Hotel Paradis is a 1931 Danish drama directed by George Schnéevoigt.  The film, based on a novel by Einar Rousthøj, stars Eyvind Johan-Svendsen and Inger Stender.  The film was also known as "Hotel Paradisets hemlighed" ("The Secret of the Paradise Hotel").

Susanne Uhlen: Susanne Uhlen (b. January 17, 1955 in Potsdam, Germany) is a German actress.  She is the daughter of actor Wolfgang Kieling, best known as being the voice of "Bert", of the "Sesame Street" duo Bert and Ernie, and German actress Gisela Uhlen, niece to German actor Max Schreck of "Nosferatu" fame.

Question: Inger Stender earned the description of being Denmark's version of what German actress?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "danish_actress": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the Danish actress."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the Danish actress."
        },
        "death_year": {
          "type": "integer",
          "description": "The death year of the Danish actress."
        }
      },
      "required": [
        "name",
        "birth_year",
        "death_year"
      ],
      "additionalProperties": false
    },
    "german_actress": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the German actress she was compared to."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the German actress."
        },
        "death_year": {
          "type": "integer",
          "description": "The death year of the German actress."
        }
      },
      "required": [
        "name",
        "birth_year",
        "death_year"
      ],
      "additionalProperties": false
    },
    "reason_for_comparison": {
      "type": "string",
      "description": "The specific attributes that led to the comparison."
    }
  },
  "required": [
    "danish_actress",
    "german_actress",
    "reason_for_comparison"
  ],
  "additionalProperties": false
}
