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
Instant Pleasure (song): The song Instant Pleasure was written by pop songwriter Seth Swirsky and was featured in Adam Sandler's highest-grossing film, "Big Daddy" (1999).  In the movie, it was sung by Rufus Wainwright.  The song was recorded by Seth Swirsky on his first solo album, Instant Pleasure, in 2004.  The album won Best Pop Album at the 2005 L.A. Music Awards.  Rockell also recorded the song for her 2002 album, Instant Pleasure.

Hotel Transylvania 2: Hotel Transylvania 2 is a 2015 American 3D computer animated fantasy-comedy film.  It is the second installment in the "Hotel Transylvania" franchise, and the sequel to the 2012 film "Hotel Transylvania", with its director, Genndy Tartakovsky, and writer, Robert Smigel, returning for the film.  Produced by Sony Pictures Animation, it was animated by Sony Pictures Imageworks, with an additional funding provided by LStar Capital.

Big Daddy (1999 film): Big Daddy is a 1999 American comedy film directed by Dennis Dugan and starring Adam Sandler and the Sprouse twins.  The film was produced by Robert Simonds and released on June 25, 1999, by Columbia Pictures, where it opened #1 at the box office with a $41,536,370 first weekend.  It was Sandler's last film before starting his production company, Happy Madison Productions, his first film distributed by Columbia Pictures, and his highest-grossing film until "Hotel Transylvania 2" (2015).

Teddy Castellucci: Theodore Ross "Teddy" Castellucci is a composer of film music.  A graduate of Lindenhurst Senior High School on Long Island, New York in 1983, Castellucci has won five BMI Film Music Awards. He's mostly known for working in comedy projects, and for being the recurring composer in films starring Adam Sandler, before being replaced by Rupert Gregson-Williams.  Castellucci appeared on screen as a band member (the guitarist) in "The Wedding Singer" and his last name was used for minor characters in both "The Wedding Singer" and "Big Daddy".

Happy Gilmore: Happy Gilmore is a 1996 American sports comedy film directed by Dennis Dugan with music by Mark Mothersbaugh and produced by Robert Simonds.  It stars Adam Sandler as the title character, an unsuccessful ice hockey player who discovers a newfound talent for golf.  The screenplay was written by Sandler and Tim Herlihy.  The film was released in cinemas on February 16, 1996 by Universal Pictures.  "Happy Gilmore" was a commercial success, earning $41.2 million on a $12 million budget.  This film was the first of multiple collaborations between Sandler and Dugan.  The film won an MTV Movie Award for "Best Fight" for Adam Sandler versus Bob Barker.

I'm in Love with a Monster: "I'm in Love with a Monster" is a song recorded by American girl group Fifth Harmony for the computer animated fantasy-comedy film, "Hotel Transylvania 2".  It was written by Harmony Samuels, Carmen Reece, Sarah Mancuso, Edgar Etienne and Ericka Coulter with production handled by Samuels.  It was released to digital retailers on August 14, 2015 through Epic Records and Syco Music and serviced to contemporary hit radio in the United States four days later on August 18.  "I'm in Love with a Monster" is a pop song that blends elements of R&B, soul, rock and hip hop with "jazzy" rhythms along with heavy and funky beats.  Critics drew comparisons to the musical style of girl groups such as The Supremes.

Magos y Gigantes: Magos y Gigantes (simply known as Wizards and Giants in English) is a 2003 Mexican animated fantasy-comedy film produced by Ánima Estudios and 20th Century Fox and released on November 19, 2003.  This is the first feature film from Ánima Estudios and the first theatrically released animated film created with Adobe Flash, a program often used for internet cartoons.  It was also the first Mexican animated feature in 30 years.

Big Daddy (BioShock): A Big Daddy is a fictional character in the "BioShock" series of video games.  Big Daddies are heavily spliced (genetically mutated and altered with ADAM) human beings who have had their bodies directly grafted into heavily armored, steampunk-inspired atmospheric diving suits.  They are armed with a rivet gun, heavy drill, rocket launcher, or ion laser.  Alpha series Big Daddies are equipped with any of several other weapons as well.  Though they make low-pitched groaning noises similar to whales, Big Daddies have no voice actor attributed to them.  Designed by Irrational Games (then under the supervision of 2K Boston/2K Australia), they first appeared in "BioShock" and were promoted heavily.  A six-inch Big Daddy action figure was included in the limited edition version of the title.  In its sequel, "BioShock 2", the player controls a prototype Big Daddy.

Jack Giarraputo: Jack Giarraputo is a film producer who has been involved in the creation of more than 30 films in a little over a decade.  He has produced movies at Disney, Paramount, Sony, Fox and Warner Brothers that have grossed over $3.5 billion in worldwide box office.  Most of his work has been in the comedy genre, notably films starring Adam Sandler.  Adam Sandler has referenced him in his comedy album "What The Hell Happened To Me?"  in his famous skit "The Goat" and Jack helped write Ode to My Car, from Adam Sandler's album "What the Hell Happened to Me?" , along with Adam and Allen Covert.  Jack currently serves as the Chairman of The Board for FUEL Sports Management Group.

Hotel Transylvania 3: Hotel Transylvania 3 is an upcoming American 3D computer-animated fantasy-comedy film produced by Sony Pictures Animation.  Featuring the reprised roles of Adam Sandler, Andy Samberg and Selena Gomez, it is the third installment in the "Hotel Transylvania" franchise and the sequel to "Hotel Transylvania 2" (2015).  The film is scheduled to be released on July 13, 2018, by Columbia Pictures.

Question: Big Daddy was the highest-grossing film by Adam Sandler until a 3D computer animated fantasy-comedy film directed by who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "original_highest_grossing_film_title": {
      "type": "string",
      "description": "The title of Adam Sandler's film that was previously his highest-grossing."
    },
    "film_that_surpassed_it": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film that surpassed the original highest-grossing film."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film that surpassed the original."
        },
        "genre_description": {
          "type": "string",
          "description": "A description of the film's genre and animation style."
        },
        "director_name": {
          "type": "string",
          "description": "The name of the director of the film that surpassed the original."
        }
      },
      "required": [
        "title",
        "release_year",
        "genre_description",
        "director_name"
      ],
      "additionalProperties": false
    },
    "adam_sandler_involvement": {
      "type": "boolean",
      "description": "Indicates if Adam Sandler was involved with the films in question (e.g., starring or associated with highest-grossing status)."
    }
  },
  "required": [
    "original_highest_grossing_film_title",
    "film_that_surpassed_it",
    "adam_sandler_involvement"
  ],
  "additionalProperties": false
}
