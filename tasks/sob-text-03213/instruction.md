{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMackenzie Phillips: Laura Mackenzie Phillips (born November 10, 1959) is an American actress and singer best known for her roles in \"American Graffiti\", as rebellious teenager Julie Mora Cooper Horvath on the sitcom \"One Day at a Time\", and for the Disney Channel science fiction show \"So Weird\".\n\nGracie Gilbert: Gracie Gilbert (born 20 October 1992) is an Australian actress, best known for her role as Tammy Lane in the Fox8 teen drama series, \"SLiDE\", as Vicki in \"Lockie Leonard\", and as Annie in \"Love Child\".\n\nDiana Ross: Diana Ernestine Earle Ross (born March 26, 1944) is an American singer, songwriter, actress, and record producer.  Born and raised in Detroit, Michigan, Ross rose to fame as the lead singer of the vocal group The Supremes, which, during the 1960s, became Motown's most successful act, and is to this day the United States' most successful vocal group, as well as one of the world's best-selling girl groups of all time.  Ross' success as lead singer of The Supremes made it possible for future African-American R&B and soul acts to find mainstream success.  The group released a record-setting twelve number-one hit singles on the US \"Billboard\" Hot 100, including \"Where Did Our Love Go\", \"Baby Love\", \"Come See About Me\", \"Stop!  In the Name of Love\", \"You Can't Hurry Love\", \"You Keep Me Hangin' On\", \"Love Child\", and \"Someday We'll Be Together\".\n\nMiranda Tapsell: Miranda Tapsell (born 11 June 1987) is an Indigenous Australian actress of both stage and screen, best known for her role as Cynthia in the Wayne Blair film, \"The Sapphires\" and her award-winning 2015 performance as Martha Tennant in the Channel 9 drama series, \"Love Child\".  2016 played Fatima in the Stan series \"Wolf Creek\".\n\nCourtney Love filmography: Courtney Love is an American musician and actress who began her professional career in film in 1986 with a supporting role in Alex Cox's \"Sid and Nancy\" (1986); she had prior studied film with experimental director George Kuchar at the San Francisco Art Institute in 1984, and appeared in one of Kuchar's short films.  After pursuing music and having a successful career as the frontwoman of alternative rock band Hole, Love also had intermittent roles in films, most notably receiving critical attention for her performance as Althea Flynt in Miloš Forman's 1996 biopic \"The People vs. Larry Flynt\", which earned her a Golden Globe Nomination for Best Actress, as well as awards from the Boston, Chicago, New York, and Los Angeles film critics associations.  Love later appeared among an ensemble cast in \"200 Cigarettes\" (1998), as well as in a leading role in \"Man on the Moon\" (1999) alongside Jim Carrey, for which she received critical recognition.  She later appeared in several independent films and short subjects as well as the thriller \"Trapped\" (2002) alongside Charlize Theron and Kevin Bacon, and \"Julie Johnson\" (2001), for which she received an award for Best Actress at Los Angeles' gay and lesbian Outfest film festival.\n\nLove Child (1982 film): Love Child is a 1982 biopic based on the life of Terry Jean Moore.  The film stars Amy Madigan, Beau Bridges, and Mackenzie Phillips.\n\nAmy Madigan: Amy Marie Madigan (born September 11, 1950) is an American actress, producer, and singer.  She was nominated for the Academy Award for Best Supporting Actress for the 1985 film \"Twice in a Lifetime\".  Her other film credits include \"Love Child\" (1982), \"Places in the Heart\" (1984), \"Field of Dreams\" (1989), \"Uncle Buck\" (1989), \"The Dark Half\" (1993), \"Pollock\" (2000), and \"Gone Baby Gone\" (2007).  Madigan won the Golden Globe Award for Best Supporting Actress on Television and was nominated for the Primetime Emmy Award for Outstanding Lead Actress in a Miniseries or a Movie for her portrayal of Sarah Weddington in the 1989 television film \"Roe vs. Wade\".\n\nMelinda Clarke: Melinda Patrice \"Mindy\" Clarke (born April 24, 1969) is an American actress who has primarily worked in television.  Clarke is known for playing Faith Taylor on the daytime drama \"Days of Our Lives\", the manipulative and cunning Julie Cooper on \"The O.C.\", and the professional dominatrix Lady Heather on \"\".  From 2010 to 2013, she portrayed Amanda on the action-thriller television series \"Nikita\".  She was added as a recurring character on \"Vegas\" in 2013, and played in \"Dallas\" as Tracey McKay.\n\nValerie Bertinelli: Valerie Anne Bertinelli (born April 23, 1960) is an American actress.  She is known for her roles as Barbara Cooper Royer on the sitcom \"One Day at a Time\" (1975–84), Gloria on the religious drama series \"Touched by an Angel\" (2001–03), Melanie Moretti on the sitcom \"Hot in Cleveland\" (2010–15); and she also hosts the cooking series \"Valerie's Home Cooking\" and \"Kids Baking Championship\" on Food Network.\n\nSophie Hensser: Sophie Hensser is an Australian actress.  She is best known for her role as Megan on \"The Saddle Club\" and Vivian Macguire on Love Child.\n\nQuestion: Love Child is a 1982 biopic that stars what American actress who is best known for her role as Julie Cooper on the sitcom \"One Day at a Time\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actress_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the American actress.\"\n    },\n    \"nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the actress.\"\n    },\n    \"film_starred_in\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film the actress starred in.\"\n    },\n    \"film_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"best_known_role\": {\n      \"type\": \"string\",\n      \"description\": \"The specific role the actress is best known for on the sitcom.\"\n    },\n    \"best_known_show\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the sitcom the actress is best known for.\"\n    }\n  },\n  \"required\": [\n    \"actress_name\",\n    \"nationality\",\n    \"film_starred_in\",\n    \"film_year\",\n    \"best_known_role\",\n    \"best_known_show\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actress_name": {
        "type": "string",
        "description": "The full name of the American actress."
      },
      "nationality": {
        "type": "string",
        "description": "The nationality of the actress."
      },
      "film_starred_in": {
        "type": "string",
        "description": "The title of the film the actress starred in."
      },
      "film_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "best_known_role": {
        "type": "string",
        "description": "The specific role the actress is best known for on the sitcom."
      },
      "best_known_show": {
        "type": "string",
        "description": "The title of the sitcom the actress is best known for."
      }
    },
    "required": [
      "actress_name",
      "nationality",
      "film_starred_in",
      "film_year",
      "best_known_role",
      "best_known_show"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
