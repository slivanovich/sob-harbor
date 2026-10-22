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
Garfield's Pet Force: Garfield's Pet Force is a 2009 direct-to-video animation comedy family Computer animation (CGI) film based on characters from the Jim Davis comic strip "Garfield" and loosely based on the Pet Force novel series.  It is the sequel to "Garfield Gets Real" and "Garfield's Fun Fest".  It was released on DVD and Blu-ray Disc on June 16, 2009.  It was written by Garfield creator Jim Davis.  In 2010 it was released in 3-D.

The Garfield Show: The Garfield Show is a French–American CGI animated television series.  Based on the American comic strip, "Garfield", the series is executive produced by Garfield creator, Jim Davis, and co-written and voice directed by Mark Evanier, who also wrote most of the episodes for the "Garfield and Friends" series.  Returning from "Garfield and Friends" are the voice actors Julie Payne (Liz) and Gregg Berger (Odie).  Frank Welker replaces Lorenzo Music (due to his death in 2001) as the voice of Garfield, and Wally Wingert replaces Thom Huge (due to his retirement that same year) as the voice of Jon Arbuckle.  Also returning is David Lander, reprising his role as Doc Boy from the earlier Garfield prime-time special "A Garfield Christmas Special" (1987).  The show is produced by Dargaud Media and Paws Inc.  The show is directed by Philippe Vidal and the music is composed by Laurent Bertaud and Jean-Christophe Prudhomme.

Odie: Odie is a fictional dog who appears in the comic strip "Garfield" by Jim Davis.  He has also appeared in the animated television series "Garfield and Friends" and "The Garfield Show", two live-action/computer-animated feature films, and three fully CGI films.

Garfield's Fun Fest: Garfield's Fun Fest is a 2008 CGI movie starring Garfield.  It was produced by Paws, Inc. in cooperation with The Animation Picture Company and distributed by 20th Century Fox Home Entertainment.  It was written by Garfield's creator Jim Davis as a sequel to "Garfield Gets Real".  The DVD was released in stores on August 5, 2008.  It was followed by a third direct to video film, "Garfield's Pet Force," in 2009.

Garfield's Halloween Adventure: Garfield's Halloween Adventure (originally titled Garfield in Disguise) is a 1985 American animated television special based on the "Garfield" comic strip.  It is directed by Phil Roman and written by "Garfield" creator Jim Davis, and features the voices of Lorenzo Music, Thom Huge, Gregg Berger and C. Lindsay Workman.

David Reddick: David Reddick (born April 14, 1971 in Anderson, Indiana) is an American artist, illustrator and cartoonist.  He is the creator of various popular comic strips such as "Legend of Bill," "The Trek Life" at CBS/ STARTREK.COM, "Gene's Journal" and "Rod & Barry" at Roddenberry.com, and he is a full-time cartoonist at "Paws, Inc.", where he works on the "Garfield" worldwide property.

Garfield statues: Marion, and surrounding Grant County, Indiana have erected a series of statues around the area depicting the comic strip character Garfield.  The brainchild of local leader Pete Beck (a county councilman at the time), the basic idea is to place a likeness of Garfield in each community in the county.  It is hoped that as the project matures Garfield fans will travel to Grant County and make a circuit to see all of the statues.  The statues are made of hollow fiberglass after private fundraising provides for the construction at each location.  Indiana native and creator of Garfield, Jim Davis has donated the artwork to create the statues royalty free.

Garfield Gets Real: Garfield Gets Real (also known as Garfield 3D in some regions) is a 2007 American CGI movie starring Garfield.  It was produced by Paws, Inc. in cooperation with Davis Entertainment, and The Animation Picture Company and distributed by 20th Century Fox Home Entertainment.  It was written by Garfield's creator Jim Davis, who started working on the script in the fall of 1996.  This was the first fully animated Garfield film since the last "Garfield and Friends" TV episode aired in 1995, and the first to be written by Davis since the 1991 television special "Garfield Gets a Life".  The movie was released in theaters August 9, 2007, and the DVD was shipped to stores on November 20, 2007.  Gregg Berger, an actor from the original series, reprises his role of Odie, but Garfield is now voiced by veteran voice actor Frank Welker, since the original actor Lorenzo Music died in 2001 and Jon is voiced by Wally Wingert, as Thom Huge retired that same year.  The film's success led to two sequels: "Garfield's Fun Fest" (2008) and "Garfield's Pet Force" (2009).

Netrunner: Netrunner is a collectible card game (CCG) designed by Richard Garfield, the creator of "".  It was published by Wizards of the Coast and introduced in 1996.  The game took place in the setting for the Cyberpunk 2020 role-playing game, but it also drew from the broader cyberpunk genre.  "Netrunner" was lauded by critics, such as "InQuest" magazine, for its balanced game play and impressive artwork.  In 1999 "Pyramid" magazine named "Netrunner" as one of "The Millennium's Most Underrated Games".  According to editor Scott Haring, "among the connoisseurs of the card game design art, "Netrunner" is considered to be one of the best-designed games ever."

Happy Birthday, Garfield: Happy Birthday, Garfield is an hour-long television special dedicated to the tenth anniversary of the "Garfield" comic strip, hosted by its creator Jim Davis.  The special was first broadcast May 17, 1988 on CBS.  It has only been released on VHS home video.

Question: Who is the creator of Garfield?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "creator_name": {
      "type": "string",
      "description": "The name of the creator."
    },
    "created_work_type": {
      "type": "string",
      "description": "The type of work created (e.g., comic strip, film)."
    },
    "created_work_title": {
      "type": "string",
      "description": "The title of the work that was created."
    },
    "creator_role": {
      "type": "string",
      "description": "The specific role of the person in relation to the work (e.g., creator, writer, executive producer)."
    }
  },
  "required": [
    "creator_name",
    "created_work_type",
    "created_work_title",
    "creator_role"
  ],
  "additionalProperties": false
}
