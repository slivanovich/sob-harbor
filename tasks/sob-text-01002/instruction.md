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
Vladimir Alexandrov: Vladimir Valentinovich Alexandrov (Russian: Владимир Валентинович Александров ; born 1938; disappeared 1985) was a Soviet/Russian physicist who created a mathematical model for the nuclear winter theory.  He disappeared while at the Second International Conference of Nuclear Free Zones Local Authorities in Cordoba, Spain on March 31 and his ultimate fate remains unknown, with much speculation continuing.  One of his last papers was "Man and Biosphere" published in 1985, it is said to have charted the moving trend in the science of nuclear winter.  It was co-authored with Nikita Moiseyev and A.M Tarko.

Editors (band): Editors are an English rock band, formed in 2002 in Birmingham.  Previously known as Pilot, The Pride and Snowfield, the band currently consists of Tom Smith (lead vocals, guitar, piano), Russell Leetch (bass guitar, synthesizer, backing vocals), Ed Lay (drums, percussion, backing vocals), Justin Lockey (lead guitar), and Elliott Williams (keys, synthesizers, guitars, and backing vocals).

Working for a Nuclear Free City (album): Working For A Nuclear Free City is the debut album by Manchester (United Kingdom) indie band Working for a Nuclear Free City.  The album was not released in the United States but all its tracks were included on their next release, the double album "Businessmen & Ghosts".  Their song "Dead Fingers Talking" was used in the first episode of the show Breaking Bad

Francis Underhill Macy: Francis Underhill Macy (February 19, 1927 – January 20, 2009) was founder and co-director of the Center for Safe Energy between 1995 till his death in 2009.  During this time Macy trained hundreds of activists in Russia, Ukraine, Georgia, and Kazakhstan to address the environmental legacy of the nuclear arms race and the Chernobyl disaster.  Initiating scores of professional delegations and exchanges between Americans and their counterparts in the former Soviet Union in the areas of psychology, environment, and citizen organizing since 1983, Macy empowered the rise of non-governmental organizations – a strong contribution to the health of post-Soviet life.  In 2005, he was awarded the Nuclear Free Future Lifetime Achievement Award.

Philip Kay: Philip Kay is a contemporary composer and producer.  He is also a founding member of the band Working For A Nuclear Free City.

Working for a Nuclear Free City: Working for a Nuclear Free City (sometimes abbreviated to WFANFC) was an indie nu gaze band from Manchester, England.

Businessmen &amp; Ghosts: Businessmen & Ghosts is a double album by British band Working for a Nuclear Free City.  The album is Working for a Nuclear Free City's U.S. debut album.

Fri (yacht): Fri, a New Zealand yacht, led a flotilla of yachts in an international protest against atmospheric nuclear tests at Moruroa in French Polynesia in 1973.  "Fri" was an important part of a series of anti-nuclear protest campaigns out of New Zealand which lasted thirty years, from which New Zealand declared itself a nuclear-free zone which was enshrined in legislation in what became the New Zealand Nuclear Free Zone, Disarmament, and Arms Control Act 1987.  In 1974, coordinated by Greenpeace New Zealand, the "Fri" embarked on a 3-year epic 40,233 kilometers “Pacific Peace Odyssey” voyage, carrying the peace message to all nuclear states around the world.

Nuclear Free World Policy: The Nuclear Free World Policy is a commitment by a bloc of countries known as the New Agenda Coalition (NAC) to shape foreign policy around the goal of "the elimination of nuclear weapons and assurance that they will never be produced again."  The policy arose from an 18-point Joint Declaration signed by the Ministers of foreign affairs of Brazil, Egypt, Ireland, Mexico, New Zealand, South Africa, Slovenia and Sweden on June 9, 1998.  The signatories of this Joint Declaration became member-states of the NAC, although Slovenia and Sweden subsequently left the Coalition.

Jojo Burger Tempest: Jojo Burger Tempest is a double album by the British band Working for a Nuclear Free City.  Released in 2010, the album is the band's third album, and the second to be released in the U.S.  The album contains one disc of 17 individual songs and one of a single 33-minute suite.

Question: Editors and Working for a Nuclear Free City, is of which nationality?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_entities": {
      "type": "array",
      "description": "List of entities mentioned in the question.",
      "items": {
        "type": "string"
      }
    },
    "nationality": {
      "type": "string",
      "description": "The nationality shared by the entities."
    },
    "bands": {
      "type": "array",
      "description": "Details of the bands and their origin.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Name of the band."
          },
          "origin_city": {
            "type": "string",
            "description": "City where the band was formed or is from."
          },
          "origin_country": {
            "type": "string",
            "description": "Country where the band is from."
          }
        },
        "required": [
          "name",
          "origin_city",
          "origin_country"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "question_entities",
    "nationality",
    "bands"
  ],
  "additionalProperties": false
}
