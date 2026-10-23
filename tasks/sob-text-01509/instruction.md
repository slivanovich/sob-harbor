{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGolu Hadawatha: Golu Hadawatha (Translation: Silence of the Heart) was a popular 1968 Sinhalese language romance movie directed by Maestro Lester James Peiris.  Wickrema Bogoda and Anula Karunathilake act the lead roles of Sugath (Sugath Weerasekera) and Dhammhi (Dhamayanthi Kariyawasam).  The movie's story is built on the novel Golu Hadawatha written by Karunasena Jayalath in 1962, based on his school time experiences and memories.  Regi Siriwardena wrote the screenplay and Veteran Sinhala musician Premasiri Khemadasa composed the music.  Golu Hadawatha is acclaimed as a movie that set a milestone in Sinhala moviemaking.  It introduced a new cinematic format to the romance and love movie genre.  The movie departs from the then traditional movie style; no hero, heroine,(\"Boy\" and \"Girl\") no enemy or villain, Joker, no songs, and fights etc.  Based on a romantic and emotional attachment between a teenage boy and a girl who study in the same class of their school, Golu Hadawatha is regarded as one of the landmarks in Sri Lankan Cinema.\n\nTomb Raider (2018 film): Tomb Raider is an upcoming 2018 American action adventure film directed by Roar Uthaug and written by Geneva Robertson-Dworet and Alastair Siddons.  It is based on the 2013 video game of the same name by Crystal Dynamics.  The film stars Alicia Vikander, Walton Goggins, Daniel Wu, and Dominic West.\n\nThe Line of Freedom (film): The Line of Freedom is a 2013 political drama film directed and produced by David Whitney and starring Antonio Aakeel.  The film had its world premiere at the Dubai International Film Festival in 2013.  It was instantly banned in Pakistan due to the controversial depiction of its security forces and subsequently contributed to a national ban of the Internet Movie Database.  The film has sparked a backlash from some titling it \"anti-state propaganda\" and resulted in its star Antonio Aakeel allegedly receiving death threats.\n\nHecho en China: \"Hecho en China \" (literally: Made In China) is a 2012 Mexican road movie directed and written by Gabriel Guzmán Sánchez, and starring Odiseo Bichir.  It is produced by Alejandra Garcia and Antonio Urdapilleta for IMAGYX Entertainment, Canal 22 and IMCINE.  It was filmed in Mexico and first released on March 7, 2012 at the Guadalajara International Film Festival.\n\nEaten by Lions (film): Eaten by Lions is a British comedy feature film written and directed by Jason Wingard.  The film stars Antonio Aakeel, Jack Carroll, Johnny Vegas, and Asim Chaudhry.  The Film is the feature-length adaptation of the director's 2013 short film 'Going to Mecca' which won best comedy at the Manchester International Film Festival.  The feature follows half-brothers Omar and Pete as they embark on a journey to find Omar's estranged father, confronting him on the day of his daughters engagement party.\n\nThe Contract (2015 film): The Contract (previously known as \"Squat\" is a 2016 British crime thriller feature film directed by Nic Auerbach.  The Contract is a nascent love story of two people from polar opposite worlds, thrown together by circumstance.  The film stars Robert Fucilla, Sarah Armstrong, Danny Webb, Patrick Ryecart, Antonio Aakeel, and Jack Brady.  The Film was released on DVD and online January 18, 2016.\n\nSapne Sajan Ke: Sapne Saajan Ke is 1992 Hindi language movie directed by Lawrence D'Souza and starring Karishma Kapoor, Rahul Roy, and Jackie Shroff.  The movie was a collaboration of director Lawrence D'Souza and producer Sudhakar Bokade after their blockbuster movie Saajan.  However, the movie was average earner at box office.  Actor Aditya Pancholi used his voice to promote the movie as another movie after super success of movie Saajan\n\nCity of Tiny Lights: City of Tiny Lights is a British crime thriller film directed by Pete Travis and written by Patrick Neate, based on his own 2005 novel of same name.  The film stars Riz Ahmed, James Floyd, Billie Piper, Cush Jumbo, Roshan Seth and Antonio Aakeel.  Principal photography began on 27 April 2015 in London.  It was screened in the Special Presentations section at the 2016 Toronto International Film Festival and was released in the United Kingdom on 7 April 2017.\n\nThe Dragon, the Hero: The Dragon, The Hero is a Hong Kong martial art movie directed by Godfrey Ho and starring Philip Ko,Dragon Lee, Tino Wong Cheung and Liu Chung-Liang.  The movie is considered as one of the best martial arts movie that Godfrey Ho directed outside of the martial arts movie fanbase.  The movie is also known as Dragon on Fire.\n\nAntonio Aakeel: Antonio Aakeel is an English actor.  He is best known for appearing in \"Skins\", \"City of Tiny Lights\" and BBC One's mini-series \"Three Girls\".  He stars in the upcoming feature films \"Eaten by Lions\", \"Tomb Raider\" and \"The Hungry\".\n\nQuestion: When will Antonio Aakeel apear in a movie directed by Roar Ulthaug?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"movie_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the movie.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the movie.\"\n    },\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the movie's director.\"\n    },\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor in question.\"\n    }\n  },\n  \"required\": [\n    \"movie_title\",\n    \"release_year\",\n    \"director_name\",\n    \"actor_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "movie_title": {
        "type": "string",
        "description": "The title of the movie."
      },
      "release_year": {
        "type": "integer",
        "description": "The release year of the movie."
      },
      "director_name": {
        "type": "string",
        "description": "The name of the movie's director."
      },
      "actor_name": {
        "type": "string",
        "description": "The name of the actor in question."
      }
    },
    "required": [
      "movie_title",
      "release_year",
      "director_name",
      "actor_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
