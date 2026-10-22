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
Barbara Gordon (filmmaker): Barbara Gordon is an American award-winning documentary filmmaker and author.  After graduating from Barnard College, she worked for almost twenty years in television as a writer and producer.  She won two Emmys for her work on the Channel 2 Eye On Series Documentary for WCBS.  She also worked on the PBS Emmy Award winning series, The Great American Dream Machine, where she filmed segments on Studs Terkel, Dalton Trumbo, and Jane Fonda.

Larry Long (singer-songwriter): Larry Long (born 1951 in Des Moines, Iowa) is an American singer-songwriter who has made his life work the celebration of everyday heroes.  Author, historian, actor, and broadcaster Studs Terkel called Larry “a true American Troubadour.”  His non-profit organization "Community Celebration of Place" encourages community building through music and intergenerational story-telling.  He lives in Minneapolis, Minnesota.

Roald Tweet: Roald Tweet is a Professor Emeritus of English at Augustana College and a historian of the upper Mississippi River.  Roald is the husband of Margaret Tweet, the brother of David Tweet, father of Randall Tweet, Gretchen O'Brien, and Jonathan Tweet.  Roald also is a grandfather and a great grandfather.  Roald is currently part of the Agustin's Historical Society, St. John's Lutheran Church, Contemporary Club, Eagle Scouts, and a member of Sons of Norway.  He holds a master's degree in English and a Ph.D. in American Literature from the University of Chicago.  He creates three-minute vignettes about local history for his radio series, "Rock Island Lines," which earned the Illinois Humanities Council's Lawrence W. Towner Award in 2001.  He earned the Studs Terkel Humanities Service Award in 2006.  His published books include "History of Transportation on the Upper Mississippi and Illinois Rivers", "A History of the Rock Island District Corps of Engineers, 1866-1983", and "The Quad Cities: An American Mosaic."  In 2014 he began co-hosting the writing-related radio show "Scribble".

John Braine: John Gerard Braine (13 April 1922 – 28 October 1986) was an English novelist.  Braine is usually listed among the Angry Young Men, a loosely defined group of English writers who emerged on the literary scene in the 1950s.

Studs Terkel: Louis "Studs" Terkel (May 16, 1912 – October 31, 2008) was an American author, historian, actor, and broadcaster.  He received the Pulitzer Prize for General Non-Fiction in 1985 for ""The Good War"", and is best remembered for his oral histories of common Americans, and for hosting a long-running radio show in Chicago.

The Jealous God: The Jealous God is a novel by John Braine which was first published in 1964.  Set in the early 1960s among the Irish Catholic community in a small Yorkshire town, the book is about a 30-year-old mummy's boy and his attempts at liberating himself from his domineering mother.  The title refers to the latter's wish that her "favourite" son, although already rather old for following his alleged vocation, become a clergyman.  It was said that it was John Braine's personal favourite novel of all those that he wrote and was finally filmed in 2005.

Damon DiMarco: Damon DiMarco (born October 16, 1971), is a New York City author, actor, playwright, and historian.  His oral history work has been compared to that of Studs Terkel.  He was born in Princeton, New Jersey.

Helen Shiller: Helen Shiller (born 1947) is a former Alderman of the 46th ward in Chicago, Illinois.  She served in the Chicago City Council for six four-year terms, from 1987 to 2011.  Shiller was elected to the City Council on her third attempt, as Harold Washington, Chicago's first black Mayor, was re-elected to his second term, and her election as alderman helped close the Council Wars era in Chicago government.  Shiller has been described as "committed to liberal causes".  Among her most significant impacts on Chicago were her advocacy for diverse, inclusive, affordable housing and helping craft Chicago's response to the HIV/AIDS crisis.  Her commitment to fostering community development without displacement often brought Shiller into contention with some constituencies, real estate developers, and editorial boards.  Shiller's oral history was collected by Pulitzer Prize-winning author and Uptown resident Studs Terkel in his 2003 book, "Hope Dies Last".

The Jealous God (film): The Jealous God (2005) is a 1960s set feature film by British writer-director Steven Woodcock.  It is based on the novel by John Braine.  The opening scenes were filmed in the grammar school in Bradford where Braine was once a pupil.  Braine became famous in 1957 for his classic "Room at the Top", a book that shocked when first published because of how it exploded British class and sexual mores of the time.  There’s a clip from the Oscar-winning 1958 film version of "Room at the Top" in "The Jealous God", when Vincent and Laura are seen sitting in a cinema.  Allan Gill in his extraordinary movie debut, dazzles as inquisitive schoolboy #4.

Studs Terkel Radio Archive: The Studs Terkel Radio Archive is an archive of over 1,000 digitized audio tapes originally aired over 45 years on Studs Terkel's radio show on WFMT-FM or used in his oral history collections in the books "Division Street America" (1967) and "Working" (1974).  Terkel donated a total of 5,600 tapes to the Chicago History Museum, which contracted the WFMT Radio network (formerly part of WFMT-FM), to publish the recordings online.  The bulk of the tapes are not yet digitized, but the archive plans to digitize and distribute as many as possible online.  The American public radio network NPR is featuring many of the tapes during the week of September 25 - October 2, 2016.  The Chicago History Museum is also working with the Library of Congress to make the tapes available online and to visitors to their buildings in Washington, DC.

Question: Which author is English, Studs Terkel or John Braine?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question posed."
    },
    "authors_compared": {
      "type": "array",
      "description": "A list of authors mentioned in the question with their respective nationalities.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the author."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the author as stated in the context."
          }
        },
        "required": [
          "name",
          "nationality"
        ],
        "additionalProperties": false
      }
    },
    "english_author_name": {
      "type": "string",
      "description": "The name of the author who is English."
    }
  },
  "required": [
    "question_asked",
    "authors_compared",
    "english_author_name"
  ],
  "additionalProperties": false
}
