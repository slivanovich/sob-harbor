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
The Penguins of Madagascar (video game): The Penguins of Madagascar is a game developed by THQ and released on Nintendo DS and Nintendo DSi on November 2, 2010.  It is a spin-off to the animated TV series The Penguins of Madagascar and is unrelated to tie-in games to the 2014 DreamWorks film Penguins of Madagascar.

Women's football in Zimbabwe: Women's football in Zimbabwe is popular but women who play the game face stigmatisation.

Game Face: Game Face is the tenth studio album by American rapper Master P, released on December 18, 2001.  It marked the debut of The New No Limit and a partnership with Universal Records.  There are three singles released from the album, "Ooohhhwee", "Real Love", and "Rock it", Music videos were released for all three.  The album received a mixed reception from critics who saw some change in Master P's production and lyrical delivery but felt that it wasn't anything new from the genre.

March of the Penguins: March of the Penguins (French La Marche de l'empereur ; ] ) is a 2005 French feature-length nature documentary directed and co-written by Luc Jacquet, and co-produced by Bonne Pioche and the National Geographic Society.  The documentary depicts the yearly journey of the emperor penguins of Antarctica.  In autumn, all the penguins of breeding age (five years old and over) leave the ocean, their normal habitat, to walk inland to their ancestral breeding grounds.  There, the penguins participate in a courtship that, if successful, results in the hatching of a chick.  For the chick to survive, both parents must make multiple arduous journeys between the ocean and the breeding grounds over the ensuing months.

FaceGen: FaceGen is a 3D face-generating 3D modeling middleware produced by Singular Inversions.  It is used where there is a need for a large number of different possible faces, either at random or from photographs.  The most notable examples of its use are for player character creation in Tiger Woods PGA Tour (photo game face), and the Football Manager series, and for the character models used in Red vs. Blue season 9 and upwards.

Tiger Woods PGA Tour 2004: Tiger Woods PGA Tour 2004 is a 2003 golf video game published by EA Sports.  It was released for Mobile phone, PlayStation 2, GameCube, Xbox, Microsoft Windows, Game Boy Advance, and the N-Gage.  It was the first to feature the Game Face feature, in which the player can create his or her own player.

2011–12 Pittsburgh Penguins season: The 2011–12 Pittsburgh Penguins season was the franchise’s 45th season in the National Hockey League (NHL).  The Penguins, led by head coach Dan Bylsma, would start the season without captain center Sidney Crosby.  The team still managed a 51–25–6 record, an East-best 29 home wins, and their 108 points second-best in the Eastern Conference.  In February, the team began the league's longest season winning streak and also saw the return of Crosby after missing more than 40 games with concussion like symptoms, before they saw the streak end in March at 11 games.  Center Evgeni Malkin was able to play in 75 games despite difficulties associated with recent knee surgery and recorded his greatest goal tally in a season (50) on the way to winning his second Art Ross Trophy.  Marc-Andre Fleury tied a franchise record for goalie wins (226) in a victory against the Atlantic division winning-New York Rangers.  The four-seed Penguins would see their playoff run end to the same team which halted their regular season winning streak, the Philadelphia Flyers, losing the first three games before perishing in Game 6 of the Eastern Conference Semifinals.

2015 MVP Cup: The 2015 Manny V. Pangilinan Cup, also known as the Master Game Face MVP Cup 2015 due to sponsorship reasons, was an invitational basketball tournament which was participated by four teams from September 11–13, 2015 at the Smart Araneta Coliseum.  While a similarly named tournament was held in 2010, the 2010 MVP Invitational Champions' Cup, the 2015 MVP Cup is considered the inaugural edition of the MVP Cup and is planned to be held annually.

Game Face (film): Game Face is a 2015 sports documentary film directed by Michiel Thomas and produced by Mark Schoen.  The documentary revolves around two LGBTQ American athletes, professional mixed martial artist Fallon Fox and college basketball player Terrence Clemens.  Both stories run parallel to each other to follow the journey of the first transgender woman professional MMA fighter and Clemens, a closeted gay male, who gets accepted to play basketball in Oklahoma.  The film follows both athletes through their coming out process with the support of their friends and family.

Cliff Pace: Cliff Pace (born May 23, 1980) often called “Game Face Pace”, is a professional bass fisherman from Petal, Mississippi.  Pace is the 43rd world champion of bass fishing and the 39th member of the B.A.S.S. Millionaires Club.  Pace has predominantly fished the Bass Anglers Sportsman Society (BASS) Bassmasters tournament series during his career.

Question: Game Face and March of the Penguins, are which type of film?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_type": {
      "type": "string",
      "description": "The common type of film for the listed titles."
    },
    "films": {
      "type": "array",
      "description": "A list of films matching the specified type.",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film."
          },
          "release_year": {
            "type": "integer",
            "description": "The release year of the film."
          },
          "director": {
            "type": "string",
            "description": "The director of the film."
          }
        },
        "required": [
          "title",
          "release_year",
          "director"
        ],
        "additionalProperties": false
      }
    },
    "number_of_films": {
      "type": "integer",
      "description": "The total number of films found."
    }
  },
  "required": [
    "film_type",
    "films",
    "number_of_films"
  ],
  "additionalProperties": false
}
