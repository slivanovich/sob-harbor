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
Machinists Union Racing: Machinists Union Racing was a CART Indy Car team owned by the International Association of Machinists and Aerospace Workers and run by the IAM's national automotive coordinator Andy Kenopensky, a former appointee to the United States Metric Board.  The team competed in CART from 1981 to 1990.

Robert Fechner: Robert Fechner (22 March 1876 – 31 December 1939) was a national labor union leader and director of the Civilian Conservation Corps (1933–39), which played a central role in the development of state and national parks in the United States.  Born in Chattanooga, Tennessee.  With only a public school elementary education he had risen to become an American labor union leader and vice president of the International Association of Machinists.  He had a reputation for fairness, tact, and patience in all his dealings.  On 5 April 1933 he was appointed by President Franklin Delano Roosevelt to be the Director of the Civilian Conservation Corps (CCC).  It was Fechner's fairness and ability for organization and administration that impressed the president to his appointment as director.  Although he had been an important labor figure, Fechner objected to attempts of union organizers to form unions among CCC enrollees in the camps.  He felt that the government was doing all it possibly could for the well-being of the enrollees: well fed, supporting dependents with monthly earnings, getting an education; and they were contributing in a constructive manner to the conservation needs of the nation.  The need for a union in this situation was not necessary, and he issued orders to keep union organizers out of the CCC camps and gave instructions that if any of the CCC enrolees joined a union they were to be discharged.  Upon Fechner's death while still serving as CCC Director he was succeeded by James McEntee.

Eastern Air Lines Shuttle: Eastern Air Lines Shuttle (or Eastern Air Shuttle) was the brand name of Eastern's air shuttle.  It began operations on April 30, 1961 and was sold in 1989 to Donald Trump, and later became the Trump Shuttle.  In April 1992, the shuttle service began as the USAir Shuttle (presently American Airlines Shuttle).  The shuttle originally flew between New York City, Boston, Washington, D.C. and Newark.  The shuttle's slogan was "Imagine life without us."

William W. Winpisinger: William Wayne Wimpisinger (December 10, 1924 – December 11, 1997) was the eleventh International President of the million-member International Association of Machinists and Aerospace Workers from 1977 until his retirement in 1989.  Well-read in the economics, history and mission of the American labor movement, he was a forceful and articulate spokesman for organized labor and was often invited to testify before House and Senate committees on legislation affecting working people.  During his twelve years as IAM President, he substantially expanded the union's human rights, community services, job safety, public relations and organizing programs.

Frank Lorenzo: Francisco Anthony "Frank" Lorenzo (born May 19, 1940) is an American businessman and philanthropist.  He is most famous for his leadership of Texas International Airlines and its successor holding company Texas Air Corporation between 1972 and 1990, through which he formed or acquired a number of major U.S. airlines including Continental Airlines, Eastern Air Lines, Frontier Airlines, New York Air and People Express Airlines.

Charlie Bryan: Charlie Bryan (11 December 1933 - 2 November 2013) was the head of the International Association of Machinists union in the southeast United States, during the mid to late 1980s.  He led machinists to strike against Eastern Air Lines and Frank Lorenzo in 1989.

Air Midwest: Air Midwest, Inc., was a Federal Aviation Administration Part 121 certificated air carrier that operated under air carrier certificate number AMWA510A issued on May 15, 1965.  It was headquartered in Wichita, Kansas, United States, and was a subsidiary of Mesa Air Group.  Besides initially flying as an independent air carrier, it later operated code sharing feeder flights on behalf of Eastern Air Lines as Eastern Air Midwest Express, on behalf of Trans World Airlines (TWA) as Trans World Express and on behalf of US Airways as US Airways Express.  It also operated feeder flights on behalf of Braniff (1983-1990) and Ozark Air Lines in addition to flying for Mesa Airlines.  Air Midwest was shut down by its parent company, Mesa Airlines, in June 2008.

Trump Shuttle: Trump Shuttle, Inc. was an airline owned by Donald Trump from 1989 to 1992.  The landing rights and some of the physical assets necessary to operate the shuttle flights were originally part of Eastern Air Lines and known as the Eastern Air Lines Shuttle.  It operated hourly flights on Boeing 727 aircraft from LaGuardia Airport in New York City to Logan International Airport in Boston, Massachusetts and Ronald Reagan Washington National Airport in Washington, D.C., then known as Washington National Airport, as well as charter service to other destinations.  Its IATA designator code was TB (later reassigned to Jetairfly).

Eastern Air Lines Flight 212: Eastern Air Lines Flight 212 was an Eastern Air Lines Douglas DC-9-31, carrying 78 passengers and four crew, operating as a scheduled flight within the United States from Charleston, South Carolina to Chicago, Illinois, with an intermediate stop in Charlotte, North Carolina.

Thomas J. Bray: Thomas J. Bray (c. 1867 − 11 December 1933) was an American businessman.  He was educated in Pittsburgh, and began work at age 16 as a pattern-making apprentice for the Lewis Foundry and Machine Company, eventually becoming chief draughtsman.  In 1890 he went back to school, acquiring a mechanical engineering degree from Lehigh University.  After graduating in 1894 he worked for the Ohio Steel Company, McGill and Company, and United Engineering and Foundry Company, where he was chief engineer from 1901 to 1906.  He joined the Republic Iron and Steel Company in 1906, and became its president in April 1911.  He kept that post until April 1928, when he became a director of the Youngstown Sheet and Tube Company.  He died suddenly on 11 December 1933 in his office in Youngstown.

Question: Charlie Bryan (11 December 1933 - 2 November 2013) was the head of the International Association of Machinists union in the southeast United States, during the mid to late 1980s, in 1989, he led machinists to strike against Eastern Air Lines and which American businessman and philanthropist, born on May 19, 1940?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the American businessman and philanthropist."
    },
    "role": {
      "type": "string",
      "description": "The primary role of the person mentioned."
    },
    "date_of_birth": {
      "type": "string",
      "description": "The birth date of the person."
    },
    "strike_details": {
      "type": "object",
      "properties": {
        "year": {
          "type": "integer",
          "description": "The year the strike occurred."
        },
        "union_leader": {
          "type": "string",
          "description": "The name of the union leader who led the strike."
        },
        "against_entities": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of entities the strike was against."
        }
      },
      "required": [
        "year",
        "union_leader",
        "against_entities"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "role",
    "date_of_birth",
    "strike_details"
  ],
  "additionalProperties": false
}
