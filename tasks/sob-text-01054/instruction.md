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
Policy Planning Staff (United States): The Policy Planning Staff (sometimes referred to as the Policy Planning Council, the Office of Policy Planning or by its in-house acronym S/P) is the principal strategic arm of the United States Department of State.  It was created in 1947 by renowned Foreign Service Officer George F. Kennan at the request of Secretary of State George Marshall to serve "as a source of independent policy analysis and advice for the Secretary of State."  Its first assignment was to design the Marshall Plan.

Director of Policy Planning: The Director of Policy Planning is the United States Department of State official in charge of the Department's internal think tank, the Policy Planning Staff.  In the Department, the Director of Policy Planning has a rank equivalent to Assistant Secretary.  The position has traditionally been held by many members of the U.S. foreign policy establishment.  Former Directors of Policy Planning include two National Security Advisors, a President of the World Bank, and several presidents of the prestigious Council on Foreign Relations.

Dennis Ross: Dennis B. Ross (born November 26, 1948) is an American diplomat and author.  He has served as the Director of Policy Planning in the State Department under President George H. W. Bush, the special Middle East coordinator under President Bill Clinton, and was a special adviser for the Persian Gulf and Southwest Asia (which includes Iran) to the former Secretary of State Hillary Clinton.

George H. W. Bush: George Herbert Walker Bush (born June 12, 1924) is an American politician who was the 41st President of the United States from 1989 to 1993 and the 43rd Vice President of the United States from 1981 to 1989.  A member of the Republican Party, he was previously a congressman, ambassador, and Director of Central Intelligence.  He is the oldest living former President and Vice President.  Previously known as simply "George Bush", since 2001, Bush has often been referred to as "George H. W. Bush", "Bush 41", "Bush the Elder", or "George Bush Senior" to distinguish him from his eldest son, George W. Bush, the 43rd President of the United States.

Jared Cohen: Jared Cohen (born November 24, 1981) is the President of Jigsaw (previously Google Ideas) and an Adjunct Senior Fellow at the Council on Foreign Relations.  Previously, he served as a member of the Secretary of State's Policy Planning Staff and as an advisor to Condoleezza Rice and later Hillary Clinton.  Initially brought in by Condoleezza Rice as a member of the Policy Planning Staff, he was one of a few staffers that stayed under Hillary Clinton later referenced in an article entitled "Tweeting While Tehran Burns".  In this capacity, he focused on counter-terrorism, counter-radicalization, Middle East/South Asia, Internet freedom, and fostering opposition in repressive countries.  According to "The New York Times Magazine", right before his departure Cohen was one of the participating architects of what was labeled in 2010 as "21st century statecraft" along with Richard Boly and several foreign service officers in the Department of State's Office of eDiplomacy In 2013, Cohen was named by Time Magazine as one of its 100 most influential people.

Anne-Marie Slaughter: Anne-Marie Slaughter (born September 27, 1958) is an international lawyer, foreign policy analyst, political scientist and public commentator.  She received a B.A. from Princeton University in 1980, an M.Phil from Oxford University in 1982, a Harvard Law School, J.D. in 1985, and a D.Phil in International Relations from Oxford in 1992.  Most notably she is a member of the International Law Association, American Society of International Law, American Bar Association, American Academy of Arts and Sciences, and World Peace Foundation.  During her academic career, she has taught at Princeton University, the University of Chicago, and Harvard University.  From 2002 to 2009, she was the Dean of Princeton University's Woodrow Wilson School of Public and International Affairs and the Bert G. Kerstetter '66 University Professor of Politics and International Affairs.  She was subsequently the first woman to serve as the Director of Policy Planning for the U.S. State Department from January 2009 until February 2011 under U.S. Secretary of State Hillary Clinton.  She is a former president of the American Society of International Law and the current President and CEO of New America.  She married Princeton professor Andrew Moravcsik; they live in Princeton with their two sons.

Richard N. Haass: Richard Nathan Haass (born July 28, 1951) is an American diplomat.  He has been president of the Council on Foreign Relations since July 2003, prior to which he was Director of Policy Planning for the United States Department of State and a close advisor to Secretary of State Colin Powell.  The Senate approved Haass as a candidate for the position of ambassador and he has been U.S. Coordinator for the Future of Afghanistan.  He succeeded George J. Mitchell as the United States Special Envoy for Northern Ireland to help the peace process in Northern Ireland, for which he received the State Department's Distinguished Service Award.  At the end of 2003, Mitchell Reiss succeeded him as special envoy.  In late 2013, Haass returned to Northern Ireland to chair inter-party talks aimed at addressing some of the unresolved issues from the peace process such as parades, flags and "the past".

Winston Lord: Winston Lord (born August 14, 1937) is a United States diplomat and leader of non-governmental foreign policy organizations.  He served as Special Assistant to the National Security Advisor (1970-1973), Director of the State Department Policy Planning Staff (1973-1977), President of the Council on Foreign Relations (1977-1985), Ambassador to China (1985–1989) and Assistant Secretary of State (1993–1997).

Angela Stent: Angela Stent is a foreign policy expert specialising in US and European relations with Russia and Russian foreign policy.  She is Professor of Government at Georgetown University and director of its Center for Eurasian, Russian, and East European Studies.  She is also a non-resident senior fellow at the Brookings Institution.  She has served in the Office of Policy Planning in the US State Department and as National Intelligence Officer for Russia and Eurasia.

The Missing Peace: The Missing Peace: The Inside Story of the Fight for Middle East Peace (ISBN  ) is a 2004 non-fiction book by Dennis Ross on the history of and his participation in the Israeli–Palestinian peace process and the Arab–Israeli peace process.  Ross, an American diplomat, was the Director of Policy Planning in the State Department under President George H. W. Bush and the special Middle East coordinator under President Bill Clinton.

Question: What other role did George H. W. Bush have besides Director of Policy Planning in the State Department? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the person in question."
    },
    "was_director_of_policy_planning": {
      "type": "boolean",
      "description": "Indicates whether the person held the role of Director of Policy Planning according to the context."
    },
    "other_significant_roles": {
      "type": "array",
      "description": "A list of other significant roles held by the person, as mentioned in the context.",
      "items": {
        "type": "string"
      }
    },
    "specific_role_answering_question": {
      "type": "string",
      "description": "The specific role that directly answers the question, chosen from the other_significant_roles."
    }
  },
  "required": [
    "person_name",
    "was_director_of_policy_planning",
    "other_significant_roles",
    "specific_role_answering_question"
  ],
  "additionalProperties": false
}
