{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nA Place for Annie: A Place for Annie is a 1994 Hallmark Hall of Fame TV movie that stars Sissy Spacek, Mary-Louise Parker and Joan Plowright.  Directed by John Gray, the first presentation aired on the ABC network on May 1, 1994.\n\nYou Don't Look 40, Charlie Brown: You Don't Look 40, Charlie Brown, the first \"Peanuts\" TV special of the 1990s, is one of many prime-time animated TV specials, based on characters from the Charles M. Schulz comic strip \"Peanuts\".  It originally aired on the CBS network on February 2, 1990.  Hosted by \"Knots Landing\" star Michele Lee, this special includes a reunion of actors and actresses who voiced \"Peanuts\" characters from 1965 to 1989.  Also included are a B.B. King performance of \"Joe Cool\" and clips from the seldom-seen 1973 \"Hallmark Hall of Fame\" live-action production of \"You're a Good Man, Charlie Brown\".  Unlike the other \"Peanuts\" anniversary specials before and after, this was the only one that was released to home video by Paramount Home Video.\n\nThe Secret Garden (1987 film): The Secret Garden is the 1987 Hallmark Hall of Fame TV film adaptation of the novel \"The Secret Garden\", aired on CBS November 30, 1987 and produced by Rosemont Productions Limited, who also produced \"Back to the Secret Garden\".  The film stars Barret Oliver, Jadrien Steele, Billie Whitelaw and Sir Derek Jacobi.\n\nThe ABC Sunday Night Movie: The ABC Sunday Night Movie is a television program that aired on Sunday nights, first for a brief time in 1962 under the title \"Hollywood Special\" (although \"Time\" magazine lists this version as \"The Sunday Night Movie\") to supposedly replace an open time slot for a cancelled TV show, \"Bus Stop\", which was cancelled after March 1962.  It then began airing regularly under its more commonly known title from late 1964 to 1998, on ABC.  Since 2004, it has aired sporadically as a special program, now titled the \"ABC Sunday Movie of the Week\", though as of the 2011-12 television season, the only films in this timeslot were aired under the \"Hallmark Hall of Fame\" banner, which transferred to ABC in that season.  However, in 2014, The Hallmark Hall of Fame moved exclusively to cable on the Hallmark Channel, and as a result, said program is no longer on broadcast television in any form (including ABC) for good.  As a result of this, the Sunday Night Movie is now exclusively relegated to 2 special holiday movies, \"The Sound of Music\" every holiday season and \"The Ten Commandments\" every Easter.\n\nThe Blackwater Lightship (film): The Blackwater Lightship is a 2004 Hallmark Hall of Fame TV movie adaptation of the novel \"The Blackwater Lightship\" by Colm Tóibín.  It aired on CBS on February 4, 2004.  The movie stars Angela Lansbury, Gina McKee, Sam Robards, Dianne Wiest, and Keith McErlean.  Lansbury received an Emmy nomination for it in 2004.\n\nThe Borrowers (1973 film): The Borrowers is a Hallmark Hall of Fame TV special first broadcast in 1973 on NBC.  This made for television special is adapted from the 1952 Carnegie Medal-winning first novel of author Mary Norton's \"The Borrowers\" series: \"The Borrowers\".  The film stars Eddie Albert, Tammy Grimes and Judith Anderson and was directed by Walter C. Miller.\n\nHave a Little Faith (film): Have a Little Faith is a Hallmark Hall of Fame television movie.  The film debuted on ABC on November 27, 2011, as the first \"Hallmark Hall of Fame\" film broadcast since CBS cancelled the series earlier in 2011.  It was the first \"Hallmark Hall of Fame\" film broadcast on ABC since 1995.\n\nBrad Cohen: Brad Cohen is an American motivational speaker, teacher, school administrator, and author who has severe Tourette syndrome (TS).  Cohen described his experiences growing up with the condition in his book, \"Front of the Class: How Tourette Syndrome Made Me the Teacher I Never Had\", co-authored with Lisa Wysocky.  The book has been made into a Hallmark Hall of Fame TV movie titled \"Front of the Class\".\n\nThe Room Upstairs: The Room Upstairs is a 1987 Hallmark Hall of Fame TV movie based on the novel \"The Room Upstairs\" by Norma Levinson, starring Stockard Channing, Sam Waterston, Joan Allen and Linda Hunt.  The young Jerry O'Connell, Devoreaux White and Sarah Jessica Parker all have small supporting roles.  The film aired on CBS on January 31, 1987 and was later distributed on DVD.\n\nTammy Grimes: Tammy Lee Grimes (January 30, 1934 – October 30, 2016) was an American actress and singer.\n\nQuestion: Tammy Lee Grimes was an American actress and singer who starred in a Hallmark Hall of Fame TV special first broadcast in 1973 on NBC called what?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"movie_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the Hallmark Hall of Fame TV special.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the TV special was first broadcast.\"\n    },\n    \"network\": {\n      \"type\": \"string\",\n      \"description\": \"The television network on which the special aired.\"\n    },\n    \"is_hallmark_hall_of_fame\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the production is a Hallmark Hall of Fame special.\"\n    },\n    \"starring_actress\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actress who starred in the special.\"\n    }\n  },\n  \"required\": [\n    \"movie_title\",\n    \"release_year\",\n    \"network\",\n    \"is_hallmark_hall_of_fame\",\n    \"starring_actress\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "movie_title": {
        "type": "string",
        "description": "The title of the Hallmark Hall of Fame TV special."
      },
      "release_year": {
        "type": "integer",
        "description": "The year the TV special was first broadcast."
      },
      "network": {
        "type": "string",
        "description": "The television network on which the special aired."
      },
      "is_hallmark_hall_of_fame": {
        "type": "boolean",
        "description": "Indicates if the production is a Hallmark Hall of Fame special."
      },
      "starring_actress": {
        "type": "string",
        "description": "The name of the actress who starred in the special."
      }
    },
    "required": [
      "movie_title",
      "release_year",
      "network",
      "is_hallmark_hall_of_fame",
      "starring_actress"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
