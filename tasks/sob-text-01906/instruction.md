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
Toby Tortoise Returns: Toby Tortoise Returns is an animated Technicolor cartoon in Walt Disney's "Silly Symphonies" series.  It was directed by Wilfred Jackson.  It is a sequel to "The Tortoise and the Hare".  It premiered on August 22, 1936.

Backgammon: Backgammon is one of the oldest board games known.  It is a two player game where playing pieces are moved according to the roll of dice, and a player wins by removing all of their pieces from the board before their opponent.  Backgammon is a member of the tables family, one of the oldest classes of board games.

The Tortoise and the Hare (film): The Tortoise and the Hare is an animated short film released on January 5, 1935 by United Artists, produced by Walt Disney and directed by Wilfred Jackson.  Based on an Aesop's fable of the same name, "The Tortoise and the Hare" won the 1934 Academy Award for Best Short Subject: Cartoons.  This cartoon is also believed to be one of the inspirations for Bugs Bunny, who first appeared in 1940.

Testudo formation: In Ancient Roman warfare, the testudo or tortoise formation was a type of shield wall formation commonly used by the Roman Legions during battles, particularly sieges.  "Testudo" is the Latin word for "tortoise".  The Greek term for this formation is "chelone" and during the Byzantine era, it seems to have evolved to what military manuals of the era call the "foulkon".

The Tortoise &amp; The Hare: The Tortoise & The Hare is a 2013 picture book of Aesop's classic fable and is illustrated by Jerry Pinkney.  It is about a tortoise and a hare that compete in a foot race with the tortoise surprisingly winning.

Tortoise Wins by a Hare: Tortoise Wins by a Hare is a Merrie Melodies cartoon released on February 20, 1943 and directed by Bob Clampett.  It stars Bugs Bunny and Cecil Turtle.  Bob Clampett took Tex Avery's scenario from "Tortoise Beats Hare" and altered it for this film.  The title is an appropriate pun on "hair".  This is one of the first shorts to feature Robert McKimson's design of Bugs Bunny.  A newspaper's front page (the "Chicago Sunday Tribunk") shown in this cartoon accurately predicts Adolf Hitler's suicide two years later.

Jazz Jackrabbit: Jazz Jackrabbit is a video game trilogy featuring the eponymous character of Jazz Jackrabbit, a green anthropomorphic hare, who fights with his turtle nemesis, Devan Shell, in a science fiction parody of the fable of "The Tortoise and the Hare".  Created by Arjan Brussee and Cliff Bleszinski and developed by Epic MegaGames, the series debuted on the personal computer in 1994 with "Jazz Jackrabbit".  The series consists of two computer games and a handheld console game.

List of films directed by Tex Avery: Tex Avery was an American animator, cartoonist, voice actor and director.  He became famous for producing animated cartoons during the Golden age of American animation and produced his most significant work while employed by the Warner Bros. and Metro-Goldwyn-Mayer studios.  He created the characters of Daffy Duck in "Porky's Duck Hunt" (1937), Elmer Fudd in "Egghead Rides Again" (1937), Bugs Bunny in "A Wild Hare" (1940), Cecil Turtle in "Tortoise Beats Hare" (1941), Droopy in "Dumb-Hounded" (1943), Screwy Squirrel in "Screwball Squirrel" (1944), George and Junior in "Henpecked Hoboes" (1946), Spike/Butch the bulldog (Tex Avery's version) in "Bad Luck Blackie" (1949), and Smedley Dog in "I'm Cold" (1954).  He would develop the characters of Porky Pig from the Warner Bros. studio and Chilly Willy from the Walter Lantz Studio into the personas for which they are best remembered.

The Story of The Tortoise &amp; the Hare: The Story of The Tortoise & the Hare is a stop motion short film directed and animated by Ray Harryhausen based on the Aesop fable "The Tortoise and the Hare".

Hare and Tortoise: Hare and Tortoise is a German-style board game designed by David Parlett in 1974 and first published by Intellect Games.  In 1978 it was released by Ravensburger in Germany, where the game became a huge hit.  It has since sold some 2 million units in at least ten languages, including several known pirated editions.  The current edition is published by Gibsons Games in the UK, Ravensburger in Germany and Rio Grande Games in the United States.

Question: Backgammon and Hare and Tortoise, are which type of entertainment?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entertainment_type": {
      "type": "string",
      "description": "The common type of entertainment for the listed items."
    },
    "items": {
      "type": "array",
      "description": "A list of entertainment items.",
      "items": {
        "type": "string"
      }
    },
    "item_count": {
      "type": "integer",
      "description": "The number of entertainment items listed."
    }
  },
  "required": [
    "entertainment_type",
    "items",
    "item_count"
  ],
  "additionalProperties": false
}
