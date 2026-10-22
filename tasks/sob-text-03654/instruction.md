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
Sung Tongs: Sung Tongs is the fifth studio album by American experimental pop band Animal Collective, released on May 3, 2004 by FatCat Records.  "Sung Tongs" is generally considered to be Animal Collective's breakthrough release; it generated much praise from critics upon its release and was featured in best-of lists at the end of 2004 and the decade of the 2000s.

The Painters: The Painters is the eighth EP by American experimental pop band Animal Collective, released on February 17, 2017.  It is the first extended play released by the band since "Monkey Been to Burn Town" (2013).  The EP serves as a companion to their 2016 studio album, Painting With.

LD &amp; the New Criticism: LD & the New Criticism was an American experimental pop band

Meeting of the Waters (EP): Meeting of the Waters is the ninth EP by American experimental pop band Animal Collective, released first on Record Store Day, April 22, 2017.  It is the second extended play released by the band in 2017.  The EP was recorded live on location in the Amazon Rainforest.  It is notable for containing many recordings of animal calls and some sounds being recorded underwater, as well as being documented in the Viceland series "Earth Works".  This is the band's first release to feature only Avey Tare (David Portner) and Geologist (Brian Weitz).

Strawberry Jam: Strawberry Jam is the seventh studio album by American experimental pop band Animal Collective.  It was released in September 2007, the band's first on Domino Records.  The album charted on the Billboard Top 200, debuting and peaking at #72.

Peacebone: "Peacebone" is a single (and later an EP) by American experimental pop band Animal Collective, released on August 13, 2007 by Domino Records.  It was issued in advance of the group's 2007 album, "Strawberry Jam".  The single version contains "Safer" as a B-side, while the EP contains two additional remixes of "Peacebone" by Black Dice and Pantha du Prince, respectively.

Avey Tare: David Michael Portner (born April 24, 1979), also known by his moniker Avey Tare, is a musician and songwriter who co-founded the American experimental pop band Animal Collective.  He has released two solo albums, as well as three collaborative albums with Panda Bear (Noah Lennox), all of which were later retroactively classified under Animal Collective's discography.

Bandstand Busking: Bandstand Busking is a project based in London, England showcasing musicians on some of the city's underused bandstands.  The sessions are recorded and shown for viewing on the Bandstand Busking website.  The first session was recorded in March 2008 with the artist Stars of Sunday League and since then over 30 acts have performed in bandstands for the project including local bands such as Fanfarlo and Alessi's Ark and some from further afield such as Of Montreal and Black Lips.

Painting With: Painting With is the tenth studio album by American experimental pop band Animal Collective, released on February 19, 2016.  The album is a follow-up to "Centipede Hz" (2012), and features contributions from John Cale and Colin Stetson.  It peaked at No. 46 on the "Billboard" 200.  Three singles were issued: "FloriDada" (2015), "Lying in the Grass", and "Golden Gal" (both 2016).  A companion EP, "The Painters", was released the following year.

Of Montreal: of Montreal is an American experimental pop band from Athens, Georgia.  It was founded by frontman Kevin Barnes in 1996, named after a failed romance between Barnes and a woman "of Montreal."  The band is identified as part of the Elephant 6 collective.  Throughout its existence, of Montreal's musical style has evolved considerably and drawn inspiration from numerous 1960s psychedelic pop acts.

Question: Which American experimental pop band was showcased in London for the Bandstand Busking project?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the American experimental pop band."
    },
    "band_origin_country": {
      "type": "string",
      "description": "The country of origin of the band."
    },
    "band_genre": {
      "type": "string",
      "description": "The musical genre of the band."
    },
    "project_name": {
      "type": "string",
      "description": "The name of the project where the band was showcased."
    },
    "project_location_city": {
      "type": "string",
      "description": "The city where the project is based."
    },
    "project_location_country": {
      "type": "string",
      "description": "The country where the project is based."
    }
  },
  "required": [
    "band_name",
    "band_origin_country",
    "band_genre",
    "project_name",
    "project_location_city",
    "project_location_country"
  ],
  "additionalProperties": false
}
