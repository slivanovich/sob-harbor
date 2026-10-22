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
The Outsiders (film): The Outsiders is a 1983 American coming-of-age drama film directed by Francis Ford Coppola, an adaptation of the novel of the same name by S. E. Hinton.  The film was released on March 25, 1983.  Jo Ellen Misakian, a librarian at Lone Star Elementary School in Fresno, California, and her students were responsible for inspiring Coppola to make the film.

Coming Through the Rye (film): Coming Through the Rye is a 2015 American coming-of-age drama film written and directed by James Steven Sadwith.  It stars Alex Wolff and Stefania LaVie Owen as two teenagers who set out to find author J.D. Salinger, played by Chris Cooper.  The film is based on Sadwith's own quest to find Salinger.  It is Sadwith's directorial debut.

Boyhood (film): Boyhood is a 2014 American coming-of-age drama film written and directed by Richard Linklater, and starring Patricia Arquette, Ellar Coltrane, Lorelei Linklater, and Ethan Hawke.  Filmed from 2002 to 2013, "Boyhood" depicts the childhood and adolescence of Mason Evans Jr. (Coltrane) from ages six to eighteen as he grows up in Texas with divorced parents (Arquette and Hawke).  Richard Linklater's daughter Lorelei plays Mason's sister, Samantha.

Vision Quest: Vision Quest (released in the UK and Australia as Crazy for You) is a 1985 American coming-of-age drama film starring Matthew Modine, Linda Fiorentino and Ronny Cox.  It is based on Terry Davis' novel of the same name.  Modine plays a Spokane high school wrestler who falls in love with an older woman, an aspiring artist from New Jersey on her way to San Francisco.  The film includes an appearance by Madonna, her first in a major motion picture, playing a singer at a local bar, where she performs the songs "Crazy for You" and "Gambler".  In some countries, the title of the film was changed to market on Madonna's emerging fame and the popularity of the song "Crazy for You".

Logan Lerman: Logan Wade Lerman (born January 19, 1992) is an American actor, known for playing the title role in the fantasy-adventure "Percy Jackson" films.  He appeared in commercials in the mid-1990s, before starring in the series "Jack & Bobby" (2004–2005) and the movies "The Butterfly Effect" (2004) and "Hoot" (2006).  Lerman gained further recognition for his roles in the western "", the thriller "The Number 23", the comedy "Meet Bill", and 2009's "Gamer" and "My One and Only".  He subsequently played d'Artagnan in 2011's "The Three Musketeers", starred in the coming-of-age dramas "The Perks of Being a Wallflower" (2012), "Indignation" (2016) and "Sidney Hall" (2017), and had major roles in the 2014 films "Noah" and "Fury".

Stand by Me (film): Stand by Me is a 1986 American coming-of-age drama film directed by Rob Reiner, and starring Wil Wheaton, River Phoenix, Corey Feldman, and Jerry O'Connell.  The film, whose plot is based on Stephen King's novella "The Body" (1982) and title is derived from Ben E. King's eponymous song, which plays over the ending credits, tells the story of four boys in a small town in Oregon who go on a hike to find the dead body of a missing child.

Mud (2012 film): Mud is a 2012 American coming-of-age drama film written and directed by Jeff Nichols.  The film stars Matthew McConaughey, Tye Sheridan, Jacob Lofland, Sam Shepard, and Reese Witherspoon.  The film competed for the Palme d'Or at the 2012 Cannes Film Festival.  It was shown at the Sundance Film Festival in January 2013.  The film opened on April 26, 2013 with a limited release in select theaters, before having a wide release on May 10, 2013.  It performed well at the box office, grossing $32.6 million on a $10 million budget and received critical acclaim.

The Perks of Being a Wallflower (film): The Perks of Being a Wallflower is a 2012 American coming-of-age drama film.  An adaptation of the 1999 epistolary novel of the same name, it was written and directed by the novel's author, Stephen Chbosky.  Filmed in Pittsburgh, Pennsylvania, the film was released on September 21, 2012, to positive critical response and commercial success, earning $33.4 million to a budget of $13 million.  The film stars Logan Lerman, Emma Watson and Ezra Miller.  Two or three years after the release of film, Chbosky began to speak more openly concerning the mental health care aspects of the film which were of significance to him in the original writing of the book and the production of the film as he conceived it.  This is one of the three films from John Malkovich, Lianne Halfon and Russell Smith's Mr. Mudd Productions that feature struggling teenagers; the other two are "Ghost World" and "Juno".

Boy Erased (film): Boy Erased is an upcoming American coming-of-age drama film based on Garrard Conley's memoir, titled "", with Lucas Hedges portraying Conley as a young man.  It is directed by Joel Edgerton from a screenplay that he wrote and will also produce.  The film is scheduled to be released by Focus Features on September 28, 2018.

Johnny Simmons: Johnny James Simmons (born November 28, 1986) is an American actor.  He is known for his roles as Dylan Baxter in "Evan Almighty" (2007), Chip Dove in "Jennifer's Body" (2009), "Young Neil" Nordegraf in "Scott Pilgrim vs. the World" (2010), Brad Hayes in "The Perks of Being a Wallflower" (2012), and Shane in "Girlboss".

Question: Johnny James Simmons, is an American actor, and is known for his role as who, in The Perks of Being a Wallflower, a 2012 American coming-of-age drama film?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The full name of the actor."
    },
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "film_release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "film_genre": {
      "type": "string",
      "description": "The genre of the film."
    },
    "character_name": {
      "type": "string",
      "description": "The name of the character played by the actor in the film."
    }
  },
  "required": [
    "actor_name",
    "film_title",
    "film_release_year",
    "film_genre",
    "character_name"
  ],
  "additionalProperties": false
}
