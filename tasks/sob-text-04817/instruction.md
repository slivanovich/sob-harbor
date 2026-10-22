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
Program Playhouse: Program Playhouse was an anthology television series aired on the DuMont Television Network on Wednesdays from June 22 to September 14, 1949.

It's Supposed to be Thicker than Water: "It's Supposed to be Thicker than Water" is the twenty-second episode of the popular 1969 ITC British television series Randall and Hopkirk (Deceased) starring Mike Pratt, Kenneth Cope and Annette Andre.  The episode was first broadcast on 13 February 1970 on the ITV.  Directed by Leslie Norman.

Dody Goodman: Dolores "Dody" Goodman (October 28, 1914 – June 22, 2008) was an American character actress, known for her playing the mother of the title character (played by Louise Lasser) in the television series "Mary Hartman, Mary Hartman".  Her high-pitched voice could be heard announcing the show's title at the beginning of each episode.  She also played in more roles in film and television through the years as well as some voice acting in the television series Alvin and the Chipmunks, the film The Chipmunk Adventure, the direct-to-video film Alvin and the Chipmunks Meet the Wolfman, and as the voice for Mrs. Lisburn, a minor character in the 2006 video game Bully, from Rockstar Games.

Thicker than Water (2005 film): Thicker than Water is a television film starring Melissa Gilbert and Lindsay Wagner.  It premiered on Hallmark Channel on March 12, 2005.

Lindsay Wagner: Lindsay Jean Wagner (born June 22, 1949) is an American film and television actress, model, author, singer, acting coach, and adjunct professor.  Wagner is best known for her portrayal of the 1970s television leading female science fiction action character Jaime Sommers, who takes on special high-risk government missions using her superhuman bionic powers in the American television series "The Bionic Woman" (1976–1978).  She first played this role on the 1970s American television series "The Six Million Dollar Man".  The Jaime Sommers character also became a pop culture icon of the 1970s.  In the late 1980s and early 1990s, she reprised the role in several bionic reunion television movies.

Porsha Williams: Porsha Dyanne Williams (born June 22, 1981), also known by her former married name Porsha Stewart, is an American television personality, model, actress and singer.  Born and raised in Atlanta, Georgia, she modeled for music videos and calendar spreads in her early adulthood.  In 2011, she came to prominence after marrying football player Kordell Stewart in an elaborate ceremony broadcast on the television series "Platinum Weddings", although they experienced a widely publicized divorce in 2013.  In 2012, Williams was cast in the fifth season of the reality television series "The Real Housewives of Atlanta".  In 2014, she launched a career in the music industry with the launch of her single "Flatline" under the record label Kandi Koated Entertainment.  Williams was a contestant on the eighth installment of the reality competition series, "The Celebrity Apprentice", now known as "The New Celebrity Apprentice".  She played for the charity "Hosea".  On January 23, 2017, she was the eighth contestant fired, finishing in 8th place and raising no money for her charity.

Thicker Than Water (TV series): Thicker Than Water is an American reality television series that premiered on November 10, 2013, on Bravo.  The series chronicles the family dynamic of former professional basketball player and an American gospel-jazz instrumentalist Ben Tankard, his wife Jewel and their children.  Bravo previously aired a pilot titled "Thicker Than Water: The Marinos" in August 2011 that had the same premise but centered on a different family.

Sound of Colors (TV series): Sound of Colors is a Chinese and Taiwanese romance television series, based on the comic book of the same name by famous Taiwanese illustrator Jimmy Liao.  It first broadcast on June 10, 2006 in Taiwan, followed by subsequent broadcasts in other Asian countries.  A film version starring Tony Leung and Miriam Yeung was made in 2003, but the TV drama and the film have completely different storylines.  While the television series is adapted from Liao's illustrations, the content of the TV version of "Sound of Colors" varies, as the plot is thicker.

Thicker than Water (audio drama): Thicker than Water is a Big Finish Productions audio drama based on the long-running British science fiction television series Doctor Who.  It is a sequel to the earlier audio play "Arrangements for War".

Aaron Brink: Aaron Brink (born November 11, 1974) is an American professional mixed martial artist and former boxer currently competing for the Gladiator Challenge promotion where he is their current Interim Heavyweight Champion.  Aaron has competed in the UFC, King of the Cage, Gladiator Challenge, RINGS and the World Extreme Cagefighting.  Brink was cast in the movie Thicker Than Water, filmed and released in 2006 in Iceland and Shipwrecked on a Great Lake, a movie released exclusively in Canada.  Aaron also briefly had a career acting in hardcore pornographic films under the name "Dick Delaware", beginning sometime in 2000 and ending in June 2005, this was first revealed after he appeared in a notorious episode of himself during a methamphetamine addiction filmed for the television series Intervention in 2006.

Question: What actress, born on June 22, 1949 stars in the television series "Thicker than Water"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The name of the actress."
    },
    "actress_birth_date": {
      "type": "string",
      "format": "date",
      "description": "The birth date of the actress in YYYY-MM-DD format."
    },
    "related_production": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the production the actress starred in."
        },
        "type": {
          "type": "string",
          "description": "The type of the production (e.g., 'television film', 'television series')."
        },
        "role_description": {
          "type": "string",
          "description": "A description of the actress's role in the production."
        }
      },
      "required": [
        "title",
        "type",
        "role_description"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actress_name",
    "actress_birth_date",
    "related_production"
  ],
  "additionalProperties": false
}
