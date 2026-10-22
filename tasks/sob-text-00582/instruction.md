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
La Vallée (film): La Vallée, also known as Obscured By Clouds, is a 1972 French film written and directed by Barbet Schroeder.  The film stars Bulle Ogier as Viviane, a woman who goes on a strange and accidental voyage of self-discovery through the New Guinea bush.

Tricheurs: Tricheurs is a 1984 film directed by Barbet Schroeder.

Jung (2000 film): Jung (translation: "War") is a 2000 Bollywood film directed by Sanjay Gupta.  The film has some similarities to the Hollywood film "Desperate Measures".

The Darjeeling Limited: The Darjeeling Limited is a 2007 American adventure comedy-drama film directed by Wes Anderson which he co-produced with Scott Rudin, Roman Coppola and Lydia Dean Pilcher and co-wrote with Coppola and Jason Schwartzman.  The film stars Owen Wilson, Adrien Brody and Schwartzman and also features Waris Ahluwalia, Amara Karan, Barbet Schroeder and Anjelica Huston with Natalie Portman, Camilla Rutherford, Irrfan Khan and Bill Murray in cameo roles.

Barfly (film): Barfly is a 1987 American comedy drama film directed by Barbet Schroeder and starring Mickey Rourke and Faye Dunaway.  The film is a semi-autobiography of poet/author Charles Bukowski during the time he spent drinking heavily in Los Angeles, and it presents Bukowski's alter ego Henry Chinaski.  The screenplay, written by Bukowski, was commissioned by the French film director Schroeder, and it was published (with illustrations by the author) in 1984, when film production was still pending.

Maîtresse: Maîtresse ("mistress" or "teacher", in French) is a 1975 French film directed by Barbet Schroeder, starring Bulle Ogier and, in one of his earliest leading roles, Gérard Depardieu.  The film provoked controversy in the United Kingdom and the United States because of its graphic depictions of sado-masochism.

Single White Female: Single White Female is a 1992 American psychological erotic thriller film based on John Lutz's novel "SWF Seeks Same".  The film stars Bridget Fonda and Jennifer Jason Leigh and is directed by Barbet Schroeder.

Before and After (film): Before and After is a 1996 American crime drama-mystery film based on the 1992 novel of the same title by American writer Rosellen Brown.  The movie was directed by Barbet Schroeder and starred Meryl Streep as Dr. Carolyn Ryan, Liam Neeson as Ben Ryan, Edward Furlong as Jacob Ryan, and Julia Weldon as Judith Ryan (who also narrated the movie).

Les films du losange: Les films du losange is a film production company founded by Barbet Schroeder and Éric Rohmer in 1962.  The company funds and distributes many films from the French nouvelle vague era, directed by Rohmer, Schroeder, Roger Planchon, Jacques Rivette, and later on Michael Haneke and Jacques Doillon.

Desperate Measures (film): Desperate Measures is a 1998 American action thriller film starring Michael Keaton, Andy García, Marcia Gay Harden and Brian Cox, directed by Barbet Schroeder.  It was filmed in both the San Francisco Bay Area and downtown Pittsburgh with such landmarks as the BNY Mellon Center, the Allegheny County Courthouse and the Oakland Bay Bridge.  The film was released on January 30, 1998 and was a critical and financial failure.  However, Andy García won an ALMA Award for "Outstanding Actor in a Feature Film in a Crossover Role".

Question: Which movie directed by Barbet Schroeder has some similarities with "Jung"

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_with_similarities_context": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film mentioned in the context as having similarities."
        }
      },
      "required": [
        "title"
      ],
      "additionalProperties": false
    },
    "schroeder_directed_film_with_similarities": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film directed by Barbet Schroeder that has similarities."
        },
        "director": {
          "type": "string",
          "description": "The director of the film."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film."
        },
        "genres": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of genres for the film."
        },
        "country": {
          "type": "string",
          "description": "The country of origin for the film."
        }
      },
      "required": [
        "title",
        "director",
        "release_year",
        "genres",
        "country"
      ],
      "additionalProperties": false
    },
    "similarity_statement": {
      "type": "string",
      "description": "The statement from the context describing the similarity."
    }
  },
  "required": [
    "film_with_similarities_context",
    "schroeder_directed_film_with_similarities",
    "similarity_statement"
  ],
  "additionalProperties": false
}
