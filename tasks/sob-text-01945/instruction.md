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
Henry Louis Gates arrest controversy: On July 16, 2009, Harvard University professor Henry Louis Gates Jr. was arrested at his Cambridge, Massachusetts home by local police officer Sgt. James Crowley, who was responding to a 9-1-1 caller's report of men breaking and entering the residence.  The arrest initiated a series of events that unfolded under the spotlight of the international news media.

Lenny McAllister: Leonard Francis McAllister Jr. (born January 13, 1972) is a conservative American political commentator for a number of newspapers and websites, including AOL and The Root.

Marcus Brauchli: Marcus W. Brauchli (born June 19, 1961) is a media investor and advisor.  He also is a consultant to Graham Holdings Company, working with the company's chairman and CEO, Donald E. Graham.  Before his current roles, he spent four-plus years as executive editor of "The Washington Post", overseeing the "Post"' s print and digital news operations, starting on September 8, 2008, and succeeding Leonard Downie, Jr. He was also the managing editor of "The Wall Street Journal" before Murdoch took over the company.

The Root (magazine): The Root is an English-language American online magazine of African-American culture launched on January 28, 2008, by Henry Louis Gates Jr. and Donald E. Graham, and was owned by Graham Holdings Company through its online subsidiary, The Slate Group.

Jacob Weisberg: Jacob Weisberg (born 1964) is an American political journalist, serving as editor-in-chief of Slate Group, a division of Graham Holdings Company.  Weisberg is also a "Newsweek" columnist.  He served as the editor of "Slate" magazine for six years, until stepping down in June 2008.  He is the son of Lois Weisberg, a Chicago social activist and connector mentioned in Malcolm Gladwell's book "The Tipping Point".

Slate (magazine): Slate is an online magazine that covers current affairs, politics, and culture in the United States from a liberal perspective.  It was created in 1996 by former "New Republic" editor Michael Kinsley, initially under the ownership of Microsoft as part of MSN.  On December 21, 2004, it was purchased by The Washington Post Company, later renamed the Graham Holdings Company.  Since June 4, 2008, "Slate" has been managed by The Slate Group, an online publishing entity created by the Graham Holdings Company to develop and manage web-only magazines.  "Slate" is based in New York City, with an additional office in Washington, D.C.

Finding Your Roots: Finding Your Roots with Henry Louis Gates Jr. is a PBS television series hosted by Henry Louis Gates Jr.  The first season aired on PBS from March 25 to May 20 of 2012.  It was broadcast in the 8–9 p.m time slot (EDT).  The series returned for a second season on September 23, 2014 and finished on November 25, 2014.  Season three began airing on January 5, 2016, concluding on March 8, 2016.  Season four is set to air on October 3, 2017.

The Slate Group: The Slate Group is a US online publishing entity established in June 2008 by Graham Holdings Company.  Among the publications overseen by The Slate Group are Slate, Slate V, and ForeignPolicy.com.

The Signifying Monkey: The Signifying Monkey: A Theory of African-American Literary Criticism is a work of literary criticism and theory by American scholar Henry Louis Gates Jr. first published in 1988.  The book traces the folkloric origins of the African-American cultural practice of “signifying” and uses the concept of Signifyin(g) to analyze the interplay between texts of prominent African-American writers, specifically Richard Wright, Ralph Ellison, Zora Neale Hurston and Ishmael Reed.

Bob Holman: Bob Holman is an American poet and poetry activist, most closely identified with the oral tradition, the spoken word, and poetry slam.  As a promoter of poetry in many media, Holman has spent the last four decades working variously as an author, editor, publisher, performer, emcee of live events, director of theatrical productions, producer of films and television programs, record label executive, university professor, and archivist.  He was described by Henry Louis Gates Jr. in "The New Yorker" as "the postmodern promoter who has done more to bring poetry to cafes and bars than anyone since Ferlinghetti."

Question: Leonard Francis McAllister Jr. (born January 13, 1972) is a conservative American political commentator for a number of newspapers and websites, including which English-language American online magazine of African-American culture launched on January 28, 2008, by Henry Louis Gates Jr. and Donald E. Graham, and was owned by Graham Holdings Company through its online subsidiary, The Slate Group?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "magazine_name": {
      "type": "string",
      "description": "The name of the online magazine."
    },
    "launch_details": {
      "type": "object",
      "properties": {
        "launch_date": {
          "type": "string",
          "description": "The date the magazine was launched."
        },
        "founders": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The individuals who launched the magazine."
        }
      },
      "required": [
        "launch_date",
        "founders"
      ],
      "additionalProperties": false
    },
    "ownership_details": {
      "type": "object",
      "properties": {
        "owning_company": {
          "type": "string",
          "description": "The main company that owns the magazine."
        },
        "online_subsidiary": {
          "type": "string",
          "description": "The online subsidiary through which the magazine is owned."
        }
      },
      "required": [
        "owning_company",
        "online_subsidiary"
      ],
      "additionalProperties": false
    },
    "cultural_focus": {
      "type": "string",
      "description": "The primary cultural focus of the magazine."
    },
    "commentator_name": {
      "type": "string",
      "description": "The name of the political commentator associated with the magazine."
    }
  },
  "required": [
    "magazine_name",
    "launch_details",
    "ownership_details",
    "cultural_focus",
    "commentator_name"
  ],
  "additionalProperties": false
}
