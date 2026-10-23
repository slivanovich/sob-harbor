{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nParent Trap III: Parent Trap III is a 1989 American made-for-television comedy film and a sequel to \"The Parent Trap II\" (1986) and the third installment in \"The Parent Trap\" series.  It originally aired in two parts on \"The Magical World of Disney\" on April 9 and 16, 1989.\n\nThe Parent Trap (1961 film): The Parent Trap is a 1961 Walt Disney Technicolor film.  It stars Hayley Mills, Maureen O'Hara and Brian Keith in a story about teenage twins on a quest to reunite their divorced parents.  The screenplay by the film's director David Swift was based upon the 1949 book \"Lottie and Lisa\" (German: \"Das Doppelte Lottchen\" ) by Erich Kästner.  \"The Parent Trap\" was nominated for two Academy Awards, was broadcast on television, saw three television sequels, was remade in 1998 with Lindsay Lohan, and has been released on digital stereo LaserDisc format in 1986 as well as VHS and DVD in 2000.  The original film was Mills' second of six films for Disney.\n\nMoon Pilot: Moon Pilot is a 1962 American Technicolor science fiction satirical comedy film from Walt Disney Productions, released through Buena Vista Distribution, directed by James Neilson, and starring Tom Tryon, Brian Keith, Edmund O'Brien, Dany Saval, and Tommy Kirk.\n\nHallie Meyers-Shyer: Hallie Meyers-Shyer (born July 26, 1987, in Los Angeles, California) is an American film actress, director and writer.  She is the youngest daughter of writer/directors Nancy Meyers and Charles Shyer, and has appeared in six of her parents' films: \"Father of the Bride\", \"I Love Trouble\", \"Father of the Bride Part II\", \"The Parent Trap\", \"What Women Want\", and \"The Affair of the Necklace\".  Her older sister Annie has also made film appearances; the twin characters in \"The Parent Trap\" were named after Hallie and Annie.\n\nCarrie Kei Heim: Carrie Kei Heim (born December 7, 1973) is an American actress, lawyer, and writer.  She is best known for her roles as Cornelia in \"\" and Nikki Ferris in \"The Parent Trap II\".  After completing \"The Parent Trap ll\", Carrie retired from acting.\n\nThe Parent Trap (song): \"The Parent Trap\" was the title song from the 1961 Disney film, \"The Parent Trap\".  It was sung by teen idols, Annette Funicello and Tommy Sands and it was written by the songwriting brother team of Robert and Richard Sherman.\n\nIL-Informed: IL-Informed is an American satirical sketch comedy television program that focuses on politics, current events, and other issues that face Chicagoans.  The half-hour-long pilot was produced by PBS member station WTTW (Channel 11) and premiered locally on Sunday, May 4, 2008.  The first episode was co-produced by Paris Schutz and Sarah Warner of WTTW, and was written and performed by the sketch comedy group, \"Schadenfreude\": Justin Kaufmann, Kate James, Sandy Marshal, and Stephen Schmidt, with Adam Witt contributing.  The pilot also features performances by \"The Second City\" veterans Joe Canale (who hosts the show), Ithamar Enriquez and Inda Craig-Galvan (of the comedy duo \"kevINda\").  The pilot episode examines housing issues facing Chicagoans though a variety of comedic sketches and includes an interview with 44th Ward Alderman Tom Tunney.\n\nThe Parent Trap II: The Parent Trap II is a 1986 American made-for-television comedy film and a sequel to Disney's 1961 classic \"The Parent Trap\" and the second installment in \"The Parent Trap\" series.  It premiered on Disney Channel on July 26, 1986 as a part of the channel's \"Sunday Night Movie\".\n\nBrian Keith: Brian Keith (born Robert Alba Keith, November 14, 1921 – June 24, 1997) was an American film, television, and stage actor who in his six-decade-long career gained recognition for his work in movies such as the Disney family film \"The Parent Trap\" (1961), the comedy \"The Russians Are Coming, The Russians Are Coming\" (1966), and the adventure saga \"The Wind and the Lion\" (1975), in which he portrayed President Theodore Roosevelt.\n\nParent Trap: Hawaiian Honeymoon: Parent Trap: Hawaiian Honeymoon is a 1989 American made-for-television comedy film and a sequel to \"Parent Trap III\" (1989) and the fourth and final installment in \"The Parent Trap\" series.  It originally aired in two parts on \"The Magical World of Disney\" on November 19 and 26, 1989.\n\nQuestion: What star of Moon Pilot also appeared in The Parent Trap?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor who appeared in both films.\"\n    },\n    \"films_appeared_in\": {\n      \"type\": \"array\",\n      \"description\": \"A list of the films the actor appeared in, as specified in the question.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    },\n    \"film_count\": {\n      \"type\": \"integer\",\n      \"description\": \"The number of films the actor appeared in, as specified in the question.\"\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"films_appeared_in\",\n    \"film_count\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor who appeared in both films."
      },
      "films_appeared_in": {
        "type": "array",
        "description": "A list of the films the actor appeared in, as specified in the question.",
        "items": {
          "type": "string"
        }
      },
      "film_count": {
        "type": "integer",
        "description": "The number of films the actor appeared in, as specified in the question."
      }
    },
    "required": [
      "actor_name",
      "films_appeared_in",
      "film_count"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
