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
George H. W. Bush: George Herbert Walker Bush (born June 12, 1924) is an American politician who was the 41st President of the United States from 1989 to 1993 and the 43rd Vice President of the United States from 1981 to 1989.  A member of the Republican Party, he was previously a congressman, ambassador, and Director of Central Intelligence.  He is the oldest living former President and Vice President.  Previously known as simply "George Bush", since 2001, Bush has often been referred to as "George H. W. Bush", "Bush 41", "Bush the Elder", or "George Bush Senior" to distinguish him from his eldest son, George W. Bush, the 43rd President of the United States.

United States elections, 1990: The 1990 United States elections were held on November 6, and elected the members of the 102nd United States Congress.  The election occurred in the middle of Republican President George H. W. Bush's term.  The Democratic Party build on its majorities in both chambers of Congress.  The Republicans lost nine seats in the U.S. House, lower than the average number of seats lost by U.S. President's party at the time, which was 29.  Out of the 33 seats up for election in the Senate, the Democratic Party picked up a net gain of one seat.  In the gubernatorial elections, both parties lost a net of one seat to third parties.

United States elections, 1986: The 1986 United States elections were held on November 4, and elected the members of the 100th United States Congress.  The elections occurred in the middle of Republican President Ronald Reagan's second term.  In an instance of the six-year itch phenomenon, the Democrats won a net gain of eight seats to recapture control of the United States Senate, taking back the chamber for the first time since the 1980 election.  The Democrats also made a net gain of five seats in the United States House of Representatives, increasing their majority in that chamber.  Despite Democratic congressional gains, in the gubernatorial elections, the Republican Party picked up a net of eight governorships.

United States elections, 1842: The 1842 United States elections occurred in the middle of President John Tyler's term, during the Second Party System.  Tyler had become president on April 4, 1841 upon the death of his predecessor, William Henry Harrison.  Elected as vice president on the Whig ticket with Harrison in 1840, Tyler was expelled from the party in September 1841.  Members of the 28th United States Congress were chosen in this election.  Florida joined the union during the 28th Congress.  Whigs kept control of the Senate, but lost control of the House.

United States elections, 1826: The 1826 United States elections occurred in the middle of Democratic-Republican President John Quincy Adams's term.  Members of the 20th United States Congress were chosen in this election.  The election took place during a transitional period between the First Party System and the Second Party System.  With the Federalist Party no longer active as a major political party, the major split in Congress was between supporters of Adams and supporters of Andrew Jackson, who Adams had defeated in the 1824 Presidential election.

United States elections, 1898: The 1898 United States elections occurred in the middle of Republican President William McKinley's first term, during the Fourth Party System.  The elections took place shortly after the end of the Spanish–American War.  Members of the 56th United States Congress were chosen in this election.  Republicans retained control of both houses of Congress.

United States elections, 1834: The 1834 United States elections occurred in the middle of Democratic President Andrew Jackson's second term.  Members of the 24th United States Congress were chosen in this election.  Taking place during the Second Party System, elections were contested between Andrew Jackson's Democratic Party and opponents of Jackson, including the remnants of the National Republican Party.  During this election, the anti-Jackson faction began to transition into the Whig Party.  Arkansas and Michigan joined the union during the 24th Congress.  Democrats retained the majority in the House, and won control of the Senate.

United States elections, 1874: The 1874 United States elections occurred in the middle of Republican President Ulysses S. Grant's second term, during the Third Party System.  Members of the 44th United States Congress were chosen in this election.  The election took place during the Reconstruction Era, and many Southerners were barred from voting.  Colorado joined the union during the 44th Congress.  Democrats took control of a chamber of Congress for the first time since the start of the Civil War, winning a huge number of seats from House Republicans.  However, the Republicans retained a majority in the Senate.  The election marked the first occurrence of the six-year itch phenomenon, in which a president's party lost a large number of Congressional seats during the president's second mid-term election.

Presidency of George W. Bush: The presidency of George W. Bush began at noon EST on January 20, 2001, when George W. Bush was inaugurated as 43rd President of the United States, and ended on January 20, 2009.  Bush, a Republican, took office following a very close win over Democratic nominee Al Gore in the 2000 presidential election.  Bush, the 43rd president, is the eldest son of the 41st president, George H. W. Bush.  Bush was re-elected in 2004, defeating his Democratic opponent John Kerry.  He was succeeded by Democrat Barack Obama, who won the 2008 presidential election.

Non-rigid designator: For example, consider the phrase "The 43rd President of the United States of America": while the 43rd President of the United States is "actually" George W. Bush, things might have been different.  Bush might have lost the election, meaning that the 43rd President might have been Al Gore or Ralph Nader instead.  ("How remote" these possible worlds are from the actual world is a discussion for physics and counterfactualism.)  "The 43rd President of the United States of America" is thus a non-rigid designator, picking out George W. Bush in some possible worlds, Al Gore in others, and yet other people in other worlds.

Question: The 1990 United States elections occurred in the middle of the presidential term of an American politician who was father to what man who was the 43rd president of the United States?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "election_details": {
      "type": "object",
      "properties": {
        "year": {
          "type": "integer",
          "description": "The year of the United States election."
        },
        "president_during_term": {
          "type": "string",
          "description": "The name of the president whose term the election occurred in the middle of."
        },
        "president_term_number": {
          "type": "integer",
          "description": "The presidential term number of the president during the election."
        }
      },
      "required": [
        "year",
        "president_during_term",
        "president_term_number"
      ],
      "additionalProperties": false
    },
    "related_president": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the related president."
        },
        "presidency_number": {
          "type": "integer",
          "description": "The presidential term number of the related president."
        },
        "relationship_to_president_during_election": {
          "type": "string",
          "description": "The relationship of this president to the president during the election (e.g., 'son')."
        }
      },
      "required": [
        "name",
        "presidency_number",
        "relationship_to_president_during_election"
      ],
      "additionalProperties": false
    },
    "final_answer_president_name": {
      "type": "string",
      "description": "The name of the president who is the answer to the question."
    }
  },
  "required": [
    "election_details",
    "related_president",
    "final_answer_president_name"
  ],
  "additionalProperties": false
}
