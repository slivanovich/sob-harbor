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
Flo Rida: Tramar Lacel Dillard (born September 17, 1979), better known by his stage name Flo Rida (pronounced ), is an American rapper, singer and songwriter from Carol City, Florida.  His 2008 breakout single "Low" was number one for 10 weeks in the United States and broke the record for digital download sales at the time of its release.

Florida City, Florida: Florida City is a city in Miami-Dade County, Florida, United States and is the southernmost municipality in the South Florida metropolitan area.  Florida City is primarily a Miami suburb and a major agricultural area.

Florida's Turnpike: Florida's Turnpike, designated as State Road 91 (SR 91) and the Ronald Reagan Turnpike, is a toll road in Florida, maintained by Florida's Turnpike Enterprise (FTE).  Spanning approximately 309 mi along a north–south axis, the turnpike is in two sections.  The SR 91 mainline runs roughly 265 mi , from its southern terminus at an interchange with Interstate 95 (I-95) in Miami Gardens to an interchange with I-75 in Wildwood at its northern terminus.  The Homestead Extension of Florida's Turnpike (abbreviated HEFT and designated as SR 821) continues from the southern end of the mainline for another 48 mi to US Highway 1 (US 1) in Florida City.

Only One Flo (Part 1): Only One Flo (Part 1) is the third studio album by American hip hop artist Flo Rida, which was released on November 30, 2010, through Atlantic Records, and his own label Poe Boy Entertainment.  The album was preceded by the singles "Club Can't Handle Me", and "Turn Around (5, 4, 3, 2, 1)" which were released in June, and November 2010 respectively.  The album received mixed reviews from critics, and peaked at number 107 on the "Billboard" 200, selling 11,000 copies in its first week in the US.  It is currently his least successful release.  It is also considerably short for a studio album, with 8 tracks which total up to less than 30 minutes.

C. Bette Wimbish: C. Bette Wimbish (March 24, 1924November 30, 2009) was one of the leading African-American woman activists in Florida promoting the desegregation of schools and civil equality.  A tough-minded woman who was determined to break the pattern of discrimination against African Americans in city employment practices, she was most commonly known as a civil rights activist, a politician, and the first African American on the St. Petersburg, Florida city council.  As well as being the first black person to hold modern elected office in the Tampa Bay area, Wimbish was also the first black female lawyer in Pinellas County, Florida.  She was the wife of Dr. Ralph Wimbish and the mother of three children: Barbara, Terry and Ralph Jr.

Who Dat Girl: "Who Dat Girl" is a song by American rapper Flo Rida.  It features American singer Akon.  The song was written by Flo Rida, Dr. Luke, Claude Kelly, Benny Blanco, Bruno Mars, and Philip Lawrence, and it was produced by Dr. Luke and Benny Blanco.  It was released on January 11, 2011 as the third single from Flo Rida's third studio album, "Only One Flo (Part 1)".  It peaked at number twenty-nine on the "Billboard" Hot 100.

Conch Republic: The Conch Republic is a micronation declared as a tongue-in-cheek secession of the city of Key West, Florida, from the United States on April 23, 1982.  It has been maintained as a tourism booster for the city since.  Since then, the term "Conch Republic" has been expanded to refer to "all of the Florida Keys, or, that geographic apportionment of land that falls within the legally defined boundaries of Monroe County, Florida, northward to 'Skeeter's Last Chance Saloon' in Florida City, Dade County, Florida, with Key West as the nation's capital and all territories north of Key West being referred to as 'The Northern Territories'.

Club Can't Handle Me: "Club Can't Handle Me" is a song by American recording artist Flo Rida featuring French producer David Guetta and Nicole Scherzinger (who is uncredited).  It was released as a digital download on iTunes on June 28, 2010 as the lead single of the "Step Up 3D" soundtrack album and is also included on Flo Rida's third studio album, "Only One Flo (Part 1)".

Homestead Extension of Florida's Turnpike: The Homestead Extension of Florida's Turnpike (HEFT), designated as State Road 821 (SR 821) and the Ronald Reagan Turnpike, is the southern extension of Florida's Turnpike, a toll road in Florida operated by Florida's Turnpike Enterprise (FTE).  Spanning approximately 48 mi along a north-south axis, it supplements the 265 mi "mainline" (designated as SR 91) to form the complete 309 mi turnpike.  The extension begins at its southern terminus at US Highway 1 (US 1) in Florida City, and transitions into the SR 91 mainline in Miramar at its northern end.  Despite their designations as different state roads, the mainline and the extension are continuous in their exit numbering.

Turn Around (5, 4, 3, 2, 1): "Turn Around (5, 4, 3, 2, 1)" is a song by American rapper Flo Rida from his third studio album, "Only One Flo (Part 1)".  It was released as the second single on 8 November 2010 in the United States.  The song contains samples of "Din Daa Daa" by German dance singer George Kranz, and "Oh Yeah" by Swiss electronica band Yello.  It debuted at number 98 on the "Billboard" Hot 100 and was featured prominently in the closing credits of "The Hangover Part II".  It was the second such use of a Flo Rida song in the closing credits of a film from "The Hangover" franchise—the first was "Right Round", which also featured DJ Frank E and was used in the closing credits of "The Hangover".

Question: Only One Flo was an album by the rapper from what Florida city?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_title": {
      "type": "string",
      "description": "The title of the album mentioned in the question."
    },
    "artist_name": {
      "type": "string",
      "description": "The stage name of the artist who released the album."
    },
    "artist_origin": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the artist is from."
        },
        "state": {
          "type": "string",
          "description": "The state where the artist is from."
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "album_title",
    "artist_name",
    "artist_origin"
  ],
  "additionalProperties": false
}
