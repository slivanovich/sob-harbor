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
Britney Spears: Britney Jean Spears (born December 2, 1981) is an American singer, dancer, and actress.  Born in McComb, Mississippi, and raised in Kentwood, Louisiana, she performed acting roles in stage productions and television shows as a child before signing with Jive Records in 1997.  Spears's first and second studio albums, "...Baby One More Time" (1999) and "Oops! ... I Did It Again" (2000), became international successes, with the former becoming the best-selling album by a teenage solo artist.  Title tracks "...Baby One More Time" and "Oops! ... I Did It Again" broke international sales records.  In 2001, Spears released her self-titled third studio album, "Britney", and played the starring role in the film "Crossroads" (2002).  She assumed creative control of her fourth studio album, "In the Zone" (2003), which yielded the worldwide success of the single "Toxic".

Mickey Mouse March: "(The) Mickey Mouse (Club) March", is the opening theme for "The Mickey Mouse Club" television show, which aired in the United States from October 1955 to 1959, on the ABC television network.  (The first two lines are: "Who’s the leader of the Club that’s made for you and me?  M-I-C-- K-E-Y-- M-O-U-S-E!")  The song is reprised with the slower "it's time to say goodbye" verse, at the end of each episode.  In the show's opening, the song is partially performed by the characters Dumbo and Jiminy Cricket.  It also ended with Donald Duck attempting to hit a gong with the "Mickey Mouse Club" title on it, but would end with comic results, such as him getting hit by lightning, or the gong turning out to be a pie, or Donald just hitting a triangle instead.

Christina Aguilera videography: American singer Christina Aguilera has released five video albums and been featured in thirty-three music videos, five films, thirteen television programs, and seven commercials.  Aguilera achieved early fame in 1993 and 1994 when she appeared in the Disney Channel television series "The New Mickey Mouse Club", which co-starred her contemporaries Britney Spears, Justin Timberlake, and Ryan Gosling.  In 1999, she rose to prominence with her eponymous debut album, whose singles "Genie in a Bottle", "What a Girl Wants", "I Turn to You" and "Come On Over Baby (All I Want Is You)" all received their music videos.  The videos for the Spanish versions of the four singles were subsequently released in conjunction with the promotion of Aguilera's 2000 Spanish album "Mi Reflejo".  In 2001, Aguilera appeared in the music video for "Lady Marmalade", a collaboration with Mýa, Lil' Kim, and Pink, which earned two MTV Video Music Awards for Video of the Year and Best Video from a Film at the 2001 ceremony.

Justin Timberlake videography: American entertainer Justin Timberlake has released four video albums and has been featured in thirty-seven music videos, seventeen films, fifteen television shows, and six commercials.  He achieved early fame when he appeared in the Disney Channel television series "The New Mickey Mouse Club", alongside singers Britney Spears and Christina Aguilera and actor Ryan Gosling.  Timberlake rose to fame in the late 1990s as the lead singer of the boy band NSYNC.  In 2002, he launched his solo career and released his solo debut single "Like I Love You", the music video for which was directed by Bucky Chrome.  Francis Lawrence directed the video for "Cry Me a River".  The video features Timberlake's character as he spies on a former lover, who according to the director portrays his former romantic interest Spears.  At the 2003 MTV Video Music Awards, the video won the accolades for Best Male Video and Best Pop Video.

Tony Lucca: Anthony James Lucca (born January 23, 1976), is an American singer, songwriter, producer, and actor.  He is perhaps best known for starting his career on "The Mickey Mouse Club".  After the Mickey Mouse Club, Lucca went to Los Angeles, California, for a brief career as an actor, then became a full-time musician.  He is a consistent touring artist and has toured with a multitude of acts, including Maroon 5, Kelly Clarkson, *NSYNC, Marc Anthony, Josh Hoge, Sara Bareilles, Matt Duke, Tyrone Wells, and the late Chris Whitley.  He was the second runner-up on the second season (2012) of the American reality television singing competition talent show, "The Voice", broadcast on NBC.

