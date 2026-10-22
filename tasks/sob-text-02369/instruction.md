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
David Cruz Thayne: David Cruz Thayne (March 10, 1971) is an American small businessman, former professional tennis player, and Democratic congressional candidate.  He formerly served as chief of staff and campaign manager to Utah State Senate Minority Leader Scott Howell, a Democrat, and currently operates his own tennis-oriented small business in Southern California which has also led to the production of two tennis oriented documentaries.  He was a candidate for California’s 26th Congressional District in the United States House of Representatives elections in California, 2012.

David Morgan (psychoanalyst): David Howell Morgan (BAHons D.Clin.Psych.  FBPAS FPBPA SMBPF.  Training Analyst Supervisor IPA.  AMBPS.  MBPC) is a psychoanalyst and consultant psychotherapist who has worked at the Portman Clinic London for 25 years.  He went on to specialise in patients' presenting with problems around sexuality and violence.  Morgan co-edited a popular textbook on sexuality, perversion and delinquency.  He is now a psychoanalyst and consultant seeing private patients and provides consultations to political groups.  He is chair of the Political Minds Seminars at the British Psychoanalytic Society.  He regularly contributes to radio and television and lectures nationally and internationally.  Morgan’s recent research has focused on the psychological implications for whistleblowers and the conditions, socially, politically, and psychologically under which a person may "turn a blind eye" or take on the responsibility of whistleblowing.  He also presents a podcast called "Frontier Psychoanalyst" on BBC i-player.  

Matilda Howell: Lida Scott Howell (August 28, 1859 – December 20, 1938) was an American female archer who competed in the early twentieth century.  She won three gold medals in Archery at the 1904 Summer Olympics in Missouri in the double national and Columbia rounds and for the US team.

Rudy Giuliani: Rudolph William Louis Giuliani {'1': ", '2': ", '3': ", '4': "} ( ; born May 28, 1944) is an American lawyer, businessman, public speaker, former mayor of New York City, and an informal adviser on cybersecurity to the White House.

Jun Choi: Jun H. Choi (born May 17, 1971) is an American politician and the former Mayor of Edison, New Jersey, a community of over 100,000 people and the fifth largest municipality in the state.  He was sworn in on January 1, 2006 as the youngest mayor in Edison history and the first Asian American mayor of a major city in New Jersey.  He began a good government, reform movement that led to greater fiscal responsibility, economic development, public education improvements, environmental protection and civic engagement.  Prior to becoming Mayor of Edison, Choi worked in both business and government.  He served as a senior official on education policy at the New Jersey Department of Education where he started the NJ SMART Program, improving public school education performance metrics for 1.4 million New Jersey children.  He also served in the White House Office of Management and Budget and worked as a management consultant focusing on strategy and technology issues for Fortune 500 US corporations.

Pete Ashdown: Peter Lynn "Pete" Ashdown (born January 11, 1967) is the founder and CEO of Utah's first independent and oldest Internet service provider, XMission.  Running as the Democratic candidate in 2006, Ashdown lost to incumbent U.S. Senator Orrin Hatch.  Ashdown ran again in 2012 for the U.S. Senate, but was defeated in his pursuit of the Democratic nomination at the state convention by Scott Howell.

Howell School: Howell School is a historic school building in Dothan, Alabama.  The school was built in 1902 to replace the previous grammar school that had burned in 1901.  It was named in 1916 for the recently deceased Dr. Robert Graves Howell, who was mayor when the first grammar school was built.  A second school was built in 1911, and Howell was replaced by Minnie T. Heard Elementary School in 1942.  After being used by the Salvation Army during World War II, the building was converted for use as a textile mill in 1947.  A number of companies operated out of the building until 1952, when the Dothan Manufacturing Company took over the property.  A one-story addition was constructed on the front of the building in 1965, obscuring the façade.  The plant closed in 1997, and was sold to the Southern Alabama Regional Council on the Aging in 2003, before the city re-acquired it in 2008.

Scott Howell (footballer): Scott Howell (born 10 May 1958) is a former Australian rules footballer who played with Carlton in the VFL during the early 1980s.

Scott Howell (political consultant): Herbert Weston Scott Howell III is an American conservative political consultant, whose recent clients include Meg Whitman and Rudy Giuliani.

United States Senate election in Utah, 2012: The 2012 United States Senate election in Utah took place on November 6, 2012, concurrently with the 2012 U.S. presidential election as well as other elections to the United States Senate and House of Representatives and as various state and local elections.  Incumbent Republican U.S. Senator Orrin Hatch won re-election to a seventh term against former state Senator and IBM executive, Scott Howell the Democratic candidate.

Question: Scott Howell is a consultant who has worked with the mayor of what city?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "consultant_name": {
      "type": "string",
      "description": "The name of the political consultant."
    },
    "client_details": {
      "type": "object",
      "properties": {
        "client_name": {
          "type": "string",
          "description": "The name of the client who was a mayor."
        },
        "client_role": {
          "type": "string",
          "description": "The role of the client, specifically related to being a mayor."
        },
        "city_of_mayorship": {
          "type": "string",
          "description": "The city where the client served as mayor."
        }
      },
      "required": [
        "client_name",
        "client_role",
        "city_of_mayorship"
      ],
      "additionalProperties": false
    },
    "relationship_type": {
      "type": "string",
      "description": "Describes the nature of the relationship between the consultant and the client."
    }
  },
  "required": [
    "consultant_name",
    "client_details",
    "relationship_type"
  ],
  "additionalProperties": false
}
