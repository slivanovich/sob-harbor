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
Central State Hospital (Kentucky): Central State Hospital is a 192-bed adult psychiatric hospital located in eastern Louisville-Jefferson County, Kentucky.  In 1869, 200 acres were purchased by the Kentucky State Legislature from the descendants of renown frontiersman Issac Hite to establish a "State House of Reform for Juvenile Delinquents."  This was located on the outskirts of what would become Anchorage, Kentucky.  In 1873, due to overcrowding at both of Kentucky's mental hospitals, the House of Reform was converted into the Fourth Kentucky Lunatic Asylum, with Dr. C.C. Forbes as its first Superintendent.  The following year an act of the legislature renamed it the Central Kentucky Lunatic Asylum.  In late 1887, it received its own post office, called simply "Asylum".  The following year its name was changed to "Lakeland", and the institution was commonly referred to as "Lakeland Hospital" or "Lakeland Asylum".  By 1900, its official name had been changed to the Central Kentucky Asylum for the Insane.  By 1912 it was known as Central State Hospital.  Comparable institutions are Eastern State Hospital at Lexington in Fayette County and Western State Hospital at Hopkinsville, Christian County, Kentucky.  All three were administered by the Board of Charitable Organizations.

Bridgewater State Hospital: Bridgewater State Hospital, located in southeastern Massachusetts, is a state facility housing the criminally insane and those whose sanity is being evaluated for the criminal justice system.  It was established in 1855 as an almshouse.  It was then used as a workhouse for inmates with short sentences who worked the surrounding farmland.  It was later rebuilt in the 1880s and again in 1974.  Bridgewater State Hospital currently houses 309 inmates all of whom are adult males.  The facility was the subject of the 1967 documentary "Titicut Follies".  Bridgewater State Hospital falls under the jurisdiction of the Massachusetts Department of Correction.

Titicut Follies: Titicut Follies is a 1967 American Direct Cinema documentary film directed by Frederick Wiseman and filmed by John Marshall, about the patient-inmates of Bridgewater State Hospital for the criminally insane, a Massachusetts Correctional Institution in Bridgewater, Massachusetts.  In 1967 the film won awards in Germany and Italy.  Later on, Wiseman made a number of such films examining social institutions (e.g. hospitals, police, schools, etc.) in the United States.

Edgewood State Hospital: Edgewood State Hospital was a tubercular/psychiatric hospital complex that formerly stood in Deer Park, New York, on Long Island, New York, USA.  It was one of four state mental asylums built on Long Island (the others being Kings Park State Hospital, Central Islip State Hospital, and Pilgrim State Hospital), and was the last one of the four to be built.

Larry Hollingsworth Strasburger: Larry H. Strasburger is an American psychiatrist.  He served at the Bridgewater State Hospital and had a contract with McLean Hospital.  He also was a vice-president of the AAPL and later became its President.

Old Colony Correctional Center: Old Colony Correctional Center is a Massachusetts Department of Correction prison for men in Bridgewater, Massachusetts.  The medium security facility is located in a 30 acre plot of land in the Bridgewater Correctional Complex with the Bridgewater State Hospital, Massachusetts Alcohol and Substance Abuse Center, and the Massachusetts Treatment Center.  Old Colony Correctional Center Minimum Unit is under the authority of the correctional center; until the closing of the Southeastern Correctional Center in 2002, the minimum unit, established in the early 1980s, was under the authority of Southeastern.

WBIM-FM: WBIM-FM (91.5 FM) is a non-commercial, educational radio station broadcasting 24/7 from the campus of Bridgewater State University.  The station has a mostly alternative and indie rock format during regular automation, but the station does have many specialty shows which cater to such formats as R&B, Metal, Jazz, Hip Hop, sports, decade specific, and many other formats.  Licensed to Bridgewater, Massachusetts, United States.  The station is currently owned by Bridgewater State University.

Worcester State Hospital Farmhouse: The Worcester State Hospital Farmhouse is a historic psychiatric hospital building at 361 Plantation Street, on the former grounds of the Worcester State Hospital in Worcester, Massachusetts.  Built in 1895, it is a well-preserved local example of Georgian Revival architecture, and is notable as a prototype for similar buildings in the Massachusetts state hospital network.  It served as an outbuilding of Worcester State Hospital until 1969, housing select residents who worked in its fields.  It now houses state mental health offices.  It was listed on the National Register of Historic Places in 2017.

Law and Order (1969 film): Law and Order is a 1969 documentary film by Frederick Wiseman that shows the daily routine of officers of the Kansas City Police Department.  It was Wiseman's third film after "Titicut Follies" (1967) and "High School" (1968).  The films were among the earliest examples of direct cinema by a U.S. filmmaker.

The True Glory: The True Glory (1945) is a co-production of the US Office of War Information and the British Ministry of Information, documenting the victory on the Western Front, from Normandy to the collapse of the Third Reich.

Question: Which film depicted patient-inmates of Bridgewater State Hospital, Titicut Follies or The True Glory?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_name": {
      "type": "string",
      "description": "The name of the film that depicted patient-inmates of Bridgewater State Hospital."
    },
    "film_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "hospital_depicted": {
      "type": "string",
      "description": "The name of the hospital whose patient-inmates were depicted in the film."
    },
    "film_director": {
      "type": "string",
      "description": "The director of the film."
    },
    "film_genre": {
      "type": "string",
      "description": "The genre of the film."
    }
  },
  "required": [
    "film_name",
    "film_year",
    "hospital_depicted",
    "film_director",
    "film_genre"
  ],
  "additionalProperties": false
}
