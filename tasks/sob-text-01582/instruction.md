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
Jeremy Strong (actor): Jeremy Strong (born December 25, 1978) is an American film, television and stage actor.  He has appeared in many films that are based on true stories, including "Zero Dark Thirty", "Lincoln" (as John George Nicolay), "Parkland" (as Lee Harvey Oswald), "Selma" (as James Reeb), "Black Mass" and "The Big Short".

List of accolades received by Zero Dark Thirty: "Zero Dark Thirty" is a 2012 American action thriller directed and co-produced by Kathryn Bigelow with screenplay by Mark Boal.  The film was released in the United States on December 19, 2012, with a limited release at five theaters in Los Angeles and New York City.  It made $124,848 in its limited release weekend, making it one of the biggest limited mid-week openings ever.  As of March 6, 2013, "Zero Dark Thirty" has grossed a worldwide total of $106.8 million.  "Zero Dark Thirty" also received a high critical acclaim, accumulating an approval rating of 93% on the review aggregator site Rotten Tomatoes.

Serenity (upcoming film): Serenity is an upcoming American noir thriller-drama film directed and written by Steven Knight.  The film stars Matthew McConaughey, Anne Hathaway, Diane Lane, Jason Clarke, Djimon Hounsou, and Jeremy Strong.

Frank Grillo: Frank Anthony Grillo (born June 8, 1965) is an American actor known for his roles in films such as "Warrior" (2011), "The Grey" (2012), "End of Watch" (2012) and "Zero Dark Thirty" (2012).  He had his first leading role in the action horror film "" (2014), portraying Sergeant Leo Barnes, a role he reprised in "" (2016).  He also plays the Marvel supervillain Brock Rumlow / Crossbones in the Marvel Cinematic Universe, and Big Daddy in the Chinese action film "Wolf Warriors 2" (2017), the highest-grossing non-Hollywood film of all time.

Jason Clarke: Jason Clarke (born 17 July 1969) is an Australian film and television actor.  Clarke has appeared in many TV series, and is known for playing Tommy Caffee on the television series "Brotherhood."  He has also appeared in many films, often as an antagonist.  Some of his film roles include "Death Race" (2008), "Public Enemies" (2009), "Zero Dark Thirty" (2013), "White House Down" (2013), "Dawn of the Planet of the Apes" (2014), "Terminator Genisys" (2015) and "Everest" (2015).

Kathryn Bigelow: Kathryn Ann Bigelow ( ; born November 27, 1951) is an American director, producer, and writer.  Her films include the vampire Western horror film "Near Dark" (1987), the action crime film "Point Break" (1991), the science fiction action thriller "Strange Days" (1995), the mystery thriller "The Weight of Water" (2000), the submarine thriller "" (2002), the war film "The Hurt Locker" (2008), the action thriller war film "Zero Dark Thirty" (2012), the short film "Last Days" (2014), and the period crime drama "Detroit" (2017).  "The Hurt Locker" won the 2009 Academy Award for Best Picture and the BAFTA Award for Best Film, and was nominated for the 2010 Golden Globe Award for Best Drama.  She has also acted as producer and writer for many of her films.

Chris Pratt: Christopher Michael Pratt (born June 21, 1979) is an American actor.  Pratt came to prominence with his television roles; he is best known for his roles as Owen Grady in "Jurassic World", Jim Preston in "Passengers" and Andy Dwyer in the NBC sitcom "Parks and Recreation" from 2009–2015, for which he received critical acclaim and was nominated for the Critics' Choice Television Award for Best Supporting Actor in a Comedy Series in 2013.  He also starred earlier in his career as Bright Abbott in The WB drama series "Everwood" (2002–2006).  His early film career began with supporting roles in such mainstream films as "Wanted" (2008), "Jennifer's Body" (2009), "Moneyball" (2011), "The Five-Year Engagement" (2012), "Zero Dark Thirty" (2013), "Delivery Man" (2013), and "Her" (2013).

Martin Delaney (actor): Martin Delaney is a British actor, best known for his work in "Zero Dark Thirty", "Judas Ghost" and his lead role in British comedy film "Amar Akbar & Tony".

Scott Adkins: Scott Edward Adkins (born 17 June 1976) is an English actor and martial artist who is best known for playing Russian prison fighter Yuri Boyka in the 2006 film "" and its following two sequels: "" (2010) and "" (2016) and Casey Bowman in Ninja and its sequel .  He is also known for playing Bradley Hume in "Holby City", Lucian in "Doctor Strange", Kiley in "The Bourne Ultimatum" and John in "Zero Dark Thirty".  Adkins has also appeared in "EastEnders", "Hollyoaks", "Doctors" as well as starred in many direct-to-video films.

Harold Perrineau: Harold Perrineau (formerly Harold Williams; born August 7, 1963) is an American actor, known for the roles of Michael Dawson in the U.S. television series "Lost", Link in "The Matrix" films and games, Augustus Hill in the American television series "Oz", Damon Pope in the FX bike gang drama "Sons of Anarchy", and Mercutio in Baz Luhrmann's "Romeo + Juliet".  He starred in ABC's comedy-drama television series "The Unusuals", playing NYPD homicide detective Leo Banks and has appeared in several high-profile films, including "The Best Man", "28 Weeks Later", "", and "Zero Dark Thirty".  He also starred alongside Anthony Hopkins and Alec Baldwin in the survival drama "The Edge".

Question: The Steven Knight film, Serenity, stars this actor who had roles in "White House Down" and "Zero Dark Thirty"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor who meets all the specified criteria."
    },
    "films_involved_in": {
      "type": "array",
      "description": "A list of films the actor was involved in, relevant to the question.",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film."
          },
          "role_type": {
            "type": "string",
            "description": "The type of involvement (e.g., 'starring', 'role')."
          },
          "director": {
            "type": "string",
            "description": "The director of the film, if specified and relevant."
          },
          "release_year": {
            "type": "integer",
            "description": "The release year of the film."
          }
        },
        "required": [
          "title",
          "role_type"
        ],
        "additionalProperties": false
      }
    },
    "total_matching_films": {
      "type": "integer",
      "description": "The total count of films found that match the criteria (Serenity, White House Down, Zero Dark Thirty)."
    }
  },
  "required": [
    "actor_name",
    "films_involved_in",
    "total_matching_films"
  ],
  "additionalProperties": false
}
