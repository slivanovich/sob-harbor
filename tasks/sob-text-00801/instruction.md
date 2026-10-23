{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nOblivion (2013 film): Oblivion is a 2013 American post-apocalyptic science fiction film based on Joseph Kosinski's unpublished Radical Publishing graphic novel of the same name.  The film was co-produced and directed by Kosinski.  It stars Tom Cruise, Morgan Freeman, Andrea Riseborough, and Olga Kurylenko.  The film was released in the U.S. on April 19, 2013.  According to Kosinski, \"Oblivion\" pays homage to science fiction films of the 1970s.\n\nJean-Marc Vallée: Jean-Marc Vallée (born March 9, 1963) film director, screenwriter, and film editor from Québec, Canada.  After studying film at the Université du Québec à Montréal, Vallée went on to make a number of acclaimed short films, including \"Stéréotypes\" (1991), \"Les Fleurs magiques\" (1995), and \"Les Mots magiques\" (1998).\n\nMarc-André Grondin: Marc-André Grondin (born March 11, 1984) is a Canadian actor, best known to date as \"Zachary Beaulieu\" in Jean-Marc Vallée's film \"C.R.A.Z.Y.\" (2005), for which he won a Jutra award for best actor.  He was born in Montreal, Quebec.\n\nFrançois Boulay: François Boulay is a Canadian film and television screenwriter, best known as cowriter with Jean-Marc Vallée of the 2005 film \"C.R.A.Z.Y.\" and as a writer for the Quebec television drama series \"Providence\".\n\nList of accolades received by The Young Victoria: \"The Young Victoria\" is a 2009 period drama film directed by Jean-Marc Vallée and written by Julian Fellowes.  It centered on the early life and reign of Queen Victoria, including her relationship with her husband, Prince Albert.  The film starred Emily Blunt and Rupert Friend among a large ensemble cast.  Martin Scorsese, Graham King, and Sarah, Duchess of York served as its producers.  A GK Films production, \"The Young Victoria\" was distributed by Momentum Pictures in the United Kingdom and by Apparition in the United States.  Its world premiere was held on 5 February 2009 at the 59th Berlin International Film Festival while its UK premiere was held in London's Leicester Square on 3 March.  The film was screened throughout 2009 and early 2010 at film festivals in Toronto, Sudbury, Ontario, Chicago, Hamptons, New York, Vermont, San Francisco, Denver, and San Joaquin, California.  \"The Young Victoria\"' s theatrical release occurred on 6 March 2009 in the UK; it was released in a limited capacity in the US on 18 December 2009, and opened nationwide on Christmas Day.  It earned a worldwide gross of $27,409,889.\n\nJoseph Kosinski: Joseph Kosinski (born May 3, 1974) is an American television commercial and feature film director best known for his computer graphics and computer generated imagery work.  He made his big-screen directorial debut with the Disney Digital 3-D science fiction film \"\", the sequel to the 1982 film \"Tron\".  His previous work has primarily been with CGI related television commercials including the \"Starry Night\" commercial for \"Halo 3\" and the award-winning \"Mad World\" commercial for \"Gears of War\".\n\nC.R.A.Z.Y.: C.R.A.Z.Y. is a 2005 French-language Canadian coming-of-age drama film directed by Jean-Marc Vallée and co-written by Vallée and François Boulay.  It tells the story of Zac, a young gay man dealing with homophobia while growing up with four brothers and a conservative father in Quebec during the 1960s and 1970s.  The film employs an extensive soundtrack, featuring artists such as Pink Floyd, Patsy Cline and The Rolling Stones.\n\nYves Bélanger (cinematographer): Yves Bélanger (born July 7, 1960) is a Canadian cinematographer.  He has worked on films by directors such as Alain Desrochers and Xavier Dolan, and he is a frequent collaborator of Jean-Marc Vallée.  In 2016, he received a Canadian Screen Award for Best Cinematography for his work in \"Brooklyn\".\n\nTron: Legacy: Tron: Legacy is a 2010 American science fiction action film directed by Joseph Kosinski from a screenplay written by Adam Horowitz and Edward Kitsis, based on a story by Horowitz, Kitsis, Brian Klugman and Lee Sternthal.  It is a sequel to the 1982 film \"Tron\", whose director Steven Lisberger returned to produce.  The cast includes Jeff Bridges and Bruce Boxleitner reprising their roles as Kevin Flynn and Alan Bradley, respectively, as well as Garrett Hedlund, Olivia Wilde, Beau Garrett and Michael Sheen.  The story follows Flynn's son Sam, who responds to a message from his long-lost father and is transported into a virtual reality called the \"Grid\", where Sam, his father and the algorithm Quorra, must stop the malevolent program Clu from invading the human world.\n\nOnly the Brave (2017 film): Only the Brave is an upcoming American drama film directed by Joseph Kosinski and written by Ken Nolan and Eric Warren Singer.  Columbia Pictures will release the film on October 20, 2017.\n\nQuestion: What profession does Jean-Marc Vallée and Joseph Kosinski have in common?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"common_profession\": {\n      \"type\": \"string\",\n      \"description\": \"The profession shared by both individuals.\"\n    },\n    \"individuals\": {\n      \"type\": \"array\",\n      \"description\": \"Details about each individual and their listed professions.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the individual.\"\n          },\n          \"professions\": {\n            \"type\": \"array\",\n            \"description\": \"A list of professions attributed to the individual in the text.\",\n            \"items\": {\n              \"type\": \"string\"\n            }\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"professions\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"reasoning\": {\n      \"type\": \"string\",\n      \"description\": \"Explanation of how the common profession was identified.\"\n    }\n  },\n  \"required\": [\n    \"common_profession\",\n    \"individuals\",\n    \"reasoning\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "common_profession": {
        "type": "string",
        "description": "The profession shared by both individuals."
      },
      "individuals": {
        "type": "array",
        "description": "Details about each individual and their listed professions.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the individual."
            },
            "professions": {
              "type": "array",
              "description": "A list of professions attributed to the individual in the text.",
              "items": {
                "type": "string"
              }
            }
          },
          "required": [
            "name",
            "professions"
          ],
          "additionalProperties": false
        }
      },
      "reasoning": {
        "type": "string",
        "description": "Explanation of how the common profession was identified."
      }
    },
    "required": [
      "common_profession",
      "individuals",
      "reasoning"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
