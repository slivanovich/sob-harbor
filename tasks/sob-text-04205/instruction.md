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
Dear Mom, Love Cher: Dear Mom, Love Cher is a 2013 American television documentary about Georgia Holt, the mother of singer and actress Cher.  The film recounts Cher's family history and features in-depth interviews with her, Holt, Holt's other daughter Georganne LaPiere, and Holt's grandchildren, from Cher, Chaz Bono and Elijah Blue Allman.  It premiered on Lifetime on May 6, 2013.  The worldwide VOD/DVD release was on September 24, 2013, the same release date as Cher's 25th studio album, "Closer to the Truth".  P. David Ebersole directed the film, and Todd Hughes was the producer.

Lacey Schwimmer: Lacey Mae Schwimmer (born June 28, 1988) is an American ballroom dancer and singer.  She is best known as a fourth place finalist of the third season of "So You Think You Can Dance".  She is the daughter of noted dancer Buddy Schwimmer, as well as the cousin of Heidi Groskreutz, who placed fourth on the second season of "So You Think You Can Dance" and younger sister of Benji Schwimmer, the winner of the show's second season.  She participated in the seventh season of "Dancing with the Stars" as a professional dancer paired with Lance Bass of 'N Sync, in the eighth season of the show paired with "Jackass" star Steve-O and in the ninth season paired with actor and Iron Chef America host Mark Dacascos.  Schwimmer returned to "Dancing with the Stars" for its eleventh season and she was partnered with Disney Channel star Kyle Massey and in the 12th season, paired with radio host Mike Catherwood.  In the thirteenth season, she was paired with transgender activist Chaz Bono.  Schwimmer did not return for season 14 of "Dancing With The Stars'.

Rod Nash Racing: Rod Nash Racing is a V8 Supercar racing entity, owned by Rod Nash.  The current driver is Chaz Mostert.  Nash owns a V8 Supercar Racing Entitlement Contract and his #55 entry is currently run by Prodrive Racing Australia, utilising a Ford FG X Falcon.

Elijah Blue Allman: Elijah Blue Allman (born July 10, 1976), known professionally as P. Exeter Blue, is an American musician, and the son of singer Cher and her second husband Gregg Allman.  He is a half-brother of Chaz Bono, Delilah Allman, Michael Allman, Layla Allman, and Devon Allman.

The Lair: The Lair is an American gay-themed vampire television series produced by here!  in 2007.  The first season, consisting of six episodes, wrapped production in January of that year.  The first two episodes premiered on June 1, 2007.  Season 2, consisting of 9 episodes debuted on September 5, 2008.  A third season of 13 episodes was announced in September 2008 and Colton Ford confirmed that filming took place in October and November 2008.  Season 3 premiered September 4, 2009.

Naked Fame: Naked Fame a documentary that follows Colton Ford's transition from the world of gay pornography to that of a mainstream singer.  It opened on February 18, 2005 in the United States to mixed critical reviews.

Colton Ford: Colton Ford (born October 12, 1962, in Pasadena, California) is the stage name of the former American gay pornographic actor, Glenn Soukesian, who returned to his original career path of singer, and actor.  As of May 2007, he resides in New York City.

Chaz Bono: Chaz Salvatore Bono (born Chastity Sun Bono, March 4, 1969) is an American advocate, writer, musician and actor.  He is the child of American entertainers Sonny Bono and Cher.

American Horror Story: Cult: American Horror Story: Cult is the seventh season of the FX horror anthology television series "American Horror Story".  The season was picked up on October 4, 2016, and premiered on September 5, 2017.  The season will consist of a total of 11 episodes.  Returning cast members from previous seasons include: Sarah Paulson, Evan Peters, Cheyenne Jackson, Adina Porter, Frances Conroy, Mare Winningham, Emma Roberts, Chaz Bono, John Carroll Lynch and James Morosini, along with new cast members Billie Lourd and Alison Pill.

Chaz Mostert: Chaz Mostert (born 10 April, 1992) is an Australian professional racing driver competing in the Virgin Australia Supercars Championship.  He currently drives the No. 55 Ford FG X Falcon for Rod Nash Racing.  Mostert was the winner of the 2014 Bathurst 1000 and has also previously won the 2010 Australian Formula Ford Championship.

Question: Are both Chaz Bono and Colton Ford singers?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question posed."
    },
    "individuals_evaluated": {
      "type": "array",
      "description": "Details for each individual mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "is_singer_or_musician": {
            "type": "boolean",
            "description": "True if the individual is identified as a singer or musician in the context."
          },
          "context_source": {
            "type": "string",
            "description": "The specific context where the information about being a singer/musician was found."
          }
        },
        "required": [
          "name",
          "is_singer_or_musician",
          "context_source"
        ],
        "additionalProperties": false
      }
    },
    "both_are_singers": {
      "type": "boolean",
      "description": "The final answer to whether both individuals are singers."
    }
  },
  "required": [
    "question_asked",
    "individuals_evaluated",
    "both_are_singers"
  ],
  "additionalProperties": false
}
