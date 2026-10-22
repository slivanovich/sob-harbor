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
American Pie Presents: Beta House: American Pie Presents: Beta House is a 2007 American sex comedy film released by Universal Pictures.  It is the third installment in the "American Pie Presents" series and the sixth installment in the "American Pie" franchise.  The film concludes a story arc that begins with "" (2006).  John White stars as Erik Stifler, a college freshman who pledges the Beta House fraternity led by his cousin Dwight Stifler (Steve Talley).  Christopher McDonald co-stars as Erik's father and Eugene Levy plays Beta House alumnus Noah Levenstein.

It Takes a Thief (1968 TV series): It Takes a Thief is an American action-adventure television series that aired on ABC for three seasons between 1968 and 1970.  It stars Robert Wagner in his television debut as sophisticated thief Alexander Mundy, who works for the U.S. government in return for his release from prison.  For most of the series, Malachi Throne played Noah Bain, Mundy's boss.

Noah Beery Sr.: Noah Nicholas Beery (January 17, 1882 – April 1, 1946) was an American actor who appeared in films from 1913 to 1945.  He was the older brother of Academy Award-winning actor Wallace Beery and the father of character actor Noah Beery Jr. Beery was billed as either Noah Beery or Noah Beery Sr. depending upon the film.

Jordan Fisher: Jordan William Fisher (born April 24, 1994) is an American singer, dancer and actor.  His self-titled EP was released by Hollywood Records on August 19, 2016.  He has had recurring roles on the television series, "The Secret Life of the American Teenager" and "Liv and Maddie", and supporting roles in the television films, "Teen Beach Movie", "Teen Beach 2" and "", and is featured on the "Moana" soundtrack.  He assumed the role of John Laurens/Philip Hamilton in the Broadway production of "Hamilton" on November 22, 2016.  He played Noah Patrick in the TV series "Teen Wolf".

Desmond Askew: Desmond Askew (born 17 December 1972) is an English actor of film and television.  In 1983 he had the lead role of 'naughty schoolboy' in the promo video of the Wham!  single "Bad Boys".  He has appeared in films such as "Go" (1999), "Repli-Kate" (2002), "The Hills Have Eyes" (2006) and "Turistas" (2006).  He has appeared in episodic television on series such as "Grange Hill", "Las Vegas", "Charmed", the short-lived "Then Came You", and as the recurring character Brody Davis on "Roswell".  He also voiced many minor characters (including Jowan and Chanter Devons) in the 2009 video game "Dragon Age Origins".  He has recently voiced as CIA Nerd in "".

American Pie Presents: The Naked Mile: American Pie Presents: The Naked Mile (also known as American Pie: The Naked Mile) is a 2006 American sex comedy film released by Universal Pictures.  It is the second installment in the "American Pie Presents" series and the fifth installment in the "American Pie" franchise.  The film begins a story arc that concludes with "" (2007).  John White stars as Erik Stifler, a high school senior who is given a "guilt free pass" by his girlfriend, Tracy Sterling (Jessy Schram), and so visits the Beta House fraternity led by his cousin, Dwight Stifler (Steve Talley), to run a mile naked.  Christopher McDonald co-stars as Erik's father, Harry, and Eugene Levy once again plays Jim's Dad, who turns out to be a family friend of both Erik's and Tracy's.  Also, it is in this film that his name is revealed to be "Noah Levenstein".

Eugene Levy: Eugene Levy, CM (born December 17, 1946) is a Canadian actor, comedian, producer, director, musician and writer.  He is the only actor to have appeared in all eight of the "American Pie" films, in his role as Noah Levenstein.  He often plays nerdy, unconventional figures, with his humour often deriving from his excessive explanations of matters and the way in which he deals with sticky situations.  Levy is a regular collaborator of actor-director Christopher Guest, appearing in and co-writing four of his films, commencing with "Waiting for Guffman" (1997).

Repli-Kate: Repli-Kate is a 2002 sex comedy film from National Lampoon, directed by Frank Longo and starring Ali Landry, James Roday, Desmond Askew and Eugene Levy.

List of American Pie characters: This is a list of characters from the film series "American Pie" consisting of "American Pie" (1999), "American Pie 2" (2001), "American Wedding" (2003), "" (2005), "" (2006), "" (2007), "" (2009), and "American Reunion" (2012).  Only one character, Noah Levenstein played by Eugene Levy, has appeared in all eight released films.  Biggs, Hannigan, Scott, Nicholas, Thomas, Coolidge, Cho, Isfield, Cheek, and Owen all play their characters in four films each; other characters appear in fewer films.

Noah Beery Jr.: Noah Lindsey Beery (August 10, 1913 – November 1, 1994), known professionally as Noah Beery Jr. or just Noah Beery, was an American actor specializing in warm, friendly character roles similar to the ones played by his paternal uncle, Wallace Beery, although Noah Beery Jr., unlike his paternal uncle, seldom broke away from playing supporting roles.  Beery's father, Noah Nicholas Beery (known professionally as Noah Beery or Noah Beery Sr.), enjoyed a similarly lengthy film career as a major supporting actor.

Question: Repli-Kate stars an actor who played Noah Levenstein in what films?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor who starred in Repli-Kate and played Noah Levenstein."
    },
    "character_name": {
      "type": "string",
      "description": "The name of the character played by the actor."
    },
    "film_franchise_name": {
      "type": "string",
      "description": "The name of the film franchise in which the character appeared."
    },
    "first_film_title_in_franchise": {
      "type": "string",
      "description": "The title of the first film in the franchise where the character appeared."
    },
    "total_appearances_in_franchise": {
      "type": "integer",
      "description": "The total number of films in the franchise where the character appeared."
    }
  },
  "required": [
    "actor_name",
    "character_name",
    "film_franchise_name",
    "first_film_title_in_franchise",
    "total_appearances_in_franchise"
  ],
  "additionalProperties": false
}
