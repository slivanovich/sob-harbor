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
Robotron: 2084: Robotron: 2084 (also referred to as Robotron) is an arcade video game developed by Eugene Jarvis and Larry DeMar of Vid Kidz and released by Williams Electronics (part of WMS Industries) in 1982.  It is a shoot 'em up with two-dimensional graphics.  The game is set in the year 2084 in a fictional world where robots have turned against humans in a cybernetic revolt.  The aim is to defeat endless waves of robots, rescue surviving humans, and earn as many points as possible.

Electronic Gaming Monthly: Electronic Gaming Monthly (often abbreviated to EGM) was a monthly American video game magazine.  It offered video game news, coverage of industry events, interviews with gaming figureheads, editorial content, and product reviews.

The Champion Pub: The Champion Pub is a pinball game released by Midway a subsidiary of WMS Industries, Inc. (under the Bally label) in 1998.  The theme of the game revolves around boxing in a 1920s pub.

Leland Corporation: The Leland Corporation was a manufacturer of several arcade video games in the 1980s and early 1990s.  Notable among these were "" in 1991, the long-anticipated follow up to the hugely successful "Dragon's Lair" from 1983 and "Ivan 'Ironman' Stewart's Super Off Road", which spawned an expansion and two sequels at Leland's successor company Midway Games ("Off Road Challenge" and "Offroad Thunder") in addition to 1990's "Pig Out".  The company was formed when Tradewest purchased the ailing Cinematronics in 1987 and was itself purchased in 1994 by WMS Industries.  At this point the Leland and Tradewest brands were phased out but much of the staff and all of the facilities continued to be used by WMS and later Midway Games.

WMS Industries: WMS Industries, Inc. is an American electronic gaming and amusement manufacturer in Enterprise, Nevada.  WMS traces its roots to 1943, to the Williams Manufacturing Company, founded by Harry E. Williams.  However, the company that became WMS Industries was formally founded in 1974 as Williams Electronics, Inc.

WMS Gaming: WMS Gaming is a manufacturer of slot machines, video lottery terminals and software to help casinos manage their gaming operations.  It also offers online and mobile games.  The company is based in Chicago, Illinois.  WMS is a subsidiary of WMS Industries, which became a wholly owned subsidiary of Scientific Games Corporation in 2013.

Montreal International Games Summit: The Montreal International Games Summit (MIGS), also known as le Sommet International du jeu de Montréal (SIJM), is a conference on video games.  The first edition was held in 2004 and usually takes place in November at le Palais des Congrès de Montréal.  The summit was founded in order to meet the needs of the rough 9000 video game workers in Quebec.  The mission of the summit is to expand the exposure of the video game community and industry in Quebec as well as develop the expertise of the Quebec video game industry.  MIGS is currently the leading professional gaming summit of the East Coast, and is arguably the largest game development event in Canada.  The overall aims of MIGS are to promote, train, network, and hire potential players in the gaming industry.  Professionals attending the summit partake in lectures and presentations largely oriented around how to better specific aspects of the industry, such as art and VFX, business, and design.  Currently, MIGS has partnered with many of the leading electronic and game development companies in Canada, including Ubisoft and Warner Bros.  Games.  The Montreal International Gaming Summit is networked similarly to the Electronic Entertainment Expo, using the same application in order to facilitate interaction between industry players and their associates.  It was only in 2008, during the fifth summit, did MIGS become an event that was open to the public.  2013 marked the tenth annual Montreal International Gaming Summit.

Early history of video games: The history of video games spans a period of time between the invention of the first electronic games and today, covering a long period of invention and changes.  Video gaming would not reach mainstream popularity until the 1970s and 1980s, when arcade video games, gaming consoles and home computer games were introduced to the general public.  Since then, video gaming has become a popular form of entertainment and a part of modern culture in most parts of the world.  The early history of video games, therefore, covers the period of time between the first interactive electronic game with an electronic display in 1947, the first true video games in the early 1950s, and the rise of early arcade video games in the 1970s ("Pong" and the beginning of the first generation of video game consoles with the Magnavox Odyssey, both in 1972).  During this time there were a wide range of devices and inventions corresponding with large advances in computing technology, and the actual first video game is dependent on the definition of "video game" used.

Midway Games: Midway Games Inc. (formerly Midway Manufacturing and Midway) was an American video game developer and publisher.  Midway's franchises included "Mortal Kombat", "Rampage", "Spy Hunter", "NBA Jam", "Cruis'n", and "NFL Blitz".  Midway also acquired the rights to video games that were originally developed by Williams Electronics and Atari Games, such as "Defender", "Joust", "Robotron 2084", "Gauntlet", and the "Rush" series.

Cloak &amp; Dagger (video game): Cloak & Dagger is an arcade game released by Atari in March 1984 The game is based on the film of the same name where it is critical to the plot.  The game saw limited arcade release as a conversion kit for Robotron 2084 cabinets.

Question: Robotron: 2084 is what type of video game released by WMS Industries, an American electronic gaming and amusement manufacturer?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "game_name": {
      "type": "string",
      "description": "The name of the video game."
    },
    "game_types": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The categories or genres of the video game."
    },
    "publisher_details": {
      "type": "object",
      "properties": {
        "publisher_name": {
          "type": "string",
          "description": "The name of the company that released the game."
        },
        "parent_company": {
          "type": "string",
          "description": "The parent company of the publisher."
        },
        "parent_company_description": {
          "type": "string",
          "description": "A description of the parent company's business."
        },
        "release_year": {
          "type": "integer",
          "description": "The year the game was released."
        }
      },
      "required": [
        "publisher_name",
        "parent_company",
        "parent_company_description",
        "release_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "game_name",
    "game_types",
    "publisher_details"
  ],
  "additionalProperties": false
}
