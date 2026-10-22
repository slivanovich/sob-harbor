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
The Baby Shower (Seinfeld): "The Baby Shower" is the tenth episode of the second season of the NBC sitcom "Seinfeld", and the show's 15th episode overall.  In the episode, Elaine Benes (Julia Louis-Dreyfus) throws a baby shower for her friend Leslie (Christine Dunford) at Jerry's (Jerry Seinfeld) apartment, while he is out of town.  Jerry's friend George Costanza (Jason Alexander) once had a terrible date with Leslie and intends to confront her at the shower.  Meanwhile, Jerry is convinced by his neighbour Kramer (Michael Richards) to install illegal cable television.

The Phone Message: "The Phone Message" is the ninth episode of the NBC sitcom "Seinfeld", and the fourth of the show's second season.  The episode concerns protagonist Jerry Seinfeld (Jerry Seinfeld) dating a woman who likes a commercial for cotton Dockers he dislikes.  Meanwhile, his friend George Costanza (Jason Alexander) leaves an obnoxious message on the answering machine of his girlfriend, and goes to great lengths to prevent her from hearing it.

List of Seinfeld episodes: "Seinfeld" is an American television sitcom created by Jerry Seinfeld and Larry David.  "Seinfeld" is a "show about nothing," similar to the self-parodying "show within a show" of fourth-season episode "The Pilot."  Jerry Seinfeld is the lead character and played as a fictionalized version of himself.  Set predominantly in an apartment block on New York City's Upper West Side, the show features a host of Jerry's friends and acquaintances, which include George Costanza, Elaine Benes, and Cosmo Kramer, who are portrayed by Jason Alexander, Julia Louis-Dreyfus, and Michael Richards, respectively.

The Apartment (Seinfeld): "The Apartment" is the fifth episode of the second season of the NBC sitcom "Seinfeld" and the show's tenth episode overall.  In the episode, protagonist Jerry Seinfeld (Jerry Seinfeld) gets his ex-girlfriend Elaine Benes (Julia Louis-Dreyfus) an apartment above his, but regrets this after realizing it might be uncomfortable living so close together.  Meanwhile, Jerry's friend George Costanza (Jason Alexander) wears a wedding ring to a party to see what effect this will have on women.

Mario Joyner: Mario Joyner (born October 3, 1961) is an American stand-up comedian best known as the host of MTV's "Half Hour Comedy Hour" from 1988–1992.  He is a longtime friend and collaborator of comedians Chris Rock and Jerry Seinfeld.  He appeared regularly on "The Chris Rock Show" and "Everybody Hates Chris".  He also guest starred in the "Seinfeld" episodes "The Engagement" and "The Puerto Rican Day," playing two different characters, and voiced the character Jackson in the film "Bee Movie".  He has opened on national tours for Chris Rock (during his "No Apologies" tour) and for Jerry Seinfeld.

Jerry Seinfeld (character): Jerome "Jerry" Seinfeld is the protagonist of the American television sitcom "Seinfeld" (1989–1998).  The straight man among his group of friends, this semi-fictionalized version of comedian Jerry Seinfeld was named after, co-created by, based on, and played by Seinfeld himself.  The series revolves around Jerry's misadventures with his best friend George Costanza, neighbor Cosmo Kramer, and ex-girlfriend Elaine Benes.  He is usually the voice of reason amidst his friends' antics and the focal point of the foursome's relationship.

The Adventures of Seinfeld &amp; Superman: The Adventures of Seinfeld & Superman was a pair of advertisement films promoting American Express, featuring Jerry Seinfeld as himself and Patrick Warburton (who appeared with Seinfeld on "Seinfeld", as David Puddy) as the voice of Superman.  The two films, "A Uniform Used to Mean Something..." and "Hindsight is 20/20", each about five minutes in length, were directed by Barry Levinson.  In addition to being on the Internet, they aired on television during 2004 and once on TBS in 2003.  In addition to promoting American Express, the premise of the films were to show Seinfeld and Superman as friends, and much of the humor originated from the various situations the two found themselves in.  For example, Superman is anticipating hooking up Seinfeld's TV to surround sound, despite the fact that he has super-hearing as Jerry points out.

The Ratings Game: The Ratings Game, is a 1984 cable television film directed by Danny DeVito and produced by David Jablin.  The Showtime comedy stars DeVito and Rhea Perlman, and features Huntz Hall, Michael Richards, George Wendt and Jerry Seinfeld.

George Wendt: George Robert Wendt III (born October 17, 1948) is an American actor and comedian, best known for the role of Norm Peterson on the television show "Cheers".

The Statue (Seinfeld): "The Statue" is the sixth episode of the second season of the NBC sitcom "Seinfeld", and the show's 11th episode overall.  In the episode, protagonist Jerry Seinfeld (Jerry Seinfeld) inherits some old possessions of his grandfather.  One of these is a statue, resembling one that his friend George Costanza (Jason Alexander) broke when he was ten years old.  When Jerry sees the statue in the house of Ray (Michael D. Conway), the man who cleaned his apartment, he believes Ray stole the statue.  Jerry struggles to get back at Ray, as his friend Elaine Benes (Julia Louis-Dreyfus) is editing a book written by Ray's girlfriend.

Question: The actor that played Norm on the tv show "Cheers" co-starred with Jerry Seinfeld on what 1984 cable tv film?

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
    "film_type": {
      "type": "string",
      "description": "The type of film (e.g., cable television film)."
    },
    "actors_involved": {
      "type": "array",
      "description": "Details about the actors involved in the film as per the question.",
      "items": {
        "type": "object",
        "properties": {
          "actor_name": {
            "type": "string",
            "description": "The name of the actor."
          },
          "connection_to_question": {
            "type": "string",
            "description": "How this actor is relevant to the question (e.g., 'played Norm on Cheers', 'Jerry Seinfeld')."
          }
        },
        "required": [
          "actor_name",
          "connection_to_question"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "film_title",
    "release_year",
    "film_type",
    "actors_involved"
  ],
  "additionalProperties": false
}
