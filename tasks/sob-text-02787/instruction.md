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
Down Three Dark Streets: Down Three Dark Streets is a 1954 documentary-style film, starring Broderick Crawford and directed by Arnold Laven.  The screenplay was written by Gordon and Mildred Gordon, based on their novel "Case File FBI".

Zeke Kinski: Ezekiel "Zeke" Kinski is a fictional character from the Australian soap opera "Neighbours", played by Matthew Werkmeister.  He made his first on-screen appearance on 22 August 2005.  Zeke is the son of Alex Kinski and the younger brother of Katya and Rachel.  His storylines have included the death of his father, being trapped in the warehouse collapse, developing an anxiety disorder, joining Pirate Net and forming many romantic relationships.  In October 2010, it was announced that Werkmeister and his character were to leave "Neighbours".  Zeke made his final appearance on 11 March 2011.  In February 2014, it was announced that Werkmeister would be returning to "Neighbours" for a brief guest stint and Zeke returned on 7 April 2014.

That Darn Cat!: That Darn Cat!  is a 1965 American Walt Disney Productions thriller comedy film starring Hayley Mills (in her last of the six films she made for the Walt Disney Studios) and Dean Jones (starring in his first film for Disney) in a story about bank robbers, a kidnapping and a mischievous cat.  The film was based on the 1963 novel "Undercover Cat" by Gordon and Mildred Gordon and was directed by Robert Stevenson.  The title song was written by the Sherman Brothers and sung by Bobby Darin.  The 1997 remake includes a cameo appearance by Dean Jones.

Undercover Cat: Undercover Cat is a novel by Gordon and Mildred Gordon, about a cat who assists the FBI in tracking down a pair of bank robbers.  It was published in 1963.

Mildred Gordon (politician): Mildred Gordon (née Fellerman; 24 August 1923 – 8 April 2016) was a British Labour politician.

Mildred Gordon (biologist): Mildred Gordon (1920–93) was an American microbiologist noted for her seminal research of human sperm and the endometrium, and of the uterus.

Experiment in Terror: Experiment in Terror is a 1962 suspense-thriller released by Columbia Pictures.  It was directed by Blake Edwards and written by Mildred Gordon and Gordon Gordon based on their 1961 novel "Operation Terror".  The film stars Glenn Ford, Lee Remick, Stefanie Powers, and Ross Martin.

Mildred Gordon (Ganas): Mildred Gordon (born 1922 - January 4, 2015) was the founder and Executive Director of the Foundation for Feedback Learning (FFL) and co-founder of the Ganas intentional community.  She was the Communications Director of ActivistSolutions.org.

That Darn Cat (1997 film): That Darn Cat is a 1997 American mystery comedy film starring Christina Ricci and Doug E. Doug.  It is a remake of the 1965 film "That Darn Cat! ", which in turn was based on the book "Undercover Cat" by Gordon and Mildred Gordon.  It is directed by British TV veteran Bob Spiers (most famous for "Fawlty Towers", as well as "Spice World") and written by Scott Alexander and Larry Karaszewski, best known for "Ed Wood" and the first two "Problem Child" films.

Dean Jones (actor): Dean Carroll Jones (January 25, 1931 – September 1, 2015) was an American actor best known for his roles as Agent Zeke Kelso in "That Darn Cat! " (1965), Jim Douglas in "The Love Bug" (1968), Albert Dooley in "The Million Dollar Duck" (1971; for which he received a Golden Globe nomination) and Dr. Herman Varnick in "Beethoven" (1992).

Question: What Gordon and Mildred Gordon novel was made into a movie in which a character named Agent Zeke Kelso was portrayed?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "novel_title": {
      "type": "string",
      "description": "The title of the novel by Gordon and Mildred Gordon."
    },
    "authors": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The authors of the novel."
    },
    "film_adaptation": {
      "type": "object",
      "properties": {
        "film_title": {
          "type": "string",
          "description": "The title of the film adaptation."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film."
        },
        "character_portrayed": {
          "type": "object",
          "properties": {
            "character_name": {
              "type": "string",
              "description": "The name of the character in the film."
            },
            "actor_name": {
              "type": "string",
              "description": "The name of the actor who portrayed the character."
            }
          },
          "required": [
            "character_name",
            "actor_name"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "film_title",
        "release_year",
        "character_portrayed"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "novel_title",
    "authors",
    "film_adaptation"
  ],
  "additionalProperties": false
}
