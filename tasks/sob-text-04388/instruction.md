{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe First Wives Club: The First Wives Club is a 1996 American comedy film, based on the best-selling 1992 novel of the same name by Olivia Goldsmith.  Narrated by Diane Keaton, it stars Keaton, Goldie Hawn, and Bette Midler as three divorced women who seek revenge on their ex-husbands who left them for younger women.  Stephen Collins, Victor Garber and Dan Hedaya co-star as the husbands, and Sarah Jessica Parker, Marcia Gay Harden and Elizabeth Berkley as their lovers, with Maggie Smith, Bronson Pinchot and Stockard Channing also starring.  Scott Rudin produced and Hugh Wilson directed; the film was distributed by Paramount Pictures.\n\nTake Me Home (2011 film): Take Me Home is a 2011 American romantic comedy film directed by and starring Sam Jaeger.  The film also stars his wife Amber Jaeger, Lin Shaye, and Victor Garber.  It premiered on April 19, 2011 at the Nashville Film Festival.  \"Take Me Home\" was released to DVD on May 29, 2012.\n\nThe Sugar Shoppe: The Sugar Shoppe were a Canadian sunshine pop vocal group who recorded in the late 1960s and featured actor Victor Garber.\n\nThe Jon Dore Television Show: The Jon Dore Television Show is a Canadian mockumentary-style comedy television series, created by Jon Dore and John Brunton.  The show stars Canadian actor and comedian Jon Dore, of recent \"Canadian Idol\" co-host fame.  The Comedy Network ordered 13 half-hour episodes of the series, which premiered on October 17, 2007 at 10pm ET.  The second season premiered on January 21, 2009.  A third season was supposed to be premiered in 2010 until Dore confirmed the series' cancellation.  The show is also currently being played on the Independent Film Channel in the United States.\n\nLegally Blonde: Legally Blonde is a 2001 American comedy film adapted from the novel of the same title by Amanda Brown.  It was directed by Robert Luketic, scripted by Karen McCullah Lutz and Kirsten Smith, and stars Reese Witherspoon, Luke Wilson, Selma Blair, Matthew Davis, Victor Garber, and Jennifer Coolidge.  The film tells the story of Elle Woods, a sorority girl who attempts to win back her ex-boyfriend by getting a law degree.  The title is a pun on the term 'legally blind'.\n\nRespawn (30 Rock): \"Respawn\" is the and season finale of the fifth season of the American television comedy series \"30 Rock\", and the 103rd overall episode of the series.  It was directed by Don Scardino, and written by Hannibal Buress and Ron Weiner.  The episode originally aired on the National Broadcasting Company (NBC) network in the United States on May 5, 2011.  Guest stars in this episode include Victor Garber, Chris Parnell, Will Forte, Adriane Lenox, and Ina Garten.\n\nYou Again: You Again is a 2010 American comedy film produced by John J. Strauss and Eric Tannenbaum and directed by Andy Fickman with music by Nathan Wang and written by Moe Jelline.  The film stars Kristen Bell, Jamie Lee Curtis, Sigourney Weaver, Odette Yustman, James Wolk, Victor Garber, Billy Unger, Kyle Bornheimer, Kristin Chenoweth, and Betty White.\n\nVictor Garber: Victor Joseph Garber (born March 16, 1949) is a Canadian actor and singer.  He is known for playing Jesus in \"Godspell\", Anthony Hope in \"\", John Wilkes Booth in \"Assassins\", Jack Bristow in the television series \"Alias\", Max in \"Lend Me a Tenor\", Thomas Andrews in James Cameron's \"Titanic\", and Ken Taylor, Canadian Ambassador to Iran, in \"Argo\".  He is currently a series regular on \"Legends of Tomorrow\" as Dr. Martin Stein, playing the same role as a guest star on \"The Flash\" and the web series \"Vixen.\n\nBig Game (2014 film): Big Game is a 2014 Finnish action adventure film directed by Jalmari Helander, based on the original story by Helander and Petri Jokiranta.  The film stars Samuel L. Jackson, Onni Tommila, Felicity Huffman, Victor Garber, Ted Levine, Jim Broadbent, and Ray Stevenson.\n\nSelf/less: Self/less is a 2015 American science fiction action thriller film directed by Tarsem Singh, produced by Ram Bergman and James D. Stern and written by Alex and David Pastor.  The film tells the story of a business tycoon and billionaire named Damian Hale, who is diagnosed with a deadly illness.  However, he manages to somehow save his life with the aid of Professor Albright, who transfers Hale's consciousness into a new, younger body.  The film stars Ryan Reynolds, Natalie Martinez, Matthew Goode, Victor Garber, Derek Luke, and Ben Kingsley.\n\nQuestion: Who directed the 2010 comedy film You Again which stars Canadian actor Victor Garber?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released.\"\n    },\n    \"genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film's director.\"\n    },\n    \"starring_actors\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of the main actors starring in the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"genre\",\n    \"director_name\",\n    \"starring_actors\"\n  ],\n  \"additionalProperties\": false\n}"
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
      "genre": {
        "type": "string",
        "description": "The genre of the film."
      },
      "director_name": {
        "type": "string",
        "description": "The name of the film's director."
      },
      "starring_actors": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of the main actors starring in the film."
      }
    },
    "required": [
      "film_title",
      "release_year",
      "genre",
      "director_name",
      "starring_actors"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
