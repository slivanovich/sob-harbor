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
Mr. &amp; Mrs. Smith (2005 film): Mr. & Mrs. Smith is a 2005 American action comedy film directed by Doug Liman and written by Simon Kinberg.  The film stars Brad Pitt and Angelina Jolie as a bored upper-middle class married couple surprised to learn that they are assassins belonging to competing agencies, and that they have been assigned to kill each other.

Adam Brody: Adam Jared Brody (born December 15, 1979) is an American actor, writer, musician and producer.  He is best known for his role as Seth Cohen on "The O.C.".  Brody has appeared in the films "Mr. & Mrs. Smith" (2005), "Thank You for Smoking" (2006), "In the Land of Women" (2007), "Jennifer's Body" (2009), "Cop Out" (2010), "Scream 4" (2011), "Lovelace" (2013), "Life Partners" (2014), and "Sleeping with Other People" (2015).

Doug Liman: Douglas Eric "Doug" Liman (born July 24, 1965) is an American film director and producer best known for "Swingers" (1996), "Go" (1999), "The Bourne Identity" (2002), "Mr. & Mrs. Smith" (2005), "Jumper" (2008), "Fair Game" (2010), and "Edge of Tomorrow" (2014).

Lucas Foster: Lucas Foster is a Hollywood Film Producer.  He is known for Mr. & Mrs. Smith (2005 film), Man on Fire (2004 film) and Equilibrium.  His movies generated all together 2.1 billion dollars of gross revenues.  In recent years, he is one of the co-founders of HeadcaseVR, a virtual reality company.

Simon Kinberg: Simon David Kinberg (born August 2, 1973) is a British-born American screenwriter, producer and director.  He is best known for his work on the "X-Men" film franchise, and has also written such films as "Mr. & Mrs. Smith" and "Sherlock Holmes".  He has served as a producer on others including "Cinderella" and "The Martian", for which he was nominated for an Academy Award for Best Picture.  His production company Kinberg Genre has a first-look deal with 20th Century Fox.  Kinberg has taken a large role in the "X-Men" film universe acting as one of the consistent members of the franchise's creative team, serving as producer and screenwriter for multiple installments.  Kinberg will make his directorial debut with "", from his own screenplay.  The film will be released November 2, 2018.

Mr. &amp; Mrs. Smith (1941 film): Mr. & Mrs. Smith is a 1941 American screwball comedy film directed by Alfred Hitchcock, written by Norman Krasna, and starring Carole Lombard and Robert Montgomery.  It also features Gene Raymond, Jack Carson, Philip Merivale, and Lucile Watson.

The Dukes of Hazzard (film): The Dukes of Hazzard is a 2005 American action comedy film based on the television series of the same name.  The film was directed by Jay Chandrasekhar and released on August 5, 2005 by Warner Bros.  Pictures.  As in the television series, "The Dukes of Hazzard" depicts the adventures of cousins Bo, Luke, Daisy and their Uncle Jesse as they outfox crooked Hazzard County commissioner Boss Hogg and Sheriff Rosco P. Coltrane.

On Your Side (Magnet album): On Your Side is Magnet's second album, first released in Norway in June 2003.  It contains a cover of Bob Dylan's "Lay Lady Lay" featuring Gemma Hayes, which was featured in the 2005 film "Mr. & Mrs. Smith".

Boy or Girl paradox: The Boy or Girl paradox surrounds a set of questions in probability theory which are also known as "The Two Child Problem", "Mr. Smith's Children" and the "Mrs. Smith Problem."  The initial formulation of the question dates back to at least 1959, when Martin Gardner published one of the earliest variants of the paradox in "Scientific American".  Titled "The Two Children Problem", he phrased the paradox as follows:

William Fichtner: William Edward Fichtner Jr. (born November 27, 1956) is an American actor.  He has appeared in a number of notable films and TV series.  He is known for his roles as Sheriff Tom Underlay in the television series "Invasion", Alexander Mahone on "Prison Break", and numerous film roles, including: "Quiz Show", "Heat", blind astronomer Kent in "Contact", "Armageddon", "The Perfect Storm", "Crash", "Blades of Glory", "Black Hawk Down", "Nine Lives", "The Longest Yard", "Mr. & Mrs. Smith", "The Dark Knight", "Date Night", "The Lone Ranger", "Phantom", "Elysium", "", and "Teenage Mutant Ninja Turtles".

Question: Also known for directing "Swingers" ,who directed the 2005 American action comedy film Mr. & Mrs. Smith?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "director_name": {
      "type": "string",
      "description": "The full name of the director."
    },
    "film_directed": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film."
        },
        "genre": {
          "type": "string",
          "description": "The genre of the film."
        }
      },
      "required": [
        "title",
        "release_year",
        "genre"
      ],
      "additionalProperties": false
    },
    "director_other_notable_films": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of other notable films directed by this person."
    }
  },
  "required": [
    "director_name",
    "film_directed",
    "director_other_notable_films"
  ],
  "additionalProperties": false
}
