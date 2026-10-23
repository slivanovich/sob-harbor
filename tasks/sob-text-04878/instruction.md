{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMarian Seldes: Marian Hall Seldes (August 23, 1928 – October 6, 2014) was an American stage, film, radio, and television actress whose career spanned over 60 years.  A five-time Tony Award nominee, she won the Tony Award for Best Featured Actress in a Play for \"A Delicate Balance\" in 1967, and received subsequent nominations for \"Father's Day\" (1971), \"Deathtrap\" (1978–82), \"Ring Round the Moon\" (1999), and \"Dinner at Eight\" (2002).  She also won a Drama Desk Award for \"Father's Day\".  Her other Broadway credits included \"Equus\" (1974–77), \"Ivanov\" (1997), and \"Deuce\" (2007).  She was inducted into the American Theater Hall of Fame in 1995 and received the Special Tony Award for Lifetime Achievement in 2010.\n\nSarah Nicklin: Sarah Nicklin is an American stage, film and television actress.  Her career is strongly focused on independent films and she is known for her girl next door quality, strong emotional range, and ability to transform into dark damaged characters.  Her first notable film role was as Sister Kelley Wrath in the independent cult-hit Nun of That in 2009.  Since then she has received four \"best actress\" nominations for her roles in Exhumed, Choices, Debeaked, and Zombie Allegiance.  She has also starred in the cult hit \"Atomic Brain Invasion\".  She also played the leading role of Sarah Burke in the horror-suspense thriller \"Abandoned Dead\".\n\nUna Merkel: Una Merkel (December 10, 1903 – January 2, 1986) was an American stage, film, radio, and television actress.\n\nStockard Channing: Stockard Channing (born Susan Antonia Williams Stockard; February 13, 1944) is an American stage, film and television actress.  She is known for playing Betty Rizzo in the film \"Grease\" (1978) and First Lady Abbey Bartlet on the NBC television series \"The West Wing\" (1999–2006).  She is also known for originating the role of Ouisa Kittredge in the stage and film versions of \"Six Degrees of Separation\", for which she was nominated for a Tony Award and the Academy Award for Best Actress.\n\nBetty Buckley: Betty Lynn Buckley (born July 3, 1947) is an American stage, film and television actress, and singer.  She starred from 1977 to 1981 on the ABC series \"Eight is Enough\", before going on to win the 1983 Tony Award for Best Featured Actress in a Musical for her role as Grizabella in the original Broadway production of \"Cats\".  Her other musical roles include playing Norma Desmond in \"Sunset Boulevard\" from 1994 to 1996, in both London and New York, receiving an Olivier Award nomination.  She is a 2012 American Theater Hall of Fame inductee.\n\nConstance Bennett: Constance Campbell Bennett (October 22, 1904 – July 24, 1965) was an American stage, film, radio and television actress.  She was a major Hollywood star during the 1920s and 1930s and for a time during the early 1930s, she was the highest-paid actress in Hollywood, as well as one of the most popular.  Bennett frequently played society women, focusing on melodramas in the early 1930s and then taking more comedic roles in the late 1930s and 1940s.  She is best known today for her leading roles in \"What Price Hollywood? \" (1932), \"Topper\" (1937), \"Topper Takes a Trip\" (1938), and had a prominent supporting role in Greta Garbo's last film, \"Two-Faced Woman\" (1941).\n\nKristen Johnston: Kristen Johnston (born September 20, 1967) is an American stage, film, and television actress.  She is most famous for her role as Sally Solomon in the television series \"3rd Rock from the Sun\".  She also starred as Wilma Flintstone in \"The Flintstones in Viva Rock Vegas\" and as Holly Franklin in the sitcom \"The Exes\".\n\nHuddle (film): Huddle is a 1932 American Pre-Code film directed by Sam Wood and starring Ramon Novarro, Madge Evans, Ralph Graves and Una Merkel.  This was the first of two films Ramon Novarro would make in 1932, and his first after appearing in the acclaimed, successful \"Mata Hari\".\n\nRuth McDevitt: Ruth McDevitt (September 13, 1895 – May 27, 1976) was an American stage, film, radio and television actress.\n\nDinah Manoff: Dinah Beth Manoff (born January 25, 1956) is an American stage, film, and television actress and television director.  She is best known for her roles as Elaine Lefkowitz on \"Soap\", Marty Maraschino in the film \"Grease\", Libby Tucker in both the stage and film adaptations of \"I Ought to Be in Pictures\", for which she won a Tony award, and Carol Weston on \"Empty Nest\".  She has starred in numerous television movies and guest-starred on various television programs.  She mostly appeared on TV during the 1990s, but she has been seen in more recent theatrical films, such as \"The Amati Girls\" and \"Bart Got a Room\", and a co-starring role on \"State of Grace\".\n\nQuestion: What American stage, film, radio, and television actress starred in Huddle?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actress_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the actress.\"\n    },\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film the actress starred in.\"\n    },\n    \"nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the actress.\"\n    },\n    \"career_media_types\": {\n      \"type\": \"array\",\n      \"description\": \"A list of media types the actress's career spanned.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    }\n  },\n  \"required\": [\n    \"actress_name\",\n    \"film_title\",\n    \"nationality\",\n    \"career_media_types\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actress_name": {
        "type": "string",
        "description": "The full name of the actress."
      },
      "film_title": {
        "type": "string",
        "description": "The title of the film the actress starred in."
      },
      "nationality": {
        "type": "string",
        "description": "The nationality of the actress."
      },
      "career_media_types": {
        "type": "array",
        "description": "A list of media types the actress's career spanned.",
        "items": {
          "type": "string"
        }
      }
    },
    "required": [
      "actress_name",
      "film_title",
      "nationality",
      "career_media_types"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
