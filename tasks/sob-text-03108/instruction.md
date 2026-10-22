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
Colin Farrell: Colin James Farrell (born 31 May 1976) is an Irish actor.  Farrell appeared in the RTE Irish drama "Ballykissangel" in 1998, made his film debut in the Tim Roth-directed drama "The War Zone" in 1999, and was discovered by Hollywood when Joel Schumacher cast him in the lead role in the war drama "Tigerland" in 2000.  He then starred in Schumacher's psychological thriller "Phone Booth" (2002) where he plays a hostage in a New York city phone booth and the American thrillers "S.W.A.T." (2003) and "The Recruit" (2003), establishing his international box-office appeal.  During that time, he also appeared in Steven Spielberg's science fiction thriller "Minority Report" (2002) and as the villain Bullseye in the superhero film "Daredevil" (2003).

As If I Am Not There: As If I Am Not There (Serbian: Као да ме нема, Kao da me nema) is a 2010 Irish drama film directed by Juanita Wilson.  The film is set in the Balkans and is shot in the Serbo-Croatian language.  The film was selected as the Irish entry for the Best Foreign Language Film at the 84th Academy Awards, but it did not make the final shortlist.

Patrick's Day (film): Patrick's Day is a 2014 Irish drama film written and directed by Terry McMahon.

Sean Mahon: Sean Mahon is an Irish stage and screen actor.  He is known for playing Nicky Giblin in the Broadway production of "The Seafarer", Richard Hannay in the Broadway production of "The 39 Steps" and Michael Hess (the lost son) in the award winning feature film, "Philomena".  In 2014 he was nominated for a best lead actor award for his portrayal of maverick cop Brian McGonigle in the Irish Drama Red Rock.  After much success in Ireland, Red Rock now plays on the BBC in the UK and on Amazon Prime in the US.

Isaach de Bankolé: Isaach or Isaac de Bankolé (born 12 August 1957) is an Ivorian actor.

Calvary (film): Calvary is a 2014 Irish drama film written and directed by John Michael McDonagh.  It stars Brendan Gleeson, Chris O'Dowd, Kelly Reilly, Aidan Gillen, Dylan Moran and Isaach de Bankolé.  The film began production in September 2012 and was released in April 2014 in Ireland and the United Kingdom, in July in Australia and August 2014 in the United States.  The film was screened at the 2014 Sundance Film Festival and at the 64th Berlin International Film Festival.

Words Upon the Window Pane: Words Upon the Window Pane is a 1994 Irish drama film and the directorial debut of Mary McGuckian.  The film is based on William Butler Yeats' one-act play of the same name.  Pat O'Connor was billed to direct the project but he personally offered McGuckian, who was writing the screenplay at the time, the opportunity to also direct.  The film received its US premiere on 10 June 1994 at the Lincoln Center for the Performing Arts as part of the largest retrospective of Irish film ever shown outside Ireland.  In September that year, the film was screened at the 51st Venice International Film Festival.

Glassland: Glassland is a 2014 Irish drama film written and directed by Gerard Barrett in his second feature following "Pilgrim Hill".  The film stars Jack Reynor as a young man who tries to help his mother (Toni Collette) with her alcoholism.

Bob Quinn (Irish filmmaker): Bob Quinn (Irish: "Roibeard Ó Cuinn" ) (born Dublin, 1935) is an Irish filmmaker, writer and photographer.  He directed the 1977 irish drama film poitin starring niall toibin and Donal McCann set in connamara co galway

The Guarantee: The Guarantee is a 2014 Irish drama film written and directed by Colin Murphy, and starring David Murray, Gary Lydon, Orla Fitzgerald, Morgan C. Jones and Peter Coonan.  Directed by Ian Power, and based on Murphy's play of the same title, the film explores the events leading up to the Irish banking crisis, the title referring to a meeting of high-level officials that was held on 29 September 2008 and resulted in the Irish Government taking the decision to guarantee Ireland's entire domestic banking system.  The film was produced by John Kelleher Media in association with the Broadcasting Authority of Ireland, the Irish Film Board and the commercial television channel TV3.

Question: Who is the Ivorian actor born on August 12, 1957 that starred in the 2014 Irish drama film Calvary?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The full name of the actor."
    },
    "actor_nationality": {
      "type": "string",
      "description": "The nationality of the actor."
    },
    "actor_birth_date": {
      "type": "string",
      "description": "The birth date of the actor in 'Day Month Year' format."
    },
    "film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film the actor starred in."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film."
        },
        "genre": {
          "type": "string",
          "description": "The genre of the film."
        }
      },
      "required": [
        "title",
        "release_year",
        "genre"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actor_name",
    "actor_nationality",
    "actor_birth_date",
    "film_details"
  ],
  "additionalProperties": false
}
