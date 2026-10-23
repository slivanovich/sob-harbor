{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLaw with Two Phases: Law with Two Phases (), also known as Law with Two Faces is a 1984 Hong Kong film written and directed by the film's lead star Danny Lee in his second directorial outing.\n\nDina Bonnevie: Geraldine Schaer Bonnevie known as Dina Bonnevie (born January 27, 1961) is an award-winning actress in the Philippines.  Before joining Philippine showbiz, Ms D (as she is popularly called) was first-runner in the Miss Magnolia 1979 Beauty Contest.  She landed her first acting assignment in the campy \"Temptation Island\" in 1979 with Joey Gosingfiao at the helm.  However, the following year, Regal Films launched her to lead star status via Joey Gosingfiao's \"Katorse\" opposite then boyfriend, Alfie Anido.  The same film introduced a young Gabby Concepcion who essayed the role of a naughty brat of a man.\n\nMana Ashida: Mana Ashida (芦田 愛菜 , Ashida Mana , born 23 June 2004) is a Japanese child actress, \"tarento\" and singer.  Ashida's first appearance was in Asahi Broadcasting Corporation's \"ABC Short Movie 2\", though she rose to prominence after acting in the television drama \"Mother\".  She became the youngest lead star in Japanese drama history when she starred in \"Sayonara Bokutachi no Youchien\".  She was the youngest lead actress in a television serial drama by appearing in the serial drama \"Marumo no Okite\" in the spring of 2011.  She also appeared in Japanese films such as \"Confessions\" and \"Usagi Drop\".\n\nRegine Velasquez filmography: Regine Velasquez is a Filipina singer-actress who has worked in theatre, television and film.  In films she has starred as a supporting cast with minor roles, but later cast as the female lead star of a remake of \"Wanted: Perfect Mother\" opposite with Christopher de Leon in 1996.  Since then she starred in numerous films the majority of which have been box office.  In 2002 she received her first acting award as \"Best Single Performance By An Actress\" at the 16th PMPC Star Awards for Television for her portrayal of a mentally challenged in drama series \"Maalaala Mo Kaya\".\n\nValery Nikolaev: Valery Valeryevich Nikolaev (Russian: Валерий Валерьевич Николаев ; born 23 August 1965) is a Russian film and theater actor, director.\n\nYaariyan (2014 film): Yaariyan (English: \"friendships\") is a 2014 Bollywood coming-of-age romance adventure film directed by Divya Khosla Kumar, starring Himansh Kohli, Rakul Preet Singh and Nicole Faria in the lead roles.  It marks the debut of the director as well as the lead star cast.  The film was produced by Bhushan Kumar and Krishan Kumar under the banner of T-Series Super Cassettes Industries.\n\nMario Maurer: Mario Maurer (Thai: มาริโอ้ เมาเร่อ ,  ] , ] ) is a Thai model and actor.  Starting off a career as a model at age 16, he later became best known for his lead role in the 2007 film, \"The Love of Siam\" and the 2010 sleeper hit, \"First Love\".  He was also the lead star of Thailand's highest grossing film of all time, \"Pee Mak\".  He is also part of a group called 4+1 Channel 3 Superstar with Nadech Kugimiya, Prin Suparat, Pakorn Chatborirak, and Phupoom Pongpanu.\n\nSuspiria (upcoming film): Suspiria is an upcoming horror film directed by Luca Guadagnino and written by David Kajganich.  It is an adaptation of the 1977 film \"Suspiria\", and stars Dakota Johnson, Chloë Grace Moretz, Mia Goth, and Tilda Swinton.  Jessica Harper, lead star of the original film, will also appear as a different character.\n\nGlory to the Filmmaker!: Glory to the Filmmaker!  (監督·ばんざい!  , Kantoku · Banzai! )  is a 2007 Japanese film written, directed, edited by the film's lead star Takeshi Kitano.  It is the second film in Kitano's surrealist autobiographical trilogy, following \"Takeshis'\", and concluding with \"Achilles and the Tortoise\".\n\nVedma (The Power of Fear): Vedma (The Power of Fear) (Russian: Ведьма) is a 2006 Russian gothic horror film directed by Oleg Fesenko and starring Valery Nikolaev in the lead.\n\nQuestion: The lead star of the horror film Vedma was born in what year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"film_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"lead_star\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the lead star.\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The birth year of the lead star.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"birth_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_genre\",\n    \"lead_star\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "film_genre": {
        "type": "string",
        "description": "The genre of the film."
      },
      "lead_star": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the lead star."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the lead star."
          }
        },
        "required": [
          "name",
          "birth_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "film_genre",
      "lead_star"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
