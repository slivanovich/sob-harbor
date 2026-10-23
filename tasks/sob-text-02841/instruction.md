{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nList of Daredevil characters: \"Daredevil\" is an American web television series created for Netflix by Drew Goddard, based on the Marvel Comics character of the same name.  It is set in the Marvel Cinematic Universe (MCU), sharing continuity with the films of the franchise, and is the first in a series of shows that will lead up to a Defenders crossover miniseries.  The series stars Charlie Cox as Matt Murdock / Daredevil, as well as Deborah Ann Woll, Elden Henson, Rosario Dawson, and Vincent D'Onofrio.  Toby Leonard Moore, Vondie Curtis-Hall, Bob Gunton, and Ayelet Zurer join them for the first season, while Jon Bernthal, Élodie Yung, and Stephen Rider join them for the second.  In addition to original characters, several other characters based on various Marvel properties also appear throughout the series.\n\nJessica Hamby: Jessica Hamby is a fictional character in the \"True Blood\" series, portrayed by Deborah Ann Woll.  In the series, which chronicles the life of human waitress Sookie Stackhouse and her friends after vampires make themselves known to humans, Jessica is a newly turned vampire who must learn to deal with her vampiric abilities, weaknesses and altered lifestyle.\n\nSennin Buraku: Sennin Buraku (仙人部落 , roughly Hermit Village) is a manga series by Kō Kojima which ran in the adult magazine \"Weekly Asahi Geinō\", published by Tokuma Shoten in Japan.  It is the longest running comic with only one artist, being published weekly since October 1956, and the longest-running strip ever in Japan.  By contrast, \"Golgo 13\" is the longest running manga to be serialized in a dedicated manga magazine with \"Doraemon\" the second longest, and \"Kochira Katsushika-ku Kameari Kōen-mae Hashutsujo\" (\"Kochi-Kame\") the third longest (Asahi Geino is not a dedicated manga magazine).  While \"Sennin Buraku\" has been running for more years than \"Peanuts\", Charles M. Schulz's strip has more \"episodes\" as it ran daily rather than weekly.  The story was a romantic comedy taking place in historical China, and it was quite risqué for its time.  The characters were very traditionally dressed (e.g. all wearing hanfu).  Although the anime is very hard to find, it has been rerun on Japanese television, its intro and outro has appeared on DVD, and an episode has resurfaced on Nico Nico Douga.\n\nDeborah Ann Woll: Deborah Ann Woll (born February 7, 1985) is an American actress.  She is known for her roles as Jessica Hamby on the HBO drama series \"True Blood\", and currently portrays Karen Page in the Netflix drama series \"Daredevil\", \"The Defenders\", and \"The Punisher\".  She has also starred in the films \"Mother's Day\", \"Someday This Pain Will Be Useful to You\", \"Catch .44\", \"Ruby Sparks\", and \"Meet Me in Montenegro\".\n\nForever (2015 film): Forever is a 2015 American drama independent film directed by Tatia Pilieva and written by Pilieva and Gill Dennis, starring Deborah Ann Woll, Luke Grimes, John Diehl, Rhys Coiro, Jill Larson, and Ioan Gruffudd.\n\nElektra (comics): Elektra Natchios ( , ) is a fictional character appearing in American comic books published by Marvel Comics.  Created by Frank Miller, the character first appeared in \"Daredevil\" #168 (January 1981).  She is a love interest of the superhero Daredevil, but her violent nature and mercenary lifestyle divide the two.\n\nCatch .44: Catch .44 is a 2011 American crime thriller film starring Forest Whitaker, Bruce Willis, Malin Åkerman, Nikki Reed, Deborah Ann Woll, and Brad Dourif.  The film is written and directed by Aaron Harvey.\n\nKaren Page: Karen Page is a fictional character appearing in American comic books published by Marvel Comics.  The character has been a regular cast member of Marvel's \"Daredevil\" series, and is the longest running love interest for the title character.\n\nMiss You Much: \"Miss You Much\" is a song recorded by American singer Janet Jackson, released as the lead single from her fourth album \"Janet Jackson's Rhythm Nation 1814\" (1989).  The single spent four weeks at number-one on the US \"Billboard\" Hot 100, making it the longest running number-one single of 1989.  \"Miss You Much\" was the second-best selling single of 1989 and the biggest radio airplay song of the year.  \"Billboard\" later listed \"Miss You Much\" as Janet Jackson's all-time biggest Hot 100 single.  It is Jackson's third longest running number-one single, behind \"That's the Way Love Goes\" (1993) and \"All for You\" (2001), which spent eight and seven weeks at number-one.\n\nBetty Cooper: Elizabeth \"Betty'\" Cooper is one of the main characters appearing in American comic books published by Archie Comics.  The character was created by Bob Montana and John L. Goldwater, and first appeared in Pep Comics #22 (cover-dated Dec. 1941), on the first page of the first \"Archie\" story, serving as a love interest to Archie Andrews.  Betty's infatuation with Archie making her strive for his attention using whatever means possible has been one of the longest running themes in the comics.  In 2011, Betty Cooper was ranked 66th in \"Comics Buyer's Guide's\" \"100 Sexiest Women in Comics\" list.\n\nQuestion: What longest running love interest for Daredevil is played by Deborah Ann Woll?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"character_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the character.\"\n    },\n    \"is_longest_running_love_interest_for_daredevil\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the character is the longest running love interest for Daredevil.\"\n    },\n    \"portrayed_by\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"actress_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actress who portrays the character.\"\n        },\n        \"series_portrayed_in\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of series where the actress portrays this specific character.\"\n        }\n      },\n      \"required\": [\n        \"actress_name\",\n        \"series_portrayed_in\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"character_name\",\n    \"is_longest_running_love_interest_for_daredevil\",\n    \"portrayed_by\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "character_name": {
        "type": "string",
        "description": "The name of the character."
      },
      "is_longest_running_love_interest_for_daredevil": {
        "type": "boolean",
        "description": "Indicates if the character is the longest running love interest for Daredevil."
      },
      "portrayed_by": {
        "type": "object",
        "properties": {
          "actress_name": {
            "type": "string",
            "description": "The name of the actress who portrays the character."
          },
          "series_portrayed_in": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of series where the actress portrays this specific character."
          }
        },
        "required": [
          "actress_name",
          "series_portrayed_in"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "character_name",
      "is_longest_running_love_interest_for_daredevil",
      "portrayed_by"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
