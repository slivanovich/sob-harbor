{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBattle Frenzy: Bloodshot is a 1994 video game developed by Jim Blackler for Domark Software and published by Acclaim in 1994 for the Sega Mega Drive/Genesis console in Europe only.  A North American release was planned, and even reviewed in gaming magazines, but never actually came out.  The game was re-released the same year for both the Mega Drive and the Sega CD , again only in Europe.  \"Bloodshot\" was one of the few first person shooters released on the Mega Drive/Genesis.\n\nList of Sega CD games: The Sega CD, originally released as the Mega-CD (メガCD , Mega-Shī Dī ) in most regions outside of North America, is an add-on device for the Sega Genesis video game console, designed and produced by Sega.  It was released in Japan in 1991, North America in 1992 and in PAL regions in 1993.  The device adds a CD-ROM drive to the console, allowing the user to play CD-based games and providing additional hardware functionality.  It can also play audio CDs and CD+G discs.  While the add-on did contain a faster central processing unit than the Genesis, as well as some enhanced graphics capabilities, the main focus of the device was to expand the size of games.  Known for several games such as \"Sonic CD\" and for the controversy of violent video games including \"Night Trap\", the Sega CD sold 2.24 million units worldwide.  It was officially discontinued in 1996.\n\n32X: The 32X is an add-on for the Sega Genesis video game console.  Codenamed \"Project Mars\", the 32X was designed to expand the power of the Genesis and serve as a transitional console into the 32-bit era until the release of the Sega Saturn.  Independent of the Genesis, the 32X uses its own ROM cartridges and has its own library of games.  The add-on was distributed under the name Super 32X in Japan, Genesis 32X in North America, Mega Drive 32X in the PAL region, and Mega 32X in Brazil.\n\nSega Genesis: The Sega Genesis, known as the Mega Drive in regions outside of North America, is a 16-bit home video game console which was developed and sold by Sega Enterprises, Ltd. The Genesis was Sega's third console and the successor to the Master System.  Sega first released the console as the Mega Drive in Japan in 1988, followed by a North American debut under the Genesis moniker in 1989.  In 1990, the console was distributed as the Mega Drive by Virgin Mastertronic in Europe, by Ozisoft in Australasia, and by Tectoy in Brazil.  In South Korea, the systems were distributed by Samsung and were known as the Super Gam*Boy, and later the Super Aladdin Boy.\n\nList of Sega video game consoles: Sega is a video game developer, publisher, and hardware development company headquartered in Tokyo, Japan, with multiple offices around the world.  The company has produced home video game consoles and handheld consoles since 1983; these systems were released from the third console generation to the sixth.  Sega was formed from the merger of slot machine developer Service Games and arcade game manufacturer Rosen Enterprises in 1964, and it produced arcade games for the next two decades.  After a downturn in the arcade game industry in the 1980s, the company transitioned to developing and publishing video games and consoles.  The first Sega console was the Japan-only SG-1000, released in 1983.  Sega released several variations of this console in Japan, the third of which, the Sega Mark III, was rebranded as the Master System and released worldwide in 1985.  They went on to produce the Genesis—known as the Mega Drive outside of North America—and its add-ons beginning in 1988, the Game Gear handheld console in 1990, the Sega Saturn in 1994, and the Dreamcast in 1998.\n\nList of Sega Genesis games: The Sega Genesis, known as Mega Drive (Japanese: メガドライブ , Hepburn: Mega Doraibu ) in most regions outside North America, is a 16-bit video game console that was developed and sold by Sega Enterprises, Ltd. First released in Japan in 1988 and in North America in 1989, the Genesis is Sega's third console and the successor to the Master System.  The system supports a library of more than 700 games created both by Sega and a wide array of third-party publishers and delivered on ROM cartridges.  It can also play the complete library of Master System games when the separately sold Power Base Converter is installed.  The Genesis also benefited from numerous peripherals, including the Sega CD and Sega 32X, several network services, and multiple first-party and third-party variations of the console that focused on extending its functionality.  The console and its games continue to be popular among fans, collectors, video game music fans, and emulation enthusiasts.  Licensed third party re-releases of the console are still being produced, and several indie game developers continue to produce games for it.  Many games have also been re-released in compilations for newer consoles and offered for download on various digital distribution services, such as Virtual Console, Xbox Live Arcade, PlayStation Network, and Steam.\n\nAnett Futatabi: Annet Futatabi (アネット再び ) , is a 1993 side scrolling, beat-em-up video game developed by Wolf Team for the Sega CD hardware add-on for the Sega Genesis.  It is the final in a trilogy of games that also includes \"Earnest Evans\" and \"El Viento\".  The game was published by Wolf Team in Japan in March 1993.\n\nSega CD: The Sega CD, released as the Mega-CD in most regions outside North America, is a CD-ROM accessory for the Sega Genesis video game console designed and produced by Sega as part of the fourth generation of video game consoles.  The add-on was released on December 12, 1991 in Japan, October 15, 1992 in North America, and 1993 in Europe.  The Sega CD lets the user play CD-based games and adds extra hardware functionality, such as a faster central processing unit and graphic enhancements.  It can also play audio CDs and CD+G discs.\n\nList of Sonic the Hedgehog video games: \"Sonic the Hedgehog\" is a video game series created by Yuji Naka.  It is published by Sega, with entries developed by Sega, Sonic Team, Dimps, SIMS Co., Ltd., BioWare, and Sumo Digital.  The series debuted in 1991 with the video game, \"Sonic the Hedgehog\", released for the Mega Drive video game console (named Genesis in North America).  Most \"Sonic the Hedgehog\" games have either been platform games or released for Sega video game consoles and handheld game consoles (handhelds) dating from the Genesis to the eighth generation of video game consoles (2012–present).  However, some of the original games were ported into versions on third-party home consoles and developed by several companies.  As of February 2013, the series has collectively sold over 85 million copies worldwide across both the platform games and spin-offs.\n\nVirtua Fighter 2: Virtua Fighter 2 (Japanese: バーチャファイター2 , Hepburn: Bācha Faitā Tsū ) is a fighting video game developed by Sega.  It is the sequel to \"Virtua Fighter\" and the second game in the \"Virtua Fighter\" series.  It was created by Sega's Yu Suzuki-headed AM2 and was released in the arcade in 1994.  It was ported to the Sega Saturn in 1995 and Microsoft Windows in 1997.  In 1996, a super deformed version of the game, \"Virtua Fighter Kids\", arrived in arcades and was ported to the Sega Saturn.  A 2D remake was released for the Mega Drive/Genesis in 1996.  In addition, \"Virtua Fighter 2\" was converted for the PlayStation 2 in 2004 as part of Sega's \"Ages 2500\" series in Japan.  The Mega Drive/Genesis port was re-released on the PS2 and PSP in 2006 as part of \"Sega Genesis Collection\", on the Virtual Console for the Wii on March 20, 2007 (Japan) and April 16, 2007 (North America), and for iOS on January 20, 2011.\n\nQuestion: Annet Futatabi, is a 1993 side scrolling, beat-em-up video game developed by Wolf Team for the Sega CD hardware add-on for which 16-bit home video game console which was developed and sold by Sega Enterprises, Ltd, and known as the Mega Drive in regions outside of North America?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"game_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the video game.\"\n    },\n    \"game_developer\": {\n      \"type\": \"string\",\n      \"description\": \"The developer of the video game.\"\n    },\n    \"game_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the video game.\"\n    },\n    \"console_add_on\": {\n      \"type\": \"string\",\n      \"description\": \"The hardware add-on the game was developed for.\"\n    },\n    \"target_console\": {\n      \"type\": \"string\",\n      \"description\": \"The 16-bit home video game console that the add-on is for.\"\n    },\n    \"target_console_attributes\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"bit_architecture\": {\n          \"type\": \"string\",\n          \"description\": \"The bit architecture of the target console.\"\n        },\n        \"developer\": {\n          \"type\": \"string\",\n          \"description\": \"The company that developed and sold the target console.\"\n        },\n        \"alternative_name_outside_north_america\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the console in regions outside of North America.\"\n        }\n      },\n      \"required\": [\n        \"bit_architecture\",\n        \"developer\",\n        \"alternative_name_outside_north_america\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"game_title\",\n    \"game_developer\",\n    \"game_release_year\",\n    \"console_add_on\",\n    \"target_console\",\n    \"target_console_attributes\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "game_title": {
        "type": "string",
        "description": "The title of the video game."
      },
      "game_developer": {
        "type": "string",
        "description": "The developer of the video game."
      },
      "game_release_year": {
        "type": "integer",
        "description": "The release year of the video game."
      },
      "console_add_on": {
        "type": "string",
        "description": "The hardware add-on the game was developed for."
      },
      "target_console": {
        "type": "string",
        "description": "The 16-bit home video game console that the add-on is for."
      },
      "target_console_attributes": {
        "type": "object",
        "properties": {
          "bit_architecture": {
            "type": "string",
            "description": "The bit architecture of the target console."
          },
          "developer": {
            "type": "string",
            "description": "The company that developed and sold the target console."
          },
          "alternative_name_outside_north_america": {
            "type": "string",
            "description": "The name of the console in regions outside of North America."
          }
        },
        "required": [
          "bit_architecture",
          "developer",
          "alternative_name_outside_north_america"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "game_title",
      "game_developer",
      "game_release_year",
      "console_add_on",
      "target_console",
      "target_console_attributes"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
