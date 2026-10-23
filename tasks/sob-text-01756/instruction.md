{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nEat, Pray, Queef: \"Eat, Pray, Queef\" is the fourth episode of the thirteenth season of the American animated television series \"South Park\".  The 185th overall episode of the series, it originally aired on Comedy Central in the United States on April 1, 2009.  In the episode, the men and boys of South Park become infuriated when the fart-joke oriented \"Terrance and Phillip\" show is replaced with the \"Queef Sisters\", a show devoted to queef jokes.  The women and girls of South Park accuse them of holding a sexist double standard when it comes to women queefing and men farting.\n\nConjoined Fetus Lady: \"Conjoined Fetus Lady\" is the fifth episode in the second season of the American animated television series \"South Park\".  The 18th episode of the series overall, it originally aired on Comedy Central in the United States on June 3, 1998.  The episode was written by series co-creators Trey Parker and Matt Stone, along with David R. Goodman, and directed by Parker.  In the episode, South Park Elementary's dodgeball team travels to China to compete for the dodgeball championship, while the town of South Park pays tribute to the school nurse, who is living with conjoined twin myslexia.\n\nChickenlover: \"Chickenlover\" is the fourth episode in the second season of the American animated television series \"South Park\".  The 16th episode of the series overall, it originally aired on Comedy Central in the United States on May 27, 1998.  The episode was written by series co-creators Trey Parker and Matt Stone, along with David R. Goodman, and directed by Parker.  In the episode, Officer Barbrady resigns as South Park's only police officer because of his illiteracy.  Anarchy ensues, just as chickens are mysteriously being molested across South Park.  Barbrady enlists the help of the boys to learn to read and discover who is molesting the chickens.  Cartman, meanwhile, masquerades as a police officer.\n\nEverybody Draw Mohammed Day: Everybody Draw Mohammed Day (or \"Draw Mohammed Day\") was a 2010 event in support of artists threatened with violence for drawing representations of the Islamic prophet Muhammad.  It stemmed from a protest against censorship of the American television show \"South Park\" episode \"201\", led by the show's distributor Comedy Central, in response to death threats that had been made against some of those responsible for two segments broadcast in April 2010.  A drawing representing Mohammed was posted on the Internet on April 20, 2010 with a message suggesting that \"everybody\" create a drawing depicting Mohammad on May 20 in support of free speech.\n\nHooked on Monkey Fonics: \"Hooked on Monkey Fonics\" is episode 12 of season 3 and the 43rd overall episode of Comedy Central's animated series \"South Park\".  It originally aired on November 10, 1999.  It features issues of homeschooling and phonics, a method of teaching children to read.  This is the final episode of South Park to feature the voice talents of Mary Kay Bergman, who committed suicide the day after the episode aired.  The final episode to use her dialogue was \"Starvin' Marvin in Space\" which ended production shortly before her death.\n\nSouth Park Is Gay!: \"South Park Is Gay!\"  is the eighth episode of the seventh season and the 104th overall episode of the American animated television series \"South Park\".  It originally aired on Comedy Central in the United States on October 22, 2003.  In it, Kyle struggles to understand a new metrosexual fad that has sprung around the men and boys of South Park and is the only one who does not want to conform to it.  The episode features a parody of the TV show, \"Queer Eye for the Straight Guy\".\n\nSummer Sucks: \"Summer Sucks\" is the eighth episode in the second season of the American animated television series \"South Park\".  The 21st episode of the series overall, it originally aired on Comedy Central in the United States on June 24, 1998.  The episode was written by series co-creator Trey Parker, along with Nancy M. Pimental, and directed by Parker.  Jonathan Katz makes a guest appearance as himself.  In the episode, Summer arrives and the town of South Park celebrate Independence Day by building and lighting a giant snake firework, since regular fireworks are illegal.  Jimbo and Ned travel to Mexico to obtain fireworks, while the giant snake threatens to destroy the country.  Meanwhile, Mr. Garrison struggles to cope with the loss of his hand puppet, Mr. Hat.\n\nMyMFB: MyMFB (previously MillatFacebook) is a Muslim-oriented social networking website.  It was launched in May 2010 in response to a controversial group on Facebook entitled \"Everybody Draw Mohammed Day\" and Pakistan's block of Facebook in response.\n\n201 (South Park): \"201\" is the sixth episode of the fourteenth season of \"South Park\", and the 201st overall episode of the series.  It originally aired on Comedy Central in the United States on April 21, 2010.  The episode continued multiple storylines from the previous episode, \"200\", in which a group of angry celebrities demand South Park produce the Muslim prophet Muhammad.  In \"201\", a superhero-like group of religious figures team up to save South Park from the celebrities and their monster Mecha-Streisand, while Eric Cartman learns the true identity of his father.\n\nFatbeard: \"Fatbeard\" is the seventh episode of the thirteenth season of the American animated television series \"South Park\".  The 188th overall episode of the series, it originally aired on Comedy Central in the United States on April 22, 2009 and in the United Kingdom on April 24, 2009.  It was the mid-season finale, marking the final \"South Park\" episode for six months.  In the episode, Cartman misinterprets news reports about piracy in the Indian Ocean to mean the return of the classic era of swashbuckling pirates, and misleads a handful of South Park boys to voyage to Mogadishu to start a pirate crew.\n\nQuestion: What episode of South Park, aired on April 21, 2010, started the \"Draw Mohammed Day\" event? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"episode_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the South Park episode.\"\n    },\n    \"air_date\": {\n      \"type\": \"string\",\n      \"format\": \"date\",\n      \"description\": \"The original air date of the episode.\"\n    },\n    \"season_number\": {\n      \"type\": \"integer\",\n      \"description\": \"The season number of the episode.\"\n    },\n    \"overall_episode_number\": {\n      \"type\": \"integer\",\n      \"description\": \"The overall episode number in the series.\"\n    },\n    \"related_event\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"event_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the event triggered or related to the episode.\"\n        },\n        \"event_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of event, e.g., 'protest', 'social media campaign'.\"\n        },\n        \"reason_for_event\": {\n          \"type\": \"string\",\n          \"description\": \"The reason or cause for the event related to the episode.\"\n        }\n      },\n      \"required\": [\n        \"event_name\",\n        \"event_type\",\n        \"reason_for_event\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"episode_title\",\n    \"air_date\",\n    \"season_number\",\n    \"overall_episode_number\",\n    \"related_event\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "episode_title": {
        "type": "string",
        "description": "The title of the South Park episode."
      },
      "air_date": {
        "type": "string",
        "format": "date",
        "description": "The original air date of the episode."
      },
      "season_number": {
        "type": "integer",
        "description": "The season number of the episode."
      },
      "overall_episode_number": {
        "type": "integer",
        "description": "The overall episode number in the series."
      },
      "related_event": {
        "type": "object",
        "properties": {
          "event_name": {
            "type": "string",
            "description": "The name of the event triggered or related to the episode."
          },
          "event_type": {
            "type": "string",
            "description": "The type of event, e.g., 'protest', 'social media campaign'."
          },
          "reason_for_event": {
            "type": "string",
            "description": "The reason or cause for the event related to the episode."
          }
        },
        "required": [
          "event_name",
          "event_type",
          "reason_for_event"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "episode_title",
      "air_date",
      "season_number",
      "overall_episode_number",
      "related_event"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
