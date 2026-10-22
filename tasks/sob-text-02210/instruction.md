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
Tyler Perry's House of Payne: Tyler Perry's House of Payne is an American sitcom television series created and produced by playwright, director, and producer Tyler Perry.  The show revolved around a multi-generational family living under one roof in Atlanta led by patriarch Curtis Payne and his wife Ella.  The show premiered in syndication on June 21, 2006, and new episodes of a retooled version were broadcast exclusively on TBS from June 6, 2007, until August 10, 2012.  While primarily a comedy sitcom, "House of Payne" was known for featuring dark themes and subject matter, such as substance abuse and addiction.  It also had elements of slapstick.  The storyline of the show is serialized, with many references to past episodes, creating a continuing story arc.

Izzy Ellis: Isadore Ellis (1910–1994), credited as I. Ellis and known throughout the animation industry as Izzy Ellis, was an American animator best known for working for Warner Bros.  Cartoons under the Bob Clampett & Frank Tashlin units.  Ellis had a long career in the animation industry, which started at Ub Iwerks Studio in 1935.  After three years, Ellis moved to Leon Schlesinger Productions, where he worked under the Clampett B/W unit, under the Ray Katz management.  Ellis continued to animate in the B/W unit under the supervision of Norman McCabe, and eventually Frank Tashlin.  Ellis reunited with Clampett after Robert McKimson took over Tashlin's unit.  However, Ellis relocated to McKimson's unit after Art Davis took over the Clampett unit.  In 1948, Ellis left to do commercial work.

Meet the Browns (TV series): Tyler Perry's Meet the Browns is an American sitcom created and produced by playwright, director, and producer Tyler Perry.  The show initially revolved around Mr. Brown running a senior citizens' home in Decatur, Georgia, with his daughter Cora Simmons, but as the show progressed, this idea was gradually phased out and it became a typical family sitcom about a multigenerational clan living under one roof.  The show premiered on Wednesday, January 7, 2009 and finished its run on November 18, 2011 on TBS.  It is made in the model of his play and film of the same name.  The show stars David Mann and Tamela Mann, who starred in the earlier stage play and motion picture.

Possessory credit: A possessory credit in filmmaking is the use of a film credit which gives primary artistic recognition to a single person – usually (but not always) the film's director.  Examples include "A Stanley Kubrick film" ("The Shining"), "A film by Quentin Tarantino" ("Pulp Fiction"), and "Alfred Hitchcock's Psycho" ("Psycho").  Possessory credit is also sometimes used in television programs, for example "Tyler Perry's House of Payne" (Tyler Perry's TBS sitcom "House of Payne").  Occasionally another word besides "film" is used such as "A Spike Lee Joint" or "A Martin Scorsese Picture".  Possessory credit may also be given to the films producer, an example of this is "Steven Spielberg presents Back To The Future".

Anita M. Cal: Anita M. Cal (born October 14, 1966) is an American author, TV Writer, film producer, and international speaker best known for writing on the TBS family comedies, Tyler Perry's House of Payne and Tyler Perry's Meet the Browns.  Cal first made a name for herself as the Writer/Producer of the comedy feature Kinfolks, developed by Showtime, Inc., starring In The House TV daughter Maia Campbell.  Cal is also known as, A.M. Cal, the author of the December 2015 historical novel, Eighth Wonder: The Thomas Bethune Story, the true tale of a slave born blind, feeble, and left for dead who began playing Mozart at the age of three.  The debut novel was awarded a SELF-e Highlighted Book by Library Journal and made available in libraries throughout the 50 states.

List of Tyler Perry's House of Payne episodes: "Tyler Perry's House of Payne" is an American comedy-drama television series created and produced by playwright, director, and producer Tyler Perry.  The show revolved around a multi-generational family living under one roof in Atlanta led by patriarch Curtis Payne and his wife Ella.  The show premiered in syndication on June 21, 2006, and new episodes were broadcast exclusively on TBS from June 6, 2007, until August 10, 2012.  While primarily a comedy sitcom, "House of Payne" was known for featuring dark themes and subject matter, such as substance abuse and addiction.  It also had elements of slapstick.  The storyline of the show is serialized, with many references to past episodes, creating a continuing story arc.

The Single Moms Club: The Single Moms Club (also known as Tyler Perry's The Single Moms Club) is a 2014 American comedy-drama film produced, written, and directed by Tyler Perry.  The film stars Nia Long, Wendi McLendon-Covey, Zulay Henao, Cocoa Brown, Amy Smart, Terry Crews, and Perry.  The film was released on March 14, 2014.

The Fuller Brush Girl: The Fuller Brush Girl is a 1950 slapstick comedy starring Lucille Ball and directed by Lloyd Bacon.  Animator Frank Tashlin wrote the script.  Ball plays a quirky door-to-door cosmetics saleswoman for the Fuller Brush Company.  The film also stars Eddie Albert and has an uncredited cameo by Red Skelton (who had starred in the Tashlin-scripted "The Fuller Brush Man" two years earlier).

Tyler Perry: Tyler Perry (born Emmitt Perry Jr.; September 13, 1969) is an American actor, comedian, filmmaker, writer, and songwriter, specializing in the gospel genre.  Perry wrote and produced many stage plays during the 1990s and early 2000s.  In 2011, "Forbes" named him the highest paid man in entertainment; he earned US$130 million between May 2010 and 2011.  With new shows lined up, along with older successful shows, his net worth in 2017 is estimated to be $600 million.

Frank Tashlin: Francis Fredrick von Taschlein (February 19, 1913 – May 5, 1972), better known by his stage name Frank Tashlin, was an American animator, screenwriter, and film director.  He was also known as Tish Tash and Frank Tash.

Question: Which man, Frank Tashlin or Tyler Perry, was an American animator, screenwriter, and film director, also known as Tish Tash? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_identified": {
      "type": "string",
      "description": "The name of the person who matches the description."
    },
    "roles": {
      "type": "array",
      "description": "A list of professions or roles attributed to the identified person.",
      "items": {
        "type": "string"
      }
    },
    "aliases": {
      "type": "array",
      "description": "A list of other names or stage names the identified person was known by.",
      "items": {
        "type": "string"
      }
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation of why this person was identified based on the context."
    }
  },
  "required": [
    "person_identified",
    "roles",
    "aliases",
    "reasoning"
  ],
  "additionalProperties": false
}
