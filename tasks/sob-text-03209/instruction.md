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
KUGS: KUGS (89.3 FM) is a college radio station in Bellingham, Washington, United States, affiliated with Western Washington University.  KUGS was founded on January 29, 1974 as a 10 watt radio station.  In 1984 this was increased to 100 watts.  KUGS remains an independent and fully student-managed college radio station.  In 1994, KUGS was the second station in the US to broadcast content online, which ended in 2002.  In 2006, KUGS began webcasting again through its website.  In 1999, the station applied to upgrade to 700 watts effective radiated power.  The FCC issued a construction permit for a power increase to 950 watts in December, 2012.

WASU-FM: WASU-FM (90.5 FM) is a college radio station broadcasting an alternative music format.  The station is owned by Appalachian State University in Boone, North Carolina, which is also the station's city of license.  The station plays a college rock format and does a weekly news segment called App 1800 covering local issues.  WASU is the winner of mtvU's "College Radio Woodie Award" for 2012, the "Shoulda Coulda Woodie Award" for 2011, and was a 2008 Finalist in the New York Festivals Radio Broadcasting Awards.

Dix Hills, New York: Dix Hills is a hamlet and census-designated place (CDP) on Long Island in the town of Huntington in Suffolk County, New York, United States.  The population was 26,892 at the 2010 census.

WFTU (AM): WFTU (1570 AM) is a college radio station licensed to Riverhead, New York and is owned and operated by Five Towns College in Dix Hills, New York on Long Island.  It broadcasts a Variety format featuring programming produced by current students and faculty of Five Towns College.  The station is also operated by a student management staff under the guidance of the general manager, a staff professor.  The studio is located on the campus in Dix Hills and transmitter is in Riverhead, New York.  The station also streams on the internet from its website.

KLSU: KLSU (91.1 FM) is the student-run college radio station for Louisiana State University in Baton Rouge, Louisiana with a radio format of variety music and specialty programming.  The radio station is part of the university's Student Media Program and employs students as DJs and management staff.  KLSU broadcasts across the Baton Rouge area at 23,000 watts of power, and is able to reach up to 40 miles beyond the LSU campus.  The station is licensed under the Federal Communications Commission (FCC) as a non-commercial educational (NCE) radio station.  KLSU is one of 700 college radio stations across the United States that submits music chart reports to the weekly publication "College Music Journal" magazine.

WSPN: WSPN (Skidmore College) is a non-commercial college radio station located at 91.1 MHz and broadcasts from Saratoga Springs, New York, USA.  The station is located on the campus of Skidmore College and is made up of student and community DJs.  Additionally, WSPN is one of the few college radio stations run entirely by a selected student board.  The station primarily programs a freeform radio format and—in addition to serving the Skidmore College campus—also serves the city of Saratoga Springs, and surrounding communities.  Unlike many college stations, WSPN is a 24-hour-a-day operation, and is on the air 365 days a year.

KXSC (AM): KXSC (1560 AM) is the student-run college radio station at the University of Southern California.  Listeners can tune in via the internet at KXSC.org/listen, and at 1560 AM in the area immediately surrounding USC's campus.  KXSC provides original programming 24 hours a day, seven days a week.  The station also provides students with the opportunity to work at a college radio station and learn the basics of the music industry.

WQHS Radio: WQHS is the only wholly student-operated college radio station at the University of Pennsylvania.  WXPN was the University's principal student radio station until 1975, with WQHS as an AM-based training ground for DJs.  After 1975, WQHS became the official student radio station of the University, with WXPN being taken over by an external company.  The radio station currently broadcasts an eclectic freeform radio format over internet radio, as a result of their radio tower, formerly on top of Harnwell College House, falling down in a severe storm in 2003.

WKNC-FM: WKNC-FM (88.1 FM), North Carolina State University's student-run, non-commercial radio station is a college radio station broadcasting from Raleigh, North Carolina in the United States.  Broadcasting with an effective radiated power of 25,000 watts, its signal covers much of the Research Triangle and outlying areas.  The station is operated as part of the Department of Student Media at N.C. State and students hold all roles from DJ to general manager.  The primary weekday format is indie rock, with specialty shows and other music genres featured during the evenings and weekends.

WPSC-FM: WPSC-FM (88.7 FM) is William Paterson University's non-commercial radio station.  Licensed to Wayne, New Jersey, USA, the station serves the northern New Jersey and western New York City area.  In 2011, WPSC was one of the top 25 stations nominated for the mtvU Woodie Award for Best College Radio Station.  In 2017, WPSC Won Best College Station In The Nation (Enrollment over 10,000 students) at the 77th IBS Awards in New York City, March 2017.  In October 2011 and also scheduled for October 2012, WPSC will also serve as international HQ for College Radio Day.

Question: What is the name of this census-designated place with a population of over 25,000, that is the home of the WFTU college radio station?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "cdp_name": {
      "type": "string",
      "description": "The name of the census-designated place."
    },
    "population": {
      "type": "integer",
      "description": "The population of the census-designated place."
    },
    "radio_station_name": {
      "type": "string",
      "description": "The name of the college radio station located in the CDP."
    },
    "state": {
      "type": "string",
      "description": "The state where the CDP is located."
    }
  },
  "required": [
    "cdp_name",
    "population",
    "radio_station_name",
    "state"
  ],
  "additionalProperties": false
}
