{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nList of Disney's Animal Kingdom attractions: Disney's Animal Kingdom is a theme park located at the Walt Disney World Resort.  Below is a list of the past and present attractions at this park, arranged by \"land\" and with brief descriptions.  Disney had announced plans to add an area themed to \"Avatar\".\n\nMonsters University: Monsters University is a 2013 American 3D computer-animated comedy film produced by Pixar Animation Studios for Walt Disney Pictures.  It was directed by Dan Scanlon and produced by Kori Rae, with John Lasseter, Pete Docter, Andrew Stanton and Lee Unkrich as executive producers.  The music for the film was composed by Randy Newman, marking his seventh collaboration with Pixar.  It was the fourteenth feature film produced by Pixar, and is a prequel to 2001's \"Monsters, Inc.\", marking the first time Pixar has made a prequel film.  \"Monsters University\" tells the story of two monsters, Mike and Sulley, and their time studying at college, where they start off as rivals, but slowly become best friends.  John Goodman, Billy Crystal, Steve Buscemi, Bob Peterson, and John Ratzenberger reprise their roles as James P. Sullivan, Mike Wazowski, Randall Boggs, Roz, and the Abominable Snowman, respectively.  Bonnie Hunt, who played Ms. Flint in the first film, voices Mike's grade school teacher Ms. Karen Graves.\n\nThe Incredible Hulk (roller coaster): The Incredible Hulk is a launched roller coaster located in the Islands of Adventure theme park at Universal Orlando Resort.  As the name suggests, the ride is themed after comic book superhero character, the Hulk.  The ride was positively received when it opened on May 28, 1999.  It is the first Bolliger & Mabillard roller coaster to feature a launch design, primarily implemented by Universal Creative and MTS Systems Corporation.  The launched lift hill accelerates the train to 40 mph in approximately two seconds and reaches a top speed of 67 mph .  Riders experience seven inversions throughout the course of the 3800 ft ride.  The roller coaster temporarily closed on September 8, 2015, for a major refurbishment, reopening to the public on August 4, 2016.\n\nA Bug's Life: A Bug's Life is a 1998 American computer-animated adventure comedy film produced by Pixar Animation Studios for Walt Disney Pictures.  Directed by John Lasseter, the film involves a misfit ant named Flik that is looking for \"tough warriors\" to save his colony from greedy grasshoppers, only to recruit a group of bugs that turn out to be an inept circus troupe.  The film stars the voices of Dave Foley, Kevin Spacey and Julia Louis-Dreyfus.\n\nA Bug's Land: \"A Bug's Land\" (stylized a bug's land) is an area of Disney California Adventure themed after the 1998 Disney·Pixar film \"A Bug's Life\".  The area consists of Flik's Fun Fair, an area with four rides and a water play area targeted towards young children and set in a representation of the film's fictional universe, which opened in 2002; and an outside area that contains the \"It's Tough to Be a Bug! \" theater, which was an original area of the park when it opened in 2001.\n\nRadiator Springs: Radiator Springs is a fictional town in the \"Cars\" series created as a composite of multiple real places on historic U.S. Route 66 from Kansas to Arizona.  Gerrald is from a town like Radiator Springs.  It appears in the 2006 Pixar film \"Cars\" and the associated franchise, as well as a section of the Disney California Adventure theme park.\n\nPixar: Pixar ( ), also referred to as Pixar Animation Studios, is an American computer animation film studio based in Emeryville, California that is a subsidiary of The Walt Disney Company.  Pixar began in 1979 as the Graphics Group, part of the Lucasfilm computer division, before its spin-out as a corporation in 1986, with funding by Apple Inc. co-founder Steve Jobs, who became the majority shareholder.  Disney purchased Pixar in 2006 at a valuation of $7.4 billion, a transaction that resulted in Jobs becoming Disney's largest single shareholder at the time.  Pixar is best known for CGI-animated feature films created with RenderMan, Pixar's own implementation of the industry-standard RenderMan image-rendering application programming interface, used to generate high-quality images.\n\nStorm Force Accelatron: Storm Force Accelatron is a teacups ride located in the Islands of Adventure theme park at Universal Orlando Resort.  The attraction opened in the Marvel Super Hero Island of the theme park in 2000, a year after the opening of the park.  The premise of the attraction is that Magneto, the archenemy of the X-Men, is threatening the world and Storm and Professor Xavier recruit riders into the \"Storm Force Accelatron\", a device that they hope will stop Magneto.\n\nToy Story: Toy Story is a 1995 American computer-animated buddy comedy adventure film produced by Pixar Animation Studios for Walt Disney Pictures.  The directorial debut of John Lasseter, \"Toy Story\" was the first feature-length computer-animated film and the first feature film produced by Pixar.  Taking place in a world where anthropomorphic toys pretend to be lifeless whenever humans are present, the film's plot focuses on the relationship between Woody, an old-fashioned pullstring cowboy doll (voiced by Tom Hanks), and Buzz Lightyear, an astronaut action figure (voiced by Tim Allen), as they evolve from rivals competing for the affections of Andy, their owner, to friends who work together to be reunited with Andy as his family prepares to move to a new home.  The screenplay was written by Joss Whedon, Andrew Stanton, Joel Cohen and Alec Sokolow, based on a story by Lasseter, Pete Docter, Stanton and Joe Ranft.  The film features music by Randy Newman, and was executive-produced by Steve Jobs and Edwin Catmull.\n\nDoctor Doom's Fearfall: Doctor Doom's Fearfall is a space shot ride located in the Islands of Adventure theme park at Universal Orlando Resort.  As the name suggests, the ride is themed after the superhero team Fantastic Four archenemy, Doctor Doom.  The ride opened on May 28, 1999.\n\nQuestion: WHAT ADVENTURE THEME PARK HAS AN AREA THEMED AFTER A FILM PRODUCED BY PIXAR ANIMATION?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"theme_park_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the adventure theme park.\"\n    },\n    \"has_pixar_themed_areas\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the theme park has areas themed after films produced by Pixar Animation.\"\n    },\n    \"themed_areas\": {\n      \"type\": \"array\",\n      \"description\": \"A list of areas within the theme park that are themed after Pixar films.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"area_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the themed area.\"\n          },\n          \"themed_after_film\": {\n            \"type\": \"string\",\n            \"description\": \"The title of the film the area is themed after.\"\n          },\n          \"film_details\": {\n            \"type\": \"object\",\n            \"properties\": {\n              \"film_title\": {\n                \"type\": \"string\",\n                \"description\": \"The full title of the film.\"\n              },\n              \"production_studio\": {\n                \"type\": \"string\",\n                \"description\": \"The studio that produced the film.\"\n              },\n              \"release_year\": {\n                \"type\": \"integer\",\n                \"description\": \"The release year of the film.\"\n              }\n            },\n            \"required\": [\n              \"film_title\",\n              \"production_studio\",\n              \"release_year\"\n            ],\n            \"additionalProperties\": false\n          }\n        },\n        \"required\": [\n          \"area_name\",\n          \"themed_after_film\",\n          \"film_details\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"theme_park_name\",\n    \"has_pixar_themed_areas\",\n    \"themed_areas\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "theme_park_name": {
        "type": "string",
        "description": "The name of the adventure theme park."
      },
      "has_pixar_themed_areas": {
        "type": "boolean",
        "description": "Indicates if the theme park has areas themed after films produced by Pixar Animation."
      },
      "themed_areas": {
        "type": "array",
        "description": "A list of areas within the theme park that are themed after Pixar films.",
        "items": {
          "type": "object",
          "properties": {
            "area_name": {
              "type": "string",
              "description": "The name of the themed area."
            },
            "themed_after_film": {
              "type": "string",
              "description": "The title of the film the area is themed after."
            },
            "film_details": {
              "type": "object",
              "properties": {
                "film_title": {
                  "type": "string",
                  "description": "The full title of the film."
                },
                "production_studio": {
                  "type": "string",
                  "description": "The studio that produced the film."
                },
                "release_year": {
                  "type": "integer",
                  "description": "The release year of the film."
                }
              },
              "required": [
                "film_title",
                "production_studio",
                "release_year"
              ],
              "additionalProperties": false
            }
          },
          "required": [
            "area_name",
            "themed_after_film",
            "film_details"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "theme_park_name",
      "has_pixar_themed_areas",
      "themed_areas"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
