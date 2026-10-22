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
The Dead Girl: The Dead Girl is a 2006 American film written and directed by Karen Moncrieff, starring Brittany Murphy, Toni Collette, Rose Byrne and Marcia Gay Harden.  The film was nominated for several 2007 Independent Spirit Awards including Best Feature and Best Director.  It is the story of a young woman's death and the people linked to her murder.  It also features Mary Beth Hurt, Kerry Washington, James Franco, Giovanni Ribisi, Josh Brolin, Mary Steenburgen and Piper Laurie.  The film was premiered at the AFI Film Festival (7 November 2006), and was given a limited US theatrical release on 29 December 2006.  It was generally well received.  It only ran for two weeks in US first-run theaters, and earned nearly all its revenue from overseas release.

Rose Byrne: Mary Rose Byrne (born 24 July 1979) is an Australian actress.  Byrne made her screen debut in 1992 with a small role in the film "Dallas Doll".  In 2000, she played a leading role in the Australian film "The Goddess of 1967", which brought her the Volpi Cup for Best Actress.  From 2007 to 2012, she played Ellen Parsons in the cable television series "Damages", which earned her two Golden Globe Award and two Primetime Emmy Award nominations.  Along with co-star Glenn Close, she appeared in all of the show's fifty-nine episodes.  Byrne has also starred in the films "Troy", "28 Weeks Later", "Knowing", "Insidious", "", "", as well as the comedies "Get Him to the Greek", "Bridesmaids", "Neighbors", "", and "Spy."

The Night We Called It a Day (film): The Night We Called It a Day, also known as All the Way, is a 2003 Australian-American comedy drama film directed by Paul Goldman and starring Dennis Hopper as Frank Sinatra and Melanie Griffith as Barbara Marx.  It also features Portia de Rossi, Joel Edgerton, Rose Byrne and David Hemmings.  The movie is based on the true events surrounding Sinatra's 1974 tour in Australia.  When the singer calls a local reporter (de Rossi) a "two-bit hooker", every union in the country black-bans the star until he issues an apology.

Rebecca Skloot: Rebecca L. Skloot (born September 19, 1972) is a freelance science writer who specializes in science and medicine.  Her first book, "The Immortal Life of Henrietta Lacks" (2010), was one of the best-selling new books of 2010, staying on "The New York Times" Bestseller list for over 2 years and eventually reaching #1.  It was made into a movie by Oprah Winfrey, which premiered on HBO on April 22, 2017 and starred Rose Byrne as Skloot.

Insidious (film): Insidious is a 2010 American-Canadian supernatural horror film directed by James Wan, written by Leigh Whannell, and starring Patrick Wilson, Rose Byrne and Barbara Hershey.  It is the first (chronologically, the third) installment in the "Insidious" franchise.  The story centers on a couple whose son inexplicably enters a comatose state and becomes a vessel for ghosts in an astral dimension who want to inhabit his body, in order to live once again.  The film was released in theaters on April 1, 2011, and was FilmDistrict's first theatrical release.  The film is followed by a sequel, "" (2013) and two prequels, "" (2015) and "" (2018).

Take Away: Take Away is a 2003 Australian comedy movie, written by Dave O'Neil, who also features as a minor character, and Mark O'Toole.  It stars Vince Colosimo, Stephen Curry, Rose Byrne, John Howard and Nathan Phillips.  The film starts in 19th century Victoria with the invention of the ever great "Take away".

Neighbors (2014 film): Neighbors (released in some countries as Bad Neighbours) is a 2014 American comedy film directed by Nicholas Stoller and written by Andrew J. Cohen and Brendan O'Brien.  The film stars Seth Rogen, Zac Efron, Rose Byrne, Dave Franco and Christopher Mintz-Plasse.  The plot follows a couple who come into conflict with a fraternity that has recently moved in next door.

Wicker Park (film): Wicker Park is a 2004 American psychological drama/romantic mystery film directed by Paul McGuigan and starring Josh Hartnett, Rose Byrne, Diane Kruger and Matthew Lillard.  The film is a remake of the 1996 French movie "L'Appartement", which in turn is loosely based on Shakespeare's "A Midsummer's Night Dream".  It was nominated for the at the Film Festival of Montreal, the city in which the movie was partially filmed.

Annie (2014 film): Annie is a 2014 American musical comedy-drama film directed by Will Gluck and produced by Village Roadshow Pictures and Will Smith's Overbrook Entertainment for Sony Pictures' Columbia Pictures.  A contemporary adaptation of the 1977 Broadway musical of the same name, the film stars Quvenzhané Wallis, Jamie Foxx, Rose Byrne, Bobby Cannavale, and Cameron Diaz.  The third film adaptation, following Columbia's 1982 theatrical film and Disney's 1999 television film, "Annie" began production in August 2013 and opened on December 19, 2014 to generally negative reviews, and was not a box office success, grossing only $133 million against a below-line production cost of over $65 million.

Adam (2009 film): Adam is an 2009 American romantic drama film written and directed by Max Mayer, starring Hugh Dancy and Rose Byrne.  The film follows the relationship between a young man named Adam (Dancy) with Asperger syndrome, and Beth (Byrne).  Mayer was inspired to write the film's script when he heard a radio interview with a man who had Asperger's.

Question: Rose Byrne starred in what movie?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "movie_title": {
      "type": "string",
      "description": "The title of the movie."
    },
    "actor_name": {
      "type": "string",
      "description": "The name of the actor who starred in the movie."
    },
    "movie_details": {
      "type": "object",
      "properties": {
        "genre": {
          "type": "string",
          "description": "The genre of the movie."
        },
        "director": {
          "type": "string",
          "description": "The director of the movie."
        },
        "release_year": {
          "type": "integer",
          "description": "The year the movie was produced or released."
        },
        "other_stars": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Other prominent actors starring in the movie."
        }
      },
      "required": [
        "genre",
        "director",
        "release_year",
        "other_stars"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "movie_title",
    "actor_name",
    "movie_details"
  ],
  "additionalProperties": false
}
