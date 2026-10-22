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
Jon Jones (director): Jon Jones is a British television director and screenwriter whose works include the ITV drama series "Cold Feet", the Channel 4 drama "A Very Social Secretary", the BBC thriller "The Debt" (2003), and the 2007 ITV adaptation of "Northanger Abbey".  His work on "Cold Feet" led to a nomination for New Director (Fiction) at the BAFTA Television Craft Awards.

Martin Clunes: Alexander Martin Clunes, OBE (born 28 November 1961) is an English actor.  He is best known for portraying Martin Ellingham in the ITV drama series "Doc Martin" and Gary Strang in "Men Behaving Badly".  Clunes has narrated a number of documentaries for ITV, the first of which was "Islands of Britain" in 2009.  He has since presented a number of documentaries centred on animals.  He has also voiced Kipper the Dog in the animated series, "Kipper".

Jack Davenport: Jack Arthur Davenport (born 1 March 1973) is an English actor.  He is best known for his roles in the television series "This Life" and "Coupling", and as James Norrington in the "Pirates of the Caribbean" series.  He has also appeared in other Hollywood films, such as "The Talented Mr. Ripley".  More recently, he was part of the ensemble cast in the drama series "FlashForward" and "Smash", and took the lead role in the 2013 ITV drama series "Breathless".

The Secret (TV series): The Secret is a 2016 Northern Irish ITV mini-series based on "Let This Be Our Secret", Belfast journalist Deric Henderson's account of the double murder of Lesley Howell and Constable Trevor Buchanan, whose bodies were discovered in a fume-filled car in the garage of a property in Castlerock, County Londonderry, in Northern Ireland in May 1991.

Katherine Kelly (actress): Katherine Kelly (born 19 November 1979) is an English actress.  A 2001 graduate of the Royal Academy of Dramatic Art, she played Becky McDonald in the ITV soap opera "Coronation Street" from 2006 to 2012, for which she won Best Actress at the 2009 British Soap Awards and Best Serial Drama Performance at the 2012 National Television Awards.  Since 2013, she has starred as Mae, Lady Loxley in the ITV drama series "Mr Selfridge".

Colin Howell: Colin Howell (born 14 March 1959) is a Northern Irish convicted double murderer.  The murders and surrounding story were the subject of an ITV drama series "The Secret" broadcast in April and May 2016.

Little Boy Blue (TV series): Little Boy Blue is an ITV drama series, shown over four sixty-minute episodes from 24 April to 15 May 2017.  The series focuses on the murder of Rhys Jones in Croxteth, Liverpool in 2007.

Andrew Buchan: Andrew Buchan (born 19 February 1979) is an English stage and television actor known for his roles as Mark Latimer in the ITV drama "Broadchurch" (2013–17), as Scott Foster in the BBC political drama "Party Animals" (2007), as John Mercer in ITV drama series "The Fixer" (2008–09), and as William Garrow in BBC period drama "Garrow's Law" (2009–11).

Crime Stories (UK TV series): Crime Stories is a British television crime drama series that aired on ITV from 12 November until 7 December 2012.  Described as "groundbreaking" television, the series was one of a number of series developed by Paul Marquess which makes use of a documentary-style feel and unscripted dialogue.  The series was panned by critics and viewers alike and was axed by ITV after just one series.  The series made use of the set previously occupied by fellow ITV drama "The Bill", for which Marquess served as executive producer from 2002–05.

Kate Buffery: Katharine Winifred Buffery (born 23 July 1957) is an English actress.  She is known for her numerous roles on British television, including the ITV drama series "Wish Me Luck" (1988-1990), BBC miniseries "Close Relations" (1998), Channel 5 legal drama "Wing and a Prayer" (1997-1999) and the ITV police drama "Trial and Retribution" (1997-2002).  Her stage work includes the 1983 original West End production of "Daisy Pulls it Off", which earned her an Olivier Award nomination.

Question: Colin Howell was a subject on the ITV drama series about the murder of which two people?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "drama_series_name": {
      "type": "string",
      "description": "The name of the ITV drama series."
    },
    "crime_type": {
      "type": "string",
      "description": "The type of crime depicted in the series."
    },
    "number_of_victims": {
      "type": "integer",
      "description": "The total number of victims in the crime."
    },
    "victims": {
      "type": "array",
      "description": "A list of the names of the victims.",
      "items": {
        "type": "object",
        "properties": {
          "full_name": {
            "type": "string",
            "description": "The full name of the victim."
          }
        },
        "required": [
          "full_name"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "drama_series_name",
    "crime_type",
    "number_of_victims",
    "victims"
  ],
  "additionalProperties": false
}
