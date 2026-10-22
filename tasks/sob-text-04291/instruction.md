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
Leavesden, Hertfordshire: Leavesden is a residential and commercial area in Hertfordshire, England, contiguous with the northern suburbs of Watford.  It lies within the M25 Motorway.  On its eastern side it is bounded by the M1 Motorway.  Leavesden is part of Abbots Langley civil parish and is also the name of a district council ward in Three Rivers District.  Leavesden Green is an adjoining residential community which lies partly in Three Rivers and partly in the Borough of Watford.

Gerald Schoenfeld: Gerald Schoenfeld (September 22, 1924 – November 25, 2008) was chairman of the Shubert Organization from 1972-2008.

Melissa van der Schyff: Melissa van der Schyff (sometimes stylized Melissa Van Der Schyff) is a Canadian award-winning actress, singer, comedian and songwriter who is best known for her work on Broadway.  She was nominated for a 2012 Drama Desk Award and Outer Critics Circle Award for ""Outstanding Featured Actress in A Musical"" for originating the role of "Blanche Barrow" in the Broadway Musical Bonnie and Clyde, which opened at the Gerald Schoenfeld Theatre in New York City on December 1, 2011.

Manhattan: Manhattan ( , ) is the most densely populated borough of New York City, its economic and administrative center, and its historical birthplace.  Locally it is often referred to simply as "The City".  The borough is coextensive with New York County, founded on November 1, 1683, as one of the original counties of the U.S. state of New York.  The borough consists mostly of Manhattan Island, bounded by the Hudson, East, and Harlem rivers; several small adjacent islands; and Marble Hill, a small neighborhood now on the U.S. mainland, physically connected to the Bronx and separated from the rest of Manhattan by the Harlem River.

Kiso Three Rivers: The Kiso Three Rivers (木曽三川 , Kiso Sansen ) refers to the three major rivers that make up the alluvial plain area of the Nōbi Plain of Japan.  The three rivers are the Kiso River, the Ibi River and the Nagara River.  Given their location, they are sometimes referred to as the Nōbi Three Rivers (濃尾三川 "Nōbi Sansen").

Three Rivers Park District: Three Rivers Park District is a special park district serving the suburban areas of the Twin Cities including suburban Hennepin, Carver, Dakota, Scott and Ramsey counties.  Three Rivers's mission is "To promote environmental stewardship through recreation and education in a natural resources-based park system."  Three Rivers operates twenty parks and ten regional trails, with at least two more regional trails planned.  Nearly seven million people visit Three Rivers facilities each year.

Big Rivers Conference (Illinois): The Big Rivers Conference of Illinois was a high school football-exclusive athletic conference that existed from the 1999 through the 2012 football season.  Upon its dissolution, it comprised ten teams (eight schools competing independently and two athletic co-operatives) located in the northwest and north-central portions of the state.  It was a member of the Illinois High School Association, and its sister conference for other sports was the Three Rivers Conference.  As of the 2013-14 school year, in tandem with a conference expansion, Big Rivers has been reabsorbed into the Three Rivers Conference.  This expansion negotiated full membership status for member schools in all Three Rivers Conference sports (with co-operatives existing for some sports and not every school necessarily fielding a team in every sport offered), thereby negating the need for a football conference carve-out.

The Bridges of Madison County (musical): The Bridges of Madison County is a musical, based on Robert James Waller's 1992 novel, with a book by Marsha Norman and music and lyrics by Jason Robert Brown.  The musical premiered on Broadway at the Gerald Schoenfeld Theatre on February 20, 2014, and closed on May 18, 2014.  The Broadway production was directed by Bartlett Sher and starred Kelli O'Hara as Francesca and Steven Pasquale as Robert.

A Behanding in Spokane: A Behanding in Spokane is a 2010 black comedy by award-winning Irish playwright Martin McDonagh.  It premiered at the Schoenfeld Theatre on Broadway in 2010.  This is McDonagh's first play set in the United States.

Gerald Schoenfeld Theatre: The Gerald Schoenfeld Theatre is a Broadway theatre, previously known as the Plymouth Theatre, located at 236 West 45th Street (George Abbott Way) in midtown Manhattan and renamed in 2005 in honor of Gerald Schoenfeld.

Question: The Gerald Schoenfeld Theatre is located in a borough bounded by what three rivers?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "theatre_name": {
      "type": "string",
      "description": "The name of the theatre."
    },
    "theatre_location_borough": {
      "type": "string",
      "description": "The borough where the theatre is located."
    },
    "bounding_rivers": {
      "type": "array",
      "description": "A list of rivers that bound the specified borough.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "theatre_name",
    "theatre_location_borough",
    "bounding_rivers"
  ],
  "additionalProperties": false
}
