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
In certi momenti: In certi momenti ("At Certain Times") is the third album by Italian pop/rock singer Eros Ramazzotti, produced by Piero Cassano and released in 1987 on the BMG label.

In ogni senso: In ogni senso ("In Every Sense") is the fifth album by Italian pop/rock singer Eros Ramazzotti, produced by Piero Cassano and released in April 10, 1990 on the BMG label.  "In ogni senso" topped the Italian Albums chart and was Ramazzotti's most successful album internationally to that point, also reaching #2 in Europe's second-largest music sales market, Germany.

Stilelibero: Stilelibero ("Freestyle") is the eighth studio album by Italian pop/rock singer Eros Ramazzotti, released in 2001 on the BMG label.  The album, featuring three tracks produced by Trevor Horn and two by Rick Nowels, was recorded in a variety of locations in London, California and Italy.  "Stilelibero" topped the Italian albums chart, as did "Fuoco nel fuoco" the singles chart. " Più che puoi", a duet with Cher, also reached the Italian top 20.

Eros (Eros Ramazzotti album): Eros is the first greatest hits album by Italian pop/rock singer Eros Ramazzotti, released in 1997 on the BMG label.  Of the album's 16 tracks, five are original recordings, nine re-recordings and two new tracks.  Two of the re-recorded tracks are duets; "Musica è" featuring Andrea Bocelli and "Cose della vita (Can't Stop Thinking of You)" with Tina Turner.  "Eros" topped the albums chart in six countries.

Musica è: Musica è (English: "Music Is" ) is a mini album and the fourth album recorded by Italian "pop/rock" singer-songwriter Eros Ramazzotti, produced by Piero Cassano and was released in 1988 on the BMG label.  Two versions of the album exist: a five track release and an expanded eight track version, which includes two remixed tracks from Ramazzotti's previous album "In certi momenti".

Eros Ramazzotti: Eros Walter Luciano Ramazzotti (born 21 May 1964) is an Italian musician and singer-songwriter.  Ramazzotti is popular in Italy and most European countries, and throughout the Spanish-speaking world, as he has released most of his albums in both Italian and Spanish.

Dove c'è musica: Dove c'è musica ("Where There Is Music") is the seventh studio album by Italian pop/rock singer Eros Ramazzotti, released in 1996 on the BMG label.  It is Ramazzotti's first self-produced album and the first without any involvement from long-time collaborator Piero Cassano.  "Dove c'è musica" was Ramazzotti's most successful album to that point, topping the Albums chart in six countries including Italy and Germany and selling an estimated 4,200,000 copies.

Nuovi eroi: Nuovi eroi ("New Heroes") is the second album by Italian pop/rock singer Eros Ramazzotti, produced by Piero Cassano and released in 1986 on the BMG label.

Più bella cosa: "Più bella cosa" (] ; meaning "Fairer Thing") is an Italian language song written by singer Eros Ramazzotti, with Claudio Guidetti, Maurizio Fabrizio, Adelio Cogliati and performed by Ramazzotti in February 1996, as a first single and pre-release from his album "Dove c'è musica" ("Where There's Music") that came out on May 13 of that year.

Cuori agitati: Cuori agitati ("Troubled Hearts") is the debut album by Italian pop/rock singer Eros Ramazzotti, produced by Piero Cassano and released in 1985 on the BMG label.

Question: Dove c'è musica ("Where There Is Music") is the seventh studio album by Italian pop/rock singer Eros Walter Luciano Ramazzotti, released in 1996 on which label , he has released most of his albums in both Italian and Spanish?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_title": {
      "type": "string",
      "description": "The title of the album."
    },
    "artist_name": {
      "type": "string",
      "description": "The full name of the artist."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the album was released."
    },
    "record_label": {
      "type": "string",
      "description": "The record label on which the album was released."
    },
    "artist_releases_in_multiple_languages": {
      "type": "boolean",
      "description": "Indicates if the artist releases most of his albums in both Italian and Spanish."
    }
  },
  "required": [
    "album_title",
    "artist_name",
    "release_year",
    "record_label",
    "artist_releases_in_multiple_languages"
  ],
  "additionalProperties": false
}
