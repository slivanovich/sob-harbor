{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSusan Bissell: Susan Bissell is the Director of the Global Partnership to End Violence Against Children.  She was previously UNICEF's Child Protection Section chief.  She is a Doctor of Philosophy.  She does not oppose international adoption, but believes that it is preferable for abandoned children to be taken back by their previous families and advises governments to provide small monetary incentives to families who are willing to do so.  She opposes the concept that there is a global orphan crisis, and believes that \"the crisis is something else... a child protection crisis.\"  In 2000, her research on child labour in Bangladesh was published.  In 2007, she spoke at the Atlantic Canada Child Welfare Forum in Halifax Regional Municipality, Nova Scotia, Canada, saying that the country should prohibit all forms of corporal punishment in the home, including spanking.  In 2009, she spoke in Dar es Salaam, Tanzania, saying that steps needed to be taken in the country to address the causes of child labour.  She identified the abolishment of primary school tuition payments as a good way to address these causes.  In 2011, when UNICEF was criticized for not acting on non-governmental organizations' claims that there was systematic use of child labour in Uzbekistan, Bissell said, \"We're not police.  We're not monitors.\"  After acting in \"Taken\", a film about the trafficking of children, Liam Neeson was inspired to combat child abuse, and, in July 2013, Bissell voiced her belief that Neeson's work on this issue would be effective.\n\nTaken (film): Taken is a 2008 English-language French action thriller film directed by Pierre Morel, written by Luc Besson and Robert Mark Kamen, and starring Liam Neeson, Maggie Grace, Leland Orser, Jon Gries, David Warshofsky, Holly Valance, Katie Cassidy, Xander Berkeley, Olivier Rabourdin, Gérard Watkins, and Famke Janssen.\n\nThe Gunman (film): The Gunman is a 2015 action thriller film directed by Pierre Morel and written by Don Macpherson, Pete Travis and Sean Penn, based on the novel \"The Prone Gunman\" (French title: \"La position du tireur couché\") by Jean-Patrick Manchette.  It stars Penn, with Idris Elba, Ray Winstone, Mark Rylance, and Javier Bardem appearing in supporting roles.  The film is about Jim Terrier (Penn), a mercenary who assassinates the Minister of Mining of the Democratic Republic of Congo in 2006 on orders from multinational mining companies.  Eight years after Terrier has retired from mercenary work, he and the people close to him become the targets of hit squads sent by a powerful multinational security firm, and he must fight to stay alive.  The film was released on March 20, 2015 by Open Road Films.  It was a box office bomb, grossing just $24 million against its $40 million budget and seeing a poor critical reception.\n\nTransporter 2: Transporter 2 (French: Le Transporteur 2) is a 2005 English-language French action thriller film directed by Louis Leterrier and produced by Luc Besson.  It is the sequel to \"The Transporter\" (2002), and is followed by \"Transporter 3\" (2008).  The film stars Jason Statham, Alessandro Gassman, Amber Valletta, Kate Nauta, François Berléand, Matthew Modine, and Jason Flemyng.\n\nDistrict 13: District 13 (French title \"Banlieue 13\" or \"B13\"), is a 2004 French action film directed by Pierre Morel and written and produced by Luc Besson.  The film is notable for its depiction of parkour in a number of stunt sequences that were completed without the use of wires or computer generated effects.  Because of this, some film critics have drawn comparisons to the popular Thai film \"\".  David Belle, regarded as the founder of parkour, plays Leïto, one of the protagonists in the film.\n\nTaken 3: Taken 3 (sometimes stylized as TAK3N) is a 2015 English-language French action thriller film directed by Olivier Megaton and written by Luc Besson and Robert Mark Kamen.  It is the third and final installment in the \"Taken\" trilogy.  The film stars Liam Neeson, Forest Whitaker, Maggie Grace and Famke Janssen.  The film is set three years after the second film.\n\nThe Transporter: The Transporter (French: Le Transporteur) is a 2002 English-language French action thriller film directed by Corey Yuen and Louis Leterrier (who is credited as artistic director on the project), and written by Luc Besson, who was inspired by BMW Films' \"The Hire\" series.  The film stars Jason Statham as Frank Martin, a driver for hire – a mercenary \"transporter\" who will deliver anything, anywhere – no questions asked – for the right price.  It also stars Shu Qi as Lai Kwai.\n\nKiss of the Dragon: Kiss of the Dragon (\"Le Baiser mortel du dragon\" in French) is a 2001 English-language French action thriller film directed by Chris Nahon, written and produced by French filmmaker Luc Besson, and starring an international cast of Jet Li, Bridget Fonda, and Tchéky Karyo.  The film is based on a story by Li.\n\nFrom Paris with Love (film): From Paris with Love is a 2010 English-language French action film starring John Travolta and Jonathan Rhys Meyers and directed by Pierre Morel.  The screenplay was co-written by Luc Besson.  The film was released in the United States on February 5, 2010.\n\nOverdrive (2017 film): Overdrive is a 2017 action thriller film directed by Antonio Negret, produced by Michael Brandt, Derek Haas and Pierre Morel and the screenplay was written by Michael Brandt and Derek Haas.  The film stars Scott Eastwood, Freddie Thorp, Ana de Armas, and Gaia Weiss.  Principal photography began on January 4, 2016 in Paris and Marseille, France.  The film tells the story of Andrew and Garret Foster, young brothers who are skilled car thieves which having expertise in the most luxury cars, they both are sent to steal a Bugatti car at Southern France, but they are getting caught by the car's owner; a ruthless local crime lord.  In exchange for their life and for apology for attempting to steal his car, the crime lord forces the brothers into stealing a luxury Ferari car from the crime lord's arch-rival.\n\nQuestion: What film did the Director of the Global Partnership to End Violence Against Children act in that is a 2008 English-language French action thriller film directed by Pierre Morel?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film that matches the description.\"\n    },\n    \"film_attributes\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the film was released.\"\n        },\n        \"languages\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"The languages in which the film was made.\"\n        },\n        \"genres\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"The genres of the film.\"\n        },\n        \"director\": {\n          \"type\": \"string\",\n          \"description\": \"The director of the film.\"\n        }\n      },\n      \"required\": [\n        \"release_year\",\n        \"languages\",\n        \"genres\",\n        \"director\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"person_of_interest\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person mentioned in the question.\"\n        },\n        \"role_in_organization\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the person in their organization.\"\n        },\n        \"relationship_to_film\": {\n          \"type\": \"string\",\n          \"description\": \"How the person is related to the film, as described in the context.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role_in_organization\",\n        \"relationship_to_film\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_attributes\",\n    \"person_of_interest\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film that matches the description."
      },
      "film_attributes": {
        "type": "object",
        "properties": {
          "release_year": {
            "type": "integer",
            "description": "The year the film was released."
          },
          "languages": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "The languages in which the film was made."
          },
          "genres": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "The genres of the film."
          },
          "director": {
            "type": "string",
            "description": "The director of the film."
          }
        },
        "required": [
          "release_year",
          "languages",
          "genres",
          "director"
        ],
        "additionalProperties": false
      },
      "person_of_interest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the person mentioned in the question."
          },
          "role_in_organization": {
            "type": "string",
            "description": "The role of the person in their organization."
          },
          "relationship_to_film": {
            "type": "string",
            "description": "How the person is related to the film, as described in the context."
          }
        },
        "required": [
          "name",
          "role_in_organization",
          "relationship_to_film"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "film_attributes",
      "person_of_interest"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
