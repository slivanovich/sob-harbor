{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFlight of the Conchords discography: The discography of Flight of the Conchords, a New Zealand-based comedy band, consists of two studio albums, one live album, two compilation albums, one extended play (EP) and seven singles. Jemaine Clement and Bret McKenzie formed Flight of the Conchords in Wellington in 1998.  Their first release was the live album \"Folk the World Tour\", which the duo self-released in 2002.  In 2006, the band signed with American independent label Sub Pop; they released the EP \"The Distant Future\" the following year, which reached number eight in New Zealand.\n\nTongan Ninja: Tongan Ninja is a 2002 kung-fu action-comedy film directed by Jason Stutter and filmed in New Zealand.  The film has received recent notoriety for co-starring and being co-written by Jemaine Clement, star of the HBO comedy \"Flight of the Conchords\".  The movie is a parody of English-dubbed martial arts films, with a few other popular films and the plot is taken from \"Way of the Dragon\".  It also features songs written by Jemaine Clement and Bret McKenzie - also from the Flight of the Conchords.\n\nSex Tape (film): Sex Tape is a 2014 American comedy film directed by Jake Kasdan and written by Kate Angelo, Jason Segel, and Nicholas Stoller.  Starring Segel, Cameron Diaz, Rob Corddry, Ellie Kemper, and Rob Lowe, the film was released on July 18, 2014, by Columbia Pictures.\n\nJemaine Clement: Jemaine Clement (born 10 January 1974) is a New Zealand comedian, actor, voice actor, singer, writer, director, and multi-instrumentalist, best known as one half of the musical comedy duo Flight of the Conchords along with Bret McKenzie.  They have released multiple albums, created a BBC radio series and a HBO American television series that aired for two seasons.\n\nSally (Flight of the Conchords): \"Sally\" is the pilot episode of the American television sitcom \"Flight of the Conchords\".  It first aired on HBO on June 17, 2007.  In this episode, New Zealanders Jemaine Clement and Bret McKenzie of the band Flight of the Conchords have moved to New York City to try to make it in the United States.  At a party, Jemaine falls for, and subsequently begins dating, Sally—Bret's former girlfriend.  As Jemaine's attentions focus on Sally, a lonely Bret is forced to deal with the advances of Mel (Kristen Schaal), the band's obsessed—and only—fan.  Meanwhile, Murray (Rhys Darby), the band's manager, helps the band film their first music video, although they cannot afford decent costumes or proper video equipment.\n\nUnnatural Love: \"Unnatural Love\" is the fifth episode of the second season of the HBO comedy series \"Flight of the Conchords\", and the seventeenth episode overall.  It first aired on February 15, 2009.  The episode was directed by Michel Gondry and written by Iain Morris and Damon Beesley.  Jemaine Clement and Bret McKenzie of the band Flight of the Conchords star as fictional versions of themselves.  The plot focuses on Jemaine's forbidden romance with the Australian Keitha (Sarah Wynter), which chagrins his fellow New Zealanders Bret and Murray (Rhys Darby), the band's manager.\n\nBret McKenzie: Bret Peter Tarrant McKenzie, ONZM (born 29 June 1976) is a New Zealand comedian, actor, musician and producer, best known for being one half of the Grammy Award-winning musical comedy duo Flight of the Conchords along with Jemaine Clement.  The duo's comedy and music became the basis of a BBC radio series and then an oft-lauded American television series, which aired for two seasons on HBO.  McKenzie served as music supervisor for two Muppet films, \"The Muppets \"(2011) and \"Muppets Most Wanted \"(2014), the former of which won him an Academy Award for Best Original Song for the song \"Man or Muppet\".  His latest work has seen him write the lyrics to the 2016 Sainsburys Christmas advert featuring James Corden on vocals.\n\nForgetting Sarah Marshall: Forgetting Sarah Marshall is a 2008 American romantic comedy-drama film directed by Nicholas Stoller and starring Jason Segel, Kristen Bell, Mila Kunis and Russell Brand.  The film, which was written by Segel and co-produced by Judd Apatow, was released by Universal Studios.  Filming began in April 2007 at the Turtle Bay Resort on the North Shore of Oahu Island in Hawaii.  The film was released for North American theaters on April 18, 2008 and in the UK a week later on April 25, 2008.\n\nThe Muppets (film): The Muppets is a 2011 American musical comedy film and the seventh theatrical film featuring the Muppets.  The film is directed by James Bobin, written by Jason Segel and Nicholas Stoller, produced by David Hoberman and Todd Lieberman, and stars Segel, Amy Adams, Chris Cooper and Rashida Jones, as well as Muppet performers Steve Whitmire, Eric Jacobson, Dave Goelz, Bill Barretta, David Rudman, Matt Vogel, and Peter Linz.  Bret McKenzie served as music supervisor, writing four of the film's five original songs, and Christophe Beck composed the film's score.  In \"The Muppets\", devoted fan Walter, his brother Gary, and Gary's girlfriend Mary help Kermit the Frog reunite the disbanded Muppets, as they must raise $10 million to save the Muppet Theater from Tex Richman, a businessman who plans to demolish the studio to drill for oil.\n\nFlight of the Conchords (TV series): Flight of the Conchords is a British-American-New Zealand television comedy series that was first shown on HBO on June 17, 2007.  The show follows the adventures of Flight of the Conchords, a two-man band from New Zealand, as its members seek fame and success in New York City.  The show stars the real-life duo of Jemaine Clement and Bret McKenzie, who play fictionalized versions of themselves.  A second season was announced on August 17, 2007 and shown from January 18, 2009.  On December 11, 2009, the duo confirmed that the series would not return for a third season.\n\nQuestion: This New Zealand comedian, actor, musician and producer best known for the Flight of the Conchords along with Jemaine Clement contributed to this film written by Jason Segel and Nicholas Stoller and starring Amy Adams, which is directed by whom?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"film_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"film_director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"film_writers\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of writers for the film.\"\n    },\n    \"film_starring_actors\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of key actors starring in the film.\"\n    },\n    \"contributor_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the contributor.\"\n        },\n        \"role_in_film\": {\n          \"type\": \"string\",\n          \"description\": \"The specific role of the contributor in the film.\"\n        },\n        \"known_for_band\": {\n          \"type\": \"string\",\n          \"description\": \"The band the contributor is best known for.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role_in_film\",\n        \"known_for_band\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_release_year\",\n    \"film_director\",\n    \"film_writers\",\n    \"film_starring_actors\",\n    \"contributor_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "film_release_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "film_director": {
        "type": "string",
        "description": "The director of the film."
      },
      "film_writers": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of writers for the film."
      },
      "film_starring_actors": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of key actors starring in the film."
      },
      "contributor_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the contributor."
          },
          "role_in_film": {
            "type": "string",
            "description": "The specific role of the contributor in the film."
          },
          "known_for_band": {
            "type": "string",
            "description": "The band the contributor is best known for."
          }
        },
        "required": [
          "name",
          "role_in_film",
          "known_for_band"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "film_release_year",
      "film_director",
      "film_writers",
      "film_starring_actors",
      "contributor_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
