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
The Count of Monte Cristo (1953 film): The Count of Monte Cristo (Spanish: El Conde de Montecristo) is a 1953 Argentine-Mexican historical adventure film directed by León Klimovsky and starring Jorge Mistral, Elina Colomer and Santiago Gómez Cou.  It is an adaptation of Alexandre Dumas's 1844 novel "The Count of Monte Cristo".

The Count of Monte Cristo (1975 film): The Count of Monte Cristo is a 1975 television film produced by ITC Entertainment and based upon the book "The Count of Monte Cristo" by Alexandre Dumas, père.  It was directed by David Greene and starred Richard Chamberlain as Edmond Dantès, Kate Nelligan as Mercedes, Tony Curtis as Fernand Mondego, Louis Jourdan (who played Edmond Dantès in the 1961 film adaptation of the novel) as De Villefort, Donald Pleasence as Danglars, Trevor Howard as Abbé Faria, and Isabelle de Valvert as Haydee.  ITC had previously produced a 39-part TV series based on the same source material, in 1956.

Monte Cristo (1922 film): Monte Cristo is a 1922 American silent film produced and distributed by Fox Film Corporation and directed by Emmett J. Flynn.  It is based on the novel "The Count of Monte Cristo" by Alexandre Dumas, which was adapted by 19th century thespian Charles Fechter and written for this screen version by Bernard McConville.  John Gilbert plays the hero with Estelle Taylor as the leading lady.  This film was long thought lost until a print surfaced in the Czech Republic.  The film has been released on DVD, packaged with Gilbert's 1926 MGM film "Bardelys the Magnificent".

The Return of Monte Cristo (1946 film): The Return of Monte Cristo is a 1946 swashbuckler film which is a sequel to "The Count of Monte Cristo" (1934) and "The Son of Monte Cristo" (1940)"

Edmond Dantès: Edmond Dantès (] ) is a title character and the protagonist of Alexandre Dumas, père's 1844 adventure novel "The Count of Monte Cristo".  Within the story's narrative, Dantès is an intelligent, honest, and loving man who turns bitter and vengeful after he is framed for a crime he did not commit.  When Dantès finds himself free and enormously wealthy, he takes it upon himself to reward those who have helped him in his plight and punish those responsible for his years of suffering.  He is known by the aliases The Count of Monte Cristo (French: "le Comte de Monte-Cristo" ), Sinbad the Sailor ("Sinbad le Marin"), Abbé Busoni, and Lord Wilmore.

The Count of Monte Cristo (James Behr musical): The Count of Monte Cristo musical, book and music by James Behr, is adapted from the famous novel by Alexander Dumas. " The Count of Monte Cristo" was awarded as Finalist in the New York Musical Theatre Festival, 2011.  It was performed in its entirety at the Off-Broadway Bleecker Street Theater in New York in 2012 as part of the Planet Connections Theatre Festivity.  The Count of Monte Cristo was also performed in part in New York in 2010 at the New York Off-Broadway Wings Theater during the 2010 West Village Musical Theatre Festival.  It received the festival award for Best Musical Score.  The performances received publication and positive reviews from online newspaper "News Blaze".  Stylistically, the musical has a sound associated with traditional Broadway musicals given that it is orchestrated and recorded with a 30-piece orchestra (i.e., strings, woodwinds and brass).

The Count of Monte Cristo (1934 film): The Count of Monte Cristo is a 1934 American adventure film directed by Rowland V. Lee and starring Robert Donat and Elissa Landi.  Based on the 1844 novel "The Count of Monte Cristo" by Alexandre Dumas, the story concerns a man who is unjustly imprisoned for 20 years for innocently delivering a letter entrusted to him.  When he finally escapes, he seeks revenge against the greedy men who conspired to put him in prison.

The Count of Monte Cristo (1942 film): The Count of Monte Cristo (Spanish: El Conde de Montecristo ) is a 1942 Mexican historical adventure film directed by Roberto Gavaldón and Chano Urueta and starring Arturo de Córdova, Mapy Cortés and Anita Blanch.  It is based on Alexandre Dumas's novel "The Count of Monte Cristo".  a story which has been adapted for film many times.

Jim Caviezel: James Patrick Caviezel (born September 26, 1968) is an American actor, best known for portraying Jesus Christ in the 2004 film "The Passion of the Christ".  Other notable roles include Private Witt in "The Thin Red Line" (1998), Detective John Sullivan in "Frequency" (2000), Jim McCormick in "Madison", Catch in "Angel Eyes" (2001), Johannes in "I Am David", Edmond Dantès in "The Count of Monte Cristo" (2002), golfer Bobby Jones in "" (2004), and Carroll Oerstadt in "Déjà Vu" (2006).  From 2011 until 2016, he starred as John Reese on the CBS science-fiction crime drama series "Person of Interest".

The Count of Monte Cristo (2002 film): The Count of Monte Cristo is a 2002 adventure drama film produced by Roger Birnbaum, Gary Barber, and Jonathan Glickman that was directed by Kevin Reynolds.  An international co-production between the United States, the United Kingdom, and Ireland, the film is an adaptation of the book of the same name by Alexandre Dumas, père and stars Jim Caviezel, Guy Pearce, and Richard Harris.  It follows the general plot of the novel (the main storyline of imprisonment and revenge is preserved); but many aspects, including the relationships between major characters and the ending, have been changed, simplified, or removed; and action scenes have been added.  The film met with modest box office success.

Question: American actor James PAtrick Caviezel starred in what 2002 adventure drama film produced by Roger Birnbaum? The Count of Monte Cristo.

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the film was released."
    },
    "genre": {
      "type": "string",
      "description": "The primary genre of the film."
    },
    "actor_details": {
      "type": "object",
      "properties": {
        "actor_name": {
          "type": "string",
          "description": "The name of the starring actor."
        },
        "role_played": {
          "type": "string",
          "description": "The character played by the actor in the film."
        }
      },
      "required": [
        "actor_name",
        "role_played"
      ],
      "additionalProperties": false
    },
    "producer_details": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "producer_name": {
            "type": "string",
            "description": "The name of a producer of the film."
          }
        },
        "required": [
          "producer_name"
        ],
        "additionalProperties": false
      },
      "description": "A list of producers for the film."
    },
    "is_adaptation": {
      "type": "boolean",
      "description": "Indicates if the film is an adaptation of a book."
    },
    "source_novel_title": {
      "type": "string",
      "description": "The title of the novel the film is adapted from."
    },
    "source_novel_author": {
      "type": "string",
      "description": "The author of the novel the film is adapted from."
    }
  },
  "required": [
    "film_title",
    "release_year",
    "genre",
    "actor_details",
    "producer_details",
    "is_adaptation",
    "source_novel_title",
    "source_novel_author"
  ],
  "additionalProperties": false
}
