{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHank Hill: Henry (Hank) Rutherford Hill is a fictional character and the main protagonist on the Fox animated television series \"King of the Hill\".  He lives in the fictional town of Arlen, Texas with his family and works as the assistant manager of a local branch of Strickland Propane, where he sells \"Propane and Propane Accessories\".  He likes to drink beer in the alley behind his house with his friends.  He is voiced by series creator Mike Judge. \" The Economist\" described Hank Hill as one of the wisest people on television, and in 1997 \"Texas Monthly\" included him on its annual list of the most influential Texans.\n\nMr. Greg: \"Mr. Greg\" is the eighth episode of the third season of American animated television series \"Steven Universe\", which premiered on July 19, 2016 on Cartoon Network.  It was written and storyboarded by Joe Johnston and Jeff Liu.  The episode was viewed by 1.549 million viewers.  It is the series' first fully musical episode, and features seven songs, far more than any other \"Steven Universe\" episode.\n\nThe Moxy Show: The Moxy Show (also known as The Moxy Pirate Show and The Moxy & Flea Show), is an American animated anthology television series produced by Turner Production for Cartoon Network.  The show ran on December 5, 1993, originally as \"The Moxy Pirate Show\", and consisted of classic cartoons divided by 3-D animated interstitials featuring Moxy and Flea, respectively a dog and a flea.  The show ran on Cartoon Network from December 5, 1993 to April 1, 2000 including reruns apparently, but the last ever episode was made in 1995, that being the sole episode for \"The Moxy & Flea Show\".  It is considered the first original series on Cartoon Network, but \"Space Ghost Coast to Coast\" was Cartoon Network's first fully produced series.\n\nWeirdmageddon 3: Take Back The Falls: \"Weirdmageddon 3: Take Back The Falls\" is the series finale of the American animated television series \"Gravity Falls\", created by Alex Hirsch.  The episode was written by Shion Takeuchi, Mark Rizzo, Josh Weinstein, Jeff Rowe, and Hirsch, and directed by Stephen Sandoval.  The series follows twelve-year-old twins Dipper (voiced by Jason Ritter) and Mabel Pines (voiced by Kristen Schaal), who stay for the summer with their grand uncle Grunkle Stan (voiced by Hirsch) in a tourist trap called the Mystery Shack, set within the fictional town of Gravity Falls, Oregon.  In this episode, Ford (voiced by J.K. Simmons) discovers the extent of Bill Cipher's plans, while the Mystery Shack crew forms a plan to fight back and reclaim the town.  A final confrontation with Bill leads to the Pines family's ultimate fate and greatest sacrifice.\n\nNot What He Seems: \"Not What He Seems\" is the eleventh episode of the second season of the American animated television series \"Gravity Falls\", created by Alex Hirsch.  The episode was written by Shion Takeuchi, Josh Weinstein, Jeff Rowe, Matt Chapman, and Hirsch, and directed by Stephen Sandoval.  The series follows twelve-year-old twins Dipper (voiced by Jason Ritter) and Mabel Pines (voiced by Kristen Schaal), who stay for the summer with their grand uncle Grunkle Stan (voiced by Hirsch) in a tourist trap called the Mystery Shack, set within the fictional town of Gravity Falls, Oregon.  In this episode, Dipper and Mabel begin to question who Stan really is after officers arrest him for stealing chemical waste.  The episode, which breaks the show's status quo by revealing Stan's brother, ends with a cliffhanger to the second half of the season.\n\nList of The Powerpuff Girls episodes: \"The Powerpuff Girls\" is an American animated television series created by Craig McCracken for Cartoon Network.  The series began as a student film called \"Whoopass Stew\", made by McCracken while he attended the California Institute of the Arts in 1992.  Two additional shorts, \"Meat Fuzzy Lumpkins\" and \"Crime 101\", later aired on Cartoon Network's \"World Premiere Toons\".  The series officially premiered on November 18, 1998, lasting 6 seasons with 78 episodes total.  A Christmas special and a 10th anniversary special were also produced.  Episodes of \"The Powerpuff Girls\" have seen numerous DVD and VHS releases as well.  The musical episode \"See Me, Feel Me, Gnomey\" was never aired in the United States, but was broadcast on YTV in Canada as well as in other countries, and is included on the complete series DVD box set.\n\nList of Steven Universe characters: \"Steven Universe\" is an American animated television series created by Rebecca Sugar.  It is produced by Cartoon Network Studios, and is the first show by the studio to be created by a woman.  The series focuses on the adventures of the Crystal Gems—magical alien warriors who protect the Earth from their own kind—and the humans they interact with in the fictional town of Beach City.  It has received critical acclaim for the diversity of its characters and their depth of characterization; its portrayal of relationships, including queer relationships; and its subversion of stereotypical gender norms.\n\nMy Musical: \"My Musical\" is a musical episode of the American comedy-drama television series \"Scrubs\".  It is the 123rd episode of the show, and was originally aired as episode 6 of season 6 on January 18, 2007.\n\nSteven Universe: Steven Universe is an American animated television series created by Rebecca Sugar for Cartoon Network.  It is the coming-of-age story of a young boy named Steven Universe (voiced by Zach Callison), who lives in the fictional town of Beach City with the \"Crystal Gems\" – Pearl (Deedee Magno), Garnet (Estelle), and Amethyst (Michaela Dietz), three magical humanoid aliens.  Steven, who is half-Gem, goes on adventures with his friends and helps the Gems protect the world from their own kind.  It premiered on November 4, 2013 as Cartoon Network's first animated series to be solely created by a woman.  Books, comics and a video game based on the series have also been released.  When the series is in a hiatus, there would usually be multiple episodes airing after it concluded.  The theme of the series is love and family as it is based on the creator's brother, Steven Sugar.\n\nList of Steven Universe episodes: \"Steven Universe\" is an American animated television series created by Rebecca Sugar for Cartoon Network.  The series revolves around Steven Universe (voiced by Zach Callison), who protects his hometown of Beach City alongside Garnet (voiced by Estelle), Amethyst (voiced by Michaela Dietz) and Pearl (voiced by Deedee Magno), three magical alien guardians known as the Crystal Gems.  The series was renewed for a fourth and fifth season in March 2016.\n\nQuestion: What is the name of the first fully musical episode of the animated television series about a boy who lives in the fictional town of Beach City with the \"Crystal Gems\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"series_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the animated television series.\"\n    },\n    \"episode_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the first fully musical episode.\"\n    },\n    \"episode_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"season_number\": {\n          \"type\": \"integer\",\n          \"description\": \"The season number of the episode.\"\n        },\n        \"episode_number_in_season\": {\n          \"type\": \"integer\",\n          \"description\": \"The episode number within its season.\"\n        },\n        \"is_first_fully_musical\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if this is the series' first fully musical episode.\"\n        },\n        \"number_of_songs\": {\n          \"type\": \"integer\",\n          \"description\": \"The total number of songs featured in the episode.\"\n        }\n      },\n      \"required\": [\n        \"season_number\",\n        \"episode_number_in_season\",\n        \"is_first_fully_musical\",\n        \"number_of_songs\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"series_name\",\n    \"episode_name\",\n    \"episode_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "series_name": {
        "type": "string",
        "description": "The name of the animated television series."
      },
      "episode_name": {
        "type": "string",
        "description": "The name of the first fully musical episode."
      },
      "episode_details": {
        "type": "object",
        "properties": {
          "season_number": {
            "type": "integer",
            "description": "The season number of the episode."
          },
          "episode_number_in_season": {
            "type": "integer",
            "description": "The episode number within its season."
          },
          "is_first_fully_musical": {
            "type": "boolean",
            "description": "Indicates if this is the series' first fully musical episode."
          },
          "number_of_songs": {
            "type": "integer",
            "description": "The total number of songs featured in the episode."
          }
        },
        "required": [
          "season_number",
          "episode_number_in_season",
          "is_first_fully_musical",
          "number_of_songs"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "series_name",
      "episode_name",
      "episode_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
