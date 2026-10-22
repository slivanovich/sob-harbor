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
Hard-Boiled Haggerty (film): Hard-Boiled Haggerty (aka Hard Boiled Haggerty) is a 1927 American silent war film directed by Charles Brabin.  The film stars Milton Sills and Molly O'Day, taking on two roles as both the character Germaine and her look-alike sister.  "Hard-Boiled Haggerty" was one of the first American films to portray aerial combat in World War I.

Lenny and the Squigtones: Lenny and the Squigtones is a fictional musical group headed by Michael McKean and David Lander, the two actors who played the characters Lenny and Squiggy on the television series "Laverne & Shirley".  The group's eponymous debut album, Lenny & Squiggy Present Lenny and the Squigtones, was released on the Casablanca label in 1979.  Recorded live at the Roxy in Hollywood, they perform parodies of 50's rock ballads ("Night After Night," "Creature Without a Head").  In between, there's plenty of schtick and patter ("So's Your Old Testament," "Babyland").  The album is now a collector’s item because of credited guitar work by future Spinal Tap member Nigel Tufnel (Christopher Guest).  A photo on the inside cover also includes two band members, "Murph", the keyboard player from The Blues Brothers, and "Ming the Merciless," purported to be Kiss drummer Peter Criss without his famous "cat" costume and make-up, though Criss denies it was him.  McKean has confirmed that the drummer in the photograph is actually Don Poncher.

Raiders of the Lost Ark: Raiders of the Lost Ark (also known as Indiana Jones and the Raiders of the Lost Ark) is a 1981 American action adventure film directed by Steven Spielberg, with a screenplay written by Lawrence Kasdan, from a story by George Lucas and Philip Kaufman.  It was produced by Frank Marshall for Lucasfilm Ltd., with Lucas and Howard Kazanjian as executive producers.  Starring Harrison Ford, it was the first installment in the "Indiana Jones" film franchise to be released, though it is the second in internal chronological order.  It pits Indiana Jones (Ford) against a group of Nazis who are searching for the Ark of the Covenant, which Adolf Hitler believes will make his army invincible.  The film co-stars Karen Allen as Indiana's former lover, Marion Ravenwood; Paul Freeman as Indiana's rival, French archaeologist René Belloq; John Rhys-Davies as Indiana's sidekick, Sallah; Ronald Lacey as Gestapo agent Arnold Toht; and Denholm Elliott as Indiana's colleague, Marcus Brody.

Ty Glaser: Ty Glaser (born 12 November 1982) is a British film, stage and television actress, best known for her role as Dr. Gemma Wilde on the BBC drama series "Holby City".  She has appeared in a number of other TV series including "Secret Diary of a Call Girl", "Above Suspicion", "The Bill" and most notably a stint in "Emmerdale" as Libby Charles.  She made her film debut in 2006 with a minor role as a police officer in "The Parole Officer" and most recently appeared in "Hard Boiled Sweets".

Paul Freeman (actor): Paul Freeman (born 18 January 1943) is an English character actor.  He is best known for his roles as rival archaeologist René Belloq in "Raiders of the Lost Ark" (1981), evil wine baron Gustav Riebmann on season 4 of "Falcon Crest" (1984–85), supervillain Ivan Ooze in "" (1995) and Reverend Shooter in "Hot Fuzz" (2007).

Hard Boiled Sweets: Hard Boiled Sweets is a 2012 British crime drama film written and directed by David LG Hughes.  It tells the story of a group of squabbling Essex gangsters.  The cast includes two actors (Paul Freeman and Ian Hart) that had appeared in Hughes' earlier short film "A Girl and a Gun" from which this, his first feature, was developed.

Chow Yun-fat: Chow Yun-fat, SBS (born 18 May 1955), previously known as Donald Chow, is a Hong Kong actor.  He is best known in Asia for his collaborations with filmmaker John Woo in the heroic bloodshed-genre films "A Better Tomorrow", "The Killer" and "Hard Boiled"; and in the West for his roles as Li Mu-bai in "Crouching Tiger, Hidden Dragon" and Sao Feng in "".  He mainly plays in dramatic films and has won three Hong Kong Film Awards for Best Actor and two Golden Horse Awards for Best Actor in Taiwan.

Valerianella locusta: Valerianella locusta is a small annual plant that is eaten as a leaf vegetable.  It has a characteristic nutty flavor, dark green color, and soft texture, and is popularly served as salad greens.  Common names include corn salad, common cornsalad, lamb's lettuce, mâche ( ), fetticus, feldsalat, nut lettuce, field salad, and rapunzel.  In restaurants that feature French cooking, it may be called doucette or raiponce, as an alternative to mâche, by which it is best known.  In German-speaking Switzerland it is known as Nüsslisalat or Nüssler, terms that have been borrowed by the area's many English-speakers.  It is typically served as a salad with chopped, hard boiled eggs and crumbled bacon.

Anthony Wong (Hong Kong actor): Anthony Wong Chau-sang (born Anthony Perry; 2 September 1961), known professionally as Anthony Wong, is a Hong Kong actor.  Wong is perhaps best known in the West for his roles in the 1992 action film "Hard Boiled", the 2002 critically acclaimed "Infernal Affairs", and as General Yang in the 2008 Hollywood film "".

Geof Darrow: Geofrey "Geof" Darrow (born October 21, 1955) is an American comic book artist, best known for his work on "Hard Boiled"; "The Big Guy and Rusty the Boy Robot", which was adapted into an animated television series of the same name, and "Shaolin Cowboy".

Question: Hard Boiled Sweets includes two actors, Ian Heart and an English actor who  is best known for his roles as rival archaeologist René Belloq in what movie?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "query_context_film": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film mentioned in the initial query."
        },
        "actors_associated": {
          "type": "array",
          "description": "A list of actors mentioned in relation to the query context film.",
          "items": {
            "type": "object",
            "properties": {
              "name": {
                "type": "string",
                "description": "The name of the actor."
              },
              "is_target_actor": {
                "type": "boolean",
                "description": "True if this actor is the one whose specific role is being queried."
              }
            },
            "required": [
              "name",
              "is_target_actor"
            ],
            "additionalProperties": false
          }
        }
      },
      "required": [
        "title",
        "actors_associated"
      ],
      "additionalProperties": false
    },
    "target_actor_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the actor whose role is being queried."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the actor."
        },
        "best_known_role_character": {
          "type": "string",
          "description": "The character name for which the actor is best known, as per the query."
        },
        "best_known_role_film_title": {
          "type": "string",
          "description": "The title of the film where the actor played the specified best-known role."
        },
        "best_known_role_film_year": {
          "type": "integer",
          "description": "The release year of the film where the actor played the specified best-known role."
        }
      },
      "required": [
        "name",
        "nationality",
        "best_known_role_character",
        "best_known_role_film_title",
        "best_known_role_film_year"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The title of the movie that answers the question."
    }
  },
  "required": [
    "query_context_film",
    "target_actor_details",
    "final_answer"
  ],
  "additionalProperties": false
}
