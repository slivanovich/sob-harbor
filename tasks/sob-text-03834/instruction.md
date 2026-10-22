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
Jay Carney: James "Jay" Carney (born May 22, 1965) is an American journalist and served as a White House press secretary for President Barack Obama.

West Wing Week: West Wing Week is a weekly released web-episode by The White House of the week's events concerning the President of the United States.  The show was created in 2010 during the 2nd year of the Presidency of Barack Obama.  The footage is currently shot and edited by the video team from the Office of Digital Strategy and narrated by White House Press Secretary Josh Earnest; it was initially shot and edited by former White House videographer Arun Chaudhary, who created the series.

Gerald Lee Warren: Gerald Lee "Jerry" Warren (August 17, 1930 – March 20, 2015) was a United States journalist and newspaper editor at "The San Diego Union-Tribune".  He served under Ron Ziegler as deputy press secretary in the Richard Nixon administration until 1974.  He served as Nixon's "de facto" final White House Press Secretary after Ron Ziegler's appointment as Assistant to the President in June 1974, though Zielger kept the title.  He then held the same position as well as White House Director of Communications in the Gerald Ford administration until 1975.

2014 State of the Union Address: The 2014 State of the Union Address was given by President Barack Obama on Tuesday, January 28, 2014, in the chamber of the United States House of Representatives.  It was addressed to the 113th United States Congress, and the Senate was present.  According to tradition, House Speaker John Boehner invited the president on December 13 to address a joint session of Congress.  White House Press Secretary Jay Carney confirmed the president's attendance later that day.

Lindsay Walters: Lindsay Walters is an American political aide, currently serving as White House Deputy Press Secretary.  Until his resignation, she had been adviser to incoming press secretary Sean Spicer.  Before this appointment, she had been National Spokesperson at Republican National Committee for a year and two-thirds.

Josh Earnest: Joshua Ryan Henry Earnest (born January 22, 1975) is an American political aide who served as White House press secretary under President Barack Obama, from 2014 to 2017.  He succeeded Jay Carney as Obama's press secretary, in 2014, and was succeeded by President Donald Trump's first Presidential press secretary, Sean Spicer.

Eric Schultz: Eric Schultz is a senior advisor to former President Barack Obama and is the founder of Schultz Group.  Schultz is a former White House Principal Deputy Press Secretary and special assistant to President Obama.  Recognized by "Politico" as the strategist “White House officials turn to in a crisis to handle communications,” Schultz was originally hired at the White House in 2011 to respond to Congressional oversight investigations.  After White House Deputy Press Secretary Josh Earnest replaced Jay Carney to become White House Press Secretary, Schultz was appointed White House Deputy Press Secretary.  In this role, Schultz often diffuses "tensions with humor.  But he can be relentless in pushing his message in both public and private conversations.”  Former White House Communications Director Jen Psaki compared Schultz to fictional crisis manager Olivia Pope, "he's the person you want next to you in a foxhole when there's a crisis."  At the end of President Obama's second term, former White House Senior Advisor Valerie Jarrett said of Schultz, “We’ve all grown to rely on his wise counsel" and that the President "trusts his sound judgement."

Dana Perino: Dana Marie Perino (born May 9, 1972) is an American political commentator and author who served as the 26th White House Press Secretary, serving under President George W. Bush from September 14, 2007 to January 20, 2009.  She was the second female White House Press Secretary, after Dee Dee Myers, who served during the Clinton Administration.  She is currently a political commentator for Fox News, while also serving as a co-host of the network's talk show "The Five", and is a book publishing executive at Random House.  Starting Monday, October 2nd, she will host "The Daily Briefing with Dana Perino" on Fox News.

James S. Brady Press Briefing Room: The James S. Brady Press Briefing Room is a small theater in the West Wing of the White House where the White House Press Secretary gives briefings to the news media and the President of the United States sometimes addresses the press and the nation.  It is located between the workspace assigned to the White House press corps and the office of the Press Secretary.

Claire Shipman: Claire Shipman is an American television journalist, currently the senior national correspondent for ABC's "Good Morning America".  She also blogs at the website "True/Slant".  She is married to Jay Carney, President Barack Obama's former White House Press Secretary.

Question: Eric Schultz is a senior advisor to former President Barack Obama and is the founder of Schultz Group, after White House Deputy Press Secretary Josh Earnest replaced Jay Carney to become White House Press Secretary, Joshua Ryan Henry Earnest, is an American political aide who served as White House press secretary under President Barack Obama, from which time span?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "press_secretary_name": {
      "type": "string",
      "description": "The full name of the White House Press Secretary."
    },
    "president_served_under": {
      "type": "string",
      "description": "The President under whom the press secretary served."
    },
    "role": {
      "type": "string",
      "description": "The specific role held by the individual."
    },
    "service_start_year": {
      "type": "integer",
      "description": "The year the individual began their service in the specified role."
    },
    "service_end_year": {
      "type": "integer",
      "description": "The year the individual ended their service in the specified role."
    }
  },
  "required": [
    "press_secretary_name",
    "president_served_under",
    "role",
    "service_start_year",
    "service_end_year"
  ],
  "additionalProperties": false
}
