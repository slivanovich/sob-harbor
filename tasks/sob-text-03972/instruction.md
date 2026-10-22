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
The Imitation Game: The Imitation Game is a 2014 American historical drama thriller film directed by Morten Tyldum and written by Graham Moore loosely based on the biography "" by Andrew Hodges (which was previously adapted as the stage play and BBC drama "Breaking the Code").  It stars Benedict Cumberbatch as real-life British cryptanalyst Alan Turing, who decrypted German intelligence codes for the British government during the Second World War.  Keira Knightley, Matthew Goode, Rory Kinnear, Charles Dance and Mark Strong also star.

Elizabeth: The Golden Age: Elizabeth: The Golden Age is a 2007 sequel to the 1998 film "Elizabeth", directed by Shekhar Kapur and produced by Universal Pictures and Working Title Films.  It stars Cate Blanchett in the title role and is a fairly fictionalised portrayal of events during the latter part of the reign of Queen Elizabeth I of England.  The film co-stars Geoffrey Rush, Clive Owen, Rhys Ifans, Jordi Mollà, Abbie Cornish and Samantha Morton.  The screenplay was written by William Nicholson and Michael Hirst, and the music score was composed by A. R. Rahman and Craig Armstrong.  Guy Hendrix Dyas was the film's production designer and co-visual effects supervisor, and the costumes were created by Alexandra Byrne.  The film was shot at Shepperton Studios and various locations around the United Kingdom.

Guy Hendrix Dyas: Guy Hendrix Dyas (born 20 August 1968) is a British production designer for feature films.  He collaborated with Christopher Nolan on his science fiction thriller "Inception" which earned him an Academy Award nomination as well as a BAFTA Award for Best Production Design.  In 2017, Dyas was nominated for another Academy Award, this time for his work on Passengers.  In 2010, Dyas became the first British designer to win a Goya Award for Best Production Design for his work on Alejandro Amenábar's historical epic "Agora" which premiered at the 2009 Cannes Film Festival.  Dyas previously received three consecutive Art Directors Guild Award nominations for his production design work on Steven Spielberg's "Indiana Jones and the Kingdom of the Crystal Skull", Shekhar Kapur's "" and "Superman Returns" for Bryan Singer.  He won an ADG award in 2011 for "Inception".  He also earned a BAFTA Award nomination in 2007 for Best Production Design for "Elizabeth: The Golden Age" and for four years in a row Dyas has been named by "The Sunday Times" as one of the top ten Brits working behind the camera in Hollywood.

Passengers (2016 film): Passengers is a 2016 American science fiction film directed by Morten Tyldum and written by Jon Spaihts.  It stars Jennifer Lawrence, Chris Pratt, Michael Sheen, and Laurence Fishburne.  The story depicts two people who are awakened some 90 years too soon from an induced hibernation on a spaceship bound for a new planet.

Fallen Angels (2008 film): Fallen Angels (Norwegian: "Varg Veum: Falne engler" ) is a 2008 film directed by Morten Tyldum.  It was nominated for numerous Amanda Awards in 2008.  It is the fourth film in the "Varg Veum" series.

Larry Dias: Larry Dias is a set decorator who was nominated at the 83rd Academy Awards for his work on the film "Inception", this was in the category of Best Art Direction.  His nomination was shared with Guy Hendrix Dyas and Doug Mowat.

Headhunters (film): Headhunters (Norwegian: "Hodejegerne" ) is a 2011 Norwegian action thriller film, based on the 2008 novel of the same name by Jo Nesbø.  The film was directed by Morten Tyldum and stars Aksel Hennie, Nikolaj Coster-Waldau and Synnøve Macody Lund.  Hennie portrays the successful but insecure corporate recruiter Roger Brown who lives a double life as an art thief to fund his lavish lifestyle.  He finds out that one of his job prospects is in possession of a valuable painting and sets out to steal it.

Gene Serdena: Gene Serdena is a set decorator.  Serdena, along with production designer K. K. Barrett, was nominated for an Academy Award for Best Production Design for the 2013 film "Her".  He was nominated again for Best Production Design, alongside production designer Guy Hendrix Dyas, for their work in 2016 film "Passengers at the 89th Academy Awards.

Buddy (2003 film): Buddy is a 2003 Norwegian film directed by Morten Tyldum after a script by Lars Gudmestad.  The music was composed by Lars Lillo-Stenberg, known from the band DeLillos.  The film was well received by critics, and won two Amanda Awards in 2004.

Doug Mowat (set decorator): He was nominated for an Academy Award during the 83rd Academy Awards for the film "Inception" in the category of Best Art Direction.  He shared his nomination with Guy Hendrix Dyas and Larry Dias.

Question: Who is a star in the 2016 American science fiction film directed by Morten Tyldum, which had Guy Hendrix Dyas as a designer?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "film_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "film_genre": {
      "type": "string",
      "description": "The genre of the film."
    },
    "director": {
      "type": "string",
      "description": "The director of the film."
    },
    "designer_involved": {
      "type": "string",
      "description": "The name of the designer involved in the film's production."
    },
    "stars": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of actors who starred in the film."
    },
    "answer_star": {
      "type": "string",
      "description": "The specific star identified as the answer to the question."
    }
  },
  "required": [
    "film_title",
    "film_year",
    "film_genre",
    "director",
    "designer_involved",
    "stars",
    "answer_star"
  ],
  "additionalProperties": false
}
