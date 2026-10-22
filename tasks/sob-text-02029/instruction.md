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
Karen Dotrice: Karen Dotrice ( ; born 9 November 1955) is a British actress, known primarily for her role as Jane Banks in Walt Disney's feature film adaptation of the "Mary Poppins" book series.  Dotrice was born in Guernsey to two accomplished stage actors.  Her career began on stage, and expanded into film and television, including starring roles as a young girl whose beloved cat magically reappears in Disney's "The Three Lives of Thomasina" and with "Thomasina" co-star Matthew Garber as one of two children pining for their parents' attentions in "Poppins".  She appeared in five television programmes between 1972 and 1978, when she made her only feature film as an adult.  Her life as an actress concluded with a short run as Desdemona in the 1981 pre-Broadway production of "Othello".

Banishing Racer: Banishing Racer (バニシングレーサー ) is a Japanese platforming video game developed and published by Jaleco Entertainment for the Game Boy exclusively in Japan.  It was released in Japan on July 26, 1991.  Banishing Racer was also sold around Hong Kong.  The game allows the player to take control of an animated car against numerous enemies that must be jumped on to defeat, in a fashion similar to Super Mario Land.  The player has three lives before being allowed to continue or start over.  One hit kills the player and forces a restart from the beginning of the level.  The car model used within the game looks very similar to a Subaru 360.

Sacred Planet: Sacred Planet is a 2004 documentary directed by Jon Long and Hairul Salleh Askor.  Robert Redford provided narration for the film.  The film was released by Walt Disney Pictures on April 22, 2004, and grossed $1,108,356.

I Led 3 Lives: I Led 3 Lives (also known as I Led Three Lives) is an American drama series which was syndicated by Ziv Television Programs from October 1, 1953 to January 1, 1956.  The series stars Richard Carlson.  The show was a companion piece of sorts to the radio drama "I Was a Communist for the FBI", which dealt with a similar subject and was also syndicated by Ziv from 1952 to 1954.

Nenjam Marappathillai (TV series): Nenjam Marappathillai (Tamil: நெஞ்சம் மறப்பதில்லை ) is an 2017 Upcoming Tamil Language Romance soap opera starring Amit Bhargav, Nisha Krishnan and Saranya.  It is a remake of the Bengali language television series Kusum Dola which airs on Star Jalsha from 2016.  Is a story of three lives, whose lives get changed after certain incidents.

Life pool: Life pool was a form of pocket billiards (pool) mainly played in the 19th century.  It was one of several pool games that were popular at this time (so called because gamblers pooled their bets at the start of play).  The object of the game was to be the last player left "alive" and therefore scoop the pool (take the winnings).  Each player had three "lives" to begin with and would lose one when another player potted their <dfn id="">coloured ball</dfn> which was designated to them at the start of the game.  Using the same number of balls as players, players take turns striking their designated ball with the cue in an attempt to collide that ball with one (or more) of their opponents' balls knocking the opponent ball into a pocket.  Once a player lost their three lives, they were declared "dead", i.e. out of the game.  The game continued in this way until there was only one player left, who was declared the winner.  Around 1875, life pool merged with black pool to form the new game of snooker, today one of the most popular cue sports in the world.

The Three Lives of Thomasina: The Three Lives of Thomasina is a 1963 British fantasy film starring Patrick McGoohan, Susan Hampshire, child actor Matthew Garber and child actress Karen Dotrice in a story about a cat and her influence on a family.  The screenplay was written by Robert Westerby and Paul Gallico.  It was based upon Gallico's 1957 novel "Thomasina, the Cat Who Thought She Was God".  The film was directed by Don Chaffey, and shot in Inveraray, Argyll, Scotland, and Pinewood Studios, England.  "Thomasina" has been broadcast on television and released to VHS and DVD.

Thomasina, the Cat Who Thought She Was God: Thomasina, the Cat Who Thought She Was God or Thomasina is a 1957 novel by Paul Gallico about a cat who is owned by a child whose father is very strict and needs to understand about how love is powerful enough to help others.  The book was made into the Disney film "The Three Lives of Thomasina" starring Karen Dotrice, Matthew Garber, Patrick Mcgoohan and Susan Hampshire and directed by Don Chaffey.

In the Flesh (2003 film): In the Flesh: three lives in prostitution is a 2003 independent documentary by Bishakha Datta about the lives of three Indian sex workers, written for a family audience.  It is a low-budget film set in Calcutta and Mumbai that describes the everyday life of its subjects.

Matthew Garber: Matthew Adam Garber (25 March 1956 – 13 June 1977) was a British child actor, best known for his role as Michael Banks in the 1964 film "Mary Poppins".  He also starred in two other Disney films, "The Three Lives of Thomasina" and "The Gnome-Mobile", all three times appearing alongside actress Karen Dotrice.

Question: Sacred Planet and The Three Lives of Thomasina, are which form of entertainment?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_entertainment_form": {
      "type": "string",
      "description": "The overarching form of entertainment shared by the listed items."
    },
    "number_of_items": {
      "type": "integer",
      "description": "The total number of entertainment items identified."
    },
    "entertainment_details": {
      "type": "array",
      "description": "Details for each identified entertainment item.",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the entertainment item."
          },
          "specific_type": {
            "type": "string",
            "description": "The specific genre or type of the entertainment item."
          },
          "release_year": {
            "type": "integer",
            "description": "The year the entertainment item was released."
          },
          "directors": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of directors for the entertainment item."
          },
          "production_company": {
            "type": "string",
            "description": "The production or release company for the entertainment item."
          }
        },
        "required": [
          "title",
          "specific_type",
          "release_year",
          "directors",
          "production_company"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "common_entertainment_form",
    "number_of_items",
    "entertainment_details"
  ],
  "additionalProperties": false
}
