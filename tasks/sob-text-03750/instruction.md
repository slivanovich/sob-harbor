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
Shivaram: S. Shivaram (born 1938), popularly known simply as Shivaram or Shivaramanna, is an Indian actor, producer and director whose Kannada cinema career has spanned six decades.  He has played roles including lead hero performances, character roles, comedic roles, as well as supporting parts.  He teamed up with his elder brother, S. Ramanathan and produced several films under the name Rashi Brothers apart from directing "Hrudaya Sangama" in 1972.  The brothers together produced few Bollywood films as well.  As an actor, Shivaram has the distinction of working with many stalwart directors out of which his association with Puttanna Kanagal is much remembered.

Philip Seymour Hoffman on stage and screen: Philip Seymour Hoffman (19672014) was an American actor, director, and producer.  He was prolific in both film and theater from the early 1990s until his death at the age of 46, after which "The New York Times" declared him "perhaps the most ambitious and widely admired American actor of his generation".

Rajesh (Kannada actor): Vidyasagar (born 15 April 1935), known by his stage name Rajesh, is an Indian actor who appears in Kannada films.  Known as 'Kala Thapswi', Rajesh is an ardent fan of literature.  Vidyasagar is the original name of Rajesh.  He appeared in many films as the lead in the late 1960s and early 1970s, but later on started appearing in character roles.  He is the father of film actress Aasha Rani who had acted in the film "Rathasapthami" with Shivrajkumar and the father in law of popular Kannada and Tamil actor Arjun Sarja.  He has acted in over 150 films.  "Kalathapasvi Rajesh Athmakathe" is the biography of Rajesh.  In 2014, he was awarded the Dr. Rajkumar Cultural Endowment Award by the Kannada Sahitya Parishat.

Arthur Samuel: Arthur Lee Samuel (December 5, 1901 – July 29, 1990) was an American pioneer in the field of computer gaming and artificial intelligence.  He coined the term "machine learning" in 1959.  The Samuel Checkers-playing Program appears to be the world's first self-learning program, and as such a very early demonstration of the fundamental concept of artificial intelligence (AI).  He was also a senior member in TeX community who devoted much time giving personal attention to the needs of users and wrote an early TeX manual in 1983.

Urmila Bhatt: Urmila Bhatt (born 1934, in Dehradun) was a reputed actress of Hindi cinema.  She started her acting career by doing acting in Drama Theatre.  She joined Sangeet Kala Academy in Rajkot as a folk dancer and singer.  It was during that time that her famous Gujarati drama Jesal Toral ran to more than a thousand performances She acted in more than 75 Gujarati films and also in 15 to 20 Rajasthani movies.She had also played character roles in Hindi films for over two and a half decades (1960s to early 1990s).  She had also acted in various television serials.  She had also been honoured with numerous awards by the government of Gujarat.

Terry Miller (politician): Terrence B. "Terry" Miller (November 10, 1942 – April 13, 1989) was an American businessman and politician.  Miller served as the fourth Lieutenant Governor of Alaska from 1978 to 1982.  His political career, which began while he was in his early 20s, lasted over two decades and was cut short by his death from bone cancer at age 46.

Philip Seymour Hoffman: Philip Seymour Hoffman (July 23, 1967 – February 2, 2014) was an American actor, director, and producer.  Best known for his distinctive supporting and character roles – typically lowlifes, eccentrics, bullies, and misfits – Hoffman acted in many films from the early 1990s until his death at age 46.

Dhumal (actor): Dhumal (29 March 1914 – 13 February 1987) was an actor in Bollywood films known for playing character roles.  He acted in many movies and was active from the mid 1940s till the late 1980s.  He started his acting career from Marathi theatre, which paved way for Marathi cinema and later he moved to Hindi cinema, where he mostly played comedy roles and late in career character roles.  He worked in notable films like, "Howrah Bridge" (1958), "Bombai Ka Babu" (1960), "Kashmir Ki Kali" (1964), "Gumnaam" (1965), "Do Badan" (1966), "Love in Tokyo" (1966) and "Benaam" (1974).

Doubt (2008 film): Doubt is a 2008 American period drama film written and directed by John Patrick Shanley based on his Pulitzer Prize-winning stage play "".  Produced by Scott Rudin, the film takes place in a St. Nicholas school led by Sister Aloysius (Meryl Streep).  Sister James (Amy Adams) tells Aloysius that Father Flynn (Philip Seymour Hoffman) might have too much personal attention with the school's only black student Donald Miller (Joseph Foster), thus leading to Aloysius starting a crusade against Flynn.  The film also stars Viola Davis as Donald Miller's mother, Mrs. Miller.

Subhendu Chatterjee: Subhendu Chatterjee (29 November 1936 – 5 July 2007) was an Indian actor of television and films in Bengali.  A contemporary of late Bengali matinee idol Uttam Kumar and actor Soumitra Chatterjee, with whom he played second hero in many films, Chatterjee with age had graduated into character roles.

Question: Which American actor, director and producer best known for his distinctive supporting and character roles- typically lowlifes, eccentrics, bullies, and misfits – Hoffman acted in many films from the early 1990s until his death at age 46, did sister James indicate might have too much personal attention with the school's only black student Donald Miller (Joseph Foster)?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the American actor, director, and producer."
    },
    "professions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of professions held by the individual."
    },
    "death_age": {
      "type": "integer",
      "description": "The age at which the actor died."
    },
    "film_details": {
      "type": "object",
      "properties": {
        "film_title": {
          "type": "string",
          "description": "The title of the film where the event occurred."
        },
        "character_played": {
          "type": "string",
          "description": "The character played by the actor in the specified film."
        },
        "accuser": {
          "type": "string",
          "description": "The name of the character who made the accusation."
        },
        "accused_of_attention_with_student": {
          "type": "string",
          "description": "The name of the student with whom the character was accused of having too much personal attention."
        }
      },
      "required": [
        "film_title",
        "character_played",
        "accuser",
        "accused_of_attention_with_student"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actor_name",
    "professions",
    "death_age",
    "film_details"
  ],
  "additionalProperties": false
}
