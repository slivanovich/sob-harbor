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
NCAA College Football 2K3: NCAA College Football 2K3 is an American football video game released in 2002 by Visual Concepts.  The cover athlete is former Nebraska Cornhuskers quarterback Eric Crouch.  It is the second College Football game by Visual Concepts (the first being for the Dreamcast ).  The game also has ESPN style game play, meaning at half-time it gives you a report on your game and others around the league.  It includes an editable roster, but you cannot name the players as, traditionally, NCAA athletes are referred to as "John Doe" and not by their full name.  There are basic game modes such as the dynasty or jump into a quick play.  Dynasty is where you lead your team over the course of a year to the National Championship.  Legacy mode is when you completely take over a team, control its recruiting classes, and remain a "Division 1" powerhouse.

EA Sports UFC: EA Sports UFC is a mixed martial arts sports video game developed by EA Canada and SkyBox Labs for the PlayStation 4 and Xbox One.  It is based on the Ultimate Fighting Championship (UFC) brand and was released on June 17, 2014.  A playable demo was released on the PlayStation Network and Xbox Marketplace on June 3, 2014, with cover athletes Jon Jones and Alexander Gustafsson as playable fighters.  It is the first UFC game since THQ sold the license to Electronic Arts.

Michael Crabtree: Michael Alex Crabtree Jr. (born September 14, 1987) also known as "The Crab Man" is an American football wide receiver for the Oakland Raiders of the National Football League (NFL).  He was drafted by the San Francisco 49ers 10th overall in the 2009 NFL Draft.  He played college football at Texas Tech, where he was a two-time unanimous All-American and twice won the Fred Biletnikoff Award as the nation's best wide receiver.

FIFA 11: FIFA 11, also known in North America as FIFA Soccer 11, is the 18th title in Electronic Arts' "FIFA" series of football video games. Developed by EA Canada, it was published by Electronic Arts worldwide under the EA Sports label.  It was released on 28 September 2010 in North America, 30 September 2010 in Australia, and 1 October 2010 in Europe for all platforms, except the Wii and Nintendo DS.  The Wii version was released on 1 October 2010 in North America and Europe and the DS version on 8 October 2010.  The PC version of "FIFA 11" is the first in the series to use the same game engine as the PlayStation 3 and Xbox 360 versions.  The game received positive reviews, and was awarded 'Sports Game of the Year' at the Golden Joystick Awards after a record-breaking 2.06 million votes.  This is the last "FIFA" title to be released for the Nintendo DS.

FIFA 12: FIFA 12 (titled FIFA Soccer 12 in North America) is the 19th game in Electronic Arts' "FIFA" series of association football video games.  It was developed by EA Canada, and published by Electronic Arts worldwide under the EA Sports label.  It was released in September 2011, on consoles for PlayStation 3, Xbox 360, Wii and PlayStation 2; on handhelds for PlayStation Portable, 3DS, Xperia Play and iOS; and on computers for Microsoft Windows and Mac OS X.  A port of the game entitled FIFA Football (titled FIFA Soccer in North America) was released as a launch title for the PlayStation Vita.

FIFA: Road to World Cup 98: FIFA: Road to World Cup 98 (commonly abbreviated to FIFA 98) is an association football video game developed by EA Canada and published by Electronic Arts.  It was the fifth game in the "FIFA" series and the second to be in 3D on the 32-bit machines.  A number of different players were featured on the cover, including David Beckham in the UK, Roy Lassiter in the USA, Mexico and Brazil, David Ginola on the French cover, Raúl on the Spanish cover, Paolo Maldini on the Italian and Andreas Möller on the German cover.  "FIFA 98" was the last "FIFA" game released for the Mega Drive in Europe.

NCAA Football 08: NCAA Football 08 is a college football video game created by EA Sports, the sports video gaming subsidiary of Electronic Arts.  It is the successor to NCAA Football 07 in the NCAA Football series.  It was officially announced with the launch of the NCAA 08 page on the EA Sports website on February 20, 2007.  EA Sports had opened up a ballot on their "NCAA Football 07" site in which fans can vote on a feature to be implemented into the PlayStation 2 version, making it the first console announced for the game and announcing at least one of its features.  Fans could vote for either in-game saves, medical red shirts, summer workouts or a lead blocker feature.  The option of medical red shirts was voted on and won, and this option is on the Dynasty Mode on all versions of NCAA Football 08.  This allows for players that are injured in the middle of the year to apply to gain another year of eligibility.  The game was released on July 17, 2007, and the first time release on PlayStation 3, marking the eleventh installment of the NCAA Football series bearing the title "NCAA Football".  As with NCAA Football 07, 08 features limited ESPN integration.

NCAA Football 07: NCAA Football 07 is a collegiate football video game published by Electronic Arts.  It is the successor to NCAA Football 06 in the NCAA Football series.  The product features former USC player Reggie Bush on the cover.  While there weren't any stunning new features added to the PS2 and Xbox games, tweaks were added to improve the existing features.

NCAA Football 10: NCAA Football 10 is a college football video game created by Electronic Arts.  It is the successor to NCAA Football 09 in the NCAA Football series.  It was released on July 14, 2009 for the Xbox 360, PlayStation 3, PlayStation Portable, and PlayStation 2 consoles.  Brian Johnson, Brian Orakpo, Mark Sanchez, and Michael Crabtree were the cover athletes for the game.

NCAA Football 09: NCAA Football 09 is a college football video game created by EA Sports, a subsidiary of Electronic Arts.  It is the successor to NCAA Football 08 in the NCAA Football series.  The game was announced on February 14, 2008 and was released on July 15, 2008 .  The Wii version of the game is titled "NCAA Football 09 All-Play" and launched under EA Sports' new "All-Play" brand exclusive to the platform.

Question: What player known as "The Crab Man" was a  cover athletes for the college football video game created by Electronic Arts?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The full name of the player."
    },
    "nickname": {
      "type": "string",
      "description": "The known nickname of the player."
    },
    "video_game_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the video game."
        },
        "developer": {
          "type": "string",
          "description": "The developer of the video game."
        },
        "genre": {
          "type": "string",
          "description": "The genre of the video game."
        },
        "is_cover_athlete": {
          "type": "boolean",
          "description": "Indicates if the player was a cover athlete for this game."
        }
      },
      "required": [
        "title",
        "developer",
        "genre",
        "is_cover_athlete"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "player_name",
    "nickname",
    "video_game_details"
  ],
  "additionalProperties": false
}
