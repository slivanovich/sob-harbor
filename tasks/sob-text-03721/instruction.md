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
Facifica Falayfay: Facifica Falayfay is a 1969 movie starring Dolphy, adapted from Mars Ravelo’s series of superhero comics.  A sequel, "Mga Anak ni Facifica Falayfay", was released in 1987.

Pasand Apni Apni: Pasand Apni Apni is a 1983 Hindi-language Indian film directed by Basu Chatterjee, starring Ashok Kumar, Mithun Chakraborty, Utpal Dutt, Rati Agnihotri, Subbiraj, Mithilesh Chaturvedi, Javed Khan and A K Hangal.  The concept of this movie is based on the 1951 British film "Happy Go Lovely" which was earlier used in the 1969 movie "Sajan" and subsequently in "Ghajini".

Pyar Ka Mausam: Pyar Ka Mausam "(English: Season of Love)" is a 1969 movie under Nasir Hussain films banner.  Hussain wrote, produced, and directed the film.  It starred Shashi Kapoor, and the Nasir Husain fixture- Asha Parekh.  It also had Bharat Bhushan, Nirupa Roy, Madan Puri, Tahir Hussain and another Nasir Husain fixture Rajendranath.  Nasir's nephew Faisal Khan who was 3 years old at the time plays Shashi Kapoor's character as a child.  Two more Husain fixtures were responsible for the memorable songs: lyricist Majrooh Sultanpuri and music composer R.D. Burman.  The musical instrument duggi was played by Homi Mullan for the song Ni sultana re.  R.D.Burman also had an acting role in the film.  The film became a Silver Jubilee Hit.

Irina Kupchenko: Irina Petrovna Kupchenko (Russian: Ирина Петровна Купченко ; born 1 March 1948 in Vienna) is a Soviet and Russian actress.  She rose to prominence after acting in Andrei Konchalovsky's 1969 movie adaptation of "A Nest of Gentlefolk".  She has performed in more than forty films since 1969.

Winning (disambiguation): Winning is a 1969 movie starring Paul Newman.

Wendell Burton: Wendell Ray Burton (July 21, 1947 – May 30, 2017) was an American television executive and former actor.  He is best known for his co-starring role with Liza Minnelli in the 1969 movie "The Sterile Cuckoo" (1969).

Freddie Steele: Freddie Steele (December 18, 1912 – August 22, 1984) was a boxer and film actor born Frederick Earle Burgett in Seattle, Washington.  He was recognized as the National Boxing Association (NBA) Middleweight Champion of the World between 1936 and 1938.  Steele was nicknamed "The Tacoma Assassin" and was trained by Jack Connor, Johnny Babnick, and Ray Arcel, while in New York.  His managers included George McAllister, Dave Miller, Eddie Miller, and Pete Reilly.  He appeared as an actor in a number of Hollywood films in the 1940s, including Preston Sturges's "Hail the Conquering Hero".

Midas Run: Midas Run (UK title A Run on Gold) is a 1969 American comedy film directed by Alf Kjellin and starring Richard Crenna, Anne Heywood and, in one of his final big-screen roles, Fred Astaire.

Fred Astaire: Fred Astaire (born Frederick Austerlitz; May 10, 1899 – June 22, 1987) was an American dancer, singer, actor, choreographer and television presenter.

L'Amour fou (1969 film): L'Amour fou is a 1969 movie directed by Jacques Rivette, who also co-wrote the script with Marilù Parolini.

Question: Who directed the 1969 movie starring the actor born Frederick Austerlitz?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "movie_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the movie."
        },
        "year": {
          "type": "integer",
          "description": "The release year of the movie."
        },
        "director": {
          "type": "string",
          "description": "The director of the movie."
        }
      },
      "required": [
        "title",
        "year",
        "director"
      ],
      "additionalProperties": false
    },
    "starring_actor_info": {
      "type": "object",
      "properties": {
        "actor_name": {
          "type": "string",
          "description": "The common name of the actor."
        },
        "birth_name": {
          "type": "string",
          "description": "The birth name of the actor."
        }
      },
      "required": [
        "actor_name",
        "birth_name"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The name of the director of the movie."
    }
  },
  "required": [
    "movie_details",
    "starring_actor_info",
    "final_answer"
  ],
  "additionalProperties": false
}
