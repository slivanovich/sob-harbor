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
Twisted Edge Extreme Snowboarding: Twisted Edge Extreme Snowboarding is a snowboarding video game released for the Nintendo 64.  It is known in Japan as King Hill 64: Extreme Snowboarding.  "Twisted Edge" was not very well received commercially or critically.

Amped: Freestyle Snowboarding: Amped: Freestyle Snowboarding is an Xbox exclusive snowboarding video game.  It is the first of the "Amped" video game series.

Mark McMorris Infinite Air: Mark McMorris Infinite Air is a snowboarding video game developed by HB Studios and published by Maximum Games.  First announced in March 2016, it was released on October 25, 2016 for Microsoft Windows, PlayStation 4 and Xbox One.  It is the first open-world, physics-based snowboarding video game.  It was built in partnership and close collaboration with Olympic snowboarder Mark McMorris.

Stoked (video game): Stoked is a snowboarding video game developed by Austrian-based Bongfish GmbH for the Xbox 360 video game console in 2009.  It is the latest entry in the "Stoked Rider" snowboard game series and is in association with Absinthe Films.  In 2009 an updated version, Stoked: Big Air Edition was released for Xbox 360 and a Microsoft Windows version was released in 2011.

SSX (2012 video game): SSX is a snowboarding video game in the "SSX" series of video games from Electronic Arts.  It is a reboot of the series.  First revealed at the Spike Video Game Awards in 2010 under the working title "SSX: Deadly Descents", the game's trailer appeared to show a much darker direction to the series than previous entries, though later footage revealed a return to a lighter tone.  "SSX" includes the use of real locations, rather than the fictional courses of past games.

Konami: Konami Holdings Corporation (Japanese: 株式会社コナミホールディングス , Hepburn: Kabushikigaisha Konami Hōrudingusu ) is a Japanese entertainment company.  It operates as a product distributor (which produces and distributes trading cards, anime, tokusatsu, slot machines and arcade cabinets), video game developer and publisher company.  It also operates health and physical fitness clubs across Japan.

Evolution Snowboarding: Evolution Snowboarding is a sports video game first released on February 25, 2002 for the Nintendo Gamecube.  It was later released on November 26 for the PlayStation 2.  The game was both developed and published by Japanese game company Konami.  The game takes a new perspective on the snowboarding genre.  Evolution Snowboarding has also spawned a sequel titled Evolution Skateboarding.

Supreme Snowboarding: Supreme Snowboarding (known as Boarder Zone in the United States), is a snowboarding video game created by Housemarque for Microsoft Windows in 1999.  It was one of the first snowboarding games for Windows to take full advantage of 3D graphics cards that were becoming the norm in the late 1990s, and eventually became an internationally bestselling game.  Over 1.5 million units were sold worldwide, allowing "Supreme Snowboarding" to become the first hit title in Finnish game development.  The game received positive critical reception, as well as acclaim for having one of the best visuals of its time, though its lack of content and replay value was sometimes criticized.

SSX Tricky: SSX Tricky is a snowboarding video game, the second game in the "SSX series" published by EA Sports Big and developed by EA Canada.  The game was developed under the working title SSX 2.  The game is built on the previous "SSX" game.  The game was released in 2001 for PlayStation 2, GameCube and Xbox and was later ported to the Game Boy Advance in October 2002.

SummitX Snowboarding: SummitX Snowboarding is a snowboarding video game from Com2us developed by Free Range Games.

Question: In what country did Konami Holdings Corporation release the Evolution Snowboarding video game?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "game_title": {
      "type": "string",
      "description": "The title of the video game."
    },
    "publisher_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the game publisher."
        },
        "country_of_origin": {
          "type": "string",
          "description": "The country where the publisher is based."
        }
      },
      "required": [
        "name",
        "country_of_origin"
      ],
      "additionalProperties": false
    },
    "release_information": {
      "type": "object",
      "properties": {
        "release_country": {
          "type": "string",
          "description": "The country where the game was released by the publisher."
        }
      },
      "required": [
        "release_country"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "game_title",
    "publisher_details",
    "release_information"
  ],
  "additionalProperties": false
}
