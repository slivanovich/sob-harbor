{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPremier Manager (series): Premier Manager is the name of a football management video game series started in 1992.  Published by Gremlin Interactive, it was first developed by Realms of Fantasy, later passed to Spanish company Dinamic Software.  The later games are published and developed by Zoo Digital Publishing, who bought the rights from Infogrames and hired some members of the original Gremlin staff.\n\nSafari Skyway: Safari Skyway was a monorail ride that opened in 1986 at Chessington World of Adventures Resort, in the Market Square area.  Manufactured by Mack Rides, the ride gave guests a guided tour of Chessington Zoo, and in its first year, the construction of Chessington World of Adventures theme park.  The ride ran for almost thirty years before closing abruptly in late July 2015.  In early January 2016, the park announced that the ride would be retired due to continuous troubles with maintenance for the ride.\n\nChessington World of Adventures: Chessington World of Adventures Resort is a theme park, zoo and hotel complex that lies 12 mi southwest of Central London, England in the Chessington area of the Kingston upon Thames borough.  Historically opened as Chessington Zoo in 1931, a theme park was developed by The Tussauds Group alongside the zoo, opening on 7 July 1987, as one of the first themed amusement parks in Britain.  The park was inherited by Merlin Entertainments after the buyout of Tussauds in 2007.  Under Merlin, Chessington has been increasingly developed into a resort tourist destination, including two on-site hotels, a high ropes course and camp site.\n\nThe Tussauds Group: The Tussauds Group is now part of Merlin Entertainments, the world's second largest leisure group, after Disney.  It is based in Poole, Dorset from where it manages a portfolio of brands and over 50 attractions including the Madame Tussauds waxworks, Legoland Theme Parks, Legoland Discovery Centers, Sea Life Centres, Gardaland in Italy, The Dungeons, The London Eye,The Orlando Eye, Alton Towers, Thorpe Park, and Chessington World of Adventures.\n\nChessington: Chessington is an area in the Royal Borough of Kingston upon Thames within Greater London.  It is the largest salient of Greater London into the neighbouring county of Surrey.  As of the 2011 census it had a population of 18,973.  The Bonesgate Stream, a tributary of the Hogsmill River runs through it.  The popular theme park resort Chessington World of Adventures, which incorporates Chessington Zoo, is located in the south-west of the area.\n\nGalaxy Zoo: Galaxy Zoo is a crowdsourced astronomy project which invites people to assist in the morphological classification of large numbers of galaxies.  (e.g.) It is an example of citizen science as it enlists the help of members of the public to help in scientific research.  There have been 15 versions as of July 2017, many of which are outlined in this article.  Galaxy Zoo is part of the Zooniverse, a group of citizen science projects.  An outcome of the project is to better determine the different aspects of objects and to separate them into classifications.\n\nZoo Holdings Group: Zoo Holdings Group is a food and beverage management company headquartered in Shanghai, China, and has its offices in China mainland, Taiwan and South Korea.  Its founder, Kim Kun Woo, has also created \"Zoo Coffee\", \"Tiger Topoki\" and \"Monkey's Kitchen\".\n\nOver-the-Jumps Carousel: The Over-the-Jumps Carousel, also known as the Herschell-Spillman Carousel is a historic carousel at the Little Rock Zoo in Little Rock, Arkansas.  Built in the 1920s and first exhibited at the 1924 Arkansas State Fair, it is believed to be the last operating \"over-the-jumps\" carousel in the world, with an original undulating wooden platform mounted on a 1960s-vintage caterpillar drive.  The horses were carved by the Allan Herschell Company.  After many years of private ownership, the carousel was acquired by a local nonprofit group and donated to the zoo in 2007.\n\nPelicans at the Zoo: Pelicans at the Zoo is an 1898 British short black-and-white silent actuality film, produced by British Mutoscope & Biograph Company, featuring pelicans being released for feeding into their enclosure at London Zoological Gardens.  The film was part of a series, with \"Elephants at the Zoo\", which were one of the earliest examples of animal life on film.\n\nThe Tangerine Zoo: The Tangerine Zoo was an American psychedelic rock band formed in Swansea, Massachusetts, in 1966.  Encompassed in Boston's psychedelic scene and considered a part of the Bosstown Sound, the band became popular regionally, and released two albums on Mainstream Records during their recording career.  The Tangerine Zoo had an opportunity to achieve national recognition at the Woodstock Festival, but was forced to decline the invitation.  Nonetheless, the group's material has been reinstated into the public conscious after 1960s psychedelic music collectors have discovered the Tangerine Zoo's work years after their disbandment.\n\nQuestion: Chessington Zoo was developed by a group that is now part of what company?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"developed_entity_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the resort complex that includes the zoo and the theme park developed by the group.\"\n    },\n    \"original_developer_group_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the group that developed the theme park alongside the zoo.\"\n    },\n    \"current_parent_company_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the company that now owns the original developer group.\"\n    },\n    \"development_description\": {\n      \"type\": \"string\",\n      \"description\": \"A description of what the group developed in relation to the zoo.\"\n    }\n  },\n  \"required\": [\n    \"developed_entity_name\",\n    \"original_developer_group_name\",\n    \"current_parent_company_name\",\n    \"development_description\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "developed_entity_name": {
        "type": "string",
        "description": "The name of the resort complex that includes the zoo and the theme park developed by the group."
      },
      "original_developer_group_name": {
        "type": "string",
        "description": "The name of the group that developed the theme park alongside the zoo."
      },
      "current_parent_company_name": {
        "type": "string",
        "description": "The name of the company that now owns the original developer group."
      },
      "development_description": {
        "type": "string",
        "description": "A description of what the group developed in relation to the zoo."
      }
    },
    "required": [
      "developed_entity_name",
      "original_developer_group_name",
      "current_parent_company_name",
      "development_description"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
