{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSchorle: Schorle is a German beverage made by diluting juice or wine with carbonated water or lemonade (lemon-lime soda).  The most common variety is Apfelschorle (made from apple juice and sparkling mineral water).  Large bottles of Schorle can be found at most grocers, stores, supermarkets and anywhere else where carbonated drinks are sold, next to the soda.  Due to its dilution it is less sweet or alcoholic than the original beverage, making it better suited as a refreshment on hot summer days or as an alternative to beer at the biergarten or .\n\nThe Long, Hot Summer (TV series): The Long, Hot Summer is an American drama series from 20th Century Fox Television that was broadcast on ABC-TV for one season from 1965-1966.  Created by Dean Riesner, \"The Long, Hot Summer\" was based on the novel \"The Hamlet\" by William Faulkner, the short story \"Barn Burning\", and the 1958 film of the same name.  The show retained the movie's theme song, \"The Long, Hot Summer,\" written by Sammy Cahn and Alex North, and Jimmie\n\nSummer Days: Summer Days (サマーデイズ , Samā Deizu ) is an erotic visual novel developed by 0verflow, released on June 23, 2006 for Windows and later ported as a DVD game and for the PlayStation Portable (PSP).  It is the second installation of \"School Days\" line of series, succeeding the visual novel of the same name and preceding \"Cross Days\".  Unlike the previous titles, that exist in the same continuity however, \"Summer Days\" is a spin-off of the original story retold from the perspective of Setsuna Kiyoura, a high school student out for summer vacation who finds herself attracted to Makoto Itou, a classmate and fellow patron of a restaurant she eventually comes to work at.  The game retains the anime-like presentation familiar to the franchise, requiring little interaction from users, engaging players through a nonlinear plot they are given opportunities to change, and concluding with an ending specific to the choices made during play.\n\nOmija-hwachae: Omija-hwachae (오미자화채 ; 五味子花菜 ) or magnolia berry punch is a sweet and tangy \"hwachae\" (punch) made with magnolia berries—\"omija\" in Korean.  The reddish-pink punch is typically served during hot summer days.\n\nGreat Molasses Flood: The Great Molasses Flood, also known as the Boston Molasses Disaster or the Great Boston Molasses Flood, occurred on January 15, 1919 in the North End neighborhood of Boston, Massachusetts.  A large molasses storage tank burst and a wave of molasses rushed through the streets at an estimated 35 mph , killing 21 and injuring 150.  The event entered local folklore and for decades afterwards residents claimed that on hot summer days the area still smelled of molasses.\n\nHot Summer Days: Hot Summer Days is a 2010 Hong Kong romantic comedy film featuring an ensemble cast including Nicholas Tse, Jacky Cheung, Daniel Wu, Vivian Hsu, Barbie Shu, Rene Liu, Angelababy and Jing Boran and also featuring a guest appearance by Maggie Cheung.  The film was released to celebrate both Chinese New Year and Valentine's Day.\n\nMisu: Misu (미수 ) is a beverage made from Korean traditional grain powder, misu-garu (미숫가루 ; \"misutgaru\"; \"\"misu\" powder\") which is a combination of 7-10 different grains.  It is usually served in the hot summer days to quench thirst or as an instant nutritious drink for breakfast or as a healthy snack.\n\nMaggie Cheung: Maggie Cheung Man-yuk (; born 20 September 1964) is a Hong Kong actress.  Raised in Britain and Hong Kong, she has over 80 films to her credit since starting her career in 1983.  Some of her most commercially successful works were in the action genre, but Cheung once said in an interview that of all the work she has done, the films that really meant something to her are \"Song of Exile\", \"Centre Stage\", \"\" and \"In the Mood for Love\".  As Emily Wang in \"Clean\", her last starring role to date, she became the first Asian actress to win a prize at the Cannes Film Festival.\n\nAchnahaird Bay: Achnahaird Bay is located on the Coigach peninsula, Wester Ross, Scotland, and can be reached by following the road to the scattered settlement of Achiltibuie.  The beautiful, wide sandy beach and stunning views of the mountains Stac Pollaidh, Canisp and Suilven mean the area is popular with tourists (and locals) on hot summer days.\n\nCalifornia Girls: \"California Girls\" is a song written by Brian Wilson and Mike Love for the American rock band the Beach Boys, featured on their 1965 album \"Summer Days (And Summer Nights!!) \".  Wilson conceived the song during his first acid trip, later arranging and producing the song's recording, and incorporating an orchestral prelude plus contrasting verse-chorus form.  Upon its release as a single, \"California Girls\" reached No. 3 on the \"Billboard\" Hot 100.  It was backed with \"Let Him Run Wild\", another track from \"Summer Days\".\n\nQuestion: The actress who had a featured guest appearance in \"Hot Summer Days\" was born in what year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"actress_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actress who made a guest appearance.\"\n    },\n    \"role_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of role the actress had in the film.\"\n    },\n    \"actress_birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the actress.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"actress_name\",\n    \"role_type\",\n    \"actress_birth_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "actress_name": {
        "type": "string",
        "description": "The name of the actress who made a guest appearance."
      },
      "role_type": {
        "type": "string",
        "description": "The type of role the actress had in the film."
      },
      "actress_birth_year": {
        "type": "integer",
        "description": "The birth year of the actress."
      }
    },
    "required": [
      "film_title",
      "actress_name",
      "role_type",
      "actress_birth_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
