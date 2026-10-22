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
Footloose (musical): Footloose is a 1998 musical based on the 1984 film of the same name.  The music is by Tom Snow (among others), the lyrics by Dean Pitchford (with additional lyrics by Kenny Loggins), and the book by Pitchford and Walter Bobbie.

Mike Gomez: Mike Gomez (born April 18, 1951) is an American actor.  Best known for his performances in such cult classics as "The Big Lebowski" and "", Gomez has costarred in numerous films including "Heartbreak Ridge" and "Milagro Beanfield War", "Zoot Suit", "The Border" and "El Norte", to name a few.  His TV credits include "Bones", "The Shield", "Desperate Housewives", and a series regular role as 'Capt. Gallardo' on the NBC series, "Hunter", among others.  On stage, Gomez' numerous theater credits include "Zoot Suit" at the Winter Garden on Broadway and the Pre-Broadway run of "Selena".

Ben Wright (American actor): Ben Wright (born September 3, 1969) is best known for originating the role of "Jack" in the Tony Award-winning musical "Into the Woods".  Wright's professional acting career started with George C. Wolfe's Off-Broadway production of "Paradise" at Playwrights Horizons.  He then went on to originate leading roles on Broadway in Stephen Sondheim's "Into The Woods" and the Tony nominated "State Fair", for which he received a Drama Desk Nomination.  He also created the role of Nanki Poo in Hot Mikado at the Ford's Theater in Washington, D.C. He has worked extensively with some of Broadway’s greatest talents, including Stephen Sondheim, James Lapine, Bernadette Peters, James Hammerstein, Paul Gemignani and Joanna Gleason.  Wright's feature film credits include the Academy Award winning "Born on the Fourth of July" with Tom Cruise as well as Penny Marshall's "Renaissance Man" with Danny DeVito.  Wright's television credits include starring opposite Judd Nelson in NBC's "" and the ABC drama series "Capital News" with Lloyd Bridges and Helen Slater.  Wright has performed at the Tony Awards two times and can be heard on several albums, including the original cast recording of State Fair and the Grammy Award winning recording of "Into the Woods".

Catherine Cox (actress): Catherine Cox is an American actress.  A regular on the Broadway stage in the 1980s, Cox's credits include the original Ethel McCormack in the production of "Footloose", the musical "Oh Coward! ", for which she was nominated for a Tony Award for Best Performance by a Leading Actress in a Musical, and "Baby (musical)" for which she won the Drama Desk Award.  Other Broadway credits include roles in "Rumors", "Music Is", "Whoopee! ", "Barnum", and "One Night Stand".  Cox has also worked extensively in regional theaters across the United States and in Off-Broadway productions in New York.  Off-Broadway she has appeared in productions of William Finn's "In Trousers", "Rap Master Ronnie", "By Strouse", "It's Better With A Band" and "The Waves".  Cox's regional credits include the role of Oolie in the LA production of "City of Angels" among others.  Her television appearances include "The Cosby Show", "Law & Order", "The Guiding Light", "Edge of Night" and "Loving" among others.  She is married to composer/musical director, David Evans and has two sons, Joe and Henry.

Sutton Foster: Sutton Lenore Foster (born March 18, 1975) is an American actress, singer and dancer.  She is known for her work on the Broadway stage, for which she has received two Tony Awards for Best Performance by a Leading Actress in a Musical, in 2002 for her role as Millie Dillmount in "Thoroughly Modern Millie", and in 2011 for her performance as Reno Sweeney in "Anything Goes".  Her other Broadway credits include "Little Women", "The Drowsy Chaperone", "Young Frankenstein", "Shrek the Musical", and "Violet".  On television, Foster played the lead role in the short-lived ABC Family comedy-drama "Bunheads" from 2012 to 2013.  Since March 2015, she has starred in the TV Land comedy-drama "Younger".

Ronn Carroll: Ronn Carroll is an American actor known primarily for his work on Broadway, with over twenty credits to his name.  Career highlights include "Oklahoma! ," directed by Trevor Nunn, "How To Succeed in Business Without Really Trying" with Matthew Broderick, and two productions of "Annie Get your Gun" with both Ethel Merman and Bernadette Peters.  Other Broadway credits include the original casts of "On Golden Pond", "Crazy for You" and "Steel Pier.

