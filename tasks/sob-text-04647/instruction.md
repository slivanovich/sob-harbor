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
Myron Angel House: The Myron Angel House is a historic house located at 714 Buchon St. in San Luis Obispo, California.  Built circa 1880, the house has a vernacular design which does not follow a particular architectural style.  The two-story wood frame house has redwood siding, a shingled gable roof, and some Eastlake details in the window surrounds and gable ends.  The house was the home of Myron Angel, the main figure in the establishment of California Polytechnic State University.  Angel, who lived in the house from 1889 to his 1911 death, proposed and lobbied for the creation of a polytechnic school in California; it was mainly due to his campaign that Cal Poly was founded in San Luis Obispo.  In addition to his educational activism, Angel was also an influential journalist and historian.

James Tuthill: James Joseph Tuthill (born March 25, 1976 in Upland, California) is a former American football placekicker in the National Football League for the Green Bay Packers, San Diego Chargers, Jacksonville Jaguars, and the Washington Redskins.  He played college football at California Polytechnic State University.

Cal Poly San Luis Obispo College of Engineering: The Cal Poly San Luis Obispo College of Engineering is the engineering college of the California Polytechnic State University in San Luis Obispo, California.  It has over 200 faculty members and more than 6,000 students enrolled in fourteen bachelor's and in eleven master's degree programs through nine engineering departments.

Neale Stoner: Neale R. Stoner is a former college athletics coach and administrator.  He served as the head men's basketball coach at the University of California, San Diego from 1966 to 1969 and at California Polytechnic State University from 1969 to 1972, compiling a career college basketball coaching record of 86–65.  Stoner was the athletic director at California State University, Fullerton from 1972 to 1979 and at the University of Illinois at Urbana–Champaign from 1980 to 1988.

2016 Cal Poly Mustangs football team: The 2016 Cal Poly Mustangs football team represented California Polytechnic State University in the 2016 NCAA Division I FCS football season.  The Mustangs were led by eighth-year head coach Tim Walsh and played their home games at Alex G. Spanos Stadium.  They were members of the Big Sky Conference.  They finished the season 7–5, 5–3 in Big Sky play to finish in a tie for fourth place.  They received an at-large bid to the FCS Playoffs where they lost to San Diego in the first round.

University of California, San Diego: The University of California, San Diego (officially known as the University of California San Diego with no comma or UC San Diego—no longer UCSD because the acronym is similar to that of other San Diego higher education institutions) is a public research university located in the La Jolla neighborhood of San Diego, California, in the United States.  The university occupies 2141 acre near the coast of the Pacific Ocean with the main campus resting on approximately 1152 acre .  Established in 1960 near the pre-existing Scripps Institution of Oceanography, UC San Diego is the seventh oldest of the 10 University of California campuses and offers over 200 undergraduate and graduate degree programs, enrolling about 22,700 undergraduate and 6,300 graduate students.

Cuyamaca College: Cuyamaca Community College is a community college in the San Diego County community of Rancho San Diego, near El Cajon, California.  Along with Grossmont College it serves the eastern suburbs in the San Diego area.  Cuyamaca opened in 1978 and now offers 81 associate's degree programs and 66 training certification programs to approximately 8,500 students.  Many of the college's students transfer to the University of California, San Diego or San Diego State University to complete their bachelor's degrees.  Cuyamaca's mascot is the coyote.

Cal Poly Mustangs men's soccer: The Cal Poly Mustangs men's soccer program represents California Polytechnic State University in men's soccer at the NCAA Division I level.  Cal Poly is coached by former United States men's national team head coach Steve Sampson.  Like most teams from Cal Poly, they play in the Big West Conference.  The Big West Conference stopped sponsoring soccer in 1991, but resumed soccer in 2001.  Over this period, Cal Poly competed in a regional conference called the MPSF.  Since the return of soccer to the Big West, the Mustangs have appeared in 2 NCAA tournaments, most recently in 2015.  Posting the program's best record in 2008 (11–6–6), Cal Poly placed 3rd in the Big West and qualified for the NCAA Division I Tournament for the first time in the school's history.  Cal Poly managed to upset #11 UCLA 1–0 to advance to second round before losing 0–3 to #14 UC Irvine.  The Mustangs play in Alex G. Spanos Stadium (capacity of 11,075) on the campus of the California Polytechnic State University.  In 2011, collegesoccernews.com chose the Cal Poly vs UCSB soccer game as the #1 rivalry in college soccer.

Michael Marlow (economist): Michael L. Marlow is a professor of economics at California Polytechnic State University (Cal Poly).  He is also an affiliated senior scholar at the Mercatus Center at George Mason University.  He holds a BA from George Washington University and a PhD from Virginia Tech, both in economics.  He joined the California Polytechnic State University faculty in 1988 and was named a University Distinguished Scholar by the university in 2007.  Prior to joining Cal Poly, he was an associate professor of economics at George Washington University from 1979 to 1983, and also worked as a senior financial economist at the U.S. Treasury from 1983 to 1988.  He is known for opposing government regulation of e-cigarettes and of unhealthy foods and beverages.  He has also argued that alcohol taxes primarily reduce consumption by light drinkers, not by heavy drinkers, and has criticized Proposition 65 for being ineffective with respect to public health benefits.  His research into the effects of smoking laws has been criticized for being funded by Philip Morris, and for methodological flaws.

California Polytechnic State University: California Polytechnic State University, also known as California Polytechnic State University, San Luis Obispo, Cal Poly San Luis Obispo, or Cal Poly, is a public university located in San Luis Obispo, California, United States.  Founded in 1901 as a vocational high school, it is currently one of only two polytechnic universities in the 23-member California State University system.  With six colleges, the university offers 64 bachelor's degrees, 32 master's degrees, and 7 teaching credentials.  The university does not grant doctoral degrees.

Question: Between University of California, San Diego and California Polytechnic State University, which school offers more degree programs?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "universities_compared": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the university."
          },
          "total_degree_programs": {
            "type": "integer",
            "description": "The total number of degree programs offered by the university."
          }
        },
        "required": [
          "name",
          "total_degree_programs"
        ],
        "additionalProperties": false
      },
      "minItems": 2,
      "maxItems": 2
    },
    "comparison_result": {
      "type": "string",
      "description": "A statement comparing the number of degree programs."
    },
    "university_with_more_programs": {
      "type": "string",
      "description": "The name of the university that offers more degree programs."
    }
  },
  "required": [
    "universities_compared",
    "comparison_result",
    "university_with_more_programs"
  ],
  "additionalProperties": false
}
