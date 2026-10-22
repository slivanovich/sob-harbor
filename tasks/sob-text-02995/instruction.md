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
Mary Shelley's Frankenstein (film): Mary Shelley's Frankenstein is a 1994 horror drama film directed by Kenneth Branagh and starring Robert De Niro, Kenneth Branagh, Tom Hulce, Helena Bonham Carter, Ian Holm, John Cleese, and Aidan Quinn.  The picture was produced on a budget of $45 million and is considered the most faithful film adaptation of Mary Shelley's novel "Frankenstein; or, The Modern Prometheus", despite several differences and additions in plot from the novel.

Showtime (film): Showtime is a 2002 American buddy cop action comedy film directed by Tom Dey.  The film stars Robert De Niro and Eddie Murphy in the lead roles alongside Rene Russo, William Shatner, Pedro Damian and De Niro's real life adopted daughter Drena De Niro.  The film was released in the United States on March 15, 2002.

Robert De Niro filmography: Robert De Niro's filmography includes the year the film was/will be released, the name of his character, and other related notes.  There is also a list of films he has produced and his appearances in theater plays, TV series and documentaries.  He is sometimes credited as Robert DeNiro and Robert De Nero.  De Niro has appeared in over 100 films throughout his career.

TriBeCa Productions: Tribeca Productions, a film and television production company, was co-founded in 1989 by actor Robert De Niro and producer Jane Rosenthal in the lower Manhattan neighborhood of TriBeCa.  In 2003, Robert De Niro, Jane Rosenthal, and Craig Hatkoff moved Tribeca Productions to become a part of Tribeca Enterprises, which organizes the Tribeca Film Festival, Tribeca Film Festival International, Tribeca Cinemas, and Tribeca Film.  De Niro, Rosenthal, and Craig Hatkoff are also the co-founders of the Tribeca Film Festival.

The Good Shepherd (film): The Good Shepherd is a 2006 spy film produced and directed by Robert De Niro and starring Matt Damon, Angelina Jolie and De Niro, with an extensive supporting cast.  De Niro also produced it with James G. Robinson and Jane Rosenthal.

John Mariano: John Mariano (born August 5, 1960 in Astoria, New York) is an American actor who has worked in film, television, animation and nightclubs.  He is known for playing tough guys with a comic edge.  His ability of physical comedy has been compared to Jerry Lewis and Buster Keaton.  Keaton's wife Eleanor was quoted as saying; "He reminded me so much of Buster, it gave me chills".  He got his start in films playing a prissy bank teller in "Tough Guys" with Burt Lancaster and Kirk Douglas.  Working steadily in both film and television, he's best remembered on television for playing Johnny the waiter in "Caroline in the City" with Lea Thompson.  A gifted improviser, sketch player and voice-over artist, his impression of Robert De Niro in a sketch entitled "De Niro Sings the Supremes" at The Groundlings, led to him playing a pigeon named Bobby in the cartoon series "Animaniacs", who is based on a character played by De Niro in "Goodfellas".

Righteous Kill: Righteous Kill is a 2008 American crime thriller film with elements of a buddy cop film directed by Jon Avnet, and starring Al Pacino and Robert De Niro.  This is the second film (the first one is "Heat") in which De Niro and Pacino appear together in the same scenes (both De Niro and Pacino starred in "The Godfather Part II", but did not appear in any of the same scenes).  "Righteous Kill" also features John Leguizamo, Carla Gugino, Donnie Wahlberg, Brian Dennehy, and Curtis "50 Cent" Jackson.  The film was released in the United States on September 12, 2008.

Robert De Niro Sr.: Robert Henry De Niro (May 3, 1922 – May 3, 1993), better known as Robert De Niro Sr., was an American abstract expressionist painter and the father of actor Robert De Niro.

Tom Hulce: Thomas Edward "Tom" Hulce ( ; born December 6, 1953) is an American actor and theater producer.  As an actor, he is best known for his role as Larry "Pinto" Kroger in "Animal House" (1978), his Academy Award-nominated portrayal of Wolfgang Amadeus Mozart in "Amadeus" (1984), and his role as Quasimodo in Disney's "The Hunchback of Notre Dame" (1996).  Additional acting awards included four Golden Globe nominations, an Emmy Award, and a Tony Award.  Hulce retired from acting in the mid-1990s to focus on stage directing and producing.  In 2007, he won a Tony Award as a lead producer of the Broadway musical "Spring Awakening".

Heat (1995 film): Heat is a 1995 American crime film written, produced and directed by Michael Mann, and starring Robert De Niro, Al Pacino, and Val Kilmer.  De Niro plays Neil McCauley, a professional thief, while Pacino plays Lt. Vincent Hanna, a LAPD robbery-homicide detective tracking down McCauley's crew.  The story is based on the former Chicago police officer Chuck Adamson's pursuit during the 1960s of a criminal named McCauley, after whom De Niro's character is named.  Heat is a remake by Mann of a TV series he had worked on, the pilot of which was released as a TV movie, "L.A. Takedown" in 1989.

Question: The actor that played Larry "Pinto" Kroger in "Animal House" stars with Robert De Niro and Kenneth Branagh in a 1994 horror film directed by who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film in question."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film."
        },
        "genre": {
          "type": "string",
          "description": "The genre of the film."
        },
        "director": {
          "type": "string",
          "description": "The director of the film."
        },
        "starring_actors": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of the main actors starring in the film."
        }
      },
      "required": [
        "title",
        "release_year",
        "genre",
        "director",
        "starring_actors"
      ],
      "additionalProperties": false
    },
    "actor_from_animal_house": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the actor who played Larry 'Pinto' Kroger."
        },
        "role_in_animal_house": {
          "type": "string",
          "description": "The character played by the actor in 'Animal House'."
        },
        "also_stars_in_target_film": {
          "type": "boolean",
          "description": "Indicates if this actor also stars in the film in question."
        }
      },
      "required": [
        "name",
        "role_in_animal_house",
        "also_stars_in_target_film"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The name of the director of the specified film."
    }
  },
  "required": [
    "film_details",
    "actor_from_animal_house",
    "final_answer"
  ],
  "additionalProperties": false
}
