{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSky and Sand: Sky and Sand is a song by German electronic music producers Paul Kalkbrenner and Fritz Kalkbrenner.  The song was originally produced as the title song of the German movie Berlin Calling written and directed by Hannes Stöhr .  It was first released on the Berlin Calling movie soundtrack album in October 2008 and in February 2009 as a single.\n\nSapne Sajan Ke: Sapne Saajan Ke is 1992 Hindi language movie directed by Lawrence D'Souza and starring Karishma Kapoor, Rahul Roy, and Jackie Shroff.  The movie was a collaboration of director Lawrence D'Souza and producer Sudhakar Bokade after their blockbuster movie Saajan.  However, the movie was average earner at box office.  Actor Aditya Pancholi used his voice to promote the movie as another movie after super success of movie Saajan\n\nGolu Hadawatha: Golu Hadawatha (Translation: Silence of the Heart) was a popular 1968 Sinhalese language romance movie directed by Maestro Lester James Peiris.  Wickrema Bogoda and Anula Karunathilake act the lead roles of Sugath (Sugath Weerasekera) and Dhammhi (Dhamayanthi Kariyawasam).  The movie's story is built on the novel Golu Hadawatha written by Karunasena Jayalath in 1962, based on his school time experiences and memories.  Regi Siriwardena wrote the screenplay and Veteran Sinhala musician Premasiri Khemadasa composed the music.  Golu Hadawatha is acclaimed as a movie that set a milestone in Sinhala moviemaking.  It introduced a new cinematic format to the romance and love movie genre.  The movie departs from the then traditional movie style; no hero, heroine,(\"Boy\" and \"Girl\") no enemy or villain, Joker, no songs, and fights etc.  Based on a romantic and emotional attachment between a teenage boy and a girl who study in the same class of their school, Golu Hadawatha is regarded as one of the landmarks in Sri Lankan Cinema.\n\nHannes Stöhr: Hannes Stöhr (born 1970) is a German film director and screenwriter.  He studied Scriptwriting and Directing at the \"Deutsche Film- und Fernsehakademie Berlin\" from 1994 to 1999.  In 2006 Stöhr was a Villa Aurora grant recipient and lived for six months in Los Angeles, California.  Hannes speaks German, Spanish, English, French and Portuguese.  Stöhr is member of the European Filmacademy, lectures film at \"Film Academy Baden-Württemberg\", \"Deutsche Film- und Fernsehakademie Berlin\" and the Goethe Institute.  He lives in Berlin.\n\nThe Dragon, the Hero: The Dragon, The Hero is a Hong Kong martial art movie directed by Godfrey Ho and starring Philip Ko,Dragon Lee, Tino Wong Cheung and Liu Chung-Liang.  The movie is considered as one of the best martial arts movie that Godfrey Ho directed outside of the martial arts movie fanbase.  The movie is also known as Dragon on Fire.\n\nPaul Kalkbrenner: Paul Kalkbrenner (] ) (born 11 June 1977) is a German live act, producer of electronic music, and actor from Berlin.  Because he breaks down his tracks into elements that are reassembled onstage, Kalkbrenner is considered a live act, as opposed to a DJ.  He is most known for his single “Sky and Sand,” which sold over 200,000 copies, went platinum, and was highly charted in countries such as Belgium and Germany.  He is also known for portraying the main character Ickarus in the movie, “Berlin Calling” written and directed by Hannes Stöhr, which ran for several years at Kino Central in Berlin.\n\nBerlin Calling: Berlin Calling is a 2008 German tragicomedy directed by Hannes Stöhr.  The movie depicts the events following DJ and producer Ickarus's (Paul Kalkbrenner) institutionalization for drug abuse.\n\nBerlin is in Germany: Berlin is in Germany is a 2001 German drama film directed by Hannes Stöhr.  Hannes Stöhr's first cinema feature, the film won the Panorama Audience award at the International Berlin Filmfestival 2001, the German critics association award, the Studio Hamburg award, and many others.\n\nOne Day in Europe: One Day in Europe is a 2005 film directed by Hannes Stöhr.  The film was nominated for Golden Bear award at the 2005 Berlin Film Festival.\n\nPhaansi: Phaansi is a 1978 Hindi movie directed by Harmesh Malhotra.  The film stars Shashi Kapoor, Sulakshana Pandit, Pran and Ranjeet.  The film's music is by Laxmikant Pyarelal.  Actor Asrani has also played a role as a Muslim guy in the movie who was a closed friend to Shashi Kapoor and actor Iftikar played role as father to Shahsi Kapoor.  Unfortunately, both of them was hanged to death by the villain (Ranjeet).  Thumbs up for Ranjeet of acting the role of Chief of Daku in the movie.The movie was declared hits due to its story line, drama, songs and good action.  A worth to watch movie of the 1970s.\n\nQuestion: What is the name of a single by an actor who was in a movie directed by Hannes Stöhr?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"single_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the single.\"\n    },\n    \"single_artists\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The artists who produced the single.\"\n    },\n    \"single_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the single was released.\"\n    },\n    \"actor_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"actor_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actor who released the single.\"\n        },\n        \"acted_in_movie\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the movie the actor was in.\"\n        },\n        \"movie_director\": {\n          \"type\": \"string\",\n          \"description\": \"The director of the movie the actor was in.\"\n        }\n      },\n      \"required\": [\n        \"actor_name\",\n        \"acted_in_movie\",\n        \"movie_director\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"single_name\",\n    \"single_artists\",\n    \"single_release_year\",\n    \"actor_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "single_name": {
        "type": "string",
        "description": "The name of the single."
      },
      "single_artists": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The artists who produced the single."
      },
      "single_release_year": {
        "type": "integer",
        "description": "The year the single was released."
      },
      "actor_details": {
        "type": "object",
        "properties": {
          "actor_name": {
            "type": "string",
            "description": "The name of the actor who released the single."
          },
          "acted_in_movie": {
            "type": "string",
            "description": "The name of the movie the actor was in."
          },
          "movie_director": {
            "type": "string",
            "description": "The director of the movie the actor was in."
          }
        },
        "required": [
          "actor_name",
          "acted_in_movie",
          "movie_director"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "single_name",
      "single_artists",
      "single_release_year",
      "actor_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
