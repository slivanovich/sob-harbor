{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSex and the City (season 4): The fourth season of the American television romantic sitcom Sex and the City aired in the United States on HBO.  The show was created by Darren Star while Star, Michael Patrick King, John P. Melfi, series lead actress Sarah Jessica Parker, Cindy Chupack, and Jenny Bicks served as executive producers.  The series was produced by Darren Star Productions, HBO Original Programming, and Warner Bros.  Television.  Sarah Jessica Parker portrays the lead character Carrie Bradshaw, while Kim Cattrall, Kristin Davis and Cynthia Nixon played her best friends Samantha Jones, Charlotte York, and Miranda Hobbes.\n\nMiss Match: Miss Match is an American comedy-drama television series created by Jeff Rake and Darren Star and produced by 20th Century Fox Television, Darren Star Productions, and Imagine Television.  It aired in the United States on NBC, Australia on Seven Network, Arena, and Fox8, and in the United Kingdom on Living, Channel 4, and is currently on E4.  Seventeen episodes of the series were filmed, but only eleven aired in the United States.  The entire series aired in both the UK and Canada.\n\nSex and the City (season 3): The third season of \"Sex and the City\", an American television romantic sitcom, aired in the United States on HBO from June 4 to October 15, 2000.  Based on the eponymous book written by Candace Bushnell, the series was created by Darren Star and produced by Darren Star Productions, HBO Original Programming, and Warner Bros.  Television.  Star, Barry Josen and Michael Patrick King served as the series' executive producers.  The show follows the relationships and sexual escapades of Carrie Bradshaw, a sex columnist for the fictional \"New York Star\", and her friends Samantha Jones, Charlotte York and Miranda Hobbes.\n\nSex and the City (season 1): The first season of \"Sex and the City\", an American television romantic sitcom, aired in the United States on HBO from June 6 to August 23, 1998.  Based on the eponymous book written by Candace Bushnell, the series was created by Darren Star and produced by Darren Star Productions, HBO Original Programming, and Warner Bros.  Television.  Star, Barry Josen and Michael Patrick King served as the series' executive producers.  The show follows the relationships and sexual escapades of Carrie Bradshaw, a sex columnist for the fictional \"New York Star\", and her friends Samantha Jones, Charlotte York and Miranda Hobbes.\n\nSex and the City (season 6): The sixth season of the American television romantic sitcom Sex and the City aired in the United States on HBO.  The show was created by Darren Star while Star, Michael Patrick King, John P. Melfi, series lead actress Sarah Jessica Parker, Cindy Chupack, and Jenny Bicks served as executive producers.  The series was produced by Darren Star Productions, HBO Original Programming, and Warner Bros.  Television.  Sarah Jessica Parker portrays the lead character Carrie Bradshaw, while Kim Cattrall, Kristin Davis and Cynthia Nixon played her best friends Samantha Jones, Charlotte York, and Miranda Hobbes.\n\nYounger (TV series): Younger is an American single-camera comedy-drama television series based on the Pamela Redmond Satran novel of the same name, created and produced by Darren Star.  The series stars Sutton Foster as the lead character, with Hilary Duff, Debi Mazar, Miriam Shor, Nico Tortorella, Molly Bernard and Peter Hermann co-starring in other main roles.  The series premiered on March 31, 2015 on TV Land and received generally positive reviews from critics.  It was renewed for a 12-episode second season in April 2015, but before the premiere of the second season on January 13, 2016, it was renewed for a third season, which began airing on September 28, 2016.  On June 14, 2016, the show was renewed for a fourth season, which premiered on June 28, 2017.  On April 20, 2017, the show was renewed for a fifth season ahead of its fourth season premiere.\n\nSex and the City (season 5): The fifth season of the American television romantic sitcom Sex and the City aired in the United States on HBO.  The show was created by Darren Star while Star, Michael Patrick King, John P. Melfi, series lead actress Sarah Jessica Parker, Cindy Chupack, and Jenny Bicks served as executive producers.  The series was produced by Darren Star Productions, HBO Original Programming, and Warner Bros.  Television.  Parker portrays the lead character Carrie Bradshaw, while Kim Cattrall, Kristin Davis and Cynthia Nixon played her best friends Samantha Jones, Charlotte York, and Miranda Hobbes.\n\nJon Gabrus: Jon Gabrus (born January 31, 1982) is an American actor and comedian, best known for his work on \"Guy Code\", the podcast \"Comedy Bang!  Bang! \", and TVLand's \"Younger\".  He is a performer at the Upright Citizens Brigade Theatre and hosts the \"High and Mighty\" podcast.\n\nSex and the City (season 2): The second season of \"Sex and the City\", an American television romantic sitcom, aired in the United States on HBO from June 6 to October 3, 1999.  Based on the eponymous book written by Candace Bushnell, the series was created by Darren Star and produced by Darren Star Productions, HBO Original Programming, and Warner Bros.  Television.  Star, Barry Josen and Michael Patrick King served as the series' executive producers.  The show follows the relationships and sexual escapades of Carrie Bradshaw, a sex columnist for the fictional \"New York Star\", and her friends Samantha Jones, Charlotte York and Miranda Hobbes.\n\n4th Man Out: Fourth Man Out is a 2016 American comedy film written by Aaron Danick and directed by Andrew Nackman.  The film stars Evan Todd as Adam, a young man living in New York state who, on his 24th birthday, comes out as gay to his best friends Chris (Parker Young), Nick (Chord Overstreet), and Ortu (Jon Gabrus).\n\nQuestion: What American comedy drama produced by Darren Star was acted in by Jon Gabrus?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"series_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the television series.\"\n    },\n    \"series_genres\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The genres of the television series.\"\n    },\n    \"creator_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the series creator.\"\n    },\n    \"producer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the series producer.\"\n    },\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor involved in the series.\"\n    }\n  },\n  \"required\": [\n    \"series_title\",\n    \"series_genres\",\n    \"creator_name\",\n    \"producer_name\",\n    \"actor_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "series_title": {
        "type": "string",
        "description": "The title of the television series."
      },
      "series_genres": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The genres of the television series."
      },
      "creator_name": {
        "type": "string",
        "description": "The name of the series creator."
      },
      "producer_name": {
        "type": "string",
        "description": "The name of the series producer."
      },
      "actor_name": {
        "type": "string",
        "description": "The name of the actor involved in the series."
      }
    },
    "required": [
      "series_title",
      "series_genres",
      "creator_name",
      "producer_name",
      "actor_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
