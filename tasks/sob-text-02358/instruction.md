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
How to Build a Better Boy: How to Build a Better Boy is a Disney Channel Original Movie directed by Paul Hoen and written by Jason Mayland.  It stars China Anne McClain, Kelli Berglund and Marshall Williams.  The first images were shown during a promo for Disney Channel's Summer 2014, while the first promo aired on June 27, 2014 during the premiere of the Disney Channel Original Movie "Zapped".  The film premiered on August 15, 2014.  The movie premiered on Disney Channel UK on September 19, 2014.

Good Luck Charlie, It's Christmas!: Good Luck Charlie, It's Christmas!  (also known as Good Luck Charlie: The Road Trip Movie in the United Kingdom and Ireland) is a 2011 Christmas film based on the Disney Channel Original Series "Good Luck Charlie".  The film was directed by Arlene Sanford and written by Geoff Rodkey, and stars Bridgit Mendler, Leigh-Allyn Baker, Bradley Steven Perry, Mia Talerico, Eric Allan Kramer, and Jason Dolley as the Duncan family.  The Disney Channel Original Movie follows the Duncan family on their road trip to Amy Duncan's parents' house for Christmas.  It premiered on December 2, 2011 on Disney Channel ten years after Disney Channel's last Christmas-themed original movie, "'Twas the Night" in 2001.

The Cheetah Girls 2: The Cheetah Girls 2 is the 2006 sequel to the Disney Channel Original Movie, "The Cheetah Girls."  Its premiere received the highest ratings of all Disney Channel Movies at its time, a total of over 8.1 million viewers, beating the premiere ratings of "High School Musical" (7.7 million), and beating previous highest rated DCOM record holder, "Cadet Kelly" (7.8 million) as well as becoming the highest rated "Cheetah Girls" movie in the trilogy.  The sequel is about a talented teen quartet who take a whirlwind tour of Spain to pursue their dreams of pop superstardom.  Unlike its predecessor which incorporated karaoke-like musical numbers, "The Cheetah Girls 2" turned into more of a musical.  This is also the last film in the series to star Raven-Symoné.  The film is currently the 7th highest-rated Disney Channel Original Movie and was the highest-rated Disney Channel Original Movie of 2006.

Northern Lights (1997 film): Northern Lights is a 1997 television film based upon the 1988 stage play of the same name by John Hoffman.  Directed by Linda Yellen, the film stars Diane Keaton, Maury Chaykin, Joseph Cross, and Kathleen York.  It was produced for the Disney Channel and premiered on August 23, 1997.  Some sources identify "Northern Lights" as the first Disney Channel Original Movie, though "Northern Lights" was not included in Disney Channel's 100 Original Movies celebration that aired in May–June 2016, and Disney Channel considers 1997's "Under Wraps" to be the first official Disney Channel Original Movie.

Tangled: The Series: Tangled: The Series is an American animated musical fantasy television series that premiered on Disney Channel on March 10, 2017 as a movie, and began airing regular episodes from March 24, 2017.  It is based on Disney's 2010 computer-animated film "Tangled" directed by Nathan Greno and Byron Howard.  It takes place between the original movie and the short "Tangled Ever After".  A teaser trailer was released during the Disney Channel Original Movie, "The Swap".  It began as a Disney Channel Original Movie, titled "", which premiered on March 10, 2017.

Twitches (film): Twitches is a 2005 Disney Channel Original Movie, is based on the popular "Twitches" book series published by Scholastic Press.  Produced by Broomsticks Productions Limited, the film stars Tia Mowry and Tamera Mowry as Alexandra Fielding and Camryn Barnes, respectively.  On its premiere night, "Twitches" scored over 7 million viewers.  The movie drew 21.5 million viewers in four airings on its first weekend and was the week's most popular cable program.  A sequel, "Twitches Too", aired on October 12, 2007, as a part of Disney Channel's Hauntober Fest.

Halloweentown High: Halloweentown High (also known as Halloweentown III) is a 2004 Disney Channel Original Movie that premiered on Disney Channel on October 8, 2004 for the holiday of Halloween.  It drew 6.1 million viewers for its premiere.  This is the third installment in the "Halloweentown" series.  It is also the last "Halloweentown" film to feature Kimberly J. Brown as Marnie, and the last film in the series to feature the character of Sophie (Emily Roeske).

Twitches Too: Twitches Too is a 2007 Disney Channel Original Movie.  It is the sequel to the Disney Channel Original Movie "Twitches", released in 2005.  The film began production in late April 2007 and was released on October 12.  It aired during "Disney Channel's Halloween Month".  The Disney Channel Original Series, "Wizards of Waverly Place", premiered following the film's premiere.  The first trailer was released during the premiere of "High School Musical 2".  On its premiere night, the movie brought in 6.96 million viewers.  To date, it is the last sequel to a Disney Channel Original Movie that is not a musical.

Finn Wittrock: Peter "Finn" Wittrock, Jr. (born October 28, 1984) is an American actor and screenwriter.  He began his career in guest roles on several television shows.  He made his film debut in 2004, in "Halloweentown High" before returning to films in the 2010 film "Twelve".  After studying theater at The Juilliard School, he was a regular in the soap opera, "All My Children," from 2009 to 2011, while performing in several theatrical productions.  In 2011, he performed in playwright Tony Kushner's Off-Broadway play "The Illusion" and made his Broadway debut in 2012 as Happy Loman in the revival of Arthur Miller's play "Death of a Salesman", directed by Mike Nichols.

Jett Jackson: The Movie: Jett Jackson: The Movie is a 2001 American Disney Channel Original Movie based on the Disney Channel series "The Famous Jett Jackson".  It is the first Disney Channel Original Movie to be based on a Disney Channel Original Series.

Question: Peter "Finn" Wittrock, Jr. made his film debut in a Disney Channel Original Movie that drew how many viewers for its premiere?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The full name of the actor."
    },
    "film_debut_movie_title": {
      "type": "string",
      "description": "The title of the Disney Channel Original Movie in which the actor made their film debut."
    },
    "premiere_year": {
      "type": "integer",
      "description": "The year the movie premiered."
    },
    "premiere_viewers_millions": {
      "type": "number",
      "description": "The number of viewers (in millions) for the movie's premiere."
    }
  },
  "required": [
    "actor_name",
    "film_debut_movie_title",
    "premiere_year",
    "premiere_viewers_millions"
  ],
  "additionalProperties": false
}
