{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nNorby (TV series): Norby is an American sitcom television series that aired from January 5 until April 6, 1955 on NBC.  This was one of the first regular weekly series broadcast by NBC in its new all-electronic compatible color system, which had been approved by the FCC in 1953.  \"Norby\" starred veteran film actor David Wayne, and was created by writer David Swift, then best known as the creator of the popular sitcom \"Mister Peepers\".  Eastman Kodak was the program's sponsor, and it was filmed in Eastmancolor.  The series ended when Kodak pulled its sponsorship due to the high costs of filming \"Norby\" in color.\n\nNew Girl: New Girl is an American sitcom television series that premiered on Fox on September 20, 2011.  Developed by Elizabeth Meriwether under the working title \"Chicks & Dicks\", the series revolves around a kooky teacher, Jess (Zooey Deschanel), after she moves into a Los Angeles loft with three men, Nick (Jake Johnson), Schmidt (Max Greenfield), and Winston (Lamorne Morris); Jess' best friend Cece (Hannah Simone) and on-again-off-again loft mate Coach (Damon Wayans Jr.) also appear regularly.  The show combines comedy and drama elements as the characters, who are in their early thirties, deal with maturing relationships and career choices.  The sixth and most current season premiered on September 20, 2016.\n\nKevin Can Wait: Kevin Can Wait is an American sitcom television series starring Kevin James.  The series premiered on September 19, 2016.  The series marked James' second starring role in a CBS sitcom, after \"The King of Queens\", which ran from 1998 until 2007.  On March 23, 2017, CBS renewed the series for a second season, which premiered on September 25, 2017.\n\nIt's Like, You Know...: It's Like, You Know... is an American sitcom television series broadcast by ABC.  It starred Steven Eckholdt, Chris Eigeman, Evan Handler, A. J. Langer, and Jennifer Grey, and depicted life in Los Angeles as viewed through the eyes of Eigeman's character, a diehard New Yorker named Arthur Garment.  The series aired for two seasons, from March 24, 1999 until January 5, 2000.\n\nGrandma's House: Grandma's House is a sitcom television series broadcast on BBC Two.  Written by Simon Amstell and long term collaborator Dan Swimer, the series stars Simon Amstell playing a version of himself: an ex-television presenter searching for meaning in his life.  Each episode takes place at his Grandma's house, where Grandma (Linda Bassett) welcomes her family, desperate to see everyone happy.\n\nProject Almanac: Project Almanac is a 2015 American found footage science fiction thriller film directed by Dean Israelite at his directorial debut, and written by Jason Harry Pagan and Andrew Deutschman.  The film stars Jonny Weston, Sofia Black-D'Elia, Sam Lerner, Allen Evangelista, Virginia Gardner and Amy Landecker.  The film tells the story of a group of high school students that build a time machine.\n\nSofia Black-D'Elia: Sofia Black-D'Elia (born December 23, 1991) is an American actress.  She is best known for her roles as Tea Marvelli in \"Skins\", Sage Spence in \"Gossip Girl\" and Andrea Cornish in \"The Night Of\".  As of 2017 Black-D'Elia stars as Sabrina on the FOX comedy \"The Mick\".\n\nThe Mick (TV series): The Mick is an American sitcom television series broadcast on Fox.  Created by Dave Chernin and John Chernin, the series stars Kaitlin Olson, who is also an executive producer.  The series premiered on January 1, 2017, and resumed in its regular Tuesday night slot on January 3, 2017.  On January 11, 2017, Fox picked up the series for a full season of 17 episodes.\n\nThe Tycoon (TV series): The Tycoon is a 32-episode American sitcom television series broadcast by ABC.  It starred Walter Brennan as the fictitious businessman Walter Andrews, similar to his birth name of Walter Andrew Brennan.  As chairman of the board of the Thunder Corporation that he founded but no longer actively runs, Brennan plays an eccentric and cantankerous millionaire (when such persons were much fewer in number) with a common touch who helps promising persons in need.  The series aired with new episodes at 9 p.m. Eastern time Tuesday from September 15, 1964, until April 27, 1965.  It continued in reruns until September 7, 1965.  The program did not develop sufficient audience, presumably because viewers may have preferred the versatile Brennan as the bucolic Grandpa Amos McCoy in his 1957-1963 ABC and CBS sitcom \"The Real McCoys\".  Oddly, \"The Tycoon\" has the same name as an episode of \"The Real McCoys\" also called \"The Tycoon,\" which aired four years earlier on August 23, 1960.\n\nCosby: Cosby is an American sitcom television series broadcast on CBS from September 16, 1996, until April 28, 2000.  The program starred Bill Cosby and Phylicia Rashad, who had previously worked together in the 1984–1992 NBC sitcom \"The Cosby Show\".  Madeline Kahn portrayed their neighbor, Pauline, until her death in 1999.  The series is loosely based on the British sitcom \"One Foot in the Grave\" airing on BBC from 1990 until 2001.\n\nQuestion: Which American sitcom television series broadcast on Fox did Sofia Black-D'Elia appear on in 2017?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"series_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the American sitcom television series.\"\n    },\n    \"network\": {\n      \"type\": \"string\",\n      \"description\": \"The broadcasting network of the series.\"\n    },\n    \"actress_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actress who appeared on the series.\"\n    },\n    \"role_played\": {\n      \"type\": \"string\",\n      \"description\": \"The character played by the actress in the series.\"\n    },\n    \"year_of_appearance\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the actress appeared on the series.\"\n    }\n  },\n  \"required\": [\n    \"series_title\",\n    \"network\",\n    \"actress_name\",\n    \"role_played\",\n    \"year_of_appearance\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "series_title": {
        "type": "string",
        "description": "The title of the American sitcom television series."
      },
      "network": {
        "type": "string",
        "description": "The broadcasting network of the series."
      },
      "actress_name": {
        "type": "string",
        "description": "The name of the actress who appeared on the series."
      },
      "role_played": {
        "type": "string",
        "description": "The character played by the actress in the series."
      },
      "year_of_appearance": {
        "type": "integer",
        "description": "The year the actress appeared on the series."
      }
    },
    "required": [
      "series_title",
      "network",
      "actress_name",
      "role_played",
      "year_of_appearance"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
