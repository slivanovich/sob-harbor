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
Substitutiary Locomotion: "Substitutiary Locomotion" is a song written by Robert and Richard Sherman for the 1971 Walt Disney musical film production "Bedknobs and Broomsticks".  It is sung by "Professor Emelius Browne" (played by David Tomlinson), "Eglantine Price" (played by Angela Lansbury), and the three children.  The spell is composed by five magic words: "Treguna Mekoides Trecorum Satis Dee", which were engraved in the Star of Astoroth.

Snow White and the Seven Dwarfs (1937 film): Snow White and the Seven Dwarfs is a 1937 American animated musical fantasy film produced by Walt Disney Productions and originally released by RKO Radio Pictures.  Based on the German fairy tale by the Brothers Grimm, it is the first full-length cel animated feature film and the earliest Disney animated feature film.  The story was adapted by storyboard artists Dorothy Ann Blank, Richard Creedon, Merrill De Maris, Otto Englander, Earl Hurd, Dick Rickard, Ted Sears and Webb Smith.  David Hand was the supervising director, while William Cottrell, Wilfred Jackson, Larry Morey, Perce Pearce, and Ben Sharpsteen directed the film's individual sequences.

Pinocchio (1940 film): Pinocchio is a 1940 American animated musical fantasy film produced by Walt Disney Productions and based on the Italian children's novel "The Adventures of Pinocchio" by Carlo Collodi.  It was the second animated feature film produced by Disney, made after the success of "Snow White and the Seven Dwarfs" (1937).

Bedknobs and Broomsticks: Bedknobs and Broomsticks is a 1971 British-American musical fantasy film produced by Walt Disney Productions and released by Buena Vista Distribution Company in North America on December 13, 1971.  It is based upon the books "The Magic Bedknob; or, How to Become a Witch in Ten Easy Lessons" (1943) and "Bonfires and Broomsticks" (1945) by English children's author Mary Norton.  The film, which combines live action and animation, stars Angela Lansbury and David Tomlinson.

The Little Mermaid (1989 film): The Little Mermaid is a 1989 American animated musical fantasy film produced by Walt Disney Feature Animation and released by Walt Disney Pictures.  Based on the Danish fairy tale of the same name by Hans Christian Andersen, "The Little Mermaid" tells the story of a beautiful mermaid princess who dreams of becoming human.  Written, produced, and directed by Ron Clements and John Musker, with music by Alan Menken and Howard Ashman (who also served as a co-producer), the film features the voices of Jodi Benson, Christopher Daniel Barnes, Pat Carroll, Samuel E. Wright, Jason Marin, Kenneth Mars, Buddy Hackett, and René Auberjonois.

David Tomlinson: David Cecil MacAlister Tomlinson (7 May 1917 – 24 June 2000) was an English stage, film and television actor and comedian.  Having been described as both a leading man and a character actor, he is primarily remembered for his roles as authority figure George Banks in "Mary Poppins", fraudulent magician Professor Emelius Browne in "Bedknobs and Broomsticks" and as hapless antagonist Peter Thorndyke in "The Love Bug".  In 2002, two years after his death, Tomlinson was posthumously inducted as a Disney Legend.

James and the Giant Peach (film): James and the Giant Peach is a 1996 British-American musical fantasy film directed by Henry Selick, based on the 1961 novel of the same name by Roald Dahl.  It was produced by Tim Burton and Denise Di Novi, directed by Henry Selick, and starred Paul Terry as James.  The film is a combination of live action and stop-motion animation.  Co-stars Joanna Lumley and Miriam Margolyes played James's aunts in the live-action segments, and Simon Callow, Richard Dreyfuss, Susan Sarandon, Jane Leeves, David Thewlis, and Margoyles voiced his insect friends in the animation sequences.

Blackbeard's Ghost: Blackbeard's Ghost is a 1968 American fantasy comedy film produced by Walt Disney Productions, starring Peter Ustinov, Dean Jones, Suzanne Pleshette and directed by Robert Stevenson.  It is based upon the novel of the same name by Ben Stahl and was shot at the Walt Disney Studios.  The Disney Channel aired this film until the late 1990s .

Beauty and the Beast (1991 film): Beauty and the Beast is a 1991 American animated musical romantic fantasy film produced by Walt Disney Feature Animation and released by Walt Disney Pictures.  The 30th Disney animated feature film and the third released during the Disney Renaissance period, it is based on the French fairy tale of the same name by Jeanne-Marie Leprince de Beaumont (who was also credited in the English version as well as in the French version), and ideas from the 1946 French film of the same name directed by Jean Cocteau.  "Beauty and the Beast" focuses on the relationship between the Beast (voice of Robby Benson), a prince who is magically transformed into a monster and his servants into household objects as punishment for his arrogance, and Belle (voice of Paige O'Hara), a young woman whom he imprisons in his castle.  To become a prince again, Beast must learn to love Belle and earn her love in return to avoid remaining a monster forever.  The film also features the voices of Richard White, Jerry Orbach, David Ogden Stiers, and Angela Lansbury.

Eglantine (song): "Eglantine" is a song written by Robert and Richard Sherman for the 1971 Walt Disney musical film "Bedknobs and Broomsticks".  Professor Emelius Browne (played by David Tomlinson) sings the song in an attempt to persuade his student witch, Miss Eglantine Price (played by Angela Lansbury), to join forces with him.  Brown tells Price:

Question: Name the British-American musical fantasy film produced by Walt Disney Productions based upon the book 'How to Become a Witch in Ten Easy Lessons' which features the fraudulent magician Professor Emelius Browne who was played by David Tomlinson the English actor and comedian?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "production_details": {
      "type": "object",
      "properties": {
        "producer": {
          "type": "string",
          "description": "The production company of the film."
        },
        "origin_countries": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The countries of origin for the film."
        },
        "genre": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The genres of the film."
        },
        "release_year": {
          "type": "integer",
          "description": "The year the film was released."
        }
      },
      "required": [
        "producer",
        "origin_countries",
        "genre",
        "release_year"
      ],
      "additionalProperties": false
    },
    "source_material": {
      "type": "object",
      "properties": {
        "book_title": {
          "type": "string",
          "description": "The title of the book the film is based upon."
        },
        "author": {
          "type": "string",
          "description": "The author of the source book."
        }
      },
      "required": [
        "book_title",
        "author"
      ],
      "additionalProperties": false
    },
    "featured_character": {
      "type": "object",
      "properties": {
        "character_name": {
          "type": "string",
          "description": "The name of the featured character."
        },
        "actor_details": {
          "type": "object",
          "properties": {
            "actor_name": {
              "type": "string",
              "description": "The name of the actor who played the character."
            },
            "nationality": {
              "type": "string",
              "description": "The nationality of the actor."
            },
            "professions": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "The professions of the actor."
            }
          },
          "required": [
            "actor_name",
            "nationality",
            "professions"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "character_name",
        "actor_details"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "production_details",
    "source_material",
    "featured_character"
  ],
  "additionalProperties": false
}
