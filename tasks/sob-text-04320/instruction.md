{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBrendan Hunt (actor): Brendan Hunt is an American actor and writer known for roles in the films \"We're the Millers\" (2013) and \"Horrible Bosses 2\" (2014) as well as voicing two characters in the video game \"Fallout 4\" (2015).\n\nChristoph Waltz: Christoph Waltz (] ; born 4 October 1956 in Vienna) is an Austrian-German actor.  Waltz is widely known for his works with American filmmaker Quentin Tarantino, he received acclaim for portraying SS-Standartenführer Hans Landa in \"Inglourious Basterds\" (2009) and bounty hunter Dr. King Schultz in \"Django Unchained\" (2012).  For both performances, he earned an Academy Award, BAFTA Award and Golden Globe Award for Best Supporting Actor.  Waltz also received the Best Actor Award at the Cannes Film Festival and a Screen Actors Guild Award for his portrayal of Landa.\n\nBrandon Richardson: Brandon Quantavius Richardson (born September 23, 1984) is an American actor.  He has played roles in \"Regular Show\", \"The Heat\", \"Meet the Browns\", \"\", \"Magic Mike XXL\", \"Horrible Bosses 2\" and \"Jurassic World\".  He is known for 2011 VH1 reality television \"Tough Love\" starring Steven Ward.\n\nShawn Robinson: Shawn Robinson (1974 – July 28, 2015) was an American stuntman who performed stunts in over the span of 20 years, including films such as \"Guardians of the Galaxy\", the \"Transformers\" film series, \"Hook\", \"Behind Enemy Lines\", \"War of the Worlds\" and more recently \"\" and \"Horrible Bosses 2\".  In television, Robinson took part in episodes of \"Criminal Minds\", \"Lost\" and \"\".  His father was legendary stuntman Dar Robinson.\n\nHorrible Bosses: Horrible Bosses is a 2011 American black comedy film directed by Seth Gordon, written by Michael Markowitz, John Francis Daley and Jonathan Goldstein, based on a story by Markowitz.  It stars Jason Bateman, Charlie Day, Jason Sudeikis, Jennifer Aniston, Colin Farrell, Kevin Spacey and Jamie Foxx.  The plot follows three friends, played by Bateman, Day and Sudeikis, who decide to murder their respective overbearing, abusive bosses, portrayed by Spacey, Aniston and Farrell.\n\nHorrible Bosses 2: Horrible Bosses 2 is a 2014 American comedy film directed by Sean Anders and written by Anders and John Morris.  A sequel to 2011's \"Horrible Bosses\", the film stars Jason Bateman, Charlie Day, Jason Sudeikis, Jennifer Aniston, Jamie Foxx, Chris Pine, and Christoph Waltz.  It was released on November 26, 2014 by Warner Bros.  Pictures.  The film grossed $107.7 million worldwide.\n\nJason Sudeikis: Daniel Jason Sudeikis ( ; born September 18, 1975) is an American actor, comedian and screenwriter.  He began his career in improv comedy.  In 2003, he was hired as a sketch writer for \"Saturday Night Live\" and was a cast member from 2005 to 2013.  He has appeared on television in \"30 Rock\", \"The Cleveland Show\", \"Eastbound & Down\", \"The Last Man on Earth\", and other shows.  He starred in the films \"Horrible Bosses\" (2011), \"Hall Pass\" (2011), \"We're the Millers\" (2013), \"Horrible Bosses 2\" (2014), \"Sleeping with Other People\" (2015), \"Tumbledown\" (2015), \"The Book of Love\" (2016) and \"Race\" (2016).\n\nJason Bateman: Jason Kent Bateman (born January 14, 1969) is an American actor, director, and producer.  He began acting on television in the early 1980s on \"Little House on the Prairie\", and in the sitcoms \"Silver Spoons\" and \"The Hogan Family\".  In the 2000s, he became known for his role of Michael Bluth using deadpan comedy in the critically acclaimed sitcom \"Arrested Development\", for which he won a Golden Globe and a Satellite Award.  He has had starring roles in the films \"Juno\" (2007), \"Hancock\" (2008), \"Up in the Air\" (2009), \"The Switch\" (2010), \"Paul\" (2011), \"Horrible Bosses\" (2011), \"The Change-Up\" (2011), \"Identity Thief\" (2013), \"Bad Words\" (2013), \"Horrible Bosses 2\" (2014), \"The Gift\" (2015), and \"Zootopia\" (2016), as well as the 2017 Netflix series \"Ozark\".\n\nKeeley Hazell: Keeley Rebecca Hazell (born 18 September 1986) is an English glamour model, actress.  Hazell became one of Britain's most successful glamour models , working with brands such as Page 3, \"FHM\", \"Loaded\", \"Nuts\" and \"Zoo Weekly\".  She has also made numerous television appearances and has, more recently, focused on her acting career, appearing in films such as \"Horrible Bosses 2\".\n\nMichael Markowitz: Michael Markowitz (born August 15, 1961) is a writer, producer, and actor who began his comedy career in The Mee-Ow Show, an improv group at Northwestern University.  Some projects he has worked on include \"Duckman\", \"Becker\", and the films \"Horrible Bosses\", \"Horrible Bosses 2\" and \"Boob Job\".  He has collaborated several times in the past with Jason Alexander.  As an actor, he appeared in the films \"The Flamingo Kid\" and \"Last Resort\", and the TV shows \"Becker\" and \"World Cup Comedy\".\n\nQuestion: Which actor from Horrible Bosses 2 is an Austrian-German actor?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor.\"\n    },\n    \"nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the actor.\"\n    },\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film the actor appeared in.\"\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"nationality\",\n    \"film_title\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor."
      },
      "nationality": {
        "type": "string",
        "description": "The nationality of the actor."
      },
      "film_title": {
        "type": "string",
        "description": "The title of the film the actor appeared in."
      }
    },
    "required": [
      "actor_name",
      "nationality",
      "film_title"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
