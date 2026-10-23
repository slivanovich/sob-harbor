{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTron: Legacy: Tron: Legacy is a 2010 American science fiction action film directed by Joseph Kosinski from a screenplay written by Adam Horowitz and Edward Kitsis, based on a story by Horowitz, Kitsis, Brian Klugman and Lee Sternthal.  It is a sequel to the 1982 film \"Tron\", whose director Steven Lisberger returned to produce.  The cast includes Jeff Bridges and Bruce Boxleitner reprising their roles as Kevin Flynn and Alan Bradley, respectively, as well as Garrett Hedlund, Olivia Wilde, Beau Garrett and Michael Sheen.  The story follows Flynn's son Sam, who responds to a message from his long-lost father and is transported into a virtual reality called the \"Grid\", where Sam, his father and the algorithm Quorra, must stop the malevolent program Clu from invading the human world.\n\nTron: Tron is a 1982 American science fiction action-adventure film written and directed by Steven Lisberger, based on a story by Lisberger and Bonnie MacBird and produced by Walt Disney Productions.  The film stars Jeff Bridges as a computer programmer who is transported inside the software world of a mainframe computer where he interacts with programs in his attempt to escape.  Bruce Boxleitner, David Warner, Cindy Morgan, and Barnard Hughes star in supporting roles.\n\nAaron Stone: Aaron Stone is a Canadian/American science fiction action-adventure television series created by Bruce Kalish.  Originally broadcast with the launch of Disney XD on February 13, 2009.  It was the first original series to air on the network.  Produced in conjunction with Canadian Shaftesbury Films and filmed in Toronto, Ontario, Canada.\n\nThe Ultimate Warrior (film): The Ultimate Warrior is a 1975 science fiction action-adventure film directed by Robert Clouse.  One of a series of post-apocalyptic films from the 1960s and 1970s, it is set in post-civilization New York City in 2012 and depicts the struggles of a small enclave of inhabitants attempting to survive in a compound beset with packs of starving pillagers.\n\nE.T. the Extra-Terrestrial: E.T. the Extra-Terrestrial is a 1982 American science fiction fantasy film co-produced and directed by Steven Spielberg, and written by Melissa Mathison.  It features special effects by Carlo Rambaldi and Dennis Muren, and stars Henry Thomas, Dee Wallace, Robert MacNaughton, Drew Barrymore, Peter Coyote and Pat Welsh.  It tells the story of Elliott (Thomas), a lonely boy who befriends an extraterrestrial, dubbed \"E.T.\", who is stranded on Earth.  Elliott and his siblings help E.T. return home while attempting to keep him hidden from their mother and the government.\n\nSlipstream (1989 film): Slipstream is a 1989 science fiction film directed by Steven Lisberger, who had previously directed the cult classic 1982 science fiction film \"Tron\".  It was produced by Gary Kurtz, best known for his collaboration with George Lucas on the first two \"Star Wars\" films and \"American Graffiti\".  \"Slipstream\" reunited Kurtz with his \"Star Wars\" lead Mark Hamill, who features alongside Bill Paxton, Bob Peck and Kitty Aldridge, with cameo appearances from Robbie Coltrane, Ben Kingsley and F. Murray Abraham.\n\nHot Pursuit (1987 film): Hot Pursuit is a 1987 American-Mexican action comedy film directed by Steven Lisberger, written by Lisberger and Steven Carabatsos, and starring John Cusack, Robert Loggia, Wendy Gazelle, and Jerry Stiller.\n\nThunderbirds (2004 film): Thunderbirds is a 2004 British-American-French science fiction action-adventure film based on the 1960s television series of the same name, directed by Jonathan Frakes.  The film, written by William Osborne and Michael McCullers, was released on 24 July 2004 in the United Kingdom and 30 July 2004 in the United States, with later opening dates in other countries.  Whereas the original TV series used a form of puppetry termed \"Supermarionation\", the film's characters are portrayed by live-action actors.\n\nSky Captain and the World of Tomorrow: Sky Captain and the World of Tomorrow is a 2004 American science fiction action-adventure film written and directed by Kerry Conran in his directorial debut, and produced by Jon Avnet, Sadie Frost, Jude Law and Marsha Oglesby.  The film stars Law, Gwyneth Paltrow and Angelina Jolie; it is an example of the \"dieselpunk\" genre.\n\nCindy Morgan: Cindy Morgan (born Cynthia Ann Cichorski; September 29, 1954) is an American actress best known for her appearances as Lora/Yori in \"Tron\" and Lacey Underall in \"Caddyshack\".\n\nQuestion: Who starred in the 1982 American science fiction action-adventure film written and directed by Steven Lisberger?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"starring_actors\": {\n      \"type\": \"array\",\n      \"description\": \"A list of actors who starred in the film.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"director\",\n    \"starring_actors\"\n  ],\n  \"additionalProperties\": false\n}"
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
        "description": "The release year of the film."
      },
      "director": {
        "type": "string",
        "description": "The director of the film."
      },
      "starring_actors": {
        "type": "array",
        "description": "A list of actors who starred in the film.",
        "items": {
          "type": "string"
        }
      }
    },
    "required": [
      "film_title",
      "release_year",
      "director",
      "starring_actors"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
