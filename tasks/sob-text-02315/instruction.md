{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTempest (Deftones song): \"Tempest\" is the second single by Sacramento, California-based alternative metal band Deftones, from their seventh studio album, \"Koi No Yokan\".  The song debuted on PureVolume's official website on October 3, 2012 along with a video featuring band members Chino Moreno and Sergio Vega giving some insight regarding the track.  The song's lyrical content is representative of the supposed end of the world that would have occurred on December 21, 2012, according to various myths related to the Mayan calendar.  It was featured in the trailer for the film \"Jack the Giant Slayer\" and an episode of \"The Following\".  An instrumental version made an appearance in the film \"Furious 7\".\n\nBryan Singer: Bryan Jay Singer (born September 17, 1965) is an American film director, film producer, writer, and actor.  He is the founder of Bad Hat Harry Productions and he has produced or co-produced almost all of the films he has directed.\n\nJack the Giant Killer (2013 direct-to-video film): Jack the Giant Killer is a 2013 American fantasy film produced by The Asylum and directed by Mark Atkins.  A modern take of the fairy tales \"Jack the Giant Killer\" and \"Jack and the Beanstalk\", the film stars Ben Cross and Jane March.  It is a mockbuster of \"Jack the Giant Slayer\".  It was released on DVD in the UK as The Giant Killer.\n\nElia Petridis: Elia Petridis (born in Paris, France) is a Lebanese-Greek film director and screenwriter, best known for \"The Man Who Shook the Hand of Vicente Fernandez\", and for his work in transmedia and virtual reality production.  He is the founder and creative director of film production company Filmatics and the transmedia production company Fever Content.\n\nEleanor Tomlinson: Eleanor May Tomlinson (born 19 May 1992) is an English actress, known for her roles as Princess Isabelle in \"Jack the Giant Slayer\" (2013), Isabel Neville in \"The White Queen\", and Demelza Poldark in \"Poldark\".\n\nJack the Giant Slayer: Jack the Giant Slayer (previously titled Jack the Giant Killer) is a 2013 American heroic fantasy adventure film based on the British fairy tales \"Jack the Giant Killer\" and \"Jack and the Beanstalk\".  The film is directed by Bryan Singer with a screenplay written by Darren Lemke, Christopher McQuarrie and Dan Studney and stars Nicholas Hoult, Eleanor Tomlinson, Stanley Tucci, Ian McShane, Bill Nighy, and Ewan McGregor.  The film tells the story of Jack, a young farmhand who must rescue a princess from a race of giants after inadvertently opening a gateway to their land in the sky.\n\nA. J. Carter: A. J. Carter (born 21 September 1980 as Adrian John Carter) is an Australian film director, screenwriter and producer.  In his recent emerging career as a film director, his debut narrative short film Ronan's Escape awarded him and his production company a total of 13 international film award nominations and 10 award wins including several 'Best Film and \"Best Director\" awards.  He is also the founder of the Smooth Motion Media Group, formerly known as Smooth Motion Films.  Smooth Motion Media Group is based in Los Angeles, California, with two production company subsidiaries Dark Arts Entertainment (Motion Picture Film & Scripted Television production), and Primordial Entertainment (Reality, Science & Documentary Television).\n\nGeorge S. J. Faber: George Stephen John Faber (born 30 November 1959 in Kensington, London) is a British television producer.  He was the founder and joint managing director of Company Pictures, one of the UK's largest independent drama production companies, twice winner of Best Independent Production Company at the Broadcast Awards and also winner of Best European Production Company at the Monte Carlo TV Festival.  In 2014 he founded \"The Forge\" which produced \"National Treasure\" starring Robbie Coltrane, Julie Walters and Andrea Riseborough.\n\nChristopher McQuarrie: Christopher McQuarrie (born 1968) is an American screenwriter, director and producer.  A regular collaborator of director Bryan Singer, he co-wrote the screenplay of Singer's \"Public Access\", wrote the screenplay for \"The Usual Suspects\", co-wrote and produced \"Valkyrie\" and co-wrote \"Jack the Giant Slayer\" and \"Edge of Tomorrow\".\n\nKyle Schickner: Kyle Schickner is an American film producer, writer, director, actor and a bisexual civil rights activist.  He is the founder of FenceSitter Films, a Production company devoted to entertainment for women, and sexual and ethnic minorities.  He currently lives and works in Los Angeles, where he directs films, music videos, a Web series and commercials for his production company FenceSitterFilms.\n\nQuestion: The director of Jack the Giant Slayer is the founder of what production company?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film mentioned in the question.\"\n    },\n    \"film_director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the specified film.\"\n    },\n    \"director_role\": {\n      \"type\": \"string\",\n      \"description\": \"The role of the person in relation to the film.\"\n    },\n    \"production_company_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the production company founded by the director.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_director\",\n    \"director_role\",\n    \"production_company_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film mentioned in the question."
      },
      "film_director": {
        "type": "string",
        "description": "The director of the specified film."
      },
      "director_role": {
        "type": "string",
        "description": "The role of the person in relation to the film."
      },
      "production_company_name": {
        "type": "string",
        "description": "The name of the production company founded by the director."
      }
    },
    "required": [
      "film_title",
      "film_director",
      "director_role",
      "production_company_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
