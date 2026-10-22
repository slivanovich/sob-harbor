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
Jersey City mayoral special election, 2004: The Jersey City 2004 mayoral special election took place on November 2, 2004.  Democrat Jerramiah Healy won the election with 28% of the vote over his nearest rivals (Assemblyman Lou Manzo, 24%, and Acting Mayor L. Harvey Smith, 22%).  The previous Mayor Glenn Cunningham, the first African-American Mayor died of a heart attack five months prior and L. Harvey Smith became Acting Mayor.  There was also an election in 2005, which Healy also won.

Frank J. Rice: Frank J. Rice (February 5, 1869, North Adams, Massachusetts – 1917) was a four-term Republican mayor of New Haven, Connecticut. .  At 18 he went into the grocery business.  And a few years after became the superintendent of H.P. Ives & Company.  He was voted in as mayor in 1909, winning the race by 402 votes.  He was a former member of the New Haven Councilmen.  At one time in his life he was a trolley conductor in New Haven.  He died midway through the first year of his fourth term as mayor.

A Night in the Life of Jimmy Reardon: A Night in the Life of Jimmy Reardon, also known as Aren't You Even Gonna Kiss Me Goodbye? , is a 1988 American coming of age drama film written and directed by William Richert and starring River Phoenix, Ann Magnuson, Meredith Salenger, Matthew Perry, Ione Skye, and Louanne.  It is based upon the novel "Aren't You Even Gonna Kiss Me Goodbye?" , also by William Richert.  The story centers on a high school graduate who must decide if he wants to go to business school at the request of his father, or go his own way and find a full-time job, while also deciding on who he wants to be in life and if he should leave his house.

Michael Barnes (North Carolina politician): Michael Barnes is the mayor pro tempore of Charlotte, North Carolina.  He also served as acting mayor for a short time following the resignation of former mayor Patrick Cannon, who was arrested on March 26, 2014 for corruption charges.  Barnes immediately became acting mayor upon Cannon's resignation.  The City Council was then required to appoint a mayor to serve out the remainder of Cannon's term (through Dec. 2015).  On April 7, the council voted to appoint Dan Clodfelter, a state senator, as the new mayor.

Branislav Belić: Branislav Belić (, ] or ] ; 1932 Belgrade, Kingdom of Yugoslavia – 17 July 2016 Belgrade, Serbia) was a Serbian politician.  He was an Acting Mayor of Belgrade following the 2008 election.  He served as an interim Chairman of the Assembly as the oldest member.  Previously this seat, which is also a seat of the acting mayor, was held by Zoran Alimpić.  Acting mayors were necessary in the period until the election of the new one, due to the death of the elected mayor Nenad Bogdanović.  His term ended with election of Dragan Đilas.

Sekesai Makwavarara: Sekesai Makwavarara is the former deputy mayor and acting mayor of Harare.  Makwararara began her work for council in 2002 for Mabvuku as a member of the Movement for Democratic Change party.  Initially a member of ZANU-PF, she temporarily was a member of the Movement for Democratic Change.  During her tenure of service for the Mabvuku city council she served under deputy mayor Elias Mudzuri until she was appointed as acting mayor following the forced deposition of Mudzuri by the national government.  After the MDC party launched a probe which identified her as being corrupt she rejoined the ZANU-PF.  She resigned from this position in 2004.  In 2006, she was appointed as the head of a commission that ran the Harare City Council's affairs until December 2008.

Hazen S. Pingree: Hazen Stuart Pingree (August 30, 1840 – June 18, 1901) was a four-term Republican mayor of Detroit (1889–1897) and the 24th Governor of the U.S. State of Michigan (1897–1901).  A Yankee who migrated from New England, he was a Georgist social reformer who battled corporations and was an early leader of the Progressive Movement.

William Richert (mayor): William Richert (October 28, 1858 – June 16, 1912) served as acting mayor of Detroit, Michigan from March 22, 1897 to April 5, 1897, following the resignation of Hazen S. Pingree.

Wilson Frost: Wilson Frost (born December 27, 1925) is a former Chicago alderman of the 34th Ward.  In 1976, upon the death of longtime mayor Richard J. Daley, Frost declared that he was now acting mayor, based upon his interpretation of the city charter and the fact that he was serving as President Pro Tempore of the City Council.  However, Wilson found himself literally locked out of the mayor's office—he was told that the keys could not be found.  In a power struggle that lasted several days, the entirely Democratic city council determined that Frost was incorrect in his claim, and appointed Alderman Michael Bilandic as acting mayor instead.  Had he been elected mayor, Wilson Frost would have been Chicago's first African American mayor.

Marcos Devers: Marcos A. Devers (born October 25, 1950) is a member of the Massachusetts House of Representatives, and a former acting mayor of Lawrence, Massachusetts.  When Devers served as acting mayor from September to November 2001 he was the first Dominican-American to execute the role of mayor in the United States and the first Latino mayor in Massachusetts.

Question: William Richert served as acting mayor of Detroit, Michigan, after what four-term Republican mayor resigned?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "former_mayor": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "political_party": {
          "type": "string"
        },
        "terms_served": {
          "type": "integer"
        },
        "city": {
          "type": "string"
        },
        "state": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "political_party",
        "terms_served",
        "city",
        "state"
      ],
      "additionalProperties": false
    },
    "acting_mayor": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "city": {
          "type": "string"
        },
        "state": {
          "type": "string"
        },
        "start_date": {
          "type": "string",
          "format": "date"
        },
        "end_date": {
          "type": "string",
          "format": "date"
        }
      },
      "required": [
        "name",
        "city",
        "state",
        "start_date",
        "end_date"
      ],
      "additionalProperties": false
    },
    "reason_for_acting_mayor": {
      "type": "string"
    }
  },
  "required": [
    "former_mayor",
    "acting_mayor",
    "reason_for_acting_mayor"
  ],
  "additionalProperties": false
}
