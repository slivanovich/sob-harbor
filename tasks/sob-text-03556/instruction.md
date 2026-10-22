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
The World's End (film): The World's End is a 2013 British-American comic science fiction film directed by Edgar Wright, written by Wright and Simon Pegg, and starring Pegg, Nick Frost, Paddy Considine, Martin Freeman, Eddie Marsan and Rosamund Pike.  The film follows a group of friends who discover an alien invasion during an epic pub crawl in their home town.

Enemies &amp; Allies: Enemies & Allies is a 2009 novel by American science fiction author Kevin J. Anderson.  The book is set in the 1950s, in the midst of the Cold War, and follows Superman and Batman.  Though suspicious of each other, they confront Lex Luthor who stages an international nuclear conflict and spreads fear of an alien invasion so that he can sell advanced weapons to governments.  Themes used in the novel, reflective of the 1950s era, include alien invasion films, nuclear threats, and Cold War paranoia.

Halo 3: ODST: Halo 3: ODST is a 2009 first-person shooter video game developed by Bungie and published by Microsoft Game Studios.  It is part of the "Halo" franchise, and was released on the Xbox 360 video game console on September 22, 2009.  Players assume the roles of United Nations Space Command soldiers, known as "Orbital Drop Shock Troopers" or ODSTs, during and after the events of "Halo 2".  In the game's campaign mode, players explore the ruined city of New Mombasa to discover what happened to their missing teammates in the midst of an alien invasion.  In the "Firefight" multiplayer option, players battle increasingly difficult waves of enemies to score points and survive as long as possible; "Halo 3"' s multiplayer is contained on a separate disc packaged with "ODST".

Brides of March: The Brides of March started as an annual Cacophony Society event that takes place in San Francisco around March 15th.  Intended as a pun on the term Ides of March and a parody of weddings in western culture.  The event, which began in 1999, is part pub crawl and part street theater, while wearing a thrift store wedding dress.  Brides may be of any gender, but the wearing of traditional white wedding dresses, or something resembling them, is the point of the event.  In recent years there have been a greater number of gothic brides who wear black, alien brides and other variations on the theme.

Tešnjar: Tešnjar () is the old quarter of the city of Valjevo, in Serbia.  It originated in the 19th century and was a long time trade center, located on the right bank of Kolubara.  It consists of one street that follows the Kolubara river course and several smaller streets below the hill.  The name is probably received after the tight streets.  Tešnjar has become famous lately due to Serbian cinema.  On weekends, Tešnjar serves as the youth's main place for a pub crawl since there are many bohemian-style pubs.  It is declared a Cultural Heritage of Serbia.

Cal McCrystal: Cal McCrystal is a British theatre director and actor.  He is the brother of the journalist Damien McCrystal and the son of the journalist and writer Cal McCrystal.  Following an early career acting in theatre, television, radio plays and commercials, McCrystal became a director specialising in comedy.  His success as Physical Comedy Director on the National Theatre's "One Man, Two Guvnors" has recently led to work on films including "The World's End" and "The Amazing Spider-Man 2".

Battle: Los Angeles: Battle: Los Angeles (also known as Battle: LA and internationally as World Invasion: Battle Los Angeles) is a 2011 American military science fiction war film directed by Jonathan Liebesman.  The storyline was conceived from a screenplay written by Chris Bertolini, based in part on a wartime incident dubbed the "Battle of Los Angeles".  The film is set in modern-day Los Angeles and follows a retiring Marine Staff Sergeant played by Aaron Eckhart who must go back into the line of duty to lead a platoon of U.S. Marines, a U.S. Navy corpsman, isolated U.S. Army soldiers and a U.S. Air Force sergeant during a global alien invasion.  The ensemble cast also features Michelle Rodriguez, Ramon Rodriguez, Bridget Moynahan, Ne-Yo, and Michael Peña.

Otley Run: The Otley Run is a pub crawl in Leeds, West Yorkshire.  The pub crawl was commonly known as the Headingly Mile prior to the Otley Run.  It was historically a mile stretch of Tetley pubs leading in to Leeds City Centre.  Over the years more pubs and bars have opened stretching it over more than a mile.  The route follows the A660, also known as Otley Road at the point the pub crawl commonly begins.  The Otley Run is a popular social gathering for student clubs and societies from The University of Leeds, Leeds College of Music, Leeds College of Art, Leeds Trinity University, Leeds Beckett University and The University of Bradford Hockey Club

Outpost 37: Outpost 37 (also known as Alien Outpost) is a 2014 science fiction action thriller film.  The film follows a documentary crew sent to record the daily lives of the soldiers of Outpost 37, 12 years after the initial alien invasion.

Armada (novel): Armada is a science fiction novel by Ernest Cline, published on July 14, 2015 by Crown Publishing Group (a division of Random House).  The story follows a teenager who plays an online video game about defending against an alien invasion, only to find out that the game is a simulator to prepare him and people around the world for defending an actual alien invasion.

Question: What is the name of the director and actor with success that led to work on a film which follows a group of friends who discover an alien invasion during an epic pub crawl?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the director and actor."
    },
    "person_professions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of professions held by the person."
    },
    "film_details": {
      "type": "object",
      "properties": {
        "film_title": {
          "type": "string",
          "description": "The title of the film the person worked on."
        },
        "film_genre": {
          "type": "string",
          "description": "The genre of the film."
        },
        "film_plot_elements": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Key plot elements of the film."
        },
        "person_role_in_film": {
          "type": "string",
          "description": "The specific role the person had in the film."
        }
      },
      "required": [
        "film_title",
        "film_genre",
        "film_plot_elements",
        "person_role_in_film"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "person_professions",
    "film_details"
  ],
  "additionalProperties": false
}
