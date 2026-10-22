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
Ratchet &amp; Clank: Up Your Arsenal: Ratchet & Clank: Up Your Arsenal (known as Ratchet & Clank 3 in Europe and Japan and Ratchet & Clank 3: Up Your Arsenal in Australia) is a 2004 3D platform video game developed by Insomniac Games and published by Sony Computer Entertainment for the PlayStation 2.  It is the third installment in the "Ratchet & Clank" series and was released in North America on November 3, 2004.  Shortly after it was released in Japan on November 25, the first volume of the Ratchet & Clank manga, drawn by Shinbo Nomura, was released.  A demo of this game was included in "".

Ratchet &amp; Clank Future: A Crack in Time: Ratchet & Clank Future: A Crack in Time (known as Ratchet & Clank: A Crack in Time in most PAL countries, Ratchet & Clank Future 2 in Japan) is a 2009 platformer video game developed by Insomniac Games and published by Sony Computer Entertainment for the PlayStation 3.  It is the sequel to "" and "".  The game was released for the PlayStation 3 in North America on October 27, 2009, in Australia on November 5, 2009 and in Europe on November 6, 2009.

Ratchet &amp; Clank: Full Frontal Assault: Ratchet & Clank: Full Frontal Assault (known as Ratchet & Clank: QForce in PAL and Japan countries) is a 2012 platform game developed by Insomniac Games for the PlayStation Network and published by Sony.  Like the previous downloadable game in the series, "", in Europe, as well as the United States for this time, it was released on Blu-ray Disc as well as the PlayStation Store.  It was produced in commemoration of the 10th anniversary of the "Ratchet & Clank" series.  It is available on the PlayStation 3 with the PlayStation Vita version delayed for a May 21, 2013 release and available for free with the PlayStation 3 version.  It is a spin-off from the series.

Ratchet &amp; Clank Future: Quest for Booty: Ratchet & Clank Future: Quest for Booty (known as Ratchet & Clank: Quest for Booty in Europe and Australia; and Ratchet & Clank Future Gaiden: Kaizoku Dark Water no Hihou in Japan) is a 2008 platformer video game developed by Insomniac Games and published by Sony Computer Entertainment for the PlayStation 3.  The game is the second installment in the "Ratchet & Clank Future" series.  It was released on PlayStation Network in Japan, North America and Europe on August 21, 2008 and on Blu-ray Disc in Europe on September 12, 2008 and in Asia on September 25, 2008.  The game continues from where "" left off, where Clank was kidnapped by the Zoni, and follows Ratchet's quest to find him.  Due to its length of approximately three to four hours of playtime, it was released at a lower price point than most standard retail games.

Bella Thorne: Annabella Avery Thorne (born October 8, 1997) is an American actress and singer.  She played Ruthy Spivey in the television series "My Own Worst Enemy", Tancy Henrickson in the fourth season of "Big Love", and CeCe Jones on the Disney Channel series "Shake It Up".  She also appeared as Hilary/"Larry" in "Blended" and as Celia in "Alexander and the Terrible, Horrible, No Good, Very Bad Day".  In 2015, she played Madison in "The DUFF", Amanda in "Perfect High" and Hazel in "Big Sky".  Thorne currently stars as Paige on the Freeform series, "Famous in Love".

Ratchet &amp; Clank: Size Matters: Ratchet & Clank: Size Matters (known as Ratchet & Clank 5 in Japan) is a 2007 platformer video game developed by High Impact Games and published by Sony Computer Entertainment for the PlayStation Portable and PlayStation 2.  The game is the first "Ratchet & Clank" title on the PSP and the fifth "Ratchet & Clank" game for the PlayStation 2.  Development company High Impact Games was spawned from the original "Ratchet & Clank" developer, Insomniac Games.  The story is about Ratchet and Clank as they are interrupted from their vacation to search for a kidnapped girl and encounter a forgotten race known as the Technomites.

Ratchet &amp; Clank: Going Commando: Ratchet & Clank: Going Commando (known as Ratchet & Clank 2: Locked and Loaded in Australia and most PAL countries) is a 2003 3D platform video game developed by Insomniac Games and published by Sony Computer Entertainment for the PlayStation 2.  "Ratchet & Clank: Going Commando" is the second game in the "Ratchet & Clank" franchise, following "Ratchet & Clank" and preceding "".  David Kaye reprises his role as Clank while James Arnold Taylor replaces Mikey Kelley as Ratchet.

Ratchet &amp; Clank Collection: Ratchet & Clank Collection (known as The Ratchet & Clank Trilogy in Europe and Ratchet & Clank 1+2+3 in Japan) is a high-definition remastered collection.  The collection includes the original three PlayStation 2 games, "Ratchet & Clank", "", and "" in native 720p @ 60fps and includes 720p stereoscopic 3D support @ 30fps.  It also includes the multiplayer of "Up Your Arsenal" over the PlayStation Network.  It includes a Trophy set for each game.  All of the games in this collection have been re-rated E10+ by the ESRB; they were originally rated T since the E10+ rating didn't exist at the time these games were released on the PlayStation 2.

Ratchet &amp; Clank (film): Ratchet & Clank is a 2016 American-Canadian 3D computer-animated science-fiction action comedy film based on the video game series of the same name.  The film stars the voices of James Arnold Taylor, David Kaye, Paul Giamatti, John Goodman, Bella Thorne, Rosario Dawson, and Sylvester Stallone.

Ratchet &amp; Clank: All 4 One: Ratchet & Clank: All 4 One (previously known as Ratchet & Clank: 4-Play) is a platform video game for the PlayStation 3 developed by Insomniac Games and published by Sony Computer Entertainment in October 2011.  It is the third spin-off from the Ratchet & Clank "Future" series.

Question: The year before she starred in Ratchet and Clank, what did Bella Thorne star in?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The name of the actress."
    },
    "ratchet_clank_film_release_year": {
      "type": "integer",
      "description": "The release year of the Ratchet & Clank film."
    },
    "previous_year": {
      "type": "integer",
      "description": "The year prior to the Ratchet & Clank film's release."
    },
    "roles_in_previous_year": {
      "type": "array",
      "description": "A list of roles and the titles Bella Thorne starred in during the previous year.",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the production."
          },
          "role": {
            "type": "string",
            "description": "The role played by the actress in the production."
          }
        },
        "required": [
          "title",
          "role"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "actress_name",
    "ratchet_clank_film_release_year",
    "previous_year",
    "roles_in_previous_year"
  ],
  "additionalProperties": false
}
