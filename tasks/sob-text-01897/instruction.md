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
Mary Reilly (film): Mary Reilly is a 1996 American film directed by Stephen Frears and starring Julia Roberts and John Malkovich.  The movie was written by Christopher Hampton and adapted from the novel "Mary Reilly" by Valerie Martin (itself inspired by Robert Louis Stevenson's "Strange Case of Dr Jekyll and Mr Hyde").  This was the re-teaming of director Frears, screenwriter Hampton, and actors Malkovich and Glenn Close, all of whom were involved in the Oscar-winning "Dangerous Liaisons" (1988).

Andy Muschietti: Andrés Muschietti (] ;; born 26 August 1973), usually credited as Andy Muschietti, is an Argentine film director and screenwriter, best known for directing the 2013 horror film "Mama" and the 2017 adaptation of Stephen King's "It".

It (2017 film): It: Chapter One, or simply It, is a 2017 American supernatural horror film directed by Andy Muschietti, based on the 1986 novel of the same name by Stephen King.  The screenplay is by Chase Palmer, Cary Fukunaga and Gary Dauberman.  The first of a planned duology, the film tells the story of seven children in Derry, Maine, who are terrorized by the eponymous being, only to face their own personal demons in the process.  The novel was previously adapted into a 1990 miniseries.

Julia Zemiro's Home Delivery: Julia Zemiro's Home Delivery is an Australian television comedy interview series, starring Julia Zemiro and produced by Cordell Jigsaw Zapruder.

Mama (2013 film): Mama is a 2013 English-language Spanish supernatural drama horror film directed and co-written by Andy Muschietti and based on his 2008 Argentine short film "Mamá".  The film stars Jessica Chastain and Nikolaj Coster-Waldau, and is produced by Zandy Federico and co-writer Barbara Muschietti, with Guillermo del Toro serving as executive producer.

Mona Lisa Smile: Mona Lisa Smile is a 2003 American drama film produced by Revolution Studios and Columbia Pictures in association with Red Om Films Productions, directed by Mike Newell, written by Lawrence Konner and Mark Rosenthal, and starring Julia Roberts , Kirsten Dunst, Julia Stiles and Maggie Gyllenhaal.  The title is a reference to the "Mona Lisa", the famous painting by Leonardo da Vinci, and the song of the same name, originally performed by Nat King Cole, which was covered by Seal for the movie.  Julia Roberts received a record $25 million for her performance, the highest ever earned by an actress at that time.

Tony Gilroy: Anthony Joseph Gilroy (born September 11, 1956) is an American screenwriter and filmmaker.  He wrote the screenplays for the first four films of the "Bourne" series starring Matt Damon, among other successful films, and directed the fourth film of the franchise.  He was nominated for Academy Awards for his direction and script for "Michael Clayton", starring George Clooney.  Gilroy wrote and directed "Duplicity", starring Julia Roberts and Clive Owen, and co-wrote "Rogue One: A Star Wars Story".

10 Days in a Madhouse: 10 days in a Madhouse is a 2015 American biographical film about the experiences of undercover journalist Nellie Bly where, as a reporter working for Joseph Pulitzer, she got herself committed to Blackwell's Island Asylum to report on atrocities.  The production was written and directed by Timothy Hines with consultation from one of Bly’s modern biographers, Brooke Kroeger.  The film draws from Bly’s exposé "Ten Days in a Mad-House", which led to significant reforms in the treatment of mental health patients in her time.  The cast includes Caroline Barry, Christopher Lambert, Kelly Le Brock, Julia Chantrey and Alexandra Callas.

Starring Julia: "Starring Julia" or in Arabic "Min Boutoulet Julia" is a short film (duration of 14 minutes) written and directed by Elie Fahed.

Julia Chantrey: Julia Ann Chantrey (born March 2, 1980 in Toronto, Canada), is a Canadian actress, known for her role as Eva in Total Drama.  She is also winner of the Gemini Award for Best Performance by an Actress in a Continuing Leading Dramatic Role.  In 2013 perform the role Nina in the horror film Mama.

Question: Which movie starring Julia Chantrey was directed by Andy Muschietti?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "movie_title": {
      "type": "string",
      "description": "The title of the movie."
    },
    "director": {
      "type": "string",
      "description": "The director of the movie."
    },
    "starring_actress": {
      "type": "string",
      "description": "The actress who starred in the movie."
    },
    "release_year": {
      "type": "integer",
      "description": "The release year of the movie."
    },
    "genre": {
      "type": "string",
      "description": "The primary genre of the movie."
    }
  },
  "required": [
    "movie_title",
    "director",
    "starring_actress",
    "release_year",
    "genre"
  ],
  "additionalProperties": false
}
