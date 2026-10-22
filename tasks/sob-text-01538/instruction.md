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
Kim Swift: Kim Swift (born 1983) is an American video game designer best known for her work at Valve with games such as "Portal" and "Left 4 Dead".  Swift was featured by Fortune as one of "30 Under 30" influential figures in the video game industry.  She was described in Mental Floss as one of the most recognized women in the industry and by WIRED as "an artist that will push the medium forward".

Video gaming in the Czech Republic: The video game industry in the Czech Republic has produced numerous globally successful video games such as and the subsequent ArmA series, the Mafia series, Truck Simulator series, the Samorost series and others.  There were 300–400 video game developers and around 30 video game companies focusing on video game development in 2014.  In 2017 it was 1,100 developers and 47 companies.  Video games are also considered by some experts to be the country's biggest cultural export.  The video game industry did not enjoy a good reputation and was unsupported by the state until 2013, when the Ministry of Industry and Trade started to seek ways to kickstart the economy.  By 2014, programs were planned to support the video game industry.  Another problem is a lack of video game development specialization at any university.

Payday 2: Payday 2 is a cooperative first-person shooter video game developed by Overkill Software and published by 505 Games has former published by Sony.  The game is a sequel to 2011's "".  It was released on 13 August 2013 for Microsoft Windows, PlayStation 3 and Xbox 360.  An improved version of the game, subtitled "Crimewave Edition", was released for PlayStation 4 and Xbox One in June 2015 (on 12 June in the UK and Europe and on 16 June in North America).  The game has been announced for the Nintendo Switch and will come out in Fall 2017.

Metro: Last Light: Metro: Last Light is a post-apocalyptic-themed, first-person shooter video game with stealth and survival horror elements.  It was developed by Ukrainian studio 4A Games, published by Deep Silver, distributed by Square Enix in North America for Microsoft Windows, PlayStation 3 and Xbox 360 in May 2013.  A remastered version of the game was released for PlayStation 4 and Xbox One in August 2014 as "Metro: Last Light Redux" within the "Metro Redux" package.

S.T.A.L.K.E.R.: Shadow of Chernobyl: S.T.A.L.K.E.R.: Shadow of Chernobyl is a first-person shooter survival horror video game developed by GSC Game World and published by THQ.  The game is set in an alternative reality, where a second nuclear disaster occurs at the Chernobyl Nuclear Power Plant Exclusion Zone in the near future and causes strange changes in the area around it.  The game has a non-linear storyline and features gameplay elements such as trading and two-way communication with NPCs.  The game includes role-playing and first person shooter elements.  In "S.T.A.L.K.E.R", the player assumes the identity of an amnesiac "Stalker", an illegal explorer/artifact scavenger in "The Zone", dubbed "The Marked One".  "The Zone" is the location of an alternate reality version of the Zone of alienation surrounding the Chernobyl Power Plant after a second fictitious meltdown, which further contaminated the surrounding area with radiation, and caused strange otherworldly changes in local fauna, flora, and the laws of physics.  "Stalker" in the context of the video game refers to the older meaning of the word as a tracker and hunter of game or guide.

Left 4 Dead 2: Left 4 Dead 2 is a cooperative first-person shooter video game developed and published by Valve Corporation.  The sequel to Turtle Rock Studios's "Left 4 Dead", the game released for Microsoft Windows and Xbox 360 in November 2009, and for OS X in October 2010, and for Linux in July 2013.

Left 4 Dead: Left 4 Dead is a cooperative first-person shooter video game with survival horror elements, developed by Valve South and published by Valve Corporation.  The game uses Valve's proprietary Source engine, and is available for Microsoft Windows, Xbox 360 and OS X.  Development on the game was completed on November 13, 2008, and two versions were released digitally: A downloadable digital version, released on November 17, 2008, and a digital retail disc version, with a release date determined by region.  The digital retail disc version was released in North America and Australia on November 18, 2008; and in Europe on November 21, 2008.

Left 4 Dead (series): The Left 4 Dead franchise is based on a series of cooperative first-person shooter, survival horror video games developed by Valve Corporation.  Set in the days after a pandemic outbreak of a viral strain transforming the majority of the population into zombie-like feral creatures, the games follow the adventures of four survivors attempting to reach safe houses and military rescue while fending off the attacking hordes.

Payday: The Heist: Payday: The Heist is a cooperative first-person shooter video game developed by Overkill Software and published by Sony Online Entertainment.  It was released on 18 October 2011, for PlayStation 3 in North America and 2 November 2011, in Europe.  It was released on 20 October 2011, for Microsoft Windows via Steam in both the United States and the United Kingdom.  The game runs on the Diesel game engine.  It contains seven different missions (including the free No Mercy downloadable content (DLC) released on 25 July 2012), with each mission containing random elements which alter the gameplay in subtle ways with the aim of enhancing replayability.  On 7 August 2012, the Wolf Pack DLC was released on PlayStation 3 and PC.  This DLC adds two heists, additional weapons, increased level cap, and a player upgrade tree.

Metroid Prime: Federation Force: Metroid Prime: Federation Force is a cooperative first-person shooter video game developed by Next Level Games and published by Nintendo for the Nintendo 3DS.  The game is a spin-off of the "Metroid Prime" series, where the player assumes the role of a Galactic Federation Marine, featuring gameplay elements similar to those of "Metroid Prime Hunters".  It also includes a multiplayer soccer-based game mode known as "Metroid Prime: Blast Ball".

Question: Which "30 Under 30" influential figures in the video game industry worked on  a cooperative first-person shooter video game with survival horror elements?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the influential figure."
    },
    "game_title": {
      "type": "string",
      "description": "The title of the video game that matches the specified criteria."
    },
    "game_genre_elements": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of genre and gameplay elements of the game."
    },
    "person_role": {
      "type": "string",
      "description": "The role of the person in the development of the game."
    }
  },
  "required": [
    "person_name",
    "game_title",
    "game_genre_elements",
    "person_role"
  ],
  "additionalProperties": false
}
