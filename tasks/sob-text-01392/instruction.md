{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPhilip Wheelwright: Philip Ellis Wheelwright (July 6, 1901 – January 6, 1970) was an American philosopher, classical scholar and literary theorist.  He was born in Elizabeth, New Jersey, on July 6, 1901, and died in Santa Barbara, California on January 6, 1970, four years after his retirement from the University of California, where he had been a professor since 1954.\n\nHopscotch (film): Hopscotch is a 1980 American cold war comedy-drama film, produced by Edie Landau and Ely A. Landau, directed by Ronald Neame, that stars Walter Matthau, Glenda Jackson, Sam Waterston, Ned Beatty, and Herbert Lom.  The screenplay was written by Bryan Forbes and Brian Garfield, based on Garfield's novel of the same name.\n\nJoe E. Brown: Joe E. Brown (July 28, 1891 – July 6, 1973) was an American actor and comedian, remembered for his amiable screen persona, comic timing, and enormous elastic-mouth smile.  He was one of the most popular American comedians in the 1930s and 1940s, with successful films like \"A Midsummer Night's Dream\", \"Earthworm Tractors\", and \"Alibi Ike\".  In his later career Brown starred in \"Some Like It Hot\" (1959), as Osgood Fielding III, in which he utters the famous punchline, \"Well, nobody's perfect.\"\n\nEve Unsell: Eve Unsell (1887 – July 6, 1937) was an American screenwriter.  She wrote for 96 films between 1914 and 1933.  She was born in Chicago, Illinois, and died in Hollywood, California.  Eve was an American scenarist who was known to also use the pseudonym Oliver W. Geoffreys as well as E.M. Unsell.  She was born in Chicago, Illinois, and died on July 6, 1937.  There is little documentation of her private life except that she was married in 1911 until her death, to a man named Lester Blankfield.  Eve Unsell was a professional in her career as a scenarist, overcoming many challenges along the way.  Eve wrote for over 96 films in her lifetime, and edited over ten.  Some of her most famous screen writes turned into productions include \"Shadows\" (1922), \"The Ancient Mariner\" (1925), \"The Plastic Age\" (1925), and \"The Spirit of Youth\" (1929).  Although she was most famous for her work in scenario writing she can also be given credit as an adapter, company director, editor, play reader, screenwriter, theatre actress, and writer.  She helped in the writing of many novels as long as editing many different pieces from literature to theatrical writing.\n\nWillie Stevenson Glanton: Willie Stevenson Glanton (March 19, 1922 – July 6, 2017) was an American lawyer and politician in the state of Iowa.  Glanton was born in Hot Springs, Arkansas and attended Tennessee State University and Robert H. Terrell Law School.  She moved to Iowa in 1951 and in 1953, became the second African American woman to be admitted to the Iowa Bar.  She was elected to the Iowa House of Representatives in 1964, becoming the first African American woman to sit in that body.  She resigned in 1966 to work as a lawyer with the United States Small Business Administration.  She was married to Judge Luther T. Glanton, Jr. and had one son, Luther T., III.  In 1986, she was inducted into the Iowa Women's Hall of Fame.  In 2010, she was named one of the ten most influential black Iowans by the \"The Des Moines Register\".  She died in Des Moines on July 6, 2017.\n\nStanley DeSantis: Stanley DeSantis (July 6, 1953 – August 16, 2005) was an American actor and businessman.  He appeared in 15 motion pictures, the last of which being \"The Aviator\", in which he portrayed Louis B. Mayer.  He also made many television appearances.  His death was credited in a dedication for the season two finale of \"Entourage\", in which had guest starred in three episodes.\n\nNed Beatty: Ned Thomas Beatty (born July 6, 1937) is an American actor.  He has appeared in more than 160 films and has been nominated for an Academy Award, two Emmy Awards, an MTV Movie Award for Best Villain and a Golden Globe Award; he also won a Drama Desk Award.\n\nCliff Bowes: Cliff Bowes (November 11, 1894 – July 6, 1929), also known as Clifford Bowes, was an American silent film actor.  Born on November 14, 1894 in Pueblo, Colorado, Bowes began his film career with a small, un-credited role in the 1916 film short \"His Lying Heart\", starring Ford Sterling.  When the United States entered World War I, Bowes served as a navy pilot.  By the end of the decade he was starring in shorts, and during the 1920s he made over 100 of them.  In 1920, he would have the featured role of Waldo Pennanink in his only full-length film, \"Up in Mary's Attic\".  In 1923 he began starring in the Education Pictures film short series \"Mermaid Comedies\", which ran through 1925.  He is best remembered for another Education series, \"Cameo Comedies\", which co-starred Virginia Vance, which also began in 1923 and ran through 1929.  His final screen performance was in a supporting role in 1929's \"Stage Struck Susie\", starring Frances Lee.  At the age of 34, Bowes died on July 6, 1929, shortly after the release of \"Stage Struck Susie\", and was buried in Forest Lawn Memorial Park in Glendale, California.\n\nPatrick McVey: Patrick \"Pat\" McVey (March 17, 1910 – July 6, 1973) was an American actor who starred in three television series between 1950 and 1961, \"Big Town\", \"Boots and Saddles\", and \"Manhunt\".\n\nAdam Busch: Adam Richard Busch (born July 6, 1978) is an American actor, film director and singer best known starring as Warren Mears on the television series \"Buffy the Vampire Slayer\".  He also starred as Neal in the TBS comedy \"Men at Work\".  He appears in the webshow \"MyMusic\" on YouTube as Indie.\n\nQuestion: Hopscotch starred which American actor who was born on July 6?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor who starred in the film.\"\n    },\n    \"actor_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the actor.\"\n    },\n    \"actor_birth_date\": {\n      \"type\": \"string\",\n      \"description\": \"The birth date of the actor.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"actor_name\",\n    \"actor_nationality\",\n    \"actor_birth_date\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "actor_name": {
        "type": "string",
        "description": "The name of the actor who starred in the film."
      },
      "actor_nationality": {
        "type": "string",
        "description": "The nationality of the actor."
      },
      "actor_birth_date": {
        "type": "string",
        "description": "The birth date of the actor."
      }
    },
    "required": [
      "film_title",
      "actor_name",
      "actor_nationality",
      "actor_birth_date"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
