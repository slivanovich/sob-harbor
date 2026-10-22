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
Worldcon: Worldcon, or more formally the World Science Fiction Convention, the annual convention of the World Science Fiction Society (WSFS), is a science fiction convention.  It has been held each year since 1939 (except for the years 1942 to 1945, during World War II).  The members of each Worldcon are the members of WSFS, and vote both to select the site of the Worldcon two years later, and to select the winners of the annual Hugo Awards, which are presented at each convention.

Planet of the Apes: Planet of the Apes is an American science fiction media franchise consisting of films, books, television series, comics, and other media about a world in which humans and intelligent apes clash for control.  The series began with French author Pierre Boulle's 1963 novel "La Planète des Singes", translated into English as "Planet of the Apes" or "Monkey Planet".  The 1968 film adaptation, "Planet of the Apes", was a critical and commercial hit, initiating a series of sequels, tie-ins, and derivative works.  Arthur P. Jacobs produced the series under APJAC Productions until his death in 1973; since then 20th Century Fox has owned the franchise.

Alien Nation: Alien Nation is an American science fiction media franchise comprising film, television, and other media productions about alien refugees living on Earth.  The series began with the 1988 film "Alien Nation", which was adapted into a Fox Network television series of the same name in 1989.  Fox cancelled the series abruptly after one season, but continued the story in five TV movies.  The series also produced other media and merchandising tie-ins, including novels and comics.  Aside from the sci-fi angle, the franchise fits into many different genres including drama, police procedural and buddy cop.

ArmadilloCon: ArmadilloCon is a science fiction convention held annually in Austin, Texas, USA, since 1979.  As the second longest running science fiction convention in Texas, it is sponsored by the Fandom Association of Central Texas and is known for its emphasis on literary science fiction.  ArmadilloCon was traditionally held in mid-October during the weekend of the Texas-OU football game, but moved to a late-summer/early-fall weekend in 1998.  The 34th annual convention was held in the Renaissance Hotel Austin from July 27–29, 2012.  ArmadilloCon 35 in 2013 was a "relaxicon" due to the 71st World Science Fiction Convention to be held in San Antonio that year.

CoastCon: CoastCon is Mississippi's longest running and largest science fiction, fantasy and gaming convention.  It is the main sponsored event of CoastCon, Inc., a non-profit literary organization.  CoastCon, Inc. and its ten-member volunteer board develop events and gatherings to promote reading, education, fellowship, and science fiction, fantasy and gaming in all formats across the Southern United States, for over thirty-five years.  The next CoastCon annual convention, CoastCon 40, will be held March 3-5, 2017, at the Mississippi Coast Coliseum and Convention Center in Biloxi, Mississippi.

ASFMA Award: The Australian Science Fiction Media Awards (ASFMA Awards) were awards given annually for achievement in non-literary media and media appreciation within Australian science fiction.  They were awarded at the Australian National Science Fiction Media Convention, from 1984 to 1997.  The award was formally dissolved and incorporated into the Ditmar Awards at the Business Meeting of the Australian National Science Fiction Convention, Spawncon II in Melbourne in 1999, with the formal merger of the Australian "Media Natcon" and the Natcon.

Treklanta: Treklanta (formerly "TrekTrax Atlanta") is an annual "Star Trek" convention based in Atlanta, Georgia that places special emphasis on fan-based events, activities, programming and productions.

Alien Nation (disambiguation): Alien Nation is an American science fiction media franchise.

Star Trek: Star Trek is an American science fiction media franchise based on the television series created by Gene Roddenberry.  The first television series, simply called "Star Trek" and now referred to as "", debuted in 1966 and aired for three seasons on the television network NBC.  It followed the interstellar adventures of Captain James T Kirk (William Shatner) and his crew aboard the starship USS "Enterprise", a space exploration vessel, built by the interstellar federal republic United Federation of Planets in the twenty-third century.  The "Star Trek" canon of the franchise includes "The Original Series", an animated series, five spin-off television series, and its film franchise in addition to further adaptations made in several media since the original.

Battlestar Galactica: Battlestar Galactica is an American science fiction media franchise created by Glen A. Larson.  The franchise began with the original television series in 1978 and was followed by a short-run sequel series ("Galactica 1980"), a line of book adaptations, original novels, comic books, a board game, and video games.  A re-imagined version of "Battlestar Galactica" aired as a two-part, three-hour miniseries developed by Ronald D. Moore and David Eick in 2003.  That miniseries led to a weekly television series, which aired until 2009.  A prequel series, "Caprica", aired in 2010.

Question: Treklanta (formerly "TrekTrax Atlanta") is an annual convention for what American science fiction media franchise?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "convention_name": {
      "type": "string",
      "description": "The current name of the science fiction convention."
    },
    "former_convention_name": {
      "type": "string",
      "description": "The previous name of the science fiction convention."
    },
    "associated_franchise": {
      "type": "string",
      "description": "The American science fiction media franchise the convention is based on."
    },
    "franchise_origin_country": {
      "type": "string",
      "description": "The country of origin for the associated media franchise."
    },
    "franchise_genre": {
      "type": "string",
      "description": "The primary genre of the associated media franchise."
    }
  },
  "required": [
    "convention_name",
    "former_convention_name",
    "associated_franchise",
    "franchise_origin_country",
    "franchise_genre"
  ],
  "additionalProperties": false
}
