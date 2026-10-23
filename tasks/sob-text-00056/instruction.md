{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nNatassia Malthe: Natassia is the younger of two daughters.  She was born in Oslo, Norway, and is of half Malaysian descent.  Her mother is from Kota Kinabalu, Sabah.  She is usually credited by her birth name but is sometimes credited as \"Lina Teal\".\n\nMatador (Danish TV series): Matador is a Danish TV series produced and shown between 1978 and 1982.  It is set in the fictional Danish town of Korsbæk between 1929 and 1947.  It follows the lives of a range of characters from across the social spectrum, focusing specifically on the rivalry between the families of two businessmen: The banker Hans Christian Varnæs, an established local worthy, and social climber Mads (Andersen-)Skjern, who arrives in town as the series opens.  The name \"Matador\" was taken from , also the series' tentative English title.  In addition, in contemporary Danish a \"matador\" is often used to describe a business tycoon, in the series referring to the character of Mads Skjern and his craftiness as a self-made entrepreneur.\n\nGideon Planish: Gideon Planish is a 1943 novel by American writer Sinclair Lewis.  The novel tells the story of Gideon Planish, an unprincipled social climber who becomes involved in various shady philanthropic organizations in his quest for stature without accountability.  The work did not fare as well with critics as some of Lewis' earlier social novels, and is considered one of his minor works.\n\nSofie Cappelen: Sofie Stange Cappelen (born February 2, 1982) is a Norwegian-born actress.\n\nConfessions page: Confessions pages are pages on social networking websites (such as Facebook) which are generally used at schools and universities for students to anonymously post their confessions and secrets to their respective communities.  Confessions, statements acknowledging personal facts that someone would prefer to not be shared under their true identity, are sent to the administrators of the page through online form services such as SurveyMonkey and Google Forms or submission portals created with purpose-built tools.  The administrators then decide which confessions to post on the page.\n\nAnna-Lisa: Anna-Lisa (born 1933) is a Norwegian-born actress who appeared primarily in American films and television.\n\nAshley Madekwe: Ashley Madekwe (born 6 December 1983) is an English actress.  She is known for her roles as call girl Bambi in the ITV2 series \"Secret Diary of a Call Girl\", social climber Ashley Davenport on the ABC drama series \"Revenge\" and the witch Tituba in the WGN America series \"Salem\".\n\nKeeping Up Appearances: Keeping Up Appearances is a British sitcom created and written by Roy Clarke for the BBC, centred on the life of eccentric and snobbish middle class social climber Hyacinth Bucket, who insists that her surname is pronounced \"Bouquet\".  The sitcom follows Hyacinth in her attempts to prove her social superiority and to gain standing with those she considers upper class; attempts that are constantly hampered by her decidedly lower class extended family whom she desperately seeks to hide.  Much of the humour comes from the culture clash between Hyacinth's vision of herself and the reality of her working-class background, plus the farcical situations in which she finds herself as she battles to protect her social credibility.\n\nBecky Sharp (character): Rebecca or Becky Sharp is the main character of William Makepeace Thackeray's satirical novel \"Vanity Fair\" (1847–48).  A cynical social climber who uses her charms to fascinate and seduce upper-class men, Sharp is contrasted with the clinging, dependent Amelia Sedley.  She befriends Amelia at an expensive girls school where she is given a place because Becky's father teaches there, and uses her as a stepping stone to gain social position.  Sharp functions as a \"picara\"—a picaresque heroine—or by being a social outsider who is able to expose the manners of the upper gentry to ridicule.\n\nConfessions of a Sociopathic Social Climber: Confessions of a Sociopathic Social Climber (also known as The Social Climber in United Kingdom and Legally Chic in Brazil) is a comedy film, based on the novel of the same name by Adele Lang.  It was released March 12, 2005 and stars Jennifer Love Hewitt as 28-year-old Katya, an advertising executive more concerned with being a well-known socialite than being a good person.  It co-stars Colin Ferguson, Joey Lawrence, Natassia Malthe, Daniel Roebuck and James Kirk.\n\nQuestion: What is the pseudonym of the Norwegian-born actress who starred in Confessions of a Sociopathic Social Climber?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"movie_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film mentioned in the question.\"\n    },\n    \"actress_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"birth_name\": {\n          \"type\": \"string\",\n          \"description\": \"The birth name of the actress.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the actress.\"\n        },\n        \"pseudonym\": {\n          \"type\": \"string\",\n          \"description\": \"The pseudonym used by the actress.\"\n        }\n      },\n      \"required\": [\n        \"birth_name\",\n        \"nationality\",\n        \"pseudonym\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"final_answer\": {\n      \"type\": \"string\",\n      \"description\": \"The pseudonym of the actress who starred in the specified movie.\"\n    }\n  },\n  \"required\": [\n    \"movie_title\",\n    \"actress_details\",\n    \"final_answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "movie_title": {
        "type": "string",
        "description": "The title of the film mentioned in the question."
      },
      "actress_details": {
        "type": "object",
        "properties": {
          "birth_name": {
            "type": "string",
            "description": "The birth name of the actress."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the actress."
          },
          "pseudonym": {
            "type": "string",
            "description": "The pseudonym used by the actress."
          }
        },
        "required": [
          "birth_name",
          "nationality",
          "pseudonym"
        ],
        "additionalProperties": false
      },
      "final_answer": {
        "type": "string",
        "description": "The pseudonym of the actress who starred in the specified movie."
      }
    },
    "required": [
      "movie_title",
      "actress_details",
      "final_answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
