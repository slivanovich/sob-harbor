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
Fred Moore (attorney): Fred H. Moore was a socialist lawyer and the defense attorney of the controversial Sacco and Vanzetti case.  He had collaborated in many labor and Industrial Workers of the World trials.  He played a minor role in several celebrated I.W.W. trials, including the Los Angeles Times bombing case in 1911 and the trial of Ettor-Giovannitti case, which arose from the 1912 Lawrence, Massachusetts, textile strike.  Following acquittal in the Ettor-Giovannitti case, Moore spent the next several years roaming the country defending I.W.W. organizers.  He was involved in the Centralia Massacre trial and the mass prosecution, on charges of sedition, of the I.W.W. in Chicago in 1918.  Errors in a later trial, however, led Big Bill Haywood to demand Moore's resignation as I.W.W. attorney in 1920.  Moore's career was revived by his hiring to head the defense team for Sacco and Vanzetti in the summer of 1920.

Bobby Lee Cook: Bobby Lee Cook is a defense attorney from Summerville, Georgia, in Chattooga County.  He has practiced law since the late 1940s, and is known for combining a sharp legal mind with a folksy demeanor.  He has represented a wide variety of clients, from rural Southerners to international businessmen and corporations.  He is reputed to have been the inspiration for the television series Matlock, which starred Andy Griffith as a Georgia attorney.

Michael Rains: Michael Rains is a California criminal defense attorney known for representing police accused of misconduct, including the case of the BART Police shooting of Oscar Grant and a successful defense of the Oakland Riders.  Rains also won acquittal of the Corcoran 8, prison guards accused of staging fights amongst inmates.  He formerly represented baseball player Barry Bonds who was ultimately exonerated by the 9th Circuit Court of Appeals with respect to a perjury allegation.

Peter DeTroy: Peter DeTroy (April 13, 1948 – May 28, 2016) was an American defense attorney from Portland, Maine.  He graduated from Bowdoin College in 1969 and then received his law degree from the University of Maine School of Law in 1972.  DeTroy was a prominent defense attorney.  He served on the Falmouth School Board.  He was partner in the firm Norman, Hansen & DeTroy from 1984 until his death.  DeTroy was named one of 50 difference-makers in Maine by Maine Magazine in 2013.  DeTroy represented the famed defense attorney F. Lee Bailey, who is now a Maine resident, in his attempt to be able to practice law in the state after having been disbarred elsewhere.

Brian Banks (American football): Brian Banks (born July 24, 1985) is a former American football linebacker.  He signed with the Atlanta Falcons of the National Football League (NFL) on April 3, 2013.  Banks previously signed as an undrafted free agent with the Las Vegas Locomotives of the United Football League in 2012.

Phil Spector (film): Phil Spector is a television film directed and written by David Mamet.  The film is based on the murder trials of record producer, songwriter and musician Phil Spector, and was released by HBO Films on March 24, 2013, in United States.  It stars Al Pacino as Phil Spector, Helen Mirren as defense attorney Linda Kenney Baden, and Jeffrey Tambor as Bruce Cutler.  It focuses primarily on the relationship between Phil Spector and Linda Kenney Baden, his defense attorney during the first of his two murder trials for the 2003 death of Lana Clarkson in his California mansion.

Cristina Gutierrez: Maria Cristina Gutierrez (February 28, 1951 – January 30, 2004) was an American criminal defense attorney who represented several high profile defendants in the 1990s and the first Hispanic woman to be counsel of record in a case before the Supreme Court of the United States.  She was the initial trial attorney for Adnan Syed, the Baltimore area teen who was convicted of murdering his ex-girlfriend, Hae Min Lee in 1999.  The murder trial and conviction gained national attention in 2014 and 2015 after being the subject of the first season of the online podcast "Serial".

Richard Brooks (actor): Richard L. Brooks (born December 9, 1962) is an American actor, singer, and director.  He is best known for his one-off role as the eccentric bounty hunter Jubal Early in the space-western "Firefly" and Paul Robinette in the NBC drama series, "Law & Order" from 1990 to 1993 and reprising his role as a defense attorney on that same show.  In 2013, he began starring as Patrick Patterson in the BET drama series, "Being Mary Jane".

Arthur L. Aidala: Arthur L. Aidala (born 1967 in Brooklyn, New York), currently a New York criminal defense lawyer and legal analyst on Fox News Channel where he appears on various day-time and prime-time programs.  He was recently a guest lecturer at Harvard University's Law School at the invitation of professor Alan Dershowitz.  In 2012, Aidala was selected as one of New York City's top criminal defense attorneys by "Super Lawyers Magazine" .  Aidala is the grandson of Artie Aidala, renowned New York State Athletic Commission's ring judge inducted into the World Boxing Hall of Fame in 2008 .  Artie Aidala was one of the three judges that decided the outcome of the 1971 Ali v. Frazier "Fight of the Century" boxing match in Madison Square Garden  .  He is the son of Louis R. Aidala, former Manhattan Assistant District Attorney and a criminal defense attorney in practice for 50 years.  Louis Aidala was a special prosecutor for the Attica prison riots and more recently represented celebrity Jennifer Lopez in New York City  .

Justin Brooks: Justin Brooks (born 1965) is an American criminal defense attorney, known internationally for his work in exonerating wrongfully-convicted people and training judges, prosecutors and defense attorneys.  He is a co-founder and currently serves as director of the California Innocence Project (CIP), which has freed a number of high-profile innocent clients, including former NFL football player Brian Banks.  The CIP is a founding member of the Innocence Network, an affiliation of organizations dedicated to providing pro bono legal and investigative services to wrongfully convicted people.  Brooks is frequently interviewed on broadcast media and in print media about his cases and other legal issues.

Question: Justin Brooks is a defense attorney that represented the NFL player who played for what team in 2013?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "defense_attorney": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the defense attorney."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "client": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the client represented by the attorney."
        },
        "profession": {
          "type": "string",
          "description": "The profession of the client."
        },
        "team_name": {
          "type": "string",
          "description": "The name of the team the client played for."
        },
        "team_signing_year": {
          "type": "integer",
          "description": "The year the client signed with the team."
        }
      },
      "required": [
        "name",
        "team_name",
        "team_signing_year"
      ],
      "additionalProperties": false
    },
    "representation_context": {
      "type": "string",
      "description": "Context of the attorney's representation of the client."
    }
  },
  "required": [
    "defense_attorney",
    "client",
    "representation_context"
  ],
  "additionalProperties": false
}
