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
Hawaii House of Representatives: The Hawaii House of Representatives is the lower house of the Hawaii State Legislature.  Pursuant to Article III, Section 3 of the Hawaii Constitution, amended during the 1978 constitutional convention, the House of Representatives consists of 51 members representing an equal amount of districts across the islands.  It is led by the Speaker of the House elected from the membership of the House, with majority and minority leaders elected from their party's respective caucuses.  The current Speaker of the House is Scott Saiki.

Speaker of the Abia State House of Assembly: The Speaker of the Abia State House of Assembly is the political head of the Abia State legislative who serves as the preciding officer of the Abia State House of Assembly.  The Speaker is elected by Members of the House with the sole responsibilities of conducting meetings of the House, appointing committees and enforcing the Rules of the House.  The current speaker is Chikwendu Kanu, a People's Democratic Party member who was sworn in on 30 December 2016, succeeding Kennedy Njoku.

Speaker of the House of Commons (Canada): The Speaker of the House of Commons of Canada (French: "Président de la Chambre des communes" ) is the presiding officer of the lower house of the Parliament of Canada and is elected at the beginning of each new parliament by fellow Members of Parliament (MPs).  The Speaker's role in presiding over Canada's House of Commons is similar to that of speakers elsewhere in other countries that use the Westminster system (see Speaker of the House of Commons).  The current Speaker is Geoff Regan.  The Speaker with the longest tenure is Peter Milliken who served four consecutive parliaments in 10 years, 124 days.

Lester Bronson: Lester Daniel Bronson (December 23, 1905 – January 24, 1972) was a Democrat and represented Nome, Alaska as a member of Alaska territorial House of Representatives 2nd District, 1955-56; in the 1st Alaska State Legislature as a Senator 1959-1960; 2nd Alaska State Legislature as a Senator 1961-1962; 3rd Alaska State Legislature 1963-1965 as a Senator and in the 6th Alaska State Legislature

Hawaii State Legislature: The Hawaii State Legislature is the state legislature of the U.S. state of Hawaii.  The state legislature is a bicameral body consisting of a lower house, the Hawaii State House of Representatives, with 51 representatives, and an upper house, the 25-member Hawaii State Senate.  There are a total of 76 representatives in the legislature, each representing single member districts across the islands.  The powers of the legislature are granted under Article III of the Constitution of Hawaii.

Linda Upmeyer: Linda L. Upmeyer (born July 23, 1952) is the Iowa State Representative from the 54th District.  She has served in the Iowa House of Representatives since 2003 and is the current Speaker of the Iowa House of Representatives.  She is the first female Speaker in Iowa's history.  She received her BSN from the University of Northern Iowa and her MSN from Drake University.  On August 19, 2015 was elected by the members of the Iowa House of Representatives Republican majority to serve as the Speaker of the House.  Upmeyer's father, Del Stromer served as Speaker from 1981–82.

Arizona State Legislature: The Arizona State Legislature is the state legislature of the U.S. state of Arizona.  It is a bicameral legislature that consists of a lower house, the House of Representatives, and an upper house, the Senate.  Composed of 90 legislators, the state legislature meets in the Capitol Complex in the state capital of Phoenix, Arizona.  Created by the Arizona Constitution upon statehood in 1912, the Arizona State Legislature met biennially until 1950.  Today, they meet annually.

Rida Cabanilla: Rida T.R. Cabanilla Arakawa (born December 24, 1952 in Ilocos Sur, Philippines) is an American politician and a Democratic member of the Hawaii House of Representatives since January 16, 2013 representing District 41.  Cabanilla consecutively served from January 2005 until 2013 in the District 42 seat.

Point of information (competitive debate): In competitive debate, most commonly in the World Schools, Karl Popper and British Parliamentary debate styles, a Point of Information or a POI is when a member of the team opposing that of the current speaker gets to briefly interrupt the current speaker, offering a POI in the form of a question or a statement.  This may be as a correction, asking for clarity or just a plain question.  As in some debating styles, such as World Schools Style, they often may not be offered in the first or last minute of any speech (known as "protected time"), or during reply speeches.  Points of information may never be offered to a member of the same team.

Dennis Pennington: Dennis Pennington (May 18, 1776 – September 2, 1854) was a farmer and a stonemason who became known for his many years in public office as an early legislator in the Indiana Territory and in Indiana's General Assembly as a representative of Harrison County, Indiana.  Pennington, a member of the Whig Party, became the first speaker of the Indiana territorial legislature's lower house in 1810, served as the territory's census enumerator in 1815, and represented Harrison County as one of its five delegates to the constitutional convention of 1816.  Pennington was the first speaker of the Indiana Senate (1816 to 1818), and served in the state legislature for eighteen years, which included five years in the Indiana House of Representatives and thirteen years in the Indiana Senate.  His major political contributions relate to his strong opposition to slavery.  Pennington ran unsuccessfully for Indiana's Lieutenant Governor in 1825.  In addition to his service in the state legislature, Penning was a Harrison County sheriff and a justice of the peace, a trustee of Indiana University, and a member of the Grand Lodge of Indiana.  He also supervised construction of the limestone courthouse that served as Indiana's first state capitol building in Corydon, Indiana.  The historic Old Capitol, the seat of state government from 1816 to 1825, is one of his most enduring legacies.  Fondly remembered as "Old Uncle Dennis" or "Father Pennington," he was known for his common sense and strong character and became one of Harrison County's most influential citizens.

Question: Who is the current Speaker of the House of the state legislature which Rida T.R. Cabanilla Arakawa is a member of?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "legislative_body": {
      "type": "string",
      "description": "The name of the legislative body."
    },
    "state": {
      "type": "string",
      "description": "The U.S. state associated with the legislative body."
    },
    "speaker_of_the_house": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the current Speaker of the House."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "member_in_question": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the member whose legislative body is being queried."
        },
        "legislative_body_membership": {
          "type": "string",
          "description": "The legislative body the member belongs to."
        }
      },
      "required": [
        "name",
        "legislative_body_membership"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "legislative_body",
    "state",
    "speaker_of_the_house",
    "member_in_question"
  ],
  "additionalProperties": false
}
