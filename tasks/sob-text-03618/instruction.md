{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nXbox One: Xbox One is a line of eighth generation home video game consoles developed by Microsoft.  Announced in May 2013, it is the successor to Xbox 360 and the third console in the Xbox family.  It was first released in North America, parts of Europe, Australia, and Brazil in November 2013, and in Japan, China, and other European countries in September 2014.  It is the first Xbox game console to be released in China, specifically in the Shanghai Free-Trade Zone.  Microsoft marketed the device as an \"all-in-one entertainment system\".  The Xbox One line mainly competes against consoles such as Sony's PlayStation 4 and Nintendo's Wii U and Switch.\n\nXbox (software): The Xbox app (originally known as \"Xbox 360 SmartGlass\" and \"Xbox One Smartglass\") is a dashboard for Xbox Live accounts.  On launch, it was positioned as a companion app for Xbox video game consoles, including Xbox 360 and Xbox One video game consoles, providing access to Xbox Live community functions, remote control, as well as second screen functionality with selected games, applications, and content.  The Xbox app is available for Microsoft Windows, Android, and iOS.\n\nContrast (video game): Contrast is a puzzle-based platform style video game developed by Compulsion Games for Microsoft Windows, PlayStation 3, PlayStation 4, Xbox 360, Xbox One, and NVIDIA Shield.\n\nXbox Games Store: Xbox Games Store (formerly Xbox Live Marketplace) is a digital distribution platform used by Microsoft's Xbox One and Xbox 360 video game consoles.  The service allows users to download or purchase video games (including both Xbox Live Arcade games and full Xbox One and Xbox 360 titles), add-ons for existing games, game demos along with other miscellaneous content such as gamer pictures and Dashboard themes.\n\nXbox Fitness: Xbox Fitness was a service exclusively for the Xbox One console, developed by Microsoft Studios in partnership with Sumo Digital, which featured fitness and exercise videos from top-tier and popular trainers Jillian Michaels, Tracy Anderson, Tony Horton of P90X and Shaun T of Insanity.  Xbox Fitness was one of the 22 game titles that launched with Xbox One and in the first 24 hours after the launch, 43.4 million points were earned by players in Xbox Fitness.  The game used the Kinect sensor to track the player's heart rate and estimated calories burned, and gave some feedback about how well the player is performing the exercise activities.\n\nList of Xbox 360 games compatible with Xbox One: On June 15, 2015, backward compatibility with supported Xbox 360 games became available to eligible Xbox Preview program users with a beta update to the Xbox One system software.  The dashboard update containing backward compatibility was released publicly on November 12, 2015.  The following is a list of all Xbox 360 games compatible with the Xbox One under this functionality.\n\nTrueAchievements: TrueAchievements is a website that tracks player's Achievements in games and applications for the Xbox One, Xbox 360, Windows Phone, Games for Windows - Live, Windows 7, Windows 8 and Windows 10 platforms.  It is published by TrueGaming Network, which also publishes the TrueSteamAchievements sister websites catering to Valve 's PC platform Steam and TrueTrophies which caters to the Sony Playstation.  TrueAchievements uses a novel method of assessment, titled \"TrueAchievement\" score, in addition to Microsoft's Xbox Live Gamerscore.  The site is a member of the Xbox Community Developer Program, and as of October 2015, TrueAchievements has over 306,000 registered users including the 2 highest scoring Xbox players.  In 2014, the TrueAchievements Xbox One application was made available to allow users to access several of the site's features directly on their consoles.\n\nChariot (video game): Chariot is a co-op platform game for the PlayStation 4, PlayStation 3, Xbox One, Wii U and Microsoft Windows developed and published by Frima Studio, with the participation of the Canada Media Fund.  It was first released on September 30, 2014 and was launched on Xbox One the next day as part of the Xbox Live Games with Gold program.\n\nForza Horizon 2: Forza Horizon 2 is an open-world racing video game developed for Microsoft's Xbox One and Xbox 360 consoles.  It is the sequel to 2012's \"Forza Horizon\" and the seventh instalment in the \"Forza\" series.  The Xbox One version of the game was developed by Playground Games, the team behind the original \"Forza Horizon\", while Sumo Digital developed the version for Xbox 360, with \"Forza\" series developer Turn 10 Studios supporting both builds.  The Xbox 360 version is also the final \"Forza\" game released for the platform.  The game received positive reviews from critics and a sequel, \"Forza Horizon 3\", was released on 27 September 2016.\n\nList of accolades received by Grand Theft Auto V: \"Grand Theft Auto V\" is an open world, action-adventure video game developed by Rockstar North and published by Rockstar Games.  Players freely roam the fictional state of San Andreas (based on Southern California), composed of open countryside and the fictional city of Los Santos (based on Los Angeles).  The game was first announced on 25 October 2011, and was widely anticipated.  At the 2012 Spike Video Game Awards (now the VGX), it was awarded Most Anticipated Game.  It was released on 17 September 2013 for the PlayStation 3 and Xbox 360, on 18 November 2014 for the PlayStation 4 and Xbox One, and on 14 April 2015 for Microsoft Windows.  Review aggregator, Metacritic, assigned the game a normalised score of 97 out of 100, indicating \"universal acclaim\", based on 50 reviews for the PlayStation 3 version, 58 reviews for the Xbox 360 version, 66 reviews for the PlayStation 4 version and 14 reviews for the Xbox One version.  Within twenty-four hours of its release, \"Grand Theft Auto V\" generated more than $815.7 million in worldwide revenue, equating to approximately 11.21 million copies sold for Take Two.  Three days after release, the game had surpassed one billion dollars in sales, making it the fastest selling entertainment product in history.\n\nQuestion: What type of media does Contrast and Xbox One have in common?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"common_media_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of media that both entities have in common.\"\n    },\n    \"entities_involved\": {\n      \"type\": \"array\",\n      \"description\": \"Details about the entities mentioned in the question.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the entity.\"\n          },\n          \"type\": {\n            \"type\": \"string\",\n            \"description\": \"The general classification of the entity (e.g., video game, console).\"\n          },\n          \"developer\": {\n            \"type\": \"string\",\n            \"description\": \"The developer of the entity.\"\n          },\n          \"platforms_mentioned\": {\n            \"type\": \"array\",\n            \"items\": {\n              \"type\": \"string\"\n            },\n            \"description\": \"A list of platforms the entity is available on or associated with.\"\n          },\n          \"generation\": {\n            \"type\": \"string\",\n            \"description\": \"The generation of the console, if applicable.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"type\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"relationship_description\": {\n      \"type\": \"string\",\n      \"description\": \"A description of how the entities relate to the common media type.\"\n    }\n  },\n  \"required\": [\n    \"common_media_type\",\n    \"entities_involved\",\n    \"relationship_description\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "common_media_type": {
        "type": "string",
        "description": "The type of media that both entities have in common."
      },
      "entities_involved": {
        "type": "array",
        "description": "Details about the entities mentioned in the question.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the entity."
            },
            "type": {
              "type": "string",
              "description": "The general classification of the entity (e.g., video game, console)."
            },
            "developer": {
              "type": "string",
              "description": "The developer of the entity."
            },
            "platforms_mentioned": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "A list of platforms the entity is available on or associated with."
            },
            "generation": {
              "type": "string",
              "description": "The generation of the console, if applicable."
            }
          },
          "required": [
            "name",
            "type"
          ],
          "additionalProperties": false
        }
      },
      "relationship_description": {
        "type": "string",
        "description": "A description of how the entities relate to the common media type."
      }
    },
    "required": [
      "common_media_type",
      "entities_involved",
      "relationship_description"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
