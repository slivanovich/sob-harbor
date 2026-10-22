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
Songs by Sam Cooke: Sam Cooke, better known as Songs by Sam Cooke (as shown on the back cover), is the debut studio album by American singer-songwriter Sam Cooke.  The backing band is the Bumps Blackwell Orchestra.

Sam Cooke discography: The discography of Sam Cooke, an African-American recording artist, singer-songwriter and entrepreneur, consists of fifteen studio albums (including one collaborative album and two notable posthumous releases), two live albums, and numerous compilations.  Over the course of his eight-year career, Cooke placed 29 singles in the Top 40 on the "Billboard" Pop Singles chart.  He also placed 20 singles in the Top Ten of "Billboard"'s R&B chart, Black Singles chart.  Between 1957 and 1960, Sam Cooke's records were produced on the Keen label.  From 1960 through 1966, they were produced on the RCA label.

Front (magazine): Front is a British men's magazine.  First published by Cabal Communications in 1998, it was created to rival IPC's publication "Loaded", catering to a demographic of 16- to 25-year-old males.  It began as part of the British "lads' mag" genre of magazines though the covers rejects this description with the statement "Front is no lads' mag".

We Remember Sam Cooke: We Remember Sam Cooke is the fifth studio album recorded by The Supremes, issued by Motown in April 1965 (see 1965 in music).  The album is a tribute album dedicated to soul musician Sam Cooke, who had died the previous December.  Notable selections on the album, consisting entirely of Cooke covers, included covers of "A Change Is Gonna Come", "You Send Me" and "(Ain't That) Good News" (led by Florence Ballard).

Sam Cooke (model): Sam Cooke (born 19 November 1985) is an English glamour model and Page 3 girl from Manchester.  Cooke has appeared in numerous British "lads' mags", including "FHM", "FRONT", "Maxim", "Loaded", "Zoo" and "Nuts" in the UK, as well as on several covers around the world.

Swing Low (album): Swing Low, also known as Sam Cooke, is the seventh studio album by American singer-songwriter Sam Cooke.  Produced by Hugo & Luigi, the album was released in March 1961 in the United States by RCA Victor.  The album includes the hit single "Chain Gang".

The Best of Sam Cooke: The Best of Sam Cooke is the second greatest hits album by American singer-songwriter Sam Cooke.  Produced by Hugo & Luigi, the album was released in 1962 in the United States by RCA Victor.  The compilation contains most of Sam Cooke's most well-known hits from 1957 to 1962.

Colin Meloy Sings Sam Cooke: Colin Meloy Sings Sam Cooke is a tour-only EP by Colin Meloy, lead singer of The Decemberists.  It is the third in a series of EPs featuring covers of influential artists, which includes works of Morrissey ("Colin Meloy Sings Morrissey") and Shirley Collins ("Colin Meloy Sings Shirley Collins").  The album was released to accompany his 2008 solo tour, and features five covers of songs previously performed by the American gospel, R&B, soul, and pop singer Sam Cooke.  Four songs were written or co-written by Cooke; one, "Summertime," is a pop standard that Cooke had performed in 1957.  The artwork of the album was designed by Carson Ellis, who has done much of the artwork for The Decemberists, and all of Colin Meloy's solo work.  The EP also includes vocals from Laura Gibson.

Sam Cooke at the Copa: Sam Cooke at the Copa is the first live album by American singer-songwriter Sam Cooke.  The album was released in October 1964 in the United States by RCA Victor.

The Wonderful World of Sam Cooke: The Wonderful World of Sam Cooke is the fourth studio album by American singer-songwriter Sam Cooke.

Question: What is the name of the magazine that featured Sam Cooke and is a British men's magazine?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "magazine": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the magazine."
        },
        "country_of_origin": {
          "type": "string",
          "description": "The country where the magazine is from."
        },
        "target_demographic": {
          "type": "string",
          "description": "The demographic the magazine caters to."
        }
      },
      "required": [
        "name",
        "country_of_origin",
        "target_demographic"
      ],
      "additionalProperties": false
    },
    "featured_person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person featured in the magazine."
        },
        "occupation": {
          "type": "string",
          "description": "The occupation of the featured person."
        }
      },
      "required": [
        "name",
        "occupation"
      ],
      "additionalProperties": false
    },
    "is_lads_mag_genre": {
      "type": "boolean",
      "description": "Indicates if the magazine is part of the 'lads' mag' genre."
    }
  },
  "required": [
    "magazine",
    "featured_person",
    "is_lads_mag_genre"
  ],
  "additionalProperties": false
}
