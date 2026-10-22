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
Gasolin' (1974 album): Gasolin' is the first album with English lyrics by rock band Gasolin' in an attempt to win the band recognition outside their native Denmark.  It is almost identical to their third Danish album, "Gasolin' 3" and was released in some Western European countries in the beginning of 1974 on CBS.  It failed to make impact on the charts anywhere, but didn't stop Gasolin' from issuing three more albums in English in the period from 1974 to 1978.

A Foreign Affair II: A Foreign Affair 2 is double compilation album released by Danish rock band Gasolin' in 2002.

Gasolin' (disambiguation): Gasolin' was a Danish rock band.

Gasolin': Gasolin' was a Danish rock band from Christianshavn in Copenhagen formed by Kim Larsen, Franz Beckerlee and Wili Jønsson in 1969.  Their first drummer was the late Bjørn Uglebjerg.  He was replaced by Søren Berlev in 1971.  At the formation the guitar playing of Franz Beckerlee was inspired by Jimi Hendrix and the singing and lyrics of Larsen was inspired by Bob Dylan, while the rhythm playing of Jønsson and Berlev owed much to The Beatles.  However, they would soon develop their own musical style.  The pop sensibility of Kim Larsen, the artistic attitude of Franz Beckerlee and the musical competence of Wili Jønsson would prove to be a recipe for success.  Gasolin's lyrics were generally written by the entire group, often with the assistance of friend Mogens Mogensen.

Kim Larsen: Kim Melius Flyvholm Larsen (born 23 October 1945) is a Danish rock musician.

Gasolin' (album): Gasolin' (also called "Gas 1") is the debut studio album by Danish rock band Gasolin'.  It was released in November 1971 by CBS Records.  Instead of boogie rock and catchy tunes, they relied on creating songs with a moody feel such as "Langebro", "Fra dag til dag" and "Tremastet beton".  The latter is recited by the poet Mogens Mogensen.  Lead singer Kim Larsen later jokingly referred to the song as the first Danish rap.  The lyrics and the music has a dark and mysterious ambience.  From this album "Langebro" was released on single with "Lilli-Lilli" on the b-side.

Gasolin' 3: Gasolin' 3 was the third album from Danish rock band Gasolin', released in November 1973.  It was the band's first album to be produced by Roy Thomas Baker.  "Gasolin' 3" was recorded in Rosenberg Studio in Copenhagen with Freddy Hansson as sound engineer.

Gør det noget: Gør det Noget is Danish Rock group Gasolin's seventh studio album.  When Gasolin' released "Gør det Noget" in November 1977 (translation: "does it matter" or "so what"), they knew it was their last album.  After the ambitious "Gas 5" and "Efter endnu en dag", Gasolin' decided to make a garage-rock album.  Therefore, the service of Roy Thomas Baker was not needed and "Gør det Noget" was produced by Gasolin' and "Rocco" Tommy Bogs.

What a Lemon: What a Lemon is an album by Danish rock band Gasolin', released 1 August 1976 on Epic Records in the United States, some parts of Europe, Japan and Australia.  It is the third of four albums with English lyrics that Gasolin' released between 1974 and 1978 in an attempt to break the international music market.  The album received good reviews from leading American rock critics, but lack of airplay and the fact that the record company invested only small efforts in promotion and distribution meant that it never earned the band the public acclaim it was striving for.

The Last Jim: The Last Jim is the second album with English lyrics by Danish rock band Gasolin'.  It was released in some Western European countries in November 1974 on CBS, simultaneously to its Danish counterpart Stakkels Jim.  The songs are identical on the two albums, except for the lyrics.  Like on their previous album Gasolin' of the same year, American Leonard "Skip" Malone, helped the band translate the Danish lyrics into English.

Question: When was the founder of the Danish rock band, Gasolin, born?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the rock band."
    },
    "founder_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the band's founder."
        },
        "role": {
          "type": "string",
          "description": "The role of the person in the band, e.g., founder, lead singer."
        },
        "birth_date": {
          "type": "string",
          "description": "The birth date of the founder in 'DD Month YYYY' format."
        }
      },
      "required": [
        "name",
        "role",
        "birth_date"
      ],
      "additionalProperties": false
    },
    "question_answered": {
      "type": "boolean",
      "description": "Indicates if the question about the founder's birth date was successfully answered."
    }
  },
  "required": [
    "band_name",
    "founder_details",
    "question_answered"
  ],
  "additionalProperties": false
}
