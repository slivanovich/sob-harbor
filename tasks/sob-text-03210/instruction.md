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
Mary von Schrader Jarrell: Mary von Schrader Jarrell (May 2, 1914 – July 30, 2007) was a patron of the arts and memoirist.  She was the widow of Randall Jarrell and worked consistently to memorialize his impact not only on herself but on the very world of American Poetry.

Poet laureate: A poet laureate (plural: poets laureate) is a poet officially appointed by a government or conferring institution, who is often expected to compose poems for special events and occasions.  The Italians Albertino Mussato and Francesco Petrarca were the first to be crowned poets laureate after the classical age, respectively in 1315 and 1342.  In Britain, the term dates from the appointment of Bernard André by Henry VII of England.  In modern times, the title may also be conferred by an organization such as the Poetry Foundation, which has a designated Children's Poet Laureate.  Other examples are the Pikes Peak Poet Laureate, which is designated by a "Presenting Partners" group from within the community; the Minnesota Poet Laureate chosen by the League of Minnesota Poets (est. 1934); the Northampton Poet Laureate chosen by the Northampton Arts Council, and the Martha's Vineyard Poet Laureate chosen by ten judges representing the Martha's Vineyard Poetry Society.

Randall Jarrell: Randall Jarrell (May 6, 1914 – October 14, 1965) was an American poet, literary critic, children's author, essayist, novelist, and the 11th Consultant in Poetry to the Library of Congress, a position that now bears the title Poet Laureate.

Martha's Vineyard Poet Laureate: The concept of the position of Martha’s Vineyard Poet Laureate (MV Poet Laureate) was formally initiated in 2011 by the Martha’s Vineyard Poetry Society.  This was the first time in Martha’s Vineyard history that a position was created to designate an island-wide poet laureate.  On similar note, the Martha’s Vineyard Poetry Society (MVPS) is the first island-wide poetry organization with membership in the history of Martha’s Vineyard.  MVPS was founded in 2008 by island poet/author/musician, William Waterway.

Indiana State Poet Laureate: The Indiana State Poet Laureate is the poet laureate for the U.S. state of Indiana.  Senate Enrolled Act No. 433 created the made the position effective July 1, 2005, but Indiana had a well-established unofficial position of state poet laureate since 1929.  Laureates serve a two year term.  The selection of Indiana State Poet Laureate is made by the Indiana Arts Commission executive director and seven members chosen by the commission who represent institutions of higher education.

United States Poet Laureate: The Poet Laureate Consultant in Poetry to the Library of Congress—commonly referred to as the United States Poet Laureate—serves as the official poet of the United States.  During their term, the Poet Laureate seeks to raise the national consciousness to a greater appreciation of the reading and writing of poetry.  The position was modeled on the Poet Laureate of the United Kingdom.  Begun in 1937, and formerly known as the Consultant in Poetry to the Library of Congress, the present title was devised and authorized by an Act of Congress in 1985.  The Poet Laureate's office is administered by the Center for the Book.

Poet Laureate of New Jersey: The Poet Laureate of New Jersey (statutorily known as New Jersey William Carlos Williams Citation of Merit) was an honor presented biennially by the Governor of New Jersey to a distinguished New Jersey poet.  Created in 1999, this position existed for less than four years and was abolished by the legislature effective July 2, 2003.  When the New Jersey State Legislature created the laureate position, the bill provided specifically for the creation of an award named in honor of twentieth-century poet and physician William Carlos Williams (1883–1963) who resided in Rutherford, New Jersey.  However, the legislature recognized that the award's recipient would "be considered the poet laureate of the State of New Jersey for a period of two years.  Before the position was abolished, only two poets, Gerald Stern and Amiri Baraka, had been appointed as the state's poet laureate.

The Arab's Mouth: The Arab's Mouth is a 1990 play by Ann-Marie MacDonald which she later revised to create "Belle Moral", at which point most of the Arabic references were cut.  The title refers to a shape found on a stone by the central character—a circle or zero.  First staged at the Factory Theatre in Toronto, MacDonald lightly revised the play for publication, at which point it was staged at Theatre Kingston in Kingston, Ontario.  It is now out of print, having been superseded by "Belle Moral".

California Poet Laureate: The California Poet Laureate is the poet laureate for the U.S. state of California.  In 2001, Governor Gray Davis created the official position.  Each poet laureate for the State of California is appointed by the Governor of California for a term of two years and must be confirmed by the senate.  Previous to Governor Davis' action in creating the position, the title was unofficial and the position was held for life.  The program is run by the California Arts Council.

Ann-Marie MacDonald: Ann-Marie MacDonald (born October 29, 1958) is a Canadian playwright, novelist, actress and broadcast host who lives in Toronto, Ontario, Canada.  The daughter of a member of Canada's military, she was born at an air force base near Baden-Baden, West Germany.  She is of Lebanese descent through her mother.

Question: Who held a position that now bears the title Poet Laureate, Ann-Marie MacDonald, Randall Jarrell, or both?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the individual who held the position."
    },
    "original_position_title": {
      "type": "string",
      "description": "The title of the position as it was known when the person held it."
    },
    "current_position_title": {
      "type": "string",
      "description": "The title the position now bears."
    },
    "position_holder_count": {
      "type": "integer",
      "description": "The number of individuals from the provided list who held such a position."
    },
    "is_poet_laureate_related": {
      "type": "boolean",
      "description": "Indicates if the position held is now known as Poet Laureate."
    }
  },
  "required": [
    "person_name",
    "original_position_title",
    "current_position_title",
    "position_holder_count",
    "is_poet_laureate_related"
  ],
  "additionalProperties": false
}
