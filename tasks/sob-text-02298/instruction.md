{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nList of Big Time Rush episodes: \"Big Time Rush\", (also known as \"BTR\"), is an American television series created by Scott Fellows about the Hollywood misadventures of four hockey players from Minnesota—Kendall, James, Carlos, and Logan, after they are selected to form a boy band.  The series premiered with an hour-long pilot episode, \"Big Time Audition\", on Nickelodeon, on November 28, 2009.  Its official debut episode premiered on January 18, 2010, earning 6.8 million viewers, making it Nickelodeon's highest-rated live-action series debut ever.  The final episode aired on July 25, 2013, after four seasons comprising a total of 74 episodes.\n\nThe Nut Job 2: Nutty by Nature: The Nut Job 2: Nutty by Nature is a 2017 3D computer-animated comedy film directed by Cal Brunker and written by Brunker, Bob Barlen and Scott Bindley.  A sequel to \"The Nut Job\" (2014), it stars the voices of Will Arnett, Maya Rudolph, Jackie Chan, Katherine Heigl, Bobby Moynihan, Bobby Cannavale, Isabela Moner, Jeff Dunham, and Gabriel Iglesias.  Produced by Gulfstream Pictures, Redrover International and ToonBox Entertainment, the film was released theatrically on August 11, 2017, by Open Road Films.\n\n100 Things to Do Before High School: 100 Things to Do Before High School is an American sitcom created by Scott Fellows that premiered on Nickelodeon on November 11, 2014, and ended on Nickelodeon on February 27, 2016.  The series stars Isabela Moner, Jaheem King Toombs, Owen Joyner, and Jack De Sena.\n\nIsabela Moraes: Isabela Moraes (born 5 April 1980) is a former synchronized swimmer from Brazil.  She competed in the women's duet competition with her twin sister, Carolina Moraes, at both the 2000 and 2004 Summer Olympics .  Both also competed for Ohio State University, winning 11 national championships, including the team routine title in 2000, and four straight titles in duet and trio routines between 1999 and 2002.  Following the Olympics, Carolina and Isabela retired and joined Cirque du Soleil, with their first performance being as part of the 2005 World Aquatics Championships opening ceremony.  Isabela has been since 2007 part of \"Le Rêve\", a show presented in Las Vegas.\n\nGuide to: The First Day and Lockers: Guide to: The First Day and Lockers is the first episode of \"Ned's Declassified School Survival Guide\" to be broadcast.  It originally aired on September 12, 2004 on Nickelodeon.  It was directed by David Kendall, and was created and written by Scott Fellows.\n\nCarolina Moraes: Carolina Moraes (born 5 April 1980) is a former synchronized swimmer from Brazil.  She competed in the women's duet competition with her twin sister, Isabela Moraes, at both the 2000 and 2004 Summer Olympics .  Both also competed for Ohio State University, winning 11 national championships, including the team routine title in 2000, and four straight titles in duet and trio routines between 1999 and 2002.  Following the Olympics, Carolina and Isabela retired and joined Cirque du Soleil, with their first performance being as part of the 2005 World Aquatics Championships opening ceremony.  Both have been part of the cast of \"Le Rêve\", a show presented in Las Vegas since 2007, though Carolina is less frequent as she travels with her husband, part of Cirque du Soleil's technical team.\n\nSupernoobs: Supernoobs is an American-Canadian flash animated series produced by DHX Media for Teletoon.  The series is about four kids who navigate through middle school and fight viruses as well.  It first premiered on Cartoon Network in the United Kingdom and Ireland on November 2, 2015.  \"Supernoobs\" was created by Scott Fellows, who also created \"Johnny Test\", \"Ned's Declassified School Survival Guide\", \"Big Time Rush\", and \"100 Things to Do Before High School\".\n\nBig Time Rush: Big Time Rush is an American television series that originally aired on Nickelodeon from November 28, 2009 until July 25, 2013.  It was created by Scott Fellows (also the creator of \"Ned's Declassified School Survival Guide\" and \"Johnny Test\" and the head writer of \"The Fairly OddParents\").  It focuses on the Hollywood misadventures of four hockey players from Minnesota: Kendall Knight, James Diamond, Carlos Garcia, and Logan Mitchell, after they are selected to form a boy band.\n\nIsabela Moner: Isabela Moner (born July 10, 2001) is an American actress and singer.  She is known for her lead role on the Nickelodeon television series \"100 Things to Do Before High School\" and for her role as Izabella in the 2017 film \"\".\n\nWishology: Wishology is a trilogy of television specials and the ninth special of the animated television series \"The Fairly OddParents\".  The first part of the trilogy, \"The Big Beginning\", originally aired on the cable network Nickelodeon in the United States on May 1, 2009; the second part, \"The Exciting Middle Part\", aired on May 2; and the last of the three parts, \"The Final Ending\", aired on May 3.  The trilogy was written by Kevin Sullivan, Scott Fellows, and Butch Hartman, and was directed by Gary Conrad.  According to Nielsen ratings, the first and third parts of the trilogy were viewed by 4 million people, while its second part garnered 3.6 million viewers.  Critical reviewers displayed mixed reactions to how three-dimensional objects interact via computer animation with the series' usual two-dimensional artwork in the trilogy.  Composer Guy Moon, who has worked throughout the series, won an Annie Award for his music in the first part of the trilogy in 2010.\n\nQuestion: \"Supernoobs\" was produced by Scott Fellows who also made what show which starred Isabela Moner and premiered on Nickelodeon on November 11, 2014?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"show_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the television series.\"\n    },\n    \"creator\": {\n      \"type\": \"string\",\n      \"description\": \"The creator of the television series.\"\n    },\n    \"star_actor\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor who starred in the series.\"\n    },\n    \"premiere_date\": {\n      \"type\": \"string\",\n      \"format\": \"date\",\n      \"description\": \"The date the series premiered.\"\n    },\n    \"network\": {\n      \"type\": \"string\",\n      \"description\": \"The television network on which the series premiered.\"\n    }\n  },\n  \"required\": [\n    \"show_title\",\n    \"creator\",\n    \"star_actor\",\n    \"premiere_date\",\n    \"network\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "show_title": {
        "type": "string",
        "description": "The title of the television series."
      },
      "creator": {
        "type": "string",
        "description": "The creator of the television series."
      },
      "star_actor": {
        "type": "string",
        "description": "The name of the actor who starred in the series."
      },
      "premiere_date": {
        "type": "string",
        "format": "date",
        "description": "The date the series premiered."
      },
      "network": {
        "type": "string",
        "description": "The television network on which the series premiered."
      }
    },
    "required": [
      "show_title",
      "creator",
      "star_actor",
      "premiere_date",
      "network"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
