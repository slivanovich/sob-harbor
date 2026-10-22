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
James and the Giant Peach (film): James and the Giant Peach is a 1996 British-American musical fantasy film directed by Henry Selick, based on the 1961 novel of the same name by Roald Dahl.  It was produced by Tim Burton and Denise Di Novi, directed by Henry Selick, and starred Paul Terry as James.  The film is a combination of live action and stop-motion animation.  Co-stars Joanna Lumley and Miriam Margolyes played James's aunts in the live-action segments, and Simon Callow, Richard Dreyfuss, Susan Sarandon, Jane Leeves, David Thewlis, and Margoyles voiced his insect friends in the animation sequences.

Karey Kirkpatrick: Karey Kirkpatrick (born December 14, 1964) is an American screenwriter and director.  His films include "James and the Giant Peach", "Chicken Run", "The Spiderwick Chronicles", "Charlotte's Web" and "The Hitchhiker's Guide to the Galaxy" adaptation, along with contributions to the "Smurfs" films.  He has also directed the films "Imagine That" starring Eddie Murphy as well as "Over the Hedge".  Kirkpatrick wrote the English-language screenplay for U.S. release of "The Secret World of Arrietty", in 2012 and "From Up on Poppy Hill", in 2013.  His brother is American songwriter and musician Wayne Kirkpatrick, with whom he wrote the 2015 musical "Something Rotten! ".

Henry Selick: Henry Selick (born November 30, 1952) is an American stop motion director, producer and writer who is best known for directing "The Nightmare Before Christmas", "James and the Giant Peach" and "Coraline".  He studied at the Program in Experimental Animation at California Institute of the Arts, under the guidance of Jules Engel.

Pasek and Paul: Benj Pasek and Justin Paul, known together as Pasek and Paul, are an American songwriting duo and composing team for musical theater, films, and television.  Their works include "", "Dogfight", "Edges", "Dear Evan Hansen", and "James and the Giant Peach".  Their original songs have been featured on NBC's "Smash", and in the film "La La Land", for which they won both the Golden Globe and Academy Award for Best Original Song for the song "City of Stars".

Corpse Bride: Corpse Bride is a 2005 British-American stop-motion-animated musical fantasy film directed by Mike Johnson and Tim Burton with a screenplay by John August, Caroline Thompson and Pamela Pettler based on characters created by Burton and Carlos Grangel.  The plot is set in a fictional Victorian era village in Europe.  Johnny Depp leads the cast as the voice of Victor, while Helena Bonham Carter voices Emily, the titular bride.  "Corpse Bride" is the third stop-motion feature film produced by Burton and the first directed by him (the previous two films, "The Nightmare Before Christmas" and "James and the Giant Peach", were directed by Henry Selick).  This is also the first stop-motion feature from Burton that was distributed by Warner Bros.  Pictures.  It was dedicated to executive producer Joe Ranft, who died during production.

M5 Industries: M5 Industries (M5i) is a special effects company located in San Francisco, California, best known as the working lab of the TV series "MythBusters".  M5 once produced special effects props for commercials and film, stop motion animation, and animatronic puppets, such as those seen in "James and the Giant Peach" and "The Nightmare Before Christmas".  They also extend into prototype development and various display projects.

David Thewlis: David Thewlis (born David Wheeler; born 20 March 1963) is an English actor, director, screenwriter, and author.  His most commercially successful role to date has been that of Remus Lupin in the "Harry Potter" film series.  Other notable performances include the films "Naked" (for which he won the Best Actor award at Cannes Film Festival), "Dragonheart", "Kingdom of Heaven", "The Boy in the Striped Pyjamas", "The Theory of Everything", "Black Beauty", "Macbeth" (as King Duncan) and "Wonder Woman".  He has also done voice work in the films "James and the Giant Peach" (1996), "The Miracle Maker" (2000), and "Anomalisa" (2015).  Thewlis has combined major motion picture work with prominent television roles, including playing Cyrus Crabb in the television miniseries "Dinotopia" and antagonist V.M. Varga in the third season of "Fargo."

Paul Terry (actor): Paul Christopher James Terry (born 7 November 1985) is an English former child actor.  He is best known internationally for starring as James in the 1996 film adaptation of Roald Dahl's "James and the Giant Peach".  He also starred in the four seasons of the children's sitcom "Microsoap" (1998–2000).

Harley Jessup: Harley Jessup (born 1954) is an American production designer and visual effects art director who has been nominated for two visual effects Academy Awards, and won once.  Currently working at Pixar Animation Studios, Jessup has served as production designer for "Monsters, Inc." (with Bob Pauley), "Ratatouille", "Cars 2", "Presto", "The Good Dinosaur" and an upcoming Pixar feature.  Before coming to Pixar, Jessup was production designer on Walt Disney Pictures' "James and the Giant Peach".

Jane Leeves: Jane Leeves (born 18 April 1961) is an English actress, model, producer, comedian, singer, and dancer.  She is best known for playing Daphne Moon on the television sitcom "Frasier" from 1993 until 2004, for which she was nominated for Emmy Awards and Golden Globe Awards.  She is also known for her role as Joy Scroggs on TV Land's sitcom "Hot in Cleveland".

Question: What actress that starred on Frasier also was the voice of an insect in James and the Giant Peach?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The name of the actress."
    },
    "film_details": {
      "type": "object",
      "properties": {
        "film_title": {
          "type": "string",
          "description": "The title of the film she was in."
        },
        "role_type": {
          "type": "string",
          "description": "The type of role she had in the film (e.g., voice actor)."
        },
        "character_category": {
          "type": "string",
          "description": "The category of character she voiced in the film."
        }
      },
      "required": [
        "film_title",
        "role_type",
        "character_category"
      ],
      "additionalProperties": false
    },
    "tv_show_details": {
      "type": "object",
      "properties": {
        "tv_show_title": {
          "type": "string",
          "description": "The title of the TV show she starred on."
        }
      },
      "required": [
        "tv_show_title"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actress_name",
    "film_details",
    "tv_show_details"
  ],
  "additionalProperties": false
}
