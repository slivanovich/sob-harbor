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
Ebertfest: Roger Ebert's Film Festival: Roger Ebert's Film Festival, originally known as Roger Ebert's Overlooked Film Festival but commonly referred to as simply Ebertfest, is an annual film festival held every April in Champaign, Illinois, United States, organized by the College of Media at the University of Illinois.  Roger Ebert, the TV and "Chicago Sun-Times" film critic, was a native of the adjoining town of Urbana, Illinois and is an alumnus of the University.  Founded in 1999, this event is the only long-running film festival created by a critic.  Despite Ebert’s death in 2013, the festival continues to operate based on Ebert’s notes and vision for the kinds of films he championed.

Life Itself (film): Life Itself is a 2014 American biographical documentary film about film critic Roger Ebert, directed by Steve James and produced by Zak Piper, Steve James and Garrett Basch.  The film is based on Ebert's 2011 memoir of the same name.  It premiered at the 2014 Sundance Film Festival and was an official selection at the 67th Cannes Film Festival.  The 41st Telluride Film Festival hosted a special screening of the film on August 28, 2014.  Magnolia Pictures released the film theatrically in the United States and simultaneously via video on demand platforms on July 4, 2014.

Ebert test: The Ebert test gauges whether a computer-based synthesized voice can tell a joke with sufficient skill to cause people to laugh.  It was proposed by film critic Roger Ebert at the 2011 TED conference as a challenge to software developers to have a computerized voice master the inflections, delivery, timing, and intonations of a speaking human.  The test is similar to the Turing test proposed by Alan Turing in 1950 as a way to gauge a computer's ability to exhibit intelligent behavior by generating performance indistinguishable from a human being.

Lee Isaac Chung: Lee Isaac Chung (born October 19, 1978) is a Korean American film director and screenwriter.  His debut feature "Munyurangabo" (2007) was an Official Selection at the 2007 Cannes Film Festival.  The first narrative feature film in the Kinyarwanda language, the film was an Official Selection at the Cannes Film Festival, the Berlin Film Festival, the Toronto International Film Festival, the Busan International Film Festival.  American critic Roger Ebert calls it "in every frame a beautiful and powerful film — a masterpiece."

Just, Melvin: Just Evil: Just, Melvin: Just Evil is a 2000 American documentary by James Ronald Whitney about his grandfather, Melvin Just, and the devastating consequences of the sexual abuse Just inflicted on their family.  It premiered at the 2000 Sundance Film Festival and aired on HBO on April 22, 2001.  The film was well received overall; critic Roger Ebert called "Just, Melvin" "one of the most powerful documentaries I've seen."

RogerEbert.com: RogerEbert.com is a film review website that archives film critic Roger Ebert's reviews for the "Chicago Sun-Times" and also shares other critics' reviews and essays.  Ebert handpicked writers from around the world to contribute to the website.  After Ebert died in 2013, the website was relaunched under Ebert Digital, a partnership between Ebert, his wife Chaz, and friend Josh Golden, begun while Ebert was still alive.

Ebert Presents: At the Movies: Ebert Presents: At the Movies was a weekly, nationally syndicated movie review television program produced and presented by film critic Roger Ebert and co-produced by his wife, Chaz Ebert.  The program aired on public television stations in the United States through American Public Television.

Patrick Creadon: Patrick Creadon (born May 1, 1967) is an American film director primarily known for his work in independent documentary films.  His first film, "Wordplay", profiled "New York Times" crossword editor Will Shortz and premiered at the 2006 Sundance Film Festival.  Soon after its premiere, "Wordplay" became the second-highest grossing documentary of that year.  His second film, "I.O.U.S.A.", examined America's debt problem and forecast the global financial crisis of 2008-2009.  "I.O.U.S.A" premiered at the 2008 Sundance Film Festival and was later named one of film critic Roger Ebert's Top 5 Documentaries of the Year.

Beyond the Call: Beyond the Call is a 2006 documentary film about three middle-aged men who are former soldiers and modern-day knights.  They travel the world delivering life saving humanitarian aid directly into the hands of civilians and doctors in some of the most dangerous yet beautiful places on Earth, the front lines of war.  It is the directorial debut of Academy Award nominee Adrian Belic.  The film has been screened in over 80 film festivals on five continents, winning 25 awards so far.

The Great Movies: The Great Movies is the name of several publications, both online and in print, from the film critic Roger Ebert.  The object was, as Ebert put it, to "make a tour of the landmarks of the first century of cinema."

Question: Which documentary did critic Roger Ebert call "one of the most powerful documentaries I've seen", 2006's Beyond the Call or 2000's Just, Melvin: Just Evil?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "documentary_title": {
      "type": "string",
      "description": "The title of the documentary film."
    },
    "release_year": {
      "type": "integer",
      "description": "The release year of the documentary."
    },
    "ebert_quote": {
      "type": "string",
      "description": "The specific quote attributed to Roger Ebert about the film."
    },
    "ebert_assessment_category": {
      "type": "string",
      "description": "A categorization of Roger Ebert's assessment of the film (e.g., 'highly positive', 'masterpiece')."
    }
  },
  "required": [
    "documentary_title",
    "release_year",
    "ebert_quote",
    "ebert_assessment_category"
  ],
  "additionalProperties": false
}
