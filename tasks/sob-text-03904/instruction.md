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
Wed 21: Wed 21 is the sixth studio album by Argentine singer and songwriter Juana Molina.  It was released on 28 October 2013 by Crammed Discs.  From 2009 to 2012, Molina worked on the album on her own, recording at her house in Buenos Aires.  Musically, "Wed 21" is a folktronica album with a sound similar to her previous releases, but with innovations like the use of bass, drums, many electric guitars, noise, a horn and more detailed electronics, which led the Argentine "Rolling Stone" to describe it as her most "rocker" album.  The album received rave reviews from music critics, who noted it was not a departure from her distinctive sound but still a progression.

Sanjay's Super Team: Sanjay's Super Team is a computer-animated short film produced by Pixar Animation Studios.  Written and directed by Sanjay Patel, and based on his childhood, it premiered on June 15, 2015 at the Annecy International Animated Film Festival in France, and accompanied the theatrical release of Pixar's "The Good Dinosaur" on November 25, 2015.

Victoria Díez Bustos de Molina: Blessed Victoria Díez Bustos de Molina (11 November 1903 - 12 August 1936) was a Spanish Roman Catholic and a member from the Teresian Association.  Molina worked as a teacher who became well-loved among her students for her deep faith and her passion as well as her commitment to the education of children.

Adrian Molina: Adrian Molina (born August 23, 1985) is an American screenwriter and storyboard artist.  He has been at Pixar since 2007, where he started as a 2D animator on "Ratatouille".  He later moved on to be a storyboard artist, working on "Toy Story 3" and "Monsters University".  After writing for "The Good Dinosaur", Molina started his first gig as a screenplay writer for "Coco" and later went on to co-direct the film.  Molina also illustrated the Little Golden Book for "Toy Story 3".

Coco (2017 film): Coco is an upcoming American computer-animated musical fantasy film produced by Pixar Animation Studios and released by Walt Disney Pictures.  Based on an original idea by Lee Unkrich, it is being directed by Unkrich, and co-directed and written by Adrian Molina.  The story follows a 12-year-old boy named Miguel who sets off a chain of events relating to a century-old mystery, leading to an extraordinary family reunion.

The Good Dinosaur: The Good Dinosaur is a 2015 American 3D computer-animated comedy-drama adventure film produced by Pixar Animation Studios and released by Walt Disney Pictures.  The film is directed by Peter Sohn in his directorial debut from a screenplay by Meg LeFauve from an original idea by Bob Peterson.  Set on a fictional Earth in which dinosaurs never became extinct, the film follows a young "Apatosaurus" named Arlo, who meets an unlikely human friend while traveling through a harsh and mysterious landscape.  The film features the voices of Raymond Ochoa, Jack Bright, Sam Elliott, Anna Paquin, A.J. Buckley, Steve Zahn, Jeffrey Wright, and Frances McDormand.

Golden Globe Award for Best Animated Feature Film: The Golden Globe Award for Best Animated Feature Film was awarded for the first time at the 64th Golden Globe Awards in 2007.  It was the first time that the Golden Globe Awards had created a separate category for animated films since its establishment.  The nominations are announced in January and an awards ceremony is held later in the month.  Initially, only three films are nominated for best animated film, in contrast to five nominations for the majority of other awards.  The Pixar film "Cars" was the first recipient of the award.  The award for best animated film has subsequently been presented to six other Pixar films: "Ratatouille" received the award in 2008, "WALL-E" was the recipient in 2009, "Up" received the award in 2010, "Toy Story 3" won in 2011, "Brave" won in 2013, and "Inside Out" won in 2016.  In 2012, "Cars 2" lost to "The Adventures of Tintin", in 2014, "Monsters University" was the first not to be nominated and also in 2016, "The Good Dinosaur" lost to "Inside Out".  In 2017, "Finding Dory" was also not nominated.  The Hollywood Foreign Press Association has been awarding Golden Globe Awards since 1944.

Harley Jessup: Harley Jessup (born 1954) is an American production designer and visual effects art director who has been nominated for two visual effects Academy Awards, and won once.  Currently working at Pixar Animation Studios, Jessup has served as production designer for "Monsters, Inc." (with Bob Pauley), "Ratatouille", "Cars 2", "Presto", "The Good Dinosaur" and an upcoming Pixar feature.  Before coming to Pixar, Jessup was production designer on Walt Disney Pictures' "James and the Giant Peach".

Raymond Ochoa: Raymond Ochoa (born October 12, 2001) is an American child actor and voice actor.  He has appeared in various commercials, television shows and movies including roles in "10 Items or Less", "Merry Christmas, Drake & Josh", and the lead character, Arlo, in the Pixar film "The Good Dinosaur".

Enrico Casarosa: Enrico Casarosa is an Italian storyboard artist and director who works at Pixar.  In 2012, he was nominated for an Academy Award for the animated short film "La Luna".  Starting in 2011, he worked as a head of story on Bob Peterson's film, "The Good Dinosaur".

Question: Adrian Molina worked with what director when making the movie The Good dinosaur?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "movie_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "director_name": {
      "type": "string",
      "description": "The name of the director of the film."
    },
    "molina_role": {
      "type": "string",
      "description": "Adrian Molina's role in the production of the film."
    }
  },
  "required": [
    "movie_title",
    "director_name",
    "molina_role"
  ],
  "additionalProperties": false
}
