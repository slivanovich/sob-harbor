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
Tomb Raider: Anniversary: Tomb Raider: Anniversary is a 2007 action-adventure video game, part of the "Tomb Raider" series.  It is a remake/re-imagining of the first video game in the series, the original 1996 "Tomb Raider".  It uses an improved version of the "" game engine, and it includes all of the original environments from "Tomb Raider".

Camilla Luddington: Camilla Luddington (born December 15, 1983) is an English actress.  She is known for her roles as Catherine Middleton in the Lifetime TV film "", and as Jo Wilson in the ABC medical drama "Grey's Anatomy".  She provided the voice and motion capture work for Lara Croft in the 2013 video game "Tomb Raider" and its 2015 sequel "Rise of the Tomb Raider".

Tomb Raider (2013 video game): Tomb Raider is an action-adventure video game developed by Crystal Dynamics and published by Square Enix.  "Tomb Raider" is the tenth title in the "Tomb Raider" franchise, and operates as a reboot that reconstructs the origins of Lara Croft.  "Tomb Raider" was released on 5 March 2013 for Microsoft Windows, PlayStation 3 and Xbox 360, and on 23 January 2014 for OS X, and on 27 April 2016 for Linux.

Lara Croft: Tomb Raider: Lara Croft: Tomb Raider (also known as simply Tomb Raider) is a 2001 action-adventure film based on the popular "Tomb Raider" video game series featuring the character Lara Croft portrayed by Angelina Jolie.  An international co-production between the United States, the United Kingdom, Japan, and Germany, it was directed by Simon West and revolves around Lara Croft trying to obtain ancient artifacts from the enemy, the Illuminati.

Lara Croft and the Temple of Osiris: Lara Croft and the Temple of Osiris is an action-adventure game developed by Crystal Dynamics and published by Square Enix for Microsoft Windows, PlayStation 4 and Xbox One.  It is the sequel to the 2010 video game "Lara Croft and the Guardian of Light", and the second instalment in "Lara Croft" spin-off series of the "Tomb Raider" franchise.  The video game was announced at E3 2014 on 9 June.  "Temple of Osiris" stars "Tomb Raider" mainstay protagonist Lara Croft, voiced by English actress Keeley Hawes.

Rise of the Tomb Raider: Rise of the Tomb Raider is an action-adventure video game developed by Crystal Dynamics and published by Square Enix.  It is the sequel to the 2013 video game "Tomb Raider", a reboot of the Tomb Raider franchise.  It was released for Xbox One and Xbox 360 in November 2015 and for Microsoft Windows in January 2016.  A special edition of the game, titled Rise of the Tomb Raider: 20 Year Celebration, was released worldwide for PlayStation 4 in October 2016.

Tomb Raider III: Tomb Raider III: Adventures of Lara Croft, or simply Tomb Raider III, is an action-adventure video game developed by Core Design and published by Eidos Interactive.  It was originally released for the PlayStation and Microsoft Windows platforms in 1998.  "Tomb Raider III" is the third title in the "Tomb Raider" video game series and a sequel to "Tomb Raider II".  The story of the game follows archaeologist-adventurer Lara Croft as she embarks upon a quest to recover four pieces of a meteorite that are scattered across the world.  To progress through the game, the player must explore five locations (India, South Pacific, London, Nevada, and Antarctica) and complete a series of levels that involve solving puzzles, jumping over obstacles, and defeating enemies.

List of Tomb Raider media: Tomb Raider is a media franchise consisting of action-adventure games, comic books, novels, theme park rides, and movies, centring on the adventures of the female fictional British archaeologist Lara Croft.  Since the release of the original "Tomb Raider" in 1996, the series developed into a lucrative franchise of related media, and Lara went on to become a major icon of the video game industry.  The "Guinness Book of World Records" has recognised Lara Croft as the "Most Successful Human Videogame Heroine" in 2006.  Six games in the series were developed by Core Design, and the latest four by Crystal Dynamics.  All the games were first published by Eidos Interactive, now Eidos officially became part of Square Enix on 22 April 2009, meaning Square Enix owns the rights to the "Tomb Raider" trademark and characters of the franchise.  To date two movies, "" and "", have been produced starring American actress Angelina Jolie as Lara Croft.  A reboot was announced in 2016.

Tomb Raider: Underworld: Tomb Raider: Underworld is an action-adventure video game, the eighth instalment of the "Tomb Raider" series, following character Lara Croft.  The story continues from the events in "" as a direct sequel, but also addresses unexplained plot elements by association with "".  "Underworld" was released by Eidos Interactive for the Xbox 360, PlayStation 3 and Microsoft Windows, in North America on 18 November 2008, Europe on 21 November 2008 and Australia on 5 December 2008.  On 14 June 2012, "Underworld" was released on the Mac OS X by Feral Interactive.  It is the third game in the series to be developed by Crystal Dynamics and is also the first "Tomb Raider" game to be released on the PlayStation 3.  Developers implemented new features into the gameplay, such as the dual-target feature and an upgraded inventory system, using an Active Sonar map and a multi-purpose grappling hook.  The game also features a hint system and a new melee combat system where Lara has the ability to battle her opponents using kicks and grapple pulls.  Downloadable content was also released exclusively for the Xbox 360, where the player takes control of Lara and her doppelgänger in two new chapters.

Tomb Raider: The Angel of Darkness: Tomb Raider: The Angel of Darkness is the sixth installment in the "Tomb Raider" series, acting as a direct sequel to "Tomb Raider Chronicles" and "".  It was developed by Core Design and published by Eidos Interactive.  The game was originally released in 2003 for Microsoft Windows, PlayStation 2 and Mac OS X and was the first "Tomb Raider" title to be released for the PlayStation 2 console.  The storyline follows Lara Croft as she attempts to clear herself of being the suspect of her former mentor Werner Von Croy's murder while investigating the activities of a black magic cult.

Question: Camilla Luddington who voiced Lara Craft in the video game Rise of the Tomb Raider also stars in what ABC medical drama?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The name of the actress."
    },
    "video_game_role": {
      "type": "object",
      "properties": {
        "character_voiced": {
          "type": "string",
          "description": "The character voiced by the actress in the video game."
        },
        "game_title": {
          "type": "string",
          "description": "The title of the video game where the character was voiced."
        }
      },
      "required": [
        "character_voiced",
        "game_title"
      ],
      "additionalProperties": false
    },
    "medical_drama_role": {
      "type": "object",
      "properties": {
        "drama_title": {
          "type": "string",
          "description": "The title of the medical drama."
        },
        "network": {
          "type": "string",
          "description": "The network on which the medical drama airs."
        },
        "character_played": {
          "type": "string",
          "description": "The character played by the actress in the medical drama."
        }
      },
      "required": [
        "drama_title",
        "network",
        "character_played"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actress_name",
    "video_game_role",
    "medical_drama_role"
  ],
  "additionalProperties": false
}
