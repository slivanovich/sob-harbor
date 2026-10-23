{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFionn Whitehead: Fionn Whitehead (born 1996/1997 ) is an English actor whose first major role was as the protagonist in \"Dunkirk\", the 2017 war film directed by Christopher Nolan.  Whitehead first acted in the 2016 ITV miniseries \"Him\".\n\nDunkirk (2017 film): Dunkirk is a 2017 war film written, co-produced, and directed by Christopher Nolan that portrays the Dunkirk evacuation of the Second World War.  Its ensemble cast includes Fionn Whitehead, Tom Glynn-Carney, Jack Lowden, Harry Styles, Aneurin Barnard, James D'Arcy, Barry Keoghan, Kenneth Branagh, Cillian Murphy, Mark Rylance, and Tom Hardy.  Distributed by Warner Bros.  Pictures, the film is a co-production between the United Kingdom, the United States, France, and the Netherlands.\n\nScooby-Doo! Curse of the Lake Monster: Scooby-Doo!  Curse of the Lake Monster is a 2010 television supernatural comedy film directed by Brian Levant for Cartoon Network and based on the Saturday morning cartoon series \"Scooby-Doo\" by Hanna-Barbera.  It is the fourth installment in the \"Scooby-Doo\" live-action film series and a sequel to the 2009 film \"Scooby-Doo!  The Mystery Begins\", whose cast reprise their roles again here.  The film was shot in Santa Clarita, California and Sherwood Country Club in Thousand Oaks, California and premiered on October 16, 2010.\n\nTera Mera Ki Rishta: Tera Mera Ki Rishta is a Punjabi film, starring Jimmy Shergill and Kulraj Randhawa in the main lead.  Rest of the cast includes Anupam Kher, Raj Babbar, Archana Puran Singh, Gurpreet Ghuggi, Binnu Dhillon, Rana Ranbir, Balkaran Brar, Tee Jay Sidhu, Dolly Minhas and Akshita.  The Movie was released worldwide on 10 April 2009 and had earned $108,741 in first two weeks.  The movie was shot by Spice Cine Vision Studios and was distributed by Eros International.  The movie was stated to be the costliest Punjabi movie ever made and was the first Punjabi movie to be shot in Switzerland.  Tera Mera Ki Rishta was also the first Punjabi Movie to be promoted online by www.punjabiportal.com and an official movie launch center website was also introduced.  This movie is the remake of super hit Telugu movie Nuvvostanante Nenoddantana\n\nMorley Safer: Morley Safer (November 8, 1931 – May 19, 2016) was a Canadian-American broadcast journalist, reporter, and correspondent for CBS News.  He was best known for his long tenure on the news magazine \"60 Minutes\", whose cast he joined in 1970 after its second year on television.  He was the longest-serving reporter on \"60 Minutes\", the most watched and most profitable program in television history.\n\nThe Green Hand: The Green Hand is a 1940 short film about a young man whose path to juvenile delinquency is rerouted through his participation in the Future Farmers of America.  The film was based on the 1932 novel by Paul W. Chapman, an agriculture professor at the University of Georgia.  Chapman appeared in the film version, whose cast consisted of students and faculty from the University of Georgia and the surrounding city of Athens, Georgia.\n\nThe Stunt Man: The Stunt Man is a 1980 American film directed by Richard Rush, starring Peter O'Toole, Steve Railsback, and Barbara Hershey.  The movie was adapted by Lawrence B. Marcus and Rush from the 1970 novel of the same name by Paul Brodeur.  It tells the story of a young fugitive who hides as a stunt double on the set of an anti-war movie whose charismatic director will do seemingly anything for the sake of his art.\n\nKen Pierce: Ken Pierce is an American performer, teacher and historian of Renaissance and Baroque dance.  He trained in ballet and modern dance at the American Ballet Theatre School and the Merce Cunningham studio.  He has performed with the Court Dance Company of New York, the New York Baroque Dance Company, and Ris et Danceries (Paris).  He directs the Ken Pierce Baroque Dance Company, collaborating with Tafelmusik, Portland Baroque Orchestra, Concerto Copenhagen, The King's Noyse, and the Boston Early Music Festival.  He was assistant choreographer for \"Quelques pas graves de Baptiste\", Francine Lancelot's baroque-style piece for the Paris Opera Ballet, whose cast included Rudolph Nureyev.  Mr. Pierce directs the early dance program at the Longy School of Music in Cambridge, Massachusetts.\n\nEducational film: An educational film is a film or movie whose primary purpose is to educate.  Educational films have been used in classrooms as an alternative to other teaching methods.\n\nFour on a Garden: Four on a Garden is a set of four One-act plays that were presented on Broadway at the Broadhurst Theatre from January 30, 1971, until March 20, 1971.  The set included \"House of Dunkelmayer\", \"Betty\", \"Toreador\", and \"The Swingers\".  The four plays were originally written by French playwrights Pierre Barillet and Jean-Pierre Gredy but were adapted into English by Abe Burrows.  Burrows directed the show whose cast included Sid Caesar, Carol Channing, Tommy Lee Jones, and George S. Irving.\n\nQuestion: Who distributed a movie whose cast includes an actor who acted in \"Him\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"distributor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film distributor.\"\n    },\n    \"film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film distributed.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the film.\"\n        },\n        \"director\": {\n          \"type\": \"string\",\n          \"description\": \"The director of the film.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\",\n        \"director\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"actor_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actor who acted in 'Him'.\"\n        },\n        \"acted_in_him_miniseries\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the actor acted in the 'Him' miniseries.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"acted_in_him_miniseries\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"distributor_name\",\n    \"film_details\",\n    \"actor_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "distributor_name": {
        "type": "string",
        "description": "The name of the film distributor."
      },
      "film_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film distributed."
          },
          "release_year": {
            "type": "integer",
            "description": "The release year of the film."
          },
          "director": {
            "type": "string",
            "description": "The director of the film."
          }
        },
        "required": [
          "title",
          "release_year",
          "director"
        ],
        "additionalProperties": false
      },
      "actor_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actor who acted in 'Him'."
          },
          "acted_in_him_miniseries": {
            "type": "boolean",
            "description": "Indicates if the actor acted in the 'Him' miniseries."
          }
        },
        "required": [
          "name",
          "acted_in_him_miniseries"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "distributor_name",
      "film_details",
      "actor_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
