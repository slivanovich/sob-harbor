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
Through the Glass (EP): Through the Glass is an extended play by Australian alternative rock band Atlas Genius.  It was released on 12 June 2012 by Warner Bros.  Records.

So Electric: When It Was Now (The Remixes): So Electric: When It Was Now (The Remixes) is a remix album by Australian alternative rock band Atlas Genius.  It was released as a 12" vinyl exclusively available at record stores on 29 November 2013.  The vinyl is limited to 3,000 copies and includes a digital download card.  The album was scheduled to be released digitally on 24 December 2013; it was ultimately released one week earlier on 17 December.  This album contains remixes of songs from Atlas Genius' debut studio album, "When It Was Now".

Atlas Genius discography: The discography of Australian alternative rock band Atlas Genius consists of two studio album, two remix albums, three extended plays, seven singles and six music videos.

Molecules Remix EP: Molecules Remix EP is an extended play (EP) and remix album by Australian alternative rock band Atlas Genius.  It was released on 13 November 2015 by Warner Bros.  Records.

Bleeker (band): Bleeker, formerly known as Bleeker Ridge, are a Canadian rock band from Orillia, Ontario, consisting of Taylor Perkins, Cole Perkins and Mike Vandyk.

When It Was Now: When It Was Now is the debut studio album by Australian alternative rock band Atlas Genius, released on 19 February 2013 by Warner Bros.  Records.  The album peaked at No. 34 on Billboard 200.  It also reached No. 10 on the Top Alternative Albums chart.  The only single from the album, "If So", reached No. 8 on the "Billboard" Alternative Songs chart.  It has sold 79,000 copies in the United States as of August 2015.

Trojans (song): Trojans is the debut single of Australian alternative rock band Atlas Genius.  It is from the extended plays "Through the Glass" and "Trojans", and later appeared on their debut studio album "When It Was Now" (2013).

Inanimate Objects: Inanimate Objects is the second studio album by Australian alternative rock band, Atlas Genius, released through Warner Bros.  Records on 28 August 2015.  It peaked at No. 150 on the "Billboard" 200, and dropped off the chart in the following week.  Their first album, "When It Was Now" (2013) had peaked at No. 34.

Trojans (EP): Trojans is an extended play by Australian alternative rock band Atlas Genius.  It was released as a 10" vinyl exclusively available in the United Kingdom on 25 February 2013.  The vinyl is limited to 300 copies.

Atlas Genius: Atlas Genius are an alternative rock band formed in Adelaide, South Australia in November 2009.  The band's mainstay members are the Jeffery brothers, Keith on lead vocals and lead guitar; Michael on drums; and Darren Sell on keyboard.  Their debut album, "When It Was Now", was issued on 9 February 2013 and peaked at No. 34 on the United States "Billboard" 200.  In 2013 two of their singles appeared on the related Alternative Songs Chart, "Trojans" (released in May 2011) at No. 4 and "If So" (February 2013) at No. 8.  In 2013 the group toured the US in April and May, United Kingdom in May, and back to the US in August.

Question: Are Atlas Genius and Bleeker both rock bands?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_names": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Names of the bands mentioned in the question."
    },
    "atlas_genius_is_rock_band": {
      "type": "boolean",
      "description": "Indicates if Atlas Genius is identified as a rock band."
    },
    "bleeker_is_rock_band": {
      "type": "boolean",
      "description": "Indicates if Bleeker is identified as a rock band."
    },
    "both_are_rock_bands": {
      "type": "boolean",
      "description": "The final answer to whether both bands are rock bands."
    }
  },
  "required": [
    "band_names",
    "atlas_genius_is_rock_band",
    "bleeker_is_rock_band",
    "both_are_rock_bands"
  ],
  "additionalProperties": false
}
