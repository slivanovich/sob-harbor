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
Deni Hines: Dohnyale "Deni" Sharon Hines (born 4 September 1970) is an Australian solo artist who has been releasing music since the early 1990s, with chart success in Australia, New Zealand, Japan and Europe.  She is the daughter of Marcia Hines.

Ian Cooper (violinist): Ian Cooper (born 14 August 1970) is an Australian violinist.  He was commissioned to compose and perform the for the opening ceremony of the Games of the XXVII Olympiad in Sydney.  The event was televised worldwide with an estimated 2.85 billion viewers.  He performs many musical styles including Classical, Gypsy, Jazz, Irish & Country music and has appeared with Tommy Emmanuel, James Morrison, Olivia Newton-John, Barry White, Simon Tedeschi, Deni Hines, and Silverchair.

Imagination (Deni Hines album): Imagination is the debut studio album by Australian singer songwriter, Deni Hines.

Water for Chocolate: Water for Chocolate is the second studio album by Deni Hines.  Released in August 2006, it was her first album to be released independently.  Three singles were released from the album: "Water for Chocolate", "Son of a Preacher Man" and "5 Days of Rain".  Hines toured the album in 2007.

I Like the Way (Deni Hines song): "I Like the Way" is a song by Australian singer songwriter, Deni Hines.  The song was released in January 1996 as the third single from her debut studio album, "Imagination" (1996).  The single missed the top fifty in Australia, but peaked at number 37 in the United Kingdom and at number 4 on the Dance Club Songs in the United States.

A Delicious Collection: A Delicious Collection is the first compilation album by Australian singer songwriter, Deni Hines.  The album was released in June 2002.

The Other Woman (Deni Hines and James Morrison album): The Other Woman (Deni Hines and James Morrison album)

Louise Wener: Louise Jane Wener (born 30 July 1966, Gants Hill, London) is an English writer, songwriter, singer and guitarist of the band Sleeper.  Sleeper recorded three full-length albums: "Smart", "The It Girl", and "Pleased to Meet You".

The Soul Sessions (Deni Hines album): The Soul Sessions is the fourth studio album by ARIA Award winner, singer songwriter, Deni Hines.  The album was recorded at Hercules Street Studio and Kings X Music studios and is due for release worldwide on November 18, 2016.

Remix Your Imagination: Remix Your Imagination is the first remix album by Australian singer songwriter, Deni Hines.  The album was released in Japan in November 1997 and in Australia in July 1998.

Question: Louise Wener and Deni Hines, are both of which musical occupation?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artists": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "occupations": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "name",
          "occupations"
        ],
        "additionalProperties": false
      }
    },
    "common_musical_occupation": {
      "type": "string"
    },
    "number_of_artists": {
      "type": "integer"
    }
  },
  "required": [
    "artists",
    "common_musical_occupation",
    "number_of_artists"
  ],
  "additionalProperties": false
}
