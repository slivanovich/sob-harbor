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
William R. Purcell: William Robert Purcell (born February 12, 1931) is a Democratic politician.  He was a member of the North Carolina General Assembly representing the state's twenty-fifth Senate district, including constituents in Anson, Richmond, Scotland and Stanly counties 1997-2013.  Purcell served as a captain in the U.S. army medical corp in France from 1957-1959.  Purcell then graduated from Davidson College and the University of North Carolina School of Medicine and was a pediatrician.  Purcell served on the Laurinburg, North Carolina city council and was mayor.

Dick Elliott (politician): Dick Elliott was a Democratic member of the South Carolina Senate, representing the 28th District since 1992.  He was previously a member of the South Carolina House of Representatives from 1982 through 1992.  He went to Wingate Junior College now Wingate University and to Clemson University.  Elliott was a real estate developer.  He served on the Horry County, South Carolina Council and the North Myrtle Beach, South Carolina City Council.

Cecil Bothwell: Cecil Bothwell (born 16 October 1950) is an American politician, writer, artist, musician and builder.  Bothwell was elected to the Asheville, North Carolina city council in 2009 and reelected in 2013.

Porter Robinson: Porter Weston Robinson (born July 15, 1992) is an American DJ, record producer and musician from Chapel Hill, North Carolina.  He has released multiple number one singles across different electronic genres.  His debut full length studio album, "Worlds", was released on August 12, 2014.

Northern Nash High School: Northern Nash High School is a high school located in Nash County, west of the Rocky Mount, North Carolina city limits.

Francis Osborne (North Carolina politician): Francis “Frank” Osborne (1853-1920) was the Attorney General of North Carolina from 1893-1896.  Osborne was born in Charlotte, North Carolina and attended the University of Virginia before reading law for 2 years in the offices of Richmond Mumford Pearson, Chief Justice of the North Carolina Supreme Court.  Osborne was admitted to the North Carolina Bar in 1875.  At age 25, he was elected mayor of the city of Charlotte.  He was elected Attorney General of North Carolina in 1893, but, defeated for reelection to the same office in 1896.  Osborne served a term as a State Senator from Mecklenburg County, North Carolina in the North Carolina General Assembly from 1898-1899.  He served on 9 standing Senate Committees.  After 1899, Osborne resumed his legal practice at the law firm of Osborne, Maxwell & Kearn.  Though, himself, a Democrat, in 1901 Osborne defended both North Carolina Supreme Court Chief Justice David M. Furches and North Carolina Supreme Court Associate Justice Robert Martin Douglas during their impeachment hearings.  Osborne was of the opinion that the Republican judges’ impeachments were unwarranted and an attempted political purge.  Osborne’s brilliant speech before the North Carolina General Assembly in closing defense of the justices caused both to be acquitted.  As reward for his successful defense of the justices, Theodore Roosevelt upon assuming office as President of the United States appointed Osborne a United States District Judge.

Winston-Salem Beltway: The Winston-Salem Beltway is a proposed freeway loop around the North Carolina city of Winston-Salem.  The northeastern and northwestern segments of this beltway, deemed the Winston-Salem Northern Beltway project, are the parts of the loop currently underway.  The eastern section of the beltway will be designated as NC 74 (Future I-74) and the western section has been designated as North Carolina Highway 452 (NC 452).

Cynthia D. Brown: Cynthia D. Brown is a former Durham, North Carolina City Councilwoman and Candidate for U.S. Senate in 2002.  Brown died November 14, 2016.  She was 58.

Astralwerks: Astralwerks is a US-based record label primarily focused on electronic and dance music.  A unit of Universal Music Group, its material is distributed via Capitol Music Group, and also releases materials mostly from EMI Music Australia.  Some of the label's most popular recent releases have come from deadmau5, Mat Zo, Porter Robinson, Empire of the Sun, Nervo and Halsey.

Gastonia Rangers: The Gastonia Rangers were a class A minor league baseball team located in Gastonia, North Carolina.  2017 Hall of Fame Inductee Iván Rodríguez played for Gastonia in 1987.  The team played first as the Rangers in the Western Carolinas League (1973–1974), then later in the same league renamed as the South Atlantic League (1987–1992), during their affiliation with the Texas Rangers.  The franchise was also the Gastonia Tigers (1986), Gastonia Jets (1985), Gastonia Expos (1983–1984) and Gastonia Cardinals (1980–1982).  Their home stadium was Sims Legion Park.  After the 1992 season, the team moved to another North Carolina city, Hickory, and have been known as the Hickory Crawdads ever since.

Question: Astralwerks was a label that released an album by the artist from what North Carolina city?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "record_label": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the record label."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "artist": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the artist whose album was released by the label."
        },
        "origin_city": {
          "type": "string",
          "description": "The city where the artist is from."
        },
        "origin_state": {
          "type": "string",
          "description": "The state where the artist is from."
        }
      },
      "required": [
        "name",
        "origin_city",
        "origin_state"
      ],
      "additionalProperties": false
    },
    "answer_city": {
      "type": "string",
      "description": "The North Carolina city associated with the artist."
    }
  },
  "required": [
    "record_label",
    "artist",
    "answer_city"
  ],
  "additionalProperties": false
}
