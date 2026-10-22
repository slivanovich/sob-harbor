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
Kickstarter: Kickstarter is an American public-benefit corporation based in Brooklyn, New York, that maintains a global crowdfunding platform focused on creativity.  The company's stated mission is to "help bring creative projects to life".  Kickstarter has reportedly received more than $1.9 billion in pledges from 9.4 million backers to fund 257,000 creative projects, such as films, music, stage shows, comics, journalism, video games, technology and food-related projects.

Orcs Must Die!: Orcs Must Die!  is an action-tower defense video game developed by Robot Entertainment.  It is a tower defense game that eschews the traditional top-down view of similar games, instead using a third-person action-oriented viewpoint.  After being demonstrated at Penny Arcade Expo East 2011, the game was released via Xbox Live Arcade on October 5, 2011, and for Windows PCs on October 12, 2011.

Gratuitous Space Battles: Gratuitous Space Battles (GSB) is a video game developed by the UK-based company Positech Games.  It was released on November 17, 2009.  On one level the title is a space warfare simulation consisting of a number of engagements between two opposing fleets of ships.  While sometimes assumed to be a real-time strategy (RTS) game based on screenshots, actual gameplay focuses on the setup prior to the battle, making it play more like a tower defense game.

GauntNet: GauntNet is a Java based tower defense game created by Landon Kryger and James Van Boxtel in a game design class at Washington State University's Computer Science Program.  The game continues to gain popularity due to its multiplayer nature.

South Park Let's Go Tower Defense Play!: South Park Let's Go Tower Defense Play!  is a 2009 video game based on the American animated television series "South Park", released on the Xbox Live Arcade service for the Xbox 360 video game console.  The game was developed by Doublesix in collaboration with South Park Digital Studios and Xbox Live Productions.  "Let's Go Tower Defense Play" is a tower defense game, with the added element of being a fast-paced action game as well.  Thus, players do not only build towers to eliminate destructive forces, but they also have to control multiple characters in order to successfully protect the town of South Park.  "South Park Let's Go Tower Defense Play!"  is the first "South Park" video game released after three early titles released between 1998 and 2000.

Hidden Path Entertainment: Hidden Path Entertainment is an American video game development company based in Bellevue, Washington, United States.  It was founded in 2006 by Michael Austin, Jim Garbarini, Dave McCoy, Jeff Pobst, and Mark Terrano.  In 2008, Hidden Path released its first original title, "" on PC and in 2009 on Xbox.  A downloadable title, "Defense Grid" garnered high acclaim with its twist on tower defense and has sold over half a million units since its release.  In 2009, Hidden Path began working with Valve Corporation to update and maintain "", first released in 2004.

Defense Grid: The Awakening: Defense Grid: The Awakening is a tower defense video game developed by Hidden Path Entertainment for Windows and Xbox Live Arcade on the Xbox 360.  The game was one of the titles promoted by Microsoft during their Game Developers Conference keynote speech on February 20, 2008.  The game was released for Microsoft Windows on December 8, 2008 and for Xbox 360 on September 2, 2009.  The OS X version shipped from Virtual Programming on July 7, 2010.

Counter-Strike: Global Offensive: Counter-Strike: Global Offensive (CS:GO) is a multiplayer first-person shooter video game developed by Hidden Path Entertainment and Valve Corporation.  It is the fourth game in the "Counter-Strike" series and was released for Microsoft Windows, OS X, Xbox 360, and PlayStation 3 in August 2012, with the Linux version being released in September 2014.  The game pits two teams against each other: the Terrorists and the Counter-Terrorists.  Both sides are tasked with eliminating the other while also completing separate objectives, the Terrorists, depending on the game mode, must either plant the bomb or defend the hostages, while the Counter-Terrorists must either prevent the bomb from being planted or rescue the hostages.  There are six game modes, all of which have distinct characteristics specific to that mode.

Defense Grid 2: Defense Grid 2 is a 2014 tower defense video game developed by Hidden Path Entertainment and published by 505 Games.  As a sequel to the 2008 "", the game was crowd-funded on Kickstarter in 2012, and released on Windows, Xbox One, and PlayStation 4 on September 23, 2014.  Linux and OS X versions were released on October 15, 2014.

Gem Tower Defense: Gem Tower Defense is a tower defense video game created by Bryan K.  It was released on February 18, 2007 under the tower defense subsection of Blizzard's "" minigames. Several game clients, Flash browser game websites and mobile devices have hosted variants of the game.  The game is based upon the strategy, mazing, decision making and chance.  The goal of the game is to eliminate computer-controlled enemies that follow a set path to reach the end of a pathway.  "Gems" are structures players build to defend their maze.  Each Gem is randomly distributed leaving it to chance for a player to acquire the one needed.  Gems are placed to form a maze for extending the length each enemy unit travels thereby increasing the attack time of the Gems.  Both the type and quality of the Gems selected determine the damage and use of the structure.

Question: In what year did the American public-benefit company based in New York help crowd fund a Hidden Path Entertainment tower defense game?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "crowdfunding_event": {
      "type": "object",
      "properties": {
        "campaign_year": {
          "type": "integer",
          "description": "The year the crowdfunding campaign for the game took place."
        },
        "game_release_year": {
          "type": "integer",
          "description": "The year the crowdfunded game was released."
        }
      },
      "required": [
        "campaign_year",
        "game_release_year"
      ],
      "additionalProperties": false
    },
    "crowdfunding_company": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "Name of the company that provided the crowdfunding platform."
        },
        "location": {
          "type": "string",
          "description": "City and state where the crowdfunding company is based."
        },
        "type": {
          "type": "string",
          "description": "Legal type of the crowdfunding company."
        }
      },
      "required": [
        "name",
        "location",
        "type"
      ],
      "additionalProperties": false
    },
    "crowdfunded_game": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "Title of the video game that was crowdfunded."
        },
        "developer": {
          "type": "string",
          "description": "Developer of the crowdfunded game."
        },
        "genre": {
          "type": "string",
          "description": "Genre of the crowdfunded game."
        }
      },
      "required": [
        "title",
        "developer",
        "genre"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "crowdfunding_event",
    "crowdfunding_company",
    "crowdfunded_game"
  ],
  "additionalProperties": false
}
