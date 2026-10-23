{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFong Sai-yuk: Fong Sai-yuk or Fang Shiyu was a (possibly fictional) Chinese martial artist and folk hero from Zhaoqing City, Guangdong Province.  He was first mentioned in \"wuxia\" stories dating from the Qing dynasty (1644–1912), such as \"Shaolin Xiao Yingxiong\" (少林小英雄; \"Young Hero of Shaolin\"), \"Wan Nian Qing\" (萬年青) and \"Qianlong You Jiangnan\" (乾隆游江南; \"The Qianlong Emperor Visits Jiangnan\").  His father, Fong Tak (方德; Fang De), was a wealthy merchant, while his mother, Miu Tsui-fa (苗翠花; Miao Cuihua), was a martial arts expert.  Fong was also associated with Hung Hei-gun and the Five Elders of the Southern Shaolin Monastery.\n\nHero of the Times: Hero of the Times () is a Singaporean-Taiwanese \"wuxia\" television series based on legends about Fong Sai-yuk (Mandarin: Fang Shiyu), a Chinese folk hero and martial artist who lived in the Qing dynasty.  It was co-produced by the Television Corporation of Singapore (now MediaCorp) and Taiwan's China Television, directed by Hu Mingkai, and starred mainland Chinese actor Vincent Zhao as Fang Shiyu.  It was first aired in Singapore on TCS Eighth Frequency (now MediaCorp Channel 8) from late 1999 to early 2000.\n\nFong Sai-yuk (disambiguation): Fong Sai-yuk is a Chinese martial artist and folk hero.\n\nJet Li: Li Lianjie (born 26 April 1963), better known by his stage name Jet Li, is a Chinese film actor, film producer, martial artist, and retired Wushu champion who was born in Beijing.  He is a naturalized Singaporean citizen.\n\nDisciples of the 36th Chamber: Disciples Of The 36th Chamber (霹靂十傑, \"Pi li shi jie\", \"Disciples of the Master Killer\" or \"Master Killer III\") is a 1985 Shaw Brothers Studio Hong Kong martial arts film comedy written, directed and choreographed Lau Kar-leung.  It is the third in a loose trilogy of films that began with \"The 36th Chamber of Shaolin\" (1978) and was followed by \"Return to the 36th Chamber\" (1980).  In \"Disciples\", the action is focused on Hsiao Ho, who portrays legendary martial artist Fong Sai-Yuk.  Gordon Liu, a constant in the \"36th Chamber\" series, reprises his role from \"The 36th Chamber of Shaolin\" as the monk San Te.\n\nHero (1997 film): Hero () is a 1997 Hong Kong martial arts film written and directed by Corey Yuen.  The film stars Taiwanese-Japanese actor Takeshi Kaneshiro, established Hong Kong action stars from the Peking Opera School (Yuen Biao, Yuen Wah, Corey Yuen, Yuen Tak) and Hong Kong actresses Valerie Chow and Jessica Hsuan.  \"Hero\" is a remake of the 1972 film, \"Boxer from Shantung\".  The film was produced by then TVB chairwoman Mona Fong.\n\nMy Father Is a Hero: My Father Is a Hero (, released in the United States as The Enforcer and Jet Li's The Enforcer) is a 1995 Hong Kong action film starring Jet Li and directed by Corey Yuen, who also co-stars in the film.  The film was released in the Hong Kong on 2 March 1995.\n\nHsiao Ho (actor): Hsiao Ho, (Hsiao Hou) (; Cantonese: Siu Hau, born 1 January 1958 (age 58) in Meixian District, Guangdong, China) is a Hong Kong martial arts film actor, stunt performer and action choreographer.  A Hakka, he has acted in many films directed by Lau Kar-leung, including \"Mad Monkey Kung Fu\" and Legendary Weapons of China.  In 1985 he portrayed legendary kung fu warrior Fong Sai-Yuk in the Lau directed action-comedy, \"Disciples of the 36th Chamber\" and also took a lead role in Fake Ghost Catchers, directed by Lau Kar Wing.  Fake Ghost Catchers is marketed by Celestial Pictures as being made two years before Ghostbusters (inferring that the idea for Ghostbusters may have come from the movie).  Hou is also known for portraying the \"disfigured swordsman\" and doubling complicated action scenes in 1993's \"Iron Monkey\".  He was also the action director for the movie Shaolin Avengers (1994).  In 1982 he was nominated for Best Action Choreography for the movie Legendary Weapons of China (for which he was action director) at the Hong Kong Film Awards alongside Lau Kar Leung and Ching Chu who also provided choreography for the film.\n\nFong Sai-yuk II: Fong Sai-yuk II, also known as The Legend II and The Legend of Fong Sai-yuk II, is a 1993 Hong Kong martial arts comedy film directed by Corey Yuen, and also produced by and starring Jet Li as Chinese folk hero Fong Sai-yuk.  The film is a sequel to \"Fong Sai-yuk\", which was released earlier in the same year.  Two former Miss Hong Kong Pageant winners, Michelle Reis and Amy Kwok, portrayed Fong Sai-yuk's wives.\n\nFong Sai-yuk (film): Fong Sai-yuk (, aka The Legend of Fong Sai-yuk, or simply, The Legend) is a 1993 Hong Kong action and comedy film directed by Corey Yuen starring Jet Li as Chinese folk hero Fong Sai-yuk.  The film won the Hong Kong Film Award and Golden Horse Award for best action choreography.  The film received positive reviews praising Josephine Siao's acting and the action choreography.\n\nQuestion: Fong Sai-yuk, is a Hong Kong action and comedy film directed by Corey Yuen starring actor Jet Li as Chinese folk hero Fong Sai-yuk, released in which year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released.\"\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"lead_actor\": {\n      \"type\": \"string\",\n      \"description\": \"The lead actor starring in the film.\"\n    },\n    \"folk_hero_portrayed\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the folk hero portrayed by the lead actor.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"director\",\n    \"lead_actor\",\n    \"folk_hero_portrayed\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "release_year": {
        "type": "integer",
        "description": "The year the film was released."
      },
      "director": {
        "type": "string",
        "description": "The director of the film."
      },
      "lead_actor": {
        "type": "string",
        "description": "The lead actor starring in the film."
      },
      "folk_hero_portrayed": {
        "type": "string",
        "description": "The name of the folk hero portrayed by the lead actor."
      }
    },
    "required": [
      "film_title",
      "release_year",
      "director",
      "lead_actor",
      "folk_hero_portrayed"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
