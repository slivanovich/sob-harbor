{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBeauty and the Beast (2014 film): Beauty and the Beast (French: La Belle et la Bête ) is a 2014 Franco-German romantic fantasy film based on the traditional fairy tale of the same name by Gabrielle-Suzanne Barbot de Villeneuve.  Written by Christophe Gans and Sandra Vo-Anh and directed by Gans, the film stars Léa Seydoux as Belle and Vincent Cassel as the Beast.\n\nBrotherhood of the Wolf: Brotherhood of the Wolf (French: Le Pacte des loups ) is a 2001 French historical action horror film directed by Christophe Gans, co-written by Gans and Stéphane Cabel, and starring Samuel Le Bihan, Mark Dacascos, Émilie Dequenne, Monica Bellucci and Vincent Cassel.\n\nSpione: Spione ] (English title: Spies, under which title it was released in the United States) is a German silent espionage thriller written and directed by Fritz Lang in 1928.  Lang's wife, Thea von Harbou, worked as a co-writer.  The film was Lang's penultimate silent film and the first for his own production company; \"Fritz Lang-film GmbH\".  As in Lang's Mabuse films, such as \"\" and \"The Testament of Dr. Mabuse\", Rudolf Klein-Rogge plays a master criminal aiming for world domination.\n\nH.P. Lovecraft's: Necronomicon: H.P. Lovecraft's: Necronomicon, original title Necronomicon, also called Necronomicon: Book of the Dead or Necronomicon: To Hell and Back is an American anthology horror film released in 1993.  It was directed by Brian Yuzna, Christophe Gans and Shusuke Kaneko and was written by Gans, Yuzna, Brent V. Friedman, and Kazunori Itō.  The film stars Bruce Payne as Edward De Lapoer, Richard Lynch as Jethro De Lapoer, Jeffrey Combs as H. P. Lovecraft, Belinda Bauer as Nancy Gallmore, and David Warner as Dr. Madden.\n\nFritz Lang filmography: Fritz Lang was an Austrian film director, producer and screenwriter.  In Lang's early career he worked primarily as a screenwriter, finishing film scripts in four to five days.  Lang went on to direct popular films of the silent era including \"Metropolis\" and one of the first important German sound films \"M\".  Lang went on to direct some of the most important crime and film noir film of the American studio era, such as \"The Big Heat\".  Lang's final film work was an acting role as himself in Jean-Luc Godard's \"Contempt\".  Lang returned to America to live out his remaining years.\n\nFritz Lang: Friedrich Christian Anton \"Fritz\" Lang (December 5, 1890 – August 2, 1976) was an Austrian filmmaker, screenwriter, and occasional film producer and actor.  One of the best-known \"émigrés\" from Germany's school of Expressionism, he was dubbed the \"Master of Darkness\" by the British Film Institute.\n\nSilent Hill (film): Silent Hill is a 2006 horror film directed by Christophe Gans and written by Roger Avary, Gans, and Nicolas Boukhrief.  The film is an adaptation of Konami's video game series \"Silent Hill\".  It stars Radha Mitchell, Sean Bean, Laurie Holden, Deborah Kara Unger, Kim Coates, Tanya Allen, Alice Krige, and Jodelle Ferland.\n\nThe Tiger of Eschnapur (1959 film): The Tiger of Eschnapur, or in original German, \"Der Tiger von Eschnapur\", is a 1959 West German-French-Italian adventure film directed by Fritz Lang.  It is the first of two films comprising what has come to be known as \"Fritz Lang's Indian Epic\"; the other is \"The Indian Tomb\" \"(Das Indische Grabmal\").  Fritz Lang returned to Germany to direct these films, which together tell the story of a German architect, the Indian maharaja for whom he is supposed to build schools and hospitals, and the Eurasian dancer who comes between them.\n\nCrying Freeman (film): Crying Freeman is a 1995 Canadian action film, directed by Christophe Gans, based on the \"Portrait of a Killer\" arc of the best-selling manga of the same name by Kazuo Koike and Ryoichi Ikegami.  The film was shot in British Columbia in October 1994.\n\nChristophe Gans: Christophe Gans (born 11 March 1960) is a French film director, producer and screenwriter, who specializes in horror and fantasy movies.\n\nQuestion: Are Fritz Lang and Christophe Gans from the same country?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"director_1_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the first director.\"\n    },\n    \"director_1_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the first director.\"\n    },\n    \"director_2_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the second director.\"\n    },\n    \"director_2_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the second director.\"\n    },\n    \"are_from_same_country\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if both directors are from the same country, false otherwise.\"\n    }\n  },\n  \"required\": [\n    \"director_1_name\",\n    \"director_1_nationality\",\n    \"director_2_name\",\n    \"director_2_nationality\",\n    \"are_from_same_country\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "director_1_name": {
        "type": "string",
        "description": "The name of the first director."
      },
      "director_1_nationality": {
        "type": "string",
        "description": "The nationality of the first director."
      },
      "director_2_name": {
        "type": "string",
        "description": "The name of the second director."
      },
      "director_2_nationality": {
        "type": "string",
        "description": "The nationality of the second director."
      },
      "are_from_same_country": {
        "type": "boolean",
        "description": "True if both directors are from the same country, false otherwise."
      }
    },
    "required": [
      "director_1_name",
      "director_1_nationality",
      "director_2_name",
      "director_2_nationality",
      "are_from_same_country"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
