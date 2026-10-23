{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLuc Bendza: Luc Bendza (born July 6, 1969) is an Gabonese-Chinese actor and martial artist.  He is known for his role as boxer Jesse Glover in \"The Legend of Bruce Lee\".\n\nThe Legend of Bruce Lee: The Legend of Bruce Lee is a 2008 Chinese biographical martial arts television series based on the life story of martial artist and actor Bruce Lee.  The 50-episode series was produced and broadcast by CCTV and began airing on October 12, 2008.  It stars Hong Kong actor Danny Chan as Bruce Lee and American actress Michelle Lang as Lee's wife, Linda Lee Cadwell.  The production period spanned nine months, with filming taking place in China, Hong Kong, Macau, the United States, Italy, and Thailand, and with a budget of 50 million yuan (US$7.3 million).\n\nThe Teenage Show: The Teenage Show, also known as \"The Teenage Hour\", is an Australian music television series which aired on Saturdays from 1958 to 1960 on Melbourne station HSV-7.  The live series was a successor to \"Teenage Mailbag\", and episodes ran about an hour (though per TV listings some episodes aired in a 55-minute time-slot).  Heather Horwood, Jack Kelleher, and Gaynor Bunning were both regulars.  Bands also appeared, including The Moontones and The Rockets.  The archival status of the series is unknown.  In one episode an Aboriginal boxer named George Bracken sang, and made enough of an impression to be signed by a label to release a single.\n\nTuxedo Gin: Tuxedo Gin (タキシード銀 , Takishiido Gin ) is a romantic comedy manga series by Tokihiko Matsuura.  It was published by Shogakukan in \"Shōnen Sunday\" from 1997 to 2000 and collected in 15 bound volumes.  It is published North America in English by Viz Communications.  The series is about a teenaged boxer named Ginji Kusanagi who is reincarnated as a penguin in order to be close to the girl he likes.  On August 4, 2011, Walt Disney Pictures and Viz Pictures announced they were adapting the Tuxedo Gin manga into a feature film under the name, \"Tux\".\n\nThe Rudy and Gogo World Famous Cartoon Show: The Rudy and GoGo World Famous Cartoon Show was a programming block of cartoons for TNT during the mid-1990s.  Hosted by \"Rowdy\" Rudy R. Moore (a marionette puppet of a young boy, who looked a little like Howdy Doody), and his pet goat Gogo (a live action nanny goat), the show featured a variety of cartoon short subjects from Turner Entertainment's library, including pre-July 1948 Warner Bros.' \"Looney Tunes\" and \"Merrie Melodies\", MGM cartoons such as \"Tom and Jerry\" and \"Droopy\", and Fleischer/Famous' \"Popeye the Sailor\".  Between cartoons, Rudy, Gogo, and an African American puppet named Jesse B. Weaver (or \"Jumpin' J.B.\" to his friends) would star in short host segments, usually involving floating around in a bizarre colorful spiral and randomly screaming.  The show also used clips from various Turner-owned films and television series from the 1960s and 1970s for added backdrops and storylines.\n\nKnight Rider (2008 film): Knight Rider is a 2008 television film which was created to serve as a backdoor pilot for the new \"Knight Rider\" television series, a revival of the series of the same name which aired during the 1980s.  This film does not refer to either the \"Knight Rider 2000\" film or the \"Team Knight Rider\" television series.\n\nJingwu Chen Zhen: Jingwu Chen Zhen is a television series based on the story of Chen Zhen, a fictional student of the Chinese martial artist Huo Yuanjia.  The series is a sequel to the 2008 television series \"Huo Yuanjia\", with Jordan Chan reprising his role as Chen Zhen.\n\nAkhilendra Mishra: Akhilendra Mishra is an Indian film and television character actor best known for his role as Kroor Singh in the 1990s Doordarshan fantasy television series \"Chandrakanta\".  His other notable works include the character of Mirchi Seth in the 1999 critically acclaimed film \"Sarfarosh\".  He also played the character of Arjan in the Academy Award nominated film \"Lagaan\".  He was born in Siwan, Bihar.  Akhilendra completed his schooling and graduation in Saran.  He played the demon king Ravana in the 2008 television adaptation of the Hindu epic Ramayana.\n\nRoxy LeBlanc: Roxanne Marie \"Roxy\" LeBlanc (\"née\" Brooks) is a fictional character on the Lifetime television series \"Army Wives\", played by Sally Pressman.  She is married to 2LT Trevor LeBlanc.  She has four sons.  T.J. and Finn are from two separate previous relationships (an abusive husband named Jesse, and a boyfriend named Whit), and were legally adopted by Trevor.  She then had twins with Trevor, Wyatt and Drew, who were born in the sixth season.\n\nYvonne Verbeeck: Yvonne Verbeeck (7 December 1913 – 26 February 2012) was a Belgian Flemish actress known for roles in theater and television.  She appeared in several Belgian films as well.  Her last role was in the 2008 television series, \"Zone Stad\".  A bronze bust of Verbeeck is dedicated in her birthplace, Rumst.\n\nQuestion: Luc Bendza plays the role of a boxer named Jesse Glover in what 2008 television series?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor.\"\n    },\n    \"role_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the character played by the actor.\"\n    },\n    \"character_type\": {\n      \"type\": \"string\",\n      \"description\": \"The profession or type of the character.\"\n    },\n    \"series_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the television series.\"\n    },\n    \"series_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the television series was released or began airing.\"\n    },\n    \"series_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the television series.\"\n    },\n    \"series_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of production, e.g., television series, film.\"\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"role_name\",\n    \"character_type\",\n    \"series_title\",\n    \"series_year\",\n    \"series_genre\",\n    \"series_type\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor."
      },
      "role_name": {
        "type": "string",
        "description": "The name of the character played by the actor."
      },
      "character_type": {
        "type": "string",
        "description": "The profession or type of the character."
      },
      "series_title": {
        "type": "string",
        "description": "The title of the television series."
      },
      "series_year": {
        "type": "integer",
        "description": "The year the television series was released or began airing."
      },
      "series_genre": {
        "type": "string",
        "description": "The genre of the television series."
      },
      "series_type": {
        "type": "string",
        "description": "The type of production, e.g., television series, film."
      }
    },
    "required": [
      "actor_name",
      "role_name",
      "character_type",
      "series_title",
      "series_year",
      "series_genre",
      "series_type"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
