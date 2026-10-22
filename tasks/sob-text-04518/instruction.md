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
De Wolfe Music: De Wolfe Music is a British production music company that became the originator of what has become known as library music.  De Wolfe Music was established by Meyer de Wolfe in 1909 and began its recorded library in 1927 with the advent of 'Talkies'.  The library consists of over 80,000 tracks, all pre-cleared for licensing and synchronisation.  They have been used in thousands of productions including "Monty Python", "Emmanuelle", "Dawn of the Dead", "American Gangster", and "Doctor Who".  Well known theme tunes include "Van der Valk", "Roobarb" and "The NFL Today".  De Wolfe built and owns Angel Recording Studios, a recording and mixing complex situated at The Angel, Islington, London.  Artists who have recorded there in recent years include Adele, Snow Patrol, Cee Lo Green, Labrinth, George Fenton (BAFTA and EMMY winner for his scores to the BBC's "The Blue Planet" and "Planet Earth"), Ian Brown, Elbow, The Doves, The Feeling, and Kaiser Chiefs.  Its specially composed department is called Inter Angel.  De Wolfe is still a family-run company.

American Gangster (film): American Gangster is a 2007 American biographical crime film directed and produced by Ridley Scott and written by Steven Zaillian.  The film is fictionally based on the criminal career of Frank Lucas, a gangster from La Grange, North Carolina who smuggled heroin into the United States on American service planes returning from the Vietnam War, before being detained by a task force led by detective Richie Roberts.  The film stars Russell Crowe and Denzel Washington in their first lead acting roles together since 1995's "Virtuosity".  The film also co-stars Ted Levine, John Ortiz, Josh Brolin, Chiwetel Ejiofor, Norman Reedus, Ruby Dee, Lymari Nadal and Cuba Gooding Jr.

Kathleen MacInnes: Kathleen MacInnes (born 30 December 1969) is a Scottish singer, television presenter and actress, who performs primarily in Scottish Gaelic.  She is a native of South Uist, Outer Hebrides, Scotland, and lives in Glasgow with her partner and three sons.  In 2010, she appeared on the soundtrack to the Ridley Scott film "Robin Hood".

Blade Runner (1997 video game): Blade Runner is a 1997 point-and-click adventure game developed by Westwood Studios and published by Virgin Interactive for Microsoft Windows.  The game is not a direct adaptation of the 1982 Ridley Scott film "Blade Runner", but is instead a "sidequel", telling an original story, which runs parallel to the film's plot, occasionally intersecting with it.

Elsie de Wolfe: Elsie de Wolfe, also known as Lady Mendl, (December 20, 1859?  – July 12, 1950) was an American actress, interior decorator, nominal author of the influential 1913 book "The House in Good Taste," and a prominent figure in New York, Paris, and London society.  According to "The New Yorker", "Interior design as a profession was invented by Elsie de Wolfe," although the praise is not strictly true.  De Wolfe was certainly the most famous name in the field until the 1930s, but the profession of interior decorator/designer was recognized as a promising one as early as 1900, five years before she received her first official commission, The Colony Club in New York.  During her married life (from 1926 until her death in 1950) the press often referred to her as Lady Mendl.  She was born in New York City and died at Versailles, France.  Cremated, her ashes were placed in a common grave, the lease expired, in Pere Lachaise Cemetery, Paris

Charles Knode: Charles Knode is a costume designer.  He studied at Wimbledon School of Art.  He designed the costumes for the 1972 epic BBC drama of Leo Tolstoy's "War and Peace" which starred amongst others, Anthony Hopkins as Pierre Bezukhov.  Among his first jobs on leaving the BBC was on Monty Python's "Life of Brian".  He has appeared as an extra in many of the Monty Python films.  He has won 2 BAFTA Awards.  The first for the Ridley Scott film "Blade Runner" and the second for "Braveheart".  His designs have also appeared in a number of music videos starring Kate Bush .  In 1996, In addition to winning the BAFTA award he was nominated for an Oscar for his work on the acclaimed Mel Gibson epic "Braveheart".  He won an Emmy Award for Alice in Wonderland

Tears in rain monologue: "Tears in Rain", also referred to as "The C-Beams Speech", is a brief monologue delivered by replicant Roy Batty (portrayed by Rutger Hauer) in the Ridley Scott film "Blade Runner".  The final form, altered from the scripted lines and improvised by Hauer on the eve of filming, has entered popular culture as "perhaps the most moving death soliloquy in cinematic history" and is an often quoted piece of science fiction writing.

Logan Marshall-Green: Logan Marshall-Green (born November 1, 1976) is an American actor.  He is known for his roles in the television series "24", "The O.C.", "Traveler", "Dark Blue", and "Quarry", and as Charlie Holloway in the 2012 Ridley Scott film "Prometheus".  He appeared in the 2017 film "" as Jackson Brice.

Alien (creature in Alien franchise): The "Alien" (also referred to as "Xenomorph XX121") is a fictional endoparasitoid extraterrestrial species that is the eponymous antagonist of the "Alien" film series.  The species made its debut in the film "Alien" (1979), and reappeared in the sequels "Aliens" (1986), "Alien 3" (1992), and "" (1997), as well as the crossover franchise "Alien vs. Predator" (2004) and "" (2007).  A similar creature of a slightly different design named the "Deacon" makes a brief appearance in the Ridley Scott film "Prometheus" (2012).  Two species, one being a different but similar creature called a "Neomorph" and the other being a variation of the Xenomorph XX121 species appear in the sequel to "Prometheus", "" (2017), which reveals the potential origin of the species.  In addition, the Alien appears in various literature and video game spin-offs from the franchises.

Eye Level: Eye Level is a 1972 single by the Simon Park Orchestra.  It was produced originally for the De Wolfe Music Library and selected by Thames Television to be the theme tune for their Netherlands based detective series, "Van der Valk".

Question: De Wolfe Music has tracks used in what 2007 Ridley Scott Film?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "director": {
      "type": "string",
      "description": "The director of the film."
    },
    "music_company": {
      "type": "string",
      "description": "The name of the music company whose tracks were used in the film."
    },
    "track_usage_confirmed": {
      "type": "boolean",
      "description": "Indicates if the use of the music company's tracks in the film is confirmed by the context."
    }
  },
  "required": [
    "film_title",
    "release_year",
    "director",
    "music_company",
    "track_usage_confirmed"
  ],
  "additionalProperties": false
}
