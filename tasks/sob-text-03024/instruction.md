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
Will Finn: Will Finn (born November 1, 1958) is an American animator, voice actor, and director.  His work in animation includes characters from Disney and Don Bluth films such as "The Secret of NIMH", "Oliver & Company", "The Little Mermaid", "The Rescuers Down Under", and "Pocahontas".  His characters includes Cogsworth in "Beauty and the Beast", Iago in "Aladdin", and Laverne in "The Hunchback of Notre Dame".  Finn wrote and directed "Home on the Range" and did some voice acting the Hollywood Fish in "Chicken Little".  In 2006, Finn directed the computer animated short Hammy's Boomerang Adventure, a spin-off of "Over the Hedge".

Tin Toy: Tin Toy is a 1988 American computer-animated short film produced by Pixar and directed by John Lasseter.  The short film, which runs five minutes, stars Tinny, a tin one-man-band toy, attempting to escape from Billy, a destructive baby.  The third short film produced by the company's small animation division, it was a risky investment: due to low revenue produced by Pixar's main product, the eponymous computer to manage animations, the company was under financial constraints.

Hammy's Boomerang Adventure: Hammy's Boomerang Adventure is a computer-animated short comedy film based on the film "Over the Hedge", which was based on a comic strip of the same name.  It can be found on the movie's DVD or the "Madly Madagascar" DVD as a bonus feature.

Maestro (2005 film): Maestro is a 2005 Hungarian computer-animated short film written, produced and directed by Géza M. Tóth.  It won the Amaryllis Tamás Award at the 7th Kecskemét Animation Film Festival, and was nominated for Best Animated Short Film at the 79th Academy Awards in 2007.  Composer Attila Pacsay wrote the film's music.

La Luna (2011 film): La Luna (IPA: /laˈluna/ [laˈluːna] , Italian for "The Moon") is a 2011 Pixar computer-animated short film, directed and written by Enrico Casarosa.  The short premiered on June 6, 2011 at the Annecy International Animated Film Festival in France, and it was paired with Pixar's "Brave" for its theatrical release on June 22, 2012, being shown before the film's beginning.  "La Luna" was released on November 13, 2012, on the "Brave" DVD and Blu-ray, and on a new "Pixar Short Films Collection, Volume 2", the second collection of Pixar's short films.  "La Luna" was nominated for an Academy Award for Best Animated Short Film at the 84th Academy Awards.

Gift of the Night Fury: Gift of the Night Fury is a 2011 computer-animated short film by DreamWorks Animation and directed by Tom Owens.  It was released on November 15, 2011, on DVD and Blu-ray, along with another original animated short film "Book of Dragons".

Early Bloomer: Early Bloomer is a 2003 computer-animated short film by Sony Pictures Imageworks.  It was created and directed by Kevin Johnson.  It was studio's second short film after "The ChubbChubbs! ".

Red's Dream: Red's Dream is a 1987 American computer-animated short film produced by Pixar and directed by John Lasseter.  The short film, which runs four minutes, stars Red, a unicycle.  Propped up in the corner of a bicycle store on a rainy night, Red dreams about a better place.  "Red's Dream" was Pixar's second computer-animated short following "Luxo Jr." in 1986, also directed by Lasseter.

Piper (2016 film): Piper is a 2016 computer-animated short film produced by Pixar Animation Studios.  Written and directed by Alan Barillaro, it was theatrically released alongside Pixar's "Finding Dory" on June 17, 2016.  It won the Academy Award for Best Animated Short Film at the 89th Academy Awards.

In a Heartbeat (film): In a Heartbeat is a 2017 computer-animated short film produced by Ringling College of Art and Design.  Written and directed by Esteban Bravo and Beth David, the project was funded through Kickstarter where it racked up a total of $14,191 from 416 backers on a goal of $3,000.  The short film concerns a closeted boy who has a crush on another boy and his heart's desire to be with him.  The short has received wide praise on various platforms.

Question: In 2006, Will Finn directed "Hammy's Boomerang Adventure", a computer-animated short film based on which film?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "short_film_title": {
      "type": "string",
      "description": "The title of the short film."
    },
    "director": {
      "type": "string",
      "description": "The director of the short film."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the short film was directed or released."
    },
    "animation_type": {
      "type": "string",
      "description": "The type of animation used for the short film."
    },
    "based_on_film_title": {
      "type": "string",
      "description": "The title of the feature film the short film is based on."
    }
  },
  "required": [
    "short_film_title",
    "director",
    "release_year",
    "animation_type",
    "based_on_film_title"
  ],
  "additionalProperties": false
}
