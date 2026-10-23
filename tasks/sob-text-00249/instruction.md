{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHank Zipzer's Christmas Catastrophe: Hank Zipzer's Christmas Catastrophe is a 2016 stand alone British Christmas movie based on the Hank Zipzer series of books by Henry Winkler and Lin Oliver and the TV series airing on CBBC.  The film will be airing on CBBC on 12 December 2016.  It is written by Joe Williams and is directed by Matt Bloom.  The film is produced by Kindle Entertainment in association with Walker Productions and DHX Media with support from Screen Yorkshire’s Yorkshire Content Fund.  It is the fourth movie based on a CBBC programme after \"\", \"Shaun the Sheep Movie\" and \"\".  It is the second movie based on a CBBC show, which has not been released in cinemas and only shown on TV after \"\"\n\nNevermore (novel): Nevermore is a historical mystery novel by William Hjortsberg.\n\nGray Matters (novel): Gray Matters is a science fiction novel by William Hjortsberg.\n\nCaravan to Vaccarès: Caravan to Vaccarès is a novel by author Alistair MacLean, originally published in 1969.  This novel is set in the Provence region of southern France.  The novel was originally written as a screenplay for producer Elliot Kastner.\n\nLegend (Tangerine Dream soundtrack): Legend is the eighth soundtrack album by the German band Tangerine Dream and their twenty-eighth overall.  It was released in 1986 for the North American theatrical version of the film \"Legend\".  It was issued a year earlier in Europe.  The film was written by William Hjortsberg, starred Tom Cruise, Mia Sara and Tim Curry, was produced by Arnon Milchan, directed by Ridley Scott and released domestically by Universal Studios.  The album was released on compact disc on 15 August 1995 through Varese Sarabande.\n\nFalling Angel: Falling Angel is a 1978 horror novel by William Hjortsberg.  Written in a hardboiled detective style with supernatural themes, it was adapted into the 1987 film \"Angel Heart\".\n\nMás sabe el diablo: Más Sabe el Diablo (Literally \"The Devil Knows More\", \"Falling Angel\" in English-speaking markets) is a Spanish-language telenovela produced by the United States-based television network Telemundo.  This melodrama features lovers embroiled in intrigue, betrayal, vengeance and unbridled passion.  It stars Gaby Espino, Jencarlos Canela and Miguel Varoni.  Telemundo says that about 1 million people tuned in each weeknight.\n\nAngel Heart: Angel Heart is a 1987 American neo-noir psychological horror and occult detective film based on William Hjortsberg's 1978 novel \"Falling Angel\".  Written and directed by Alan Parker, the film stars Mickey Rourke, Robert De Niro and Lisa Bonet.  The story follows Harry Angel (Rourke), a New York City private investigator hired to solve the disappearance of a man known as Johnny Favorite.  Angel's investigation takes him to New Orleans, where he becomes embroiled in a series of brutal occult-related murders.\n\nAdam Elliot: Adam Elliot (born 2 January 1972 in Berwick, Victoria, Australia) is an independent Australian stop-motion animation writer, director and producer based in Melbourne, Australia.  His five films have collectively participated in over seven hundred film festivals and have received over one hundred awards, including an Academy Award for \"Harvie Krumpet\" and five Annecy Cristals.  Elliot calls himself an auteur filmmaker and each of his films have a bittersweet nature to them.  He does not engage with commercial work and works exclusively on his own film projects.  Based loosely on his family and friends, Elliot calls each of his works a Clayography – clay animated biography.  Each film takes up to five years to complete.  He is noted for his use of traditional 'in-camera' techniques, which means every prop set and character is a 'real' miniature handcrafted object.  Elliot does not use digital additions or computer generated imagery to enhance his visual aesthetic.  His company, Adam Elliot Clayographies, produce the films and Elliot’s work practices adhere to the French auteur methodology.  Each film has been voiced by notable actors including, Philip Seymour Hoffman, Toni Collette, Geoffrey Rush, Eric Bana, William McInnes , Barry Humphries and John Flaus.  Elliot is also a voting member of the Academy of Motion Picture Arts and Sciences and in 1999 was awarded The Young Achiever of the Year for Victoria.\n\nElliott Kastner: Elliott Kastner (January 7, 1930 – June 30, 2010) was an American film producer, whose best known credits include \"Where Eagles Dare\" (1968), \"The Long Goodbye\" (1973), \"The Missouri Breaks\" (1976) and \"Angel Heart\" (1987).\n\nQuestion: What movie based  William Hjortsberg's 1978 novel \"Falling Angel was produced by Elliot Kastner?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"movie_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the movie.\"\n    },\n    \"novel_source\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the novel the movie is based on.\"\n    },\n    \"novel_author\": {\n      \"type\": \"string\",\n      \"description\": \"The author of the source novel.\"\n    },\n    \"novel_publication_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The publication year of the source novel.\"\n    },\n    \"producer\": {\n      \"type\": \"string\",\n      \"description\": \"The producer of the movie.\"\n    }\n  },\n  \"required\": [\n    \"movie_title\",\n    \"novel_source\",\n    \"novel_author\",\n    \"novel_publication_year\",\n    \"producer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "movie_title": {
        "type": "string",
        "description": "The title of the movie."
      },
      "novel_source": {
        "type": "string",
        "description": "The title of the novel the movie is based on."
      },
      "novel_author": {
        "type": "string",
        "description": "The author of the source novel."
      },
      "novel_publication_year": {
        "type": "integer",
        "description": "The publication year of the source novel."
      },
      "producer": {
        "type": "string",
        "description": "The producer of the movie."
      }
    },
    "required": [
      "movie_title",
      "novel_source",
      "novel_author",
      "novel_publication_year",
      "producer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
