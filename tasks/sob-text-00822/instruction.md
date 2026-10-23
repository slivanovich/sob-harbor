{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJill Eikenberry: Jill Susan Eikenberry (born January 21, 1947) is an American film, stage, and television actress.  She is known for her role as lawyer Ann Kelsey on the NBC drama \"L.A. Law\" (1986–94), for which she is a five-time Emmy Award and four-time Golden Globe Award nominee, winning the Golden Globe for Best Actress in a Drama Series in 1989.  She received an Obie Award in 1986 for the Off-Broadway plays \"Lemon Sky\" and \"Life Under Water\", and was nominated for a 2011 Drama Desk Award for the Off-Broadway musical \"The Kid\".  Her film appearances include \"Hide in Plain Sight\" (1980), \"Arthur\" (1981) and \"The Manhattan Project\" (1986).\n\nFarrah Fawcett: Farrah Fawcett (born Ferrah Leni Fawcett; February 2, 1947 – June 25, 2009) was an American actress, model, and artist.  A four-time Emmy Award nominee and six-time Golden Globe Award nominee, Fawcett rose to international fame when she posed for her iconic red swimsuit poster – which became the best selling pin-up poster in history – and starred as private investigator Jill Munroe in the first season of the television series \"Charlie's Angels\" (1976–1977).  In 1996, she was ranked No. 26 on \"TV Guide\"'s \"50 Greatest TV stars of All-Time\".\n\n1408 (film): 1408 is a 2007 American psychological horror film based on Stephen King's 1999 short story of the same name.  It is directed by Swedish director Mikael Håfström and stars John Cusack, Samuel L. Jackson, Mary McCormack, Tony Shalhoub, Len Cariou, Isiah Whitlock, Jr., and Jasmine Jessica Anthony.  The film was released in the United States on June 22, 2007, although July 13 (which in 2007 fell on a Friday) is mentioned as the release date on the website.\n\nJohn Cusack: John Paul Cusack ( ; born June 28, 1966) is an American actor, producer and screenwriter.  He began acting on films during the 1980s.  Cusack was nominated for a Golden Globe Award for Best Actor – Motion Picture Musical or Comedy for his performance in \"High Fidelity\" (2000).  Other films including \"Grosse Pointe Blank\" (1997), \"Being John Malkovich\" (1999), \"1408\" (2007), \"2012\" (2009), \"Hot Tub Time Machine\" (2010), and \"The Raven\" (2012).\n\nSusan Dey: Susan Hallock Dey (born December 10, 1952) is an American actress, known for her television roles as Laurie Partridge on the sitcom \"The Partridge Family\" from 1970 to 1974, and as Grace Van Owen on the NBC drama series \"L.A. Law\" from 1986 to 1992.  A three-time Emmy Award nominee and six-time Golden Globe Award nominee, she won the Golden Globe for Best Actress in a Drama Series for \"L.A. Law\" in 1988.\n\nHigh Fidelity HDTV: High Fidelity HDTV was a Canadian licensed television broadcaster specializing in HD content.  The company was founded in 2003 by co-founders John Panikkar and Ken Murphy, both of whom have been involved in the Canadian broadcasting industry for many years.  David Patterson, an experienced Canadian senior broadcast executive, joined the company in 2005 as a partner and part owner of the company, and Frank Bertolas, also an experienced Canadian senior broadcast executive, joined the company in 2010.  High Fidelity HDTV was headquartered in Toronto, Ontario and it operated 4 HD channels.  In 2006, the company was set to launch a 5th HD channel, Baby HD.  In 2007, the company was poised to launch more HD channels: Aqua HD, Centre Stage HD, Clash HD, Crafts & Hobbies HD, Eureka!  HD, GameWorld HD, Seniors Life HD, Women's Sports HD, Horror HD, & W HD.  In 2008, the company proposed 2 more HD channels, Diversion HD & Canada HD, as well as a non-HD network, Diversion.  However, the applications for the channels was denied by the Canadian Radio-television and Telecommunications Commission (CRTC).  In 2010, the company was set to launch yet another channel (non-HD), The Wedding Channel.\n\nGolden Globe Award for Best Animated Feature Film: The Golden Globe Award for Best Animated Feature Film was awarded for the first time at the 64th Golden Globe Awards in 2007.  It was the first time that the Golden Globe Awards had created a separate category for animated films since its establishment.  The nominations are announced in January and an awards ceremony is held later in the month.  Initially, only three films are nominated for best animated film, in contrast to five nominations for the majority of other awards.  The Pixar film \"Cars\" was the first recipient of the award.  The award for best animated film has subsequently been presented to six other Pixar films: \"Ratatouille\" received the award in 2008, \"WALL-E\" was the recipient in 2009, \"Up\" received the award in 2010, \"Toy Story 3\" won in 2011, \"Brave\" won in 2013, and \"Inside Out\" won in 2016.  In 2012, \"Cars 2\" lost to \"The Adventures of Tintin\", in 2014, \"Monsters University\" was the first not to be nominated and also in 2016, \"The Good Dinosaur\" lost to \"Inside Out\".  In 2017, \"Finding Dory\" was also not nominated.  The Hollywood Foreign Press Association has been awarding Golden Globe Awards since 1944.\n\nKate Jackson: Lucy Kate Jackson (born October 29, 1948) is an American actress, director and producer, known for her television roles as Sabrina Duncan in the 1970s series \"Charlie's Angels\" (1976–79) and Amanda King in the 1980s series \"Scarecrow and Mrs. King\" (1983–87).  Her film roles include \"Making Love\" (1982) and \"Loverboy\" (1989).  She is a three-time Emmy Award nominee and four-time Golden Globe Award nominee.\n\nHenry Kloss: Henry Kloss (1929, Altoona, Pennsylvania – January 31, 2002, Cambridge, Massachusetts) was a prominent American audio engineer and entrepreneur who helped advance high fidelity loudspeaker and radio receiver technology beginning in the 1950s.  Kloss (pronounced with a long o, like \"close\") was an undergraduate student in physics at the Massachusetts Institute of Technology (class of 1953), but never received a degree.  He was responsible for a number of innovations, including, in part, the acoustic suspension loudspeaker, and the high fidelity cassette deck.  In 2000, Kloss was one of the first inductees into the Consumer Electronics Association's Hall of Fame.  He earned an Emmy Award for his development of a projection television system, the Advent VideoBeam 1000.\n\nLesley Ann Warren: Lesley Ann Warren (born August 16, 1946) is an American actress and singer.  She was nominated for the Academy Award for Best Supporting Actress for the 1982 film \"Victor/Victoria\".  She is also an Emmy Award nominee and five-time Golden Globe Award nominee, winning the Golden Globe for Best Actress in a Drama Series for the 1977 NBC miniseries \"Harold Robbins' 79 Park Avenue\".\n\nQuestion: What 2007 American psychological horror film did a Golden Globe Award nominee for High Fidelity star in?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"film_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"film_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"starring_actor\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actor who starred in the film.\"\n        },\n        \"golden_globe_nomination_for_high_fidelity\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"year\": {\n              \"type\": \"integer\",\n              \"description\": \"The year of the Golden Globe nomination for 'High Fidelity'.\"\n            },\n            \"category\": {\n              \"type\": \"string\",\n              \"description\": \"The category of the Golden Globe nomination for 'High Fidelity'.\"\n            }\n          },\n          \"required\": [\n            \"year\",\n            \"category\"\n          ],\n          \"additionalProperties\": false\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"golden_globe_nomination_for_high_fidelity\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_year\",\n    \"film_genre\",\n    \"starring_actor\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "film_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "film_genre": {
        "type": "string",
        "description": "The genre of the film."
      },
      "starring_actor": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actor who starred in the film."
          },
          "golden_globe_nomination_for_high_fidelity": {
            "type": "object",
            "properties": {
              "year": {
                "type": "integer",
                "description": "The year of the Golden Globe nomination for 'High Fidelity'."
              },
              "category": {
                "type": "string",
                "description": "The category of the Golden Globe nomination for 'High Fidelity'."
              }
            },
            "required": [
              "year",
              "category"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "name",
          "golden_globe_nomination_for_high_fidelity"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "film_year",
      "film_genre",
      "starring_actor"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
