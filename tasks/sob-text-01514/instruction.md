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
Watergate Seven: The Watergate Seven has two meanings: (1) it refers to the five men caught June 17, 1972 burglarizing the Democratic National Committee’s headquarters in the Watergate Hotel and their two handlers, E. Howard Hunt and G. Gordon Liddy (two Nixon campaign aides), all of whom were tried before Judge John Sirica in January 1973; (2) it refers to the seven advisors and aides to United States President Richard M. Nixon who were indicted by a grand jury on March 1, 1974 for their role in the Watergate scandal.  The grand jury also named Nixon an unindicted conspirator.  The indictments marked the first time in U.S. history that a president was so named.

G. Gordon Liddy: George Gordon Battle Liddy (born November 30, 1930), better known as G. Gordon Liddy, is a (disbarred) American lawyer who is best known as the chief operative in the White House Plumbers unit that existed from July to September 1971, during Richard Nixon's presidency.  He was convicted of conspiracy, burglary, and illegal wiretapping for his role in the Watergate scandal.

White House Plumbers: The White House Plumbers, sometimes simply called the Plumbers, was a covert White House Special Investigations Unit, established July 24, 1971, during the presidency of Richard Nixon.  Its task was to stop the leaking of classified information, such as the "Pentagon Papers", to the news media.  Its members branched into illegal activities while working for the Committee to Re-elect the President, including the Watergate break-in and the ensuing Watergate scandal.

E. Howard Hunt: Everette Howard Hunt Jr. (October 9, 1918 – January 23, 2007), better known as E. Howard Hunt, was an American intelligence officer and writer.  From 1949 to 1970, Hunt served as an officer in the Central Intelligence Agency (CIA).  Along with G. Gordon Liddy and others, Hunt was one of the Nixon administration "plumbers", a secret team of operatives charged with fixing "leaks" – real or perceived causes of confidential administration information being leaked to outside parties.  Hunt and Liddy plotted the Watergate burglaries and other undercover operations for the Nixon administration.  In the ensuing Watergate scandal, Hunt was convicted of burglary, conspiracy, and wiretapping, eventually serving 33 months in prison.

Anthony Ulasewicz: Anthony "Tony" Ulasewicz (December 14, 1918 in New York, United States – December 17, 1997 in Glens Falls, New York) was a figure in the Watergate scandal, delivering hundreds of thousands of dollars in "hush money" to Watergate defendants G. Gordon Liddy and E. Howard Hunt.  He also investigated the lives of notable Democrats like Senator Edward M. Kennedy.  He was of Polish descent.

John Sirica: John Joseph Sirica (March 19, 1904 – August 14, 1992) was the Chief Judge for the United States District Court for the District of Columbia, where he became famous for his role in the trials stemming from the Watergate scandal.  He rose to national prominence during the Watergate scandal when he ordered President Richard Nixon to turn over his recordings of White House conversations.

The Final Days: The Final Days is a 1976 non-fiction book written by Bob Woodward and Carl Bernstein about the Watergate scandal.  A follow up to their book "All the President's Men", "The Final Days" concerns itself with the final months of the Presidency of Richard Nixon including battles over the Nixon White House tapes and the impeachment process against Richard Nixon.

White House horrors: The White House Horrors is a term attributed to Richard Nixon's former United States Attorney General, John N. Mitchell to describe the crimes and abuses committed by Nixon's staff during his presidency.  The revelation of their existence and scope is among the many events of the Watergate scandal.  More than 70 people were convicted of crimes related to Watergate (some pleaded guilty before trial).

Geoff Shepard: Geoffrey Carroll "Geoff" Shepard (born November 7, 1944) is an American lawyer, author and lecturer.  He is best known for his work on the White House staff of President Richard Nixon and his subsequent efforts to document policy initiatives of the Nixon Administration — including presenting alternative views of the Watergate scandal that drove President Nixon from office.

Will: G. Gordon Liddy: Will: G. Gordon Liddy is an American television film which first aired on NBC in January 1982.  The film depicts the rise and fall of Watergate co-conspirator G. Gordon Liddy.  Liddy was portrayed by two different actors: American actor Robert Conrad played Liddy as an adult and child-actor Danny Lloyd portrayed him in his youth.  Other figures associated with the Watergate scandal and portrayed in this film include Jeb Magruder and John Dean.  The movie was directed by Robert Lieberman and was based on Liddy's 1980 autobiography.

Question: Anthony "Tony" Ulasewicz, was a figure in the Watergate scandal, delivering hundreds of thousands of dollars in "hush money" to which Watergate defendant, George Gordon Battle Liddy is a (disbarred) American lawyer who is best known as the chief operative in the White House Plumbers unit that existed from July to September 1971, during Richard Nixon's presidency, better known as who ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the individual."
    },
    "better_known_as": {
      "type": "string",
      "description": "The common name or alias by which the individual is known."
    },
    "role_in_scandal": {
      "type": "string",
      "description": "The primary role or association of the individual in the Watergate scandal."
    },
    "associated_units": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Units or groups the individual was associated with."
    }
  },
  "required": [
    "person_name",
    "better_known_as",
    "role_in_scandal",
    "associated_units"
  ],
  "additionalProperties": false
}
