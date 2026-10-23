{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDunkirk (2017 film): Dunkirk is a 2017 war film written, co-produced, and directed by Christopher Nolan that portrays the Dunkirk evacuation of the Second World War.  Its ensemble cast includes Fionn Whitehead, Tom Glynn-Carney, Jack Lowden, Harry Styles, Aneurin Barnard, James D'Arcy, Barry Keoghan, Kenneth Branagh, Cillian Murphy, Mark Rylance, and Tom Hardy.  Distributed by Warner Bros.  Pictures, the film is a co-production between the United Kingdom, the United States, France, and the Netherlands.\n\nTimothy Hutton: Timothy Tarquin Hutton (born August 16, 1960) is an American actor and director.  He is the youngest male actor to win the Academy Award for Best Supporting Actor, which he won at the age of 20 for his performance as Conrad Jarrett in \"Ordinary People\" (1980).  Hutton has since appeared regularly in feature films and on television, with featured roles in the drama \"Taps\" (1981), the spy film \"The Falcon and the Snowman\" (1985), and the horror film \"The Dark Half\" (1993), among others.\n\nArsi Nami: Arsalan Nami (Persian: ارسلان نامی‎ ‎ ) (born May 21, 1984 in Shiraz) better known as Arsi Nami, is a Persian-Swedish singer, songwriter, music therapist, actor and philanthropist living in Los Angeles, California.  Credits include music on Fox TV shows Bones (TV series) and The Goodwin Games as well Cannes Film Festival winning film Love is Blind and Crown Prince of Heaven.  He was the lead actor and composer in drama shortfilm, Love Is Blind, which won the 2017 Jury Prize at Cannes International Film Festival Entr'2 Marches for sharing disability awareness.  His commercial acting credits include giant brands such as Hewlett Packard, Ford Motor Company, Samsung, Disney, NBA, Guitar Center, Los Defensores.  Arsi Nami nominated for Best lead male actor in comedy film Villa, a 2017 Official Selection at Premio Tortoreto alla Cultura in Italy, AM Film Festival in Egypt and International Festival of Short Films on Culture & Tourism, India.  also one of the lead actors in 2017 European Cinematography Award winning Drama film Camelia as Vincent the painter.\n\nThe Killing of a Sacred Deer: The Killing of a Sacred Deer is a 2017 psychological horror-thriller film directed by Yorgos Lanthimos, from a screenplay by Lanthimos and Efthymis Filippou.  It stars Colin Farrell and Nicole Kidman.  It was selected to compete for the Palme d'Or in the main competition section at the 2017 Cannes Film Festival.  At Cannes, Lanthimos and Filippou won the Best Screenplay award.  The film is scheduled to be released in the United States on October 20, 2017, by A24, before being released in the United Kingdom on November 17, 2017, by Curzon Artificial Eye.\n\nBarry Keoghan: Barry Keoghan (born 18 October 1992) is an Irish actor.  He has appeared in the films \"Dunkirk\" along with Mark Rylance, Tom Hardy, Cillian Murphy, Kenneth Branagh, Tom Glynn-Carney; \"The Killing of a Sacred Deer\" with Nicole Kidman, Colin Farrell and Alicia Silverstone; and \"Trespass Against Us\" with Michael Fassbender and Brendan Gleeson.  He has also played the \"heartless cat killer\" Wayne in the RTÉ drama \"Love/Hate\".\n\nIIFA Award for Star Debut of the Year – Male: The IIFA Award for Star Debut of the Year – Male is given by the International Indian Film Academy as part of its annual award ceremony to recognise a male actor who has delivered an outstanding performance in his debut film.  Originally known as the \"IIFA Award for Fresh Face of the Year (Male)\", it was officially given its new title in 2006.  During its inaugural year in 2001, four separate actors were presented with an award.\n\nARY Film Award for Best Star Debut Male: ARY Film Award for Best Star Debut Male is one of the ARY Film Awards of Merit presented annually by the ARY Digital Network and Entertainment Channel to recognize the male actor who has delivered an outstanding debut performance while working in the film industry.  Since its inception, however, the award has commonly been referred to as the AFA for Best Star Debut Male.  While actors are nominated for this award by AFA members who are actors and actresses themselves, winners are selected by the AFA membership as a whole.\n\nSaturn Award for Best Actor: The Saturn Award for Best Actor is an award presented annually by the Academy of Science Fiction, Fantasy & Horror Films to honor the top works in science fiction, fantasy, and horror in film, television, and home video.  The Saturn Awards were devised by Dr. Donald A. Reed, who felt that films within those genres were never given the appreciation they deserved.  The physical award is a representation of the planet Saturn, surrounded with a ring of film.  The award was initially and is still sometimes loosely referred to as a \"Golden Scroll\".  The award for Best Actor was first introduced in 1976 for the 1974 and 1975 years, to reward a lead performance by a male actor in film.\n\nMohammad-Reza Foroutan: Mohammad-Reza Foroutan (Persian: محمد رضا فروتن‎ ‎ , born December 28, 1968 in Tehran, Iran) is an Iranian actor.  He graduated with a master's degree in clinical psychology from Azad University and now is a Ph.D candidate of Health Psychology.  He has passed some free courses in acting.  His first film was \"Goal\".  After some minor roles his performance in an episode of TV series \"The Clue\" revealed his capabilities and Masoud Kimiay chose him for the leading role of Mercedes.  He has been acting as actor for more than two decades and received several awards including best male actor award for acting in Germez 1999 Fajr International Film Festival and best male actor award for acting in  Be Ahestegi  Fajr International Film Festival 2005.\n\nProducers Guild Film Award for Best Male Debut: The Producers Guild Film Award for Best Male Debut (previously known as the Apsara Award for Best Male Debut) is given by the producers of the film and television guild as part of its annual award ceremony for Hindi films, to recognise a male actor who has delivered an outstanding performance in his debut film.  While the official awards ceremony started in 2004, awards for the best male debut commenced four years later.\n\nQuestion: What other male actor did Barry Keoghan co-star with the 2017 horror film The Killing of a Sacred Deer?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film in question.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"actor_in_question\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actor whose co-stars are being sought.\"\n        }\n      },\n      \"required\": [\n        \"name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"co_star_actors\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of a co-star actor.\"\n          },\n          \"gender\": {\n            \"type\": \"string\",\n            \"enum\": [\n              \"male\",\n              \"female\"\n            ],\n            \"description\": \"The gender of the co-star actor.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"gender\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"description\": \"A list of other actors who co-starred in the film with the actor in question.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"genre\",\n    \"actor_in_question\",\n    \"co_star_actors\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film in question."
      },
      "release_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "genre": {
        "type": "string",
        "description": "The genre of the film."
      },
      "actor_in_question": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actor whose co-stars are being sought."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      },
      "co_star_actors": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of a co-star actor."
            },
            "gender": {
              "type": "string",
              "enum": [
                "male",
                "female"
              ],
              "description": "The gender of the co-star actor."
            }
          },
          "required": [
            "name",
            "gender"
          ],
          "additionalProperties": false
        },
        "description": "A list of other actors who co-starred in the film with the actor in question."
      }
    },
    "required": [
      "film_title",
      "release_year",
      "genre",
      "actor_in_question",
      "co_star_actors"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