Dennis Courtney: Denis Beaulne (born April 30, 1958), better known by his stage name Dennis Courtney, is an American stage director, choreographer, actor and teacher of master classes in auditioning for the theatre.  As a director, he is notable for winning the 2008 Israeli National Theatre Prize (Israel's TONY Award equivalent) for his work in the Cameri Theatre production of Fiddler On The Roof, in Tel Aviv.  The production closed on January 27, 2016 after a near 8-year run.  As an actor, he made his Broadway debut in the 1979 production of Peter Pan with Sandy Duncan and George Rose.  Subsequent Broadway/National Tour/Production credits include Shenandoah with John Raitt (1984), Joseph And The Amazing Technicolor Dreamcoat (1984), Roza (1987) and Starlight Express (1989-1990).  He directed and choreographed a production of My Way, for the Riverside Center Theatre in Virginia and It Shoulda Been You starring Kim Zimmer and for Gretna Theatre in July and August 2016.  In early 2017, he directed and choreographed Kiss Me, Kate at Kent State.  In March 2017 he directed the pre-Broadway workshop production of The Last Adam, a new musical by George Alex Livings and Jonathan Hickey.  He has collaborated with playwright David Brian Colbert on a new play with music about the life of legendary performer, Ethel Waters, entitled .  The play is currently in development.

Jason Tam: Jason Tam (born June 28, 1982) in Honolulu, Hawaii is an actor and dancer.  His most notable roles include Markko Rivera on the daytime soap opera "One Life to Live", Paul in the 2006 revival of the Broadway musical "A Chorus Line", Xander in "Lysistrata Jones" on Broadway and Shoe on the teen drama "Beyond the Break".  His other stage performances include "Les Misérables" on Broadway, "She Loves Me" at The Guthrie Theatre, "West Side Story," "Oklahoma! ," "Footloose" the Sacramento Music Circus, and "King and I" at Casa Manana.  He is also a frequent collaborator with musical theatre writer Joe Iconis.  In 2014 he joined the original cast of the Tom Kitt and Brian Yorkey collaboration "If/Then" at the Richard Rodgers Theater as David.  He played the role for the entire run of If/Then.  He can be heard on the 2014 "Broadway’s Carols for a Cure" album.

Footloose (song): "Footloose" is a song co-written and recorded by American singer-songwriter Kenny Loggins.  It was released in January 1984 as the first of two singles by Loggins from the 1984 film of the same name (the other one being "I'm Free (Heaven Helps the Man)").  The song spent three weeks at number one, March 31—April 14, 1984 on the US "Billboard" Hot 100, and was the first of two number-one hits from the film.  "Billboard" ranked it at the No. 4 song for 1984.

Renée Elise Goldsberry: Renée Elise Goldsberry (born January 2, 1971) is an American actress, singer and songwriter, known for originating the role of Angelica Schuyler Church in the Broadway musical "Hamilton", for which she won the 2016 Tony Award for Best Featured Actress in a Musical.  Her other Broadway credits include Nettie Harris in the original Broadway cast of "The Color Purple", Mimi Márquez in "Rent", and Nala in "The Lion King".  She has portrayed many roles on television, including Geneva Pine on "The Good Wife", and Evangeline Williamson on "One Life to Live", for which she received two Daytime Emmy Award for Outstanding Supporting Actress in a Drama Series nominations.

Question: Catherine Cox is an American actress, and was a regular on the Broadway stage in the 1980s, Cox's credits include the original Ethel McCormack in the production of "Footloose", a musical, released in which year, based on the 1984 film of the same name?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The name of the actress mentioned in the question."
    },
    "musical_title": {
      "type": "string",
      "description": "The title of the musical."
    },
    "musical_release_year": {
      "type": "integer",
      "description": "The release year of the musical."
    },
    "film_basis_year": {
      "type": "integer",
      "description": "The release year of the film the musical is based on."
    },
    "role_played": {
      "type": "string",
      "description": "The role played by the actress in the musical."
    }
  },
  "required": [
    "actress_name",
    "musical_title",
    "musical_release_year",
    "film_basis_year",
    "role_played"
  ],
  "additionalProperties": false
}
