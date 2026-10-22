Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
101 Dalmatians (1996 film): 101 Dalmatians is a 1996 American live-action comedy adventure film based on Walt Disney's animated 1961 movie adaptation of Dodie Smith's 1956 novel "The Hundred and One Dalmatians."  Directed by Stephen Herek and co-produced by John Hughes and Ricardo Mestres, it stars Glenn Close, Jeff Daniels, Joely Richardson, Joan Plowright, Hugh Laurie, Mark Williams and Tim McInnerny.  In contrast with the 1961 film, none of the animals talk in this version.  Released on November 27, 1996 by Walt Disney Pictures, the film was praised for its faithfulness to the animated classic.  It received mixed reviews, but was a commercial success, grossing $320.6 million in theaters against a $75 million budget.  Close, who was universally praised for her portrayal as Cruella de Vil, was nominated for a Golden Globe for Best Performance by an Actress in a Motion Picture - Comedy or Musical, but lost to Madonna in "Evita".  The film was also nominated for a BAFTA award for best makeup effects.  A theatrical sequel titled "102 Dalmatians" was released on November 22, 2000 with Close and McInnerny reprising their roles.

102 Dalmatians: 102 Dalmatians is a 2000 American live action and CG-animated film adventure drama film directed by Kevin Lima in his live-action directorial debut and produced by Edward S. Feldman and Walt Disney Pictures.  It is the sequel to the 1996 film "101 Dalmatians", a live-action remake of the 1961 Disney animated film of the same name and stars Glenn Close reprising her role as Cruella de Vil as she attempts to steal puppies for her "grandest" fur coat yet.  Close and Tim McInnerny were the only two actors from the first film to return for the sequel, however.  The film was nominated for an Academy Award for Best Costume Design, but lost to "Gladiator."

Freaky Friday (1976 film): Freaky Friday is a 1976 American fantasy-comedy film directed by Gary Nelson and starring Barbara Harris as Ellen Andrews, Jodie Foster as her daughter Annabel, and John Astin as her husband, Bill Andrews.

Kevin Lima: Kevin Lima (born 1962) is an American film director who has directed a number of Disney films including his debut film "A Goofy Movie" in 1995, "Tarzan" (1999), "102 Dalmatians" (2000), and "Enchanted" (2007).  He is married to Brenda Chapman, the head of story of "The Lion King" (1994) and co-director of "The Prince of Egypt" (1998) and "Brave" (2012).

Kristen Buckley: Kristen Buckley (born June 9, 1968 in New York City, New York) is an American screenwriter and author.  She co-wrote the screenplays for "102 Dalmatians" (for which she also co-wrote the story), "How to Lose a Guy in 10 Days", and "Shoe Addicts Anonymous".  She also wrote "The Parker Grey Show" (a novel) and "Tramps Like Us" (a memoir).

Body swap appearances in media: Body swaps have been a common storytelling device in fiction media.  Books such as "Vice Versa" (1882) and "Freaky Friday" (1972) have inspired a number of adaptation films as well as television shows, some of which have used derivatives of "Freaky Friday" for its episode titles.  In 2013, Disney Channel held a "Freaky Freakend" with seven shows that featured body-swapping episodes.

Roger Pratt (cinematographer): Roger Pratt BSC (born 27 February 1947) is a British cinematographer.  Pratt has been the director of photography for more than 35 films.  Among his body of films, he has worked on "Batman" (1989), "Frankenstein" (1994), "102 Dalmatians" (2000), "Harry Potter and the Chamber of Secrets" (2002), "Troy" (2004), and more recently "Harry Potter and the Goblet of Fire" (2005), "Inkheart" (2008) and "The Karate Kid" (2010).

Cruella de Vil: Cruella de Vil (spelled de Vil in the novel, spelled De Vil by Disney) is a character who appeared in Dodie Smith's 1956 novel "The Hundred and One Dalmatians", Disney's animated film adaptations "101 Dalmatians" and "", and Disney's live-action film adaptations "101 Dalmatians" and "102 Dalmatians" as the main antagonist.

Brian Regan (writer): Brian Regan is an American screenwriter.  He co-wrote the screenplays for "102 Dalmatians" (for which he also co-wrote the story), "How to Lose a Guy in 10 Days", and the yet-to-be-produced "Shoe Addicts Anonymous".

102 Dalmatians: Puppies to the Rescue: 102 Dalmatians: Puppies to the Rescue is a platform video game developed by Toys for Bob and published by Eidos Interactive for Microsoft Windows, PlayStation, Dreamcast and Game Boy color.  It is loosely based on the live-action Disney movie "102 Dalmatians".

Question: Which film was released first, 102 Dalmatians or Freaky Friday?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "films_compared": {
      "type": "array",
      "description": "Details of the films being compared for their release dates.",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film."
          },
          "release_year": {
            "type": "integer",
            "description": "The year the film was released."
          }
        },
        "required": [
          "title",
          "release_year"
        ],
        "additionalProperties": false
      }
    },
    "earliest_film": {
      "type": "object",
      "description": "The film that was released first.",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film released first."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film released first."
        }
      },
      "required": [
        "title",
        "release_year"
      ],
      "additionalProperties": false
    },
    "comparison_statement": {
      "type": "string",
      "description": "A statement summarizing which film was released first."
    }
  },
  "required": [
    "films_compared",
    "earliest_film",
    "comparison_statement"
  ],
  "additionalProperties": false
}