Just Be Free: Just Be Free is a demo album released by Warlock Records featuring music recorded by American recording artist Christina Aguilera.  After finishing her run on "The New Mickey Mouse Club", a then fifteen-year-old Aguilera began recording the album with New Jersey-based producers Roberts Alleca and Michael Brown.  The pair gave Aguilera the opportunity to use a recording studio and presented her with demo music with the understanding that they could use the material for their own purpose, but also claiming they would not commercially release the recordings.  Musically, the album consisted of dance style tracks as well as ballads, and saw Aguilera performing in Spanish language songs.  The record was conceived to showcase Aguilera's vocals in an effort to reach out to record labels, a venture which actually backfired after the recordings were not very well received among critics.  Six years after the completion of the album and Aguilera had achieved mainstream success, Brown and Allecca released the record and "Just Be Free" has sold over 128,000 copies in the United States.

Hidden Mickey: A Hidden Mickey is a representation of Mickey Mouse that has been inserted subtly into the design of a ride, attraction, or other location in a Disney theme park, Disney properties, animated film, feature-length movie, TV series, or other Disney product.  The most common Hidden Mickey is a formation of three circles that may be perceived as the silhouette of the head and ears of Mickey Mouse, often referred to by Disney aficionados as a "Classic Mickey".  Mickeys may be painted, made up of objects (such as rocks, or three plates on a table), or be references such as someone wearing Mickey Mouse Club ears in a painting.  Hidden Mickeys can take on many sizes and forms.

Christina Aguilera: Christina María Aguilera (born December 18, 1980) is an American singer, songwriter, actress and television personality.  Born in Staten Island, New York and raised in Rochester and Wexford, Pennsylvania, she appeared on the television series "Star Search" and "The Mickey Mouse Club" in her early years.  After recording "Reflection", the theme for Disney's 1998 film "Mulan", Aguilera signed with RCA Records.  She rose to prominence with her 1999 self-titled debut album that spawned the "Billboard" Hot 100 number-one singles "Genie in a Bottle", "What a Girl Wants", and "Come On Over Baby (All I Want Is You)".  The following year, Aguilera released two studio albums; the Spanish-language album "Mi Reflejo" and the holiday album "My Kind of Christmas".

Jimmie Dodd: James Wesley Dodd (March 28, 1910 – November 10, 1964), better known as Jimmie Dodd, was best known as the MC of the popular 1950s Walt Disney television series "The Mickey Mouse Club," as well as the writer of its well-known theme song, "The Mickey Mouse Club March."  A slowed-down version of this march, with different lyrics, became the "alma mater" that closed the show.

Come On Over Baby (All I Want Is You): "Come On Over Baby (All I Want Is You)" is a song by American singer Christina Aguilera, taken from her debut studio album "Christina Aguilera".  It was released on September 26, 2000 by RCA Records as the fourth and final single from the album, and was the first where she was given significant creative control.  The song was written by Johan Aberg, Paul Rein, Christina Aguilera, Ron Fair, C. Blackmon, R. Cham, E. Dawkins, Shelly Peiken, and Guy Roche; a re-recorded version included a rapped verse written by Aguilera.  Lyrically, it sees Aguilera eyeing a prospective boyfriend.

Question: What McComb, Mississippi native starred with Christina Aguilera on "The New Mickey Mouse Club"

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the individual."
    },
    "birthplace": {
      "type": "string",
      "description": "The city and state where the person was born."
    },
    "television_show": {
      "type": "string",
      "description": "The name of the television show they appeared in."
    },
    "co_star_name": {
      "type": "string",
      "description": "The name of the co-star mentioned in the question."
    },
    "role_description": {
      "type": "string",
      "description": "A description of their role or involvement in the show."
    }
  },
  "required": [
    "person_name",
    "birthplace",
    "television_show",
    "co_star_name",
    "role_description"
  ],
  "additionalProperties": false
}
