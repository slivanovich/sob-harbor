{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nParis Hilton: Paris Whitney Hilton (born February 17, 1981) is an American businesswoman, socialite, television and media personality, model, actress, singer, and DJ.  She is the great-granddaughter of Conrad Hilton, the founder of Hilton Hotels.  Born in New York City and raised there and in Beverly Hills, California, Hilton began her modeling career as a teenager when she signed with New York-based modelling development agency Trump Model Management.  Her lifestyle and rumored short-lived relationships made her a feature of entertainment news and tabloid magazines, and Hilton was proclaimed \"New York's leading It girl\" in 2001.  In 2003, a sex tape with Hilton and her then-boyfriend Rick Salomon, later released as \"1 Night in Paris\", was leaked to the public.  Released only three weeks before the premiere of the reality television series \"The Simple Life\", in which she starred alongside her long-time friend Nicole Richie, the sex tape became a media sensation.\n\nEllie Kemper: Elizabeth Claire Kemper (born May 2, 1980) is an American actress and comedian.  She gained prominence when she starred in the NBC series \"The Office\" as receptionist Erin Hannon for the final five seasons.  After her role in \"The Office\", she was cast in a leading role as Kimmy Schmidt in the Netflix comedy series \"Unbreakable Kimmy Schmidt\", for which she has received critical acclaim.  Kemper is also known for her supporting roles in the films \"Bridesmaids\" (2011) and \"21 Jump Street\" (2012).\n\nCarrie Kemper: Carrie Kemper is an American television writer who worked as a staff writer on the NBC sitcom \"The Office\".  She is the younger sister of actress Ellie Kemper.\n\nIranian sex tape scandal: The so-called Iranian sex tape scandal involves the public outcry and judicial proceedings against Zahra Amir Ebrahimi, an actress who appeared in the soap opera \"Nargess\", and an associate producer, accused of appearing together in an explicit sex tape, allegedly filmed for private consumption with a camcorder, a serious crime under Iranian law.  The actress denies that the tape is of her, while the film producer reportedly has claimed that it is him.  The scandal virtually ended the actress's career; she was banned from Iranian films in 2006.\n\nCelebrity sex tape: A celebrity sex tape is typically an amateur pornographic video recording involving one or more celebrity famous person(s) which has, intentionally or unintentionally, been made available publicly.  Such video tapes are often released without the consent of their subjects, and could damage celebrities' careers.  In 1988, a sex tape caused significant damage to Rob Lowe's career.\n\nUnbreakable Kimmy Schmidt: Unbreakable Kimmy Schmidt is an American television sitcom created by Tina Fey and Robert Carlock, starring Ellie Kemper in the title role, that has streamed on Netflix since March 6, 2015.  Originally set for a 13-episode first season on NBC for spring 2015, the show was sold to Netflix and given a two-season order.\n\nBridesmaids (2011 film): Bridesmaids is a 2011 American comedy film directed by Paul Feig, written by Annie Mumolo and Kristen Wiig, and produced by Judd Apatow, Barry Mendel and Clayton Townsend.  The plot centers on Annie (Wiig), who suffers a series of misfortunes after being asked to serve as maid of honor for her best friend, Lillian, played by Maya Rudolph.  Rose Byrne, Melissa McCarthy, Ellie Kemper, and Wendi McLendon-Covey co-star as Lillian's bridesmaids, with Chris O'Dowd, Rebel Wilson, Matt Lucas, Michael Hitchcock, and Jill Clayburgh, in her final film appearance, in supporting roles.\n\nSex Tape (film): Sex Tape is a 2014 American comedy film directed by Jake Kasdan and written by Kate Angelo, Jason Segel, and Nicholas Stoller.  Starring Segel, Cameron Diaz, Rob Corddry, Ellie Kemper, and Rob Lowe, the film was released on July 18, 2014, by Columbia Pictures.\n\nList of Unbreakable Kimmy Schmidt episodes: \"Unbreakable Kimmy Schmidt\" is an American sitcom created by Tina Fey and Robert Carlock, starring Ellie Kemper in the title role, that has streamed on Netflix since March 6, 2015.  Originally set for a 13-episode first season on NBC for spring 2015, the show was sold to Netflix and given a two-season order.\n\nSpooked (The Office): \"Spooked\" is the fifth episode of the eighth season of the American comedy television series \"The Office\", and the show's 157th episode overall.  The episode originally aired on NBC in the United States on October 27, 2011.  It was written by Carrie Kemper, sister of cast member Ellie Kemper, and directed by Randall Einhorn.  The episode guest starred David Mazouz.\n\nQuestion: Sex Tape co-star Ellie Kemper starred in what NBC series?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actress in question.\"\n    },\n    \"film_co_starred_in\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film where the person was a co-star.\"\n    },\n    \"nbc_series_starred_in\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the NBC series the person starred in.\"\n    },\n    \"role_in_nbc_series\": {\n      \"type\": \"string\",\n      \"description\": \"The character name played by the person in the NBC series.\"\n    },\n    \"seasons_in_nbc_series\": {\n      \"type\": \"integer\",\n      \"description\": \"The number of seasons the person starred in the NBC series.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"film_co_starred_in\",\n    \"nbc_series_starred_in\",\n    \"role_in_nbc_series\",\n    \"seasons_in_nbc_series\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the actress in question."
      },
      "film_co_starred_in": {
        "type": "string",
        "description": "The name of the film where the person was a co-star."
      },
      "nbc_series_starred_in": {
        "type": "string",
        "description": "The name of the NBC series the person starred in."
      },
      "role_in_nbc_series": {
        "type": "string",
        "description": "The character name played by the person in the NBC series."
      },
      "seasons_in_nbc_series": {
        "type": "integer",
        "description": "The number of seasons the person starred in the NBC series."
      }
    },
    "required": [
      "person_name",
      "film_co_starred_in",
      "nbc_series_starred_in",
      "role_in_nbc_series",
      "seasons_in_nbc_series"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
