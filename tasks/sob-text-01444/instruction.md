{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMove On (2012 film): Move On is an international film project from 2012 directed by Asger Leth in collaboration with Deutsche Telekom AG.  The leading actor is Mads Mikkelsen, who is supported by German actress Alexandra Maria Lara and newly discovered Slovak actress Gabriela Marcinkova.  At www.move-on-film.com, a new episode of the movie appeared each week, and since its world premiere on 6 November 2012 in Berlin, all eight episodes can be viewed there.\n\nPauline Starke: Pauline Starke (January 10, 1901 – February 3, 1977) was an American silent-film actress born in Joplin, Missouri.\n\nAbigail Eames: Abigail Eames is a British child actress born on October 5, 2003, and first appeared on British television and most recently the Bollywood movie \"Shivaay\".  She is best known for being her roles in \"Mr Selfridge\" (2013), \"Crimson Fields\" (2014), \"Lawless\" (2013), \"Harry and Paul's of 2s\" (2014), \"Doctor Who\" and \"The Interceptor\".  She made her Bollywood debut alongside Ajay Devgan in his movie \"Shivaay\" (2016).  Abigail got positive response for her performance as the daughter of Ajay Devgn in Shivaay.\n\nCastle Keep: Castle Keep is a \"firmly pro- and anti-war\" 1969 American Technicolor war film combining surrealism with tragic realism filmed in Panavision.  It was directed by Sydney Pollack and starred Burt Lancaster, Patrick O'Neal, Jean-Pierre Aumont, Bruce Dern, and Peter Falk.  The movie appeared in the summer of 1969, a few months before the arrival of Pollack's smash hit \"They Shoot Horses, Don't They? \".\n\nWhat Ever Happened to Aunt Alice?: What Ever Happened to Aunt Alice?  is a 1969 American thriller film directed by Lee H. Katzin with Bernard Girard (uncredited), and starring Geraldine Page, Ruth Gordon, Rosemary Forsyth, Robert Fuller and Mildred Dunnock.  The screenplay by Theodore Apstein, based on the novel \"The Forbidden Garden\" by Ursula Curtiss, focuses on an aging Arizona widow who hires elderly female housekeepers and cons them out of their money before murdering them.\n\nIrina Kupchenko: Irina Petrovna Kupchenko (Russian: Ирина Петровна Купченко ; born 1 March 1948 in Vienna) is a Soviet and Russian actress.  She rose to prominence after acting in Andrei Konchalovsky's 1969 movie adaptation of \"A Nest of Gentlefolk\".  She has performed in more than forty films since 1969.\n\nYumiko Nogawa: Yumiko Nogawa (野川由美子 , Nogawa Yumiko ) (born August 30, 1944) is a Japanese actress born in Kyoto, Japan.  She has starred in several movies, notably \"Gate of Flesh\" (1964), a Japanese erotic film, part of a trilogy of films she made with director Seijun Suzuki.  Including \"Story of a Prostitute\" (1965) and \"Carmen from Kawachi\" (1966), these films are known as Nogawa's \"Flesh Trilogy\".  Nogawa has appeared in numerous films in Japan, including director Nagisa Oshima's \"The Pleasures of the Flesh\" (1965) and \"Zatoichi and the Fugitives\" (1968), the eighteenth film in the \"Zatoichi\" series.  She has also appeared in television series on Nippon Television, TV Tokyo, Fuji TV, and NHK.\n\nMildred Dunnock: Mildred Dorothy Dunnock (January 25, 1901 – July 5, 1991) was an American theater, film and television actress.\n\nKaitlyn Maher: Kaitlyn Ashley Maher (born January 10, 2004) is an American child singer and actress born in Michigan, and raised in Ashburn, Virginia.  In 2008, at the age of 4, she appeared on the third season of \"America's Got Talent\" and for her audition sang \"Somewhere Out There\".  She reached the top 10 of AGT season 3, and was the youngest person to ever reach that level.  Maher has since appeared live at The Great Kids Expo in Chantilly, Virginia, on October 25, 2008, a live broadcast of the 2008 lighting of the National Christmas Tree, on December 4, 2008, attended by President George W. Bush and over 7,000 guests, and the 2009 Cherry Blossom Festival on April 11, 2009.  On October 3, 2009, Maher was the opening act of The Addi and Cassi Hempel Fund benefit.  Maher has appeared in a Harris Teeter commercial airing during December 2008.  She was also selected by Compassion International as its first ever Child Ambassador, visited children in El Salvador with Compassion, got to meet her sponsored child, and shot a music video to her title song \"You Were Meant to Be.\"\n\nMarianne Oswald: Marianne Oswald (January 9, 1901 – February 25, 1985) was the stage name of Sarah Alice Bloch, a French singer and actress born in Sarreguemines in Alsace-Lorraine.  She took this stage name from a character she much admired, the unhappy Oswald in the Ibsen play Ghosts.  She was noted for her hoarse voice, heavy half-Lorraine, half-German accent, and for singing about unrequited love, despair, sadness, and death.  She sang the songs of Kurt Weill and Bertolt Brecht.  She was friends with Jean Cocteau, Jacques Prévert, François Mauriac, and Albert Camus.  In fact, the text for one of her album covers was written by Camus.  She was an inspiration for the composers Francis Poulenc and Arthur Honegger.\n\nQuestion: What director was involved in the 1969 movie appeared in by the actress born on January 25, 1901?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"movie_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the movie.\"\n    },\n    \"movie_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the movie.\"\n    },\n    \"actress\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actress.\"\n        },\n        \"birth_date\": {\n          \"type\": \"string\",\n          \"description\": \"The birth date of the actress in 'Month Day, Year' format.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"birth_date\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the director involved in the movie.\"\n    }\n  },\n  \"required\": [\n    \"movie_title\",\n    \"movie_year\",\n    \"actress\",\n    \"director_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "movie_title": {
        "type": "string",
        "description": "The title of the movie."
      },
      "movie_year": {
        "type": "integer",
        "description": "The release year of the movie."
      },
      "actress": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actress."
          },
          "birth_date": {
            "type": "string",
            "description": "The birth date of the actress in 'Month Day, Year' format."
          }
        },
        "required": [
          "name",
          "birth_date"
        ],
        "additionalProperties": false
      },
      "director_name": {
        "type": "string",
        "description": "The name of the director involved in the movie."
      }
    },
    "required": [
      "movie_title",
      "movie_year",
      "actress",
      "director_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
