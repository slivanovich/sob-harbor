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
Galaxie (band): Galaxie is a francophone indie garage rock band formed in 2002 in Montreal, Quebec, Canada.  Formerly known as Galaxie 500, they should not be confused with the American alternative rock band Galaxie 500.

Richard Ashcroft: Richard Paul Ashcroft (born 11 September 1971) is an English singer and songwriter.  He was the lead singer and occasional rhythm guitarist of the alternative rock band The Verve from their formation in 1990 until their original split in 1999.  He became a successful solo artist in his own right, releasing three UK top three solo albums.  The Verve reformed in 2007 but again broke up by summer 2009.  Ashcroft then founded a new band, RPA & The United Nations of Sound, and released a new album on 19 July 2010.  On 22 February 2016 Ashcroft announced his fourth solo album, "These People", set for release 20 May 2016.  Chris Martin of Coldplay has described Ashcroft as "the best singer in the world".

Dean Wareham: Dean Wareham (born 1 August 1963) is an American musician and actor who formed the band Galaxie 500 in 1987.  He left Galaxie 500 in April 1991 and founded the band Luna.  Since Luna's breakup in 2005, Wareham has released albums with fellow Luna bandmate (and wife) Britta Phillips (see Dean and Britta).  He also works as a film composer, notably on the Noah Baumbach film "The Squid and the Whale".  He released a self-titled album in 2014 and reformed Luna in 2015.

On Fire (Galaxie 500 album): On Fire is the second studio album by American alternative rock band Galaxie 500, released in 1989 on Rough Trade Records.  It was recorded at Noise NY in New York City with Mark Kramer handling production duties.  The "Rolling Stone Album Guide" called it Galaxie 500's "best album by far".

The Portable Galaxie 500: The Portable Galaxie 500 is a greatest hits studio album by the rock band Galaxie 500.  It was released in 1998 on Rykodisc.

Ford 300: The Ford 300 is an automobile which was built in the USA by Ford for the model year 1963 only.  It was the base trim level of the full-size 1963 Ford line below the Galaxie, Galaxie 500 & Galaxie 500XL.  It featured almost no chrome trim or luxury equipment and could be compared to the Chevrolet Biscayne in trim level.

Ford Galaxie: The Ford Galaxie is a full-sized car that was built in the United States of America by Ford for model years 1959 through to 1974.  The name was used for the top models in Ford's full-size range from 1958 until 1961, in a marketing attempt to appeal to the excitement surrounding the Space Race.  For 1962, all full-size Fords wore the Galaxie badge, with "500" and "500/XL" denoting the higher series.  The Galaxie 500/LTD was introduced for 1965 followed by the Galaxie 500 7-Litre for 1966.  The Galaxie 500 part was dropped from the LTD in 1966, and from the XL in 1967; however the basic series structuring levels were maintained.  The "regular" Galaxie 500 continued below the LTD as Ford's mid-level full-size model from 1965 until its demise at the end of the 1974 model year.

Uncollected: Uncollected is a compilation album by Galaxie 500, originally released in 1996 as a part of the Galaxie 500 box set.  It was later reissued as a single disc in 2004 by Rykodisc Records

Today (Galaxie 500 album): Today is the debut studio album by American dream pop band Galaxie 500.  It was released in 1988 on the independent label Aurora Records.

Galaxie 500: Galaxie 500 was an American alternative rock band that formed in 1987 and split up in 1991 after releasing three albums.

Question: What music genre do Richard Ashcroft and the band Galaxie 500 play?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artists_and_bands": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the artist or band."
          },
          "genres": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of music genres associated with the artist or band."
          }
        },
        "required": [
          "name",
          "genres"
        ],
        "additionalProperties": false
      },
      "description": "Details about the artists and bands mentioned in the question and their genres."
    },
    "all_unique_genres": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A comprehensive list of all unique music genres identified for the queried artists/bands."
    },
    "genre_summary": {
      "type": "string",
      "description": "A summary statement of the music genres played by the artists/bands."
    }
  },
  "required": [
    "artists_and_bands",
    "all_unique_genres",
    "genre_summary"
  ],
  "additionalProperties": false
}
