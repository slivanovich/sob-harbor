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
Chuck Barris: Charles Hirsch Barris (June 3, 1929 – March 21, 2017) was an American game show creator, producer and host.  Barris was known for hosting "The Gong Show", and creating "The Dating Game" and "The Newlywed Game".  He was also a songwriter, who wrote "Palisades Park" for Freddy Cannon.  Barris wrote an autobiography titled "Confessions of a Dangerous Mind", which was made into the film of the same name directed by George Clooney.

Chris Bearde: Chris Bearde (18 June 1936 – 23 April 2017) was a British-born comedy writer, producer and director best known for his work as a writer on the 1960s zeitgeist hit "Rowan & Martin's Laugh-In" and for co-writing and producing television specials for Elvis Presley, Bob Hope, Sonny & Cher, Bill Cosby, Steve Martin, Jim Carrey, Andy Williams, The Jackson 5, The Osmonds, Dinah Shore, Diana Ross, and Lucille Ball.  He also created the format for the original "Gong Show" and a number of network and pay-cable comedy series including "That's My Mama" and "Sherman Oaks".

Derek Mooney: Derek James Mooney (born 4 March 1967) is an Irish radio and television presenter, as well as a radio producer.  Until January 2015 he presented a weekday afternoon programme called "Mooney" on RTÉ Radio 1.  He is the current executive producer across RTÉ Radio 1's nature and wildlife programming

The Unknown Comic: “The Unknown Comic” is the stage name adopted by Canadian actor and stand-up comic Murray Langston (born June 27, 1945, Dartmouth, Nova Scotia, Canada), best known for his comic performances on "The Gong Show," in which he usually appeared with a paper bag over his head.  As of 2015, Langston was making his residence in Bathurst, New Brunswick, Canada.

Lkhagva Erdene: Lkhagva Erdene (born in Darkhan City, Mongolia, March 11, 1987) is a Mongolian TV host, television producer, investigative reporter and activist.  He is the television host of Mongol TV’s “Nuudel Shiidel” debate show and the channel’s current Executive Producer of News.  He has written for "The Diplomat" and is a regular contributor to Ikon.mn.

Shaunie O'Neal: Shaunie O'Neal is the current executive producer of VH-1’s reality TV series, "Basketball Wives", "Basketball Wives LA", and Baller Wives, and is the former wife of NBA center Shaquille O’Neal.  Formerly a film marketer, O'Neal is, as of May 2012, a TV personality and producer, entrepreneur, philanthropist and mother of five children.

Will Arnett: William Emerson Arnett ( ; born May 4, 1970) is a Canadian-American actor, voice actor and comedian.  He is best known for his role as George Oscar "Gob" Bluth II in the Fox/Netflix series "Arrested Development" (2003–2006, 2013, 2018); as well as his titular role as BoJack Horseman in the Netflix Original Series of the same name (2014-present).  He has appeared in films such as "Blades of Glory" (2007), "Hot Rod" (2007) and "Teenage Mutant Ninja Turtles" (2014).

The Radio Chick: The Radio Chick is the on-air name for Leslie Gold, an American radio personality whose talk show features comedian Chuck Nice and her producer, Paul "Butch" Brennan.  Leslie is a recurring guest host on the Fox News Radio Network heard nationally.  She is the Executive Producer of "The Gong Show Live - Off Broadway", a theatrical recreation of the classic TV show.  She is a graduate of Syracuse University and The Harvard Business School.

The Gong Show: The Gong Show is an amateur talent contest franchised by Sony Pictures Television to many countries.  It was broadcast on NBC's daytime schedule from June 14, 1976, through July 21, 1978, and in first-run syndication from 1976 to 1980 and 1988 to 1989, and was revived in 2017 for broadcast on ABC.  The show was created and originally produced by Chuck Barris, who also served as host for the NBC run and from 1977 to 1980 in syndication.  It is currently executive produced by Will Arnett and hosted by Tommy Maitland, a fictional character performed by an uncredited Mike Myers.  "The Gong Show" is known for its absurdist humor and style, with the actual competition secondary to the often outlandish acts presented; a small cash prize has typically been awarded to each show's winner.

Jeff Fager: Jeff Fager (born December 10, 1954) is the former Chairman of CBS News and the current Executive Producer of "60 Minutes", the hour-long CBS news magazine created in 1968.

Question: the current executive producer of The Gong Show was born in which year ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "show_name": {
      "type": "string",
      "description": "The name of the television show."
    },
    "executive_producer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the executive producer."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the executive producer."
        }
      },
      "required": [
        "name",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "role": {
      "type": "string",
      "description": "The role of the person in relation to the show."
    }
  },
  "required": [
    "show_name",
    "executive_producer",
    "role"
  ],
  "additionalProperties": false
}
