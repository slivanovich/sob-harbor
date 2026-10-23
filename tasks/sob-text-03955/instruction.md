{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSamHas7Friends: Sam Has 7 Friends was a 2006 web television series drama created, produced, and funded by the production company Big Fantastic and subsequently bought and distributed by the web TV studio Vuguru.  The series appeared on YouTube, Revver, iTunes and its own web site.  The show revolved around its tagline, \"Samantha Breslow has seven friends.  On December 15, 2006, one of them will kill her,\" with each episode bringing Sam one day closer to her death.\n\nDaredevil (TV series): Marvel's Daredevil, or simply Daredevil, is an American web television series created for Netflix by Drew Goddard, based on the Marvel Comics character of the same name.  It is set in the Marvel Cinematic Universe (MCU), sharing continuity with the films of the franchise, and is the first in a series of shows that lead to \"The Defenders\" crossover miniseries.  The series is produced by Marvel Television in association with ABC Studios and Goddard Textiles, with DeKnight Productions for the first season.  Steven S. DeKnight serves as showrunner on the first season, with Doug Petrie and Marco Ramirez taking over for the second; Goddard serves as a consultant on both seasons.\n\nThe Virgin Suicides (film): The Virgin Suicides is a 1999 American drama film written and directed by Sofia Coppola, co-produced by Francis Ford Coppola, and starring James Woods, Kathleen Turner, Kirsten Dunst, Josh Hartnett, and A. J. Cook.  The film also features Scott Glenn and Danny DeVito in minor roles, and a voice narration by Giovanni Ribisi.\n\nChris Chianelli: Christopher \"Chris\" John Chianelli (December 26 1950 – January 20, 2009) was an American radio control expert, television personality, industry icon, and host of \"The Radio Control Show\".  This Web TV series is produced by Air Age Media and broadcast biweekly on www.rccaraction.com and www.modelairplanenews.com, and covers all aspects of R/C cars, boats, planes and helicopters, with information ranging from the basics of R/C to tips for the most seasoned pros.\n\nMingle Media TV Network: Mingle Media TV Network is a digital TV network offering scripted, unscripted, live and produced lifestyle, celebrity and entertainment programming seven days a week.  Founded on 8 February 2010, the network is a leading producer of independent filmmaker content in the web TV series.  Mingle Media TV Network publishes their content through its web syndication network, including iTunes, Blip.TV, YouTube, Facebook, Twitter, Blogs, DailyMotion, Roku, Boxee and via the Stickam.com mobile app.\n\nMartial Arts Odyssey: Martial Arts Odyssey is an American web TV show with a martial arts travel theme.  Created and hosted by Antonio Graceffo, the series has run more than 180 episodes shot in Taiwan, Thailand, Vietnam, the Philippines, Malaysia, Laos, Burma, and Cambodia.  Martial arts featured on the show include: Muay Thai, Muay Chaiya, Pradal Serey (Khmer boxing), Bokator, Filipino Kuntaw, Mixed Martial Arts (MMA), Kung Fu, Silat Kalam, Silat Melayu, Tomoi, boxing, Muay Lao, Ziyou Bodji, urban combat, Lai Tai, Muay Boran, military hand-to-hand combat, Silambam, and others.\n\nScott Glenn: Theodore Scott Glenn (born January 26, 1941), better known as Scott Glenn, is an American actor.  His roles have included Wes Hightower in \"Urban Cowboy\" (1980), astronaut Alan Shepard in \"The Right Stuff\" (1983), Emmett in \"Silverado\" (1985), Commander Bart Mancuso in \"The Hunt for Red October\" (1990), Jack Crawford in \"The Silence of the Lambs\" (1991), Roger in \"Training Day\" (2001), Ezra Kramer in \"The Bourne Ultimatum\" (2007), Kevin Garvey, Sr. in \"The Leftovers\" (2014–2017) and as Stick in both \"Daredevil\" (2015–) and \"The Defenders\" (2017).\n\nThe Defenders (miniseries): Marvel's The Defenders, or simply The Defenders, is an American web television miniseries created by Douglas Petrie and Marco Ramirez for Netflix, based on the Marvel Comics characters Daredevil, Jessica Jones, Luke Cage and Iron Fist, who form the eponymous superhero team.  It is set in the Marvel Cinematic Universe (MCU), sharing continuity with the films of the franchise and is the culmination of a series of interconnected shows from Marvel and Netflix.  The miniseries is produced by Marvel Television in association with ABC Studios, Nine and a Half Fingers, Inc., and Goddard Textiles, with Ramirez serving as showrunner.\n\nAll-for-nots: All-for-nots, produced by Michael Eisner, was a web TV mocumentary-comedy that followed the ups and downs of an indie rock band touring on the road.  The web series was created by Kathleen Grace and Thom Woodley of Dinosaur Diorama, the co-creators of the popular internet sitcom \"The Burg\".\n\nOddbods: Oddbods is an award-winning, Singaporian-British CGI-animated comedy television series produced by the Singapore-based studio One Animation.  The series centers on seven non-speaking characters—Fuse, Newt, Pogo, Bubbles, Jeff, Zee and Slick.  The series has won awards, including the Asian Television Awards, Apollo Awards, Gold Panda Awards and Web TV Asia Awards.\n\nQuestion: Which Netflix Web TV series features Scott Glenn in Marvel's universe?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"series_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the web TV series.\"\n    },\n    \"streaming_platform\": {\n      \"type\": \"string\",\n      \"description\": \"The platform where the series is distributed.\"\n    },\n    \"fictional_universe\": {\n      \"type\": \"string\",\n      \"description\": \"The fictional universe the series is set in.\"\n    },\n    \"featured_actor\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actor featured in the series.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The character role played by the actor in the series.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"series_name\",\n    \"streaming_platform\",\n    \"fictional_universe\",\n    \"featured_actor\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "series_name": {
        "type": "string",
        "description": "The name of the web TV series."
      },
      "streaming_platform": {
        "type": "string",
        "description": "The platform where the series is distributed."
      },
      "fictional_universe": {
        "type": "string",
        "description": "The fictional universe the series is set in."
      },
      "featured_actor": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actor featured in the series."
          },
          "role": {
            "type": "string",
            "description": "The character role played by the actor in the series."
          }
        },
        "required": [
          "name",
          "role"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "series_name",
      "streaming_platform",
      "fictional_universe",
      "featured_actor"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
