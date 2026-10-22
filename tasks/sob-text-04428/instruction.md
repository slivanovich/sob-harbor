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
Lost Moon: Lost Moon: The Perilous Voyage of Apollo 13 (published in paperback as Apollo 13), is a non-fiction book first published in 1994 by astronaut James Lovell and journalist Jeffrey Kluger, about the failed April 1970 Apollo 13 lunar landing mission which Lovell commanded.  The book is the basis of the 1995 film adaptation "Apollo 13", directed by Ron Howard.

Gene Kranz: Eugene Francis "Gene" Kranz (born August 17, 1933) is an American aerospace engineer, retired fighter pilot and a retired NASA Flight Director and manager.  Kranz served as a Flight Director, the successor to NASA founding Flight Director Chris Kraft, during the Gemini and Apollo programs, and is best known for his role in directing the successful Mission Control team efforts to save the crew of Apollo 13, which later became the subject story of a major motion picture of the same name, in which he was portrayed by actor Ed Harris, and serving as flight director during the first lunar landing of Apollo 11.  He is also noted for his trademark close-cut flattop hairstyle, and the wearing of dapper "mission" vests (waistcoats), of different styles and materials made by his wife, Marta Kranz, during missions for which he acted as Flight Director.

Lunar plaque: Stainless steel commemorative plaques measuring 9 by were attached to the ladders on the descent stages of the United States Apollo Lunar Modules flown on lunar landing missions Apollo 11 through Apollo 17, to be left permanently on the lunar surface.  The plaques were originally suggested and designed by NASA's head of technical services Jack Kinzler, who oversaw their production.  All of the plaques bear facsimiles of the participating astronauts' signatures.  For this reason, an extra plaque had to be made for Apollo 13 due to the late replacement of one crewmember.  The first (Apollo 11) and last (Apollo 17) plaques bear a facsimile of the signature of Richard Nixon, President of the United States during the landings, along with references to the start and "completion" of "man's" "first" explorations of the Moon and expressions of peace for "all mankind".  All, except the Apollo 12 plaque (which is also textured differently), bear pictures of the two hemispheres of Earth.  Apollo 17's plaque bears a depiction of the lunar globe in addition to the Earth.  The plaques used on missions 13 through 16 bear the call-sign of each mission's Lunar Module.  All the plaques were left on the Moon, except the two for the aborted Apollo 13 which did not land on the Moon.

Milton Windler: Milton "Milt" Windler is a retired NASA Flight Director.  He is best known for his work as one of the four flight directors of Apollo 13 Mission Operations Team, all of whom were awarded the Presidential Medal of Freedom by President Richard M. Nixon for their work in guiding the crippled spacecraft safely back to Earth.  Previously a jet fighter pilot, he began working at NASA in 1959 during Project Mercury.  Originally working in the recovery division, he was promoted to flight director by Chris Kraft to support Eugene Kranz, who had acquired additional responsibilities in the months following the Apollo 1 fire.  Windler also served as flight director for Apollo 8, Apollo 10, Apollo 14, Apollo 15, and all three Skylab missions.  Following the conclusion of the Apollo Program, Windler worked in the Space Shuttle Project Office on Remote Manipulator Systems Operations until 1978.  He is a recipient of the NASA Exceptional Service Medal.

Jay Greene: Jay H. Greene is a retired NASA engineer.  Between 2000 and 2004, he served as Chief Engineer at Johnson Space Center, where his role consisted primarily of advising the Center Director.  He worked as a FIDO flight controller during the Apollo Program and a flight director from 1982 to 1986, most notably as ascent flight director during the Challenger accident in 1986.  Greene worked for four years as a manager on the International Space Station project and received several awards for his work including the NASA Distinguished Service Medal.  After his retirement in 2004 he served as a part-time consultant on the Exploration Systems Architecture Study.  NASA Associate Administrator Rex Geveden described him as "a famous technical curmudgeon in the Agency."

Apollo 13 (film): Apollo 13 is a 1995 American space adventure docudrama film directed by Ron Howard and starring Tom Hanks, Kevin Bacon, Bill Paxton, Gary Sinise, and Ed Harris.  The screenplay by William Broyles, Jr. and Al Reinert, that dramatizes the aborted 1970 Apollo 13 lunar mission, is an adaptation of the book "Lost Moon: The Perilous Voyage of Apollo 13" by astronaut Jim Lovell and Jeffrey Kluger.  The film depicts astronauts Lovell, Jack Swigert, and Fred Haise aboard Apollo 13 for America's third Moon landing mission.  En route, an on-board explosion deprives their spacecraft of most of its oxygen supply and electric power, forcing NASA's flight controllers to abort the Moon landing, and turning the mission into a struggle to get the three men home safely.

Houston, we have a problem: "Houston, we have a problem" is a popular but erroneous quote from the radio communications between the Apollo 13 astronaut Jack Swigert and the NASA Mission Control Center ("Houston") during the Apollo 13 spaceflight, as the astronauts communicated their discovery of the explosion that crippled their spacecraft.  The erroneous wording was popularized by the 1995 film "Apollo 13", a dramatization of the Apollo 13 mission, in which actor Tom Hanks, portraying Mission Commander Jim Lovell, uses that wording, which became one of the film's taglines.

Glynn Lunney: Glynn Stephen Lunney (born November 27, 1936) is a retired NASA engineer.  An employee of NASA since its creation in 1958, Lunney was a flight director during the Gemini and Apollo programs, and was on duty during historic events such as the Apollo 11 lunar ascent and the pivotal hours of the Apollo 13 crisis.  At the end of the Apollo program, he became manager of the Apollo-Soyuz Test Project, the first collaboration in spaceflight between the United States and the Soviet Union.  Later, he served as manager of the Space Shuttle program before leaving NASA in 1985 and later becoming a vice president of the United Space Alliance.

Don Puddy: Donald R. Puddy (May 31, 1937 – November 22, 2004) was a NASA engineer and manager.  He joined NASA in 1964, eventually becoming the agency's tenth flight director. His Flight Team colors were Crimson.  He served as a flight director during the Apollo 17, Skylab, and Apollo-Soyuz Test Project missions, Skylab, and the first Space Shuttle mission.  He earned a number of awards for his service, including the Presidential Medal of Freedom and the NASA Outstanding Leadership Medal.

Failure Is Not an Option: Failure Is Not an Option is a presentation on the History Channel documenting the United States' space program with insights from the flight engineers, project managers, flight controllers, astronauts, and others involved inside the National Aeronautics and Space Administration.  Speakers include Chris Kraft, Gene Kranz, Jim Lovell, Jerry Bostick, Ed Fendell, Gene Cernan, John Llewellen, John Aaron, Glynn Lunney, Wally Schirra, and Gerry Griffin.  It takes the viewer from the Launch of Sputnik through the moon missions.  It was produced in 2003.

Question: The documentary featuring the Flight director that guided the crew of Apollo 13 was produced what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "documentary_title": {
      "type": "string",
      "description": "The title of the documentary."
    },
    "production_year": {
      "type": "integer",
      "description": "The year the documentary was produced."
    },
    "featured_flight_director": {
      "type": "string",
      "description": "The name of the flight director featured in the documentary and relevant to the question."
    },
    "flight_director_role": {
      "type": "string",
      "description": "The specific role of the flight director related to the mission."
    }
  },
  "required": [
    "documentary_title",
    "production_year",
    "featured_flight_director",
    "flight_director_role"
  ],
  "additionalProperties": false
}
